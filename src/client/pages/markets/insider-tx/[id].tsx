import Head from 'next/head';
import Header from '@/components/Header';
import TickerBanner from '@/components/TickerBanner';
import { TrackingProvider } from '@/providers/TrackingProvider';
import { GetServerSideProps, NextPage } from 'next';
import { Inter } from "next/font/google";
import { useEffect, useState } from 'react';
import dynamic from 'next/dynamic';
import styles from '../../../styles/pages/markets/insider-tx.module.css'


const inter = Inter({ subsets: ["latin"] });




export const getServerSideProps: GetServerSideProps = async (context) => {
    const { id } = context.params!;

    console.log('filing ID', id)
    
    // ToDo: Get the filing data from the backend
    const filingData = {}
  
    return {
        props: { filingData }, // Filing data passed to the page component as props
    };
}
  
const PostPage: NextPage<any> = ({ post }: any) => {


    return (
        <TrackingProvider>
            <Head>
                <title>
                    Four Four | Insider Transaction Details
                </title>
                <meta
                    name="description"
                    content={`Four Four | Insider Transaction Details`}
                />
            </Head>
            <div className={inter.className}>
                <Header/>
                <TickerBanner/>
                <div className={styles['insider-tx-filing-component']}>
                    <div>

                    </div>
                    <div className={styles['itxfc-center']}>
                        <div className={styles['itxfc-topbar']}>
                            Filing Page Top Bar
                        </div>
                    </div>
                    <div>

                    </div>
                </div>
                
            </div>
        </TrackingProvider>
    );
};
  
export default PostPage;