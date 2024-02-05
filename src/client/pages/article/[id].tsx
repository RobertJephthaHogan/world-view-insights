import Head from 'next/head';
import Header from '@/components/Header';
import IndexBanner from '@/components/IndexBanner';
import TickerBanner from '@/components/TickerBanner';
import { TrackingProvider } from '@/providers/TrackingProvider';
import { GetServerSideProps, NextPage } from 'next';
import { Inter } from "next/font/google";
import { newsService } from '@/services/news.service';

const inter = Inter({ subsets: ["latin"] });



const ArticlePage: NextPage<any> = ({ article }) => {
  return (
	<TrackingProvider>
		<Head>
			<title>
				Article | WorldView Insights
			</title>
		</Head>
		<div className={inter.className}>
			<Header/>
			<TickerBanner/>
			<IndexBanner/>
			<h1>{article?.title}</h1>
			<p>{article?.content}</p>
			<p>Article Page!</p>
		</div>
	</TrackingProvider>
  );
};

export const getServerSideProps: GetServerSideProps = async (context) => {
	const { id } = context.params!;
  
	try {
		const resp = await newsService.getArticleById(id); // Use await to wait for the promise to resolve
		console.log('resp', resp);
	
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