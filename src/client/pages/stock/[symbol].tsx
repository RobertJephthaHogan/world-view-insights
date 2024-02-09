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
import dynamic from 'next/dynamic';
// import { PlusOutlined, StarOutlined } from '@ant-design/icons';
// import PlusOutlined from '@ant-design/icons/PlusOutlined'
// import StarOutlined from '@ant-design/icons/StarOutlined'


const inter = Inter({ subsets: ["latin"] });

const Button = dynamic(() => import('antd').then(mod => mod.Button));
const PlusOutlined = dynamic(() => import('@ant-design/icons/PlusOutlined').then(mod => mod));
const StarOutlined = dynamic(() => import('@ant-design/icons/StarOutlined').then(mod => mod));



const StockDataPage: NextPage<any> = ({ companyData }) => {

    console.log('StockDataPage')
    console.log('companyData', companyData)

  return (
	<TrackingProvider>
		<Head>
			<title>
				Stock Data Page | WorldView Insights
			</title>
			{/* <meta
				name="description"
				content={companyData?.title}
			/> */}
		</Head>
		<div className={inter.className}>
			<Header/>
			<TickerBanner/>
			<IndexBanner/>
			<div className={styles['stock-component']}>
				<div>

				</div>
				<div className={styles['sc-center']}>
					<div className={styles['stock-info-topbar']}>
                        <div  className={styles['sit-logo']}>
                            <img 
                                src={companyData?.profile?.image} 
                                alt="Image" 
                                style={{ 
                                    width: 70, 
                                    height: 70, 
                                    objectFit: 'cover' // This makes the image cover the div without losing aspect ratio
                                }} 
                            />
                        </div>
                        <div className={styles['sit-tit-container']}>
                            <span className={styles['sit-tit-text']}>
                                {companyData?.profile?.companyName}  ({companyData?.profile?.symbol} )
                            </span>
                        </div>
                        <div className={styles['sit-price-container']}>
                            <span className={styles['sit-price-text']}>
                                ${companyData?.profile?.price}
                            </span>
                        </div>
                        <div className={styles['sit-change-container']}>
                            <span className={styles['sit-change-text']}>
                                {companyData?.profile?.changes} ({((companyData?.profile?.changes / companyData?.profile?.price)*100).toFixed(2)}%)
                            </span>
                        </div>
                        <div  className={styles['sit-actions-container']}>
                            <Button className={styles['sit-action-btn']}>
                                <StarOutlined/>
                                <span>
                                    Add To Favorites
                                </span>
                            </Button>
                            <Button className={styles['sit-action-btn']}>
                                <PlusOutlined/>
                                <span>
                                    Add To Watchlist
                                </span>
                            </Button>
                        </div>
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
	const { symbol } = context.params!;
  
	try {
        const resp = await stockService.getStockPageData(symbol)
	
		return {
			props: { companyData: resp }, 
		};
	} catch (error) {
		console.error('Error', error);
	
		return {
			props: { article: null }
		};
	}
  };

export default StockDataPage;