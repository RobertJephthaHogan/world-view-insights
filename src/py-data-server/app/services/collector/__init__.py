from app.services.edgar import EdgarService
from app.services.open_ai import OpenAiService
from app.models.FormFour import FormFour
from app.database.form_four_operations import FormFourOperations
from app.services.form_four.form_four_parser import parseFormFour
from app.services.form_four import FormFourService
from app.database.news_article_operations import NewsArticleOperations
from app.services.news import NewsService
from app.models.NewsArticle import NewsArticle
from bson import ObjectId
import json



class CollectorService:
    
    
    async def collect_form_fours():
        
        finalDTO = {}
        newFilingsList = []
        alreadyInDB = 0
        newFilings = 0
        recentFilings = await EdgarService.getRecentFilings("4", "", "")
                
        for filing in recentFilings:
                        
            # check if the filing exists in the database, 
            filing_exists = await FormFourOperations.retrieve_form_four_by_accession_id(filing)
            
            # if the filing already exists, do nothing
            if (len(filing_exists)):
                pass
            
            # if the filing does not already exist, create the entry
            if not (len(filing_exists)):
                                
                newFiling = filing
                soup, filing = await EdgarService.getFiling(newFiling)                
                
                form_four_dto = await FormFourService().parse_form_four(soup, filing)
                
                form_four_dto['id'] = str(ObjectId())
                
                form_four_obj = FormFour(**form_four_dto)
                await FormFourOperations.add_form_four(form_four_obj)
                
                
                
    async def collect_business_news_articles():
        
        # get the news articles to collect
        articles = await NewsService.get_business_news_articles()

        # iterate through articles, store articles that are not already stored       
        for article in articles:
                        
            # check if article exists by title, if so pass, if not, add the article
            article_exists = await NewsArticleOperations().retrieve_news_article_by_reference_title(article['title'])
            if article_exists:
                pass 
            else :
                
                # Set the Author to our AI financial Journalist
                article['author'] = 'Aaron Horowitz'
                
                # set the title as referenceTitle so it can be searched for
                article['referenceTitle'] = article['title']
                
                # Use Aaron to write competitor article title here
                competitor_content = article['content']
                aaron_content = await OpenAiService.write_competitor_article(competitor_content)
                print('aaron_content', aaron_content)
                article['content'] = aaron_content
                
                # Use Aaron to write competitor article here
                competitor_article_title = article['title']
                aaron_article_title = await OpenAiService.write_competitor_article_title(competitor_article_title)
                print('aaron_article_title', aaron_article_title)
                # quotes generated in title
                no_double_quotes = aaron_article_title.replace('"', '')
                title_no_quotes = no_double_quotes.replace("'", '')
                
                article['title'] = title_no_quotes
                
                article_instance = NewsArticle(**article)
                await NewsArticleOperations.add_news_article(article_instance)
                
        return {"status": "complete"}
                
                
                
        
        