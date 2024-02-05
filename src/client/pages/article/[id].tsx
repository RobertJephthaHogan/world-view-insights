import Head from 'next/head';
import Header from '@/components/Header';
import IndexBanner from '@/components/IndexBanner';
import TickerBanner from '@/components/TickerBanner';
import { TrackingProvider } from '@/providers/TrackingProvider';
import { GetServerSideProps, NextPage } from 'next';
import { Inter } from "next/font/google";
import { newsService } from '@/services/news.service';
import styles from '../../styles/pages/article.module.css'

const inter = Inter({ subsets: ["latin"] });



const ArticlePage: NextPage<any> = ({ article }) => {
  return (
	<TrackingProvider>
		<Head>
			<title>
				{article?.title}
			</title>
			<meta
				name="description"
				content={article?.title}
			/>
		</Head>
		<div className={inter.className}>
			<Header/>
			<TickerBanner/>
			<IndexBanner/>
			<div className={styles['article-component']}>
				<div>

				</div>
				<div className={styles['ac-center']}>
					<div className={styles['ticker-wrapper']}>
						<span>
							{article?.tickers}
						</span>
					</div>
					<div className={styles['article-title-container']}>
						<span className={styles['article-title']}>
							{article?.title}
						</span>
					</div>
					<div className={styles['article-info']}>
						<span className={styles['article-info-text']}>
							Published at {article?.datePosted}
						</span>
						<span className={styles['article-info-text']}>
							by {article?.author}
						</span>
					</div>
					<div>
						<p className={styles['article-content']}>
							{article?.content}
						</p>
					</div>
				</div>
				<div>

				</div>
			</div>
			
		</div>
	</TrackingProvider>
  );
};

export const getServerSideProps: GetServerSideProps = async (context) => {
	const { id } = context.params!;
  
	try {
		const resp = await newsService.getArticleById(id); // Use await to wait for the promise to resolve
	
		// Assuming resp directly contains the article data you want to pass as props
		return {
			props: { article: resp }, // Pass the article data under the article prop
		};
	} catch (error) {
		console.error('Error getting article by id', error);
	
		// Handle the error case by returning an empty object or error information
		// You can also redirect or return a 404 page here
		return {
			props: { article: null }, // Example error handling
		};
	}
  };

export default ArticlePage;