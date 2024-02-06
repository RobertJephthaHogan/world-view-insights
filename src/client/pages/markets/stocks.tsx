import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';
import Header from '@/components/Header';
import { Inter } from "next/font/google";
import styles from '../../styles/pages/markets/stocks.module.css'
import ComingSoon from '@/components/ComingSoon';


const inter = Inter({ subsets: ["latin"] });



export default function Stocks() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Stocks | WorldView Insights
                </title>
                <meta
                    name="description"
                    content="United Stated Stock Data - WorldView Insights"
                />
            </Head>
            <div className={inter.className}>
                <Header/>
                <div className={styles['stocks-component']}>
                    <div>

                    </div>
                    <div className={styles['sc-center']}>
                        <ComingSoon/>
                    </div>
                    <div>

                    </div>
                </div>
            </div>
        </TrackingProvider>
    )
}