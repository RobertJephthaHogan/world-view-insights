import Head from 'next/head';
import Header from '@/components/Header';
import IndexBanner from '@/components/IndexBanner';
import TickerBanner from '@/components/TickerBanner';
import { TrackingProvider } from '@/providers/TrackingProvider';
import { GetServerSideProps, NextPage } from 'next';
import { Inter } from "next/font/google";
import { stockService } from '@/services/stock.service';
import styles from '../../styles/pages/stock.module.css'
import { useEffect, useState } from 'react';

const inter = Inter({ subsets: ["latin"] });



const StockDataPage: NextPage<any> = ({ article }) => {

    console.log('StockDataPage')
    console.log('article', article)

  return (
	<TrackingProvider>
		<Head>
			<title>
				Stock Data Page | WorldView Insights
			</title>
			{/* <meta
				name="description"
				content={article?.title}
			/> */}
		</Head>
		<div className={inter.className}>
			<Header/>
			<TickerBanner/>
			<IndexBanner/>
			<div className={styles['stock-component']}>
				<div>

				</div>
				<div className={styles['ac-center']}>
					center
				</div>
				<div>

				</div>
			</div>
			
		</div>
	</TrackingProvider>
  );
};

export const getServerSideProps: GetServerSideProps = async (context) => {
	const { symbol } = context.params!;
  
	try {
		//const resp = await newsService.getArticleById(id); 
        const resp = await stockService.getStockPageData(symbol)

        console.log('symbol test', symbol)
	
		return {
			props: { article: resp }, 
		};
	} catch (error) {
		console.error('Error', error);
	
		return {
			props: { article: null }
		};
	}
  };

export default StockDataPage;