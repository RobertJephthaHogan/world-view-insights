import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';
import Header from '@/components/Header';
import { Inter } from "next/font/google";
import styles from '../../styles/pages/markets/overview.module.css'
import ComingSoon from '@/components/ComingSoon';


const inter = Inter({ subsets: ["latin"] });



export default function MarketOverview() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Market Overview | WorldView Insights
                </title>
                <meta
                    name="description"
                    content="Stock Market Overview - WorldView Insights"
                />
            </Head>
            <div className={inter.className}>
                <Header/>
                <div className={styles['market-overview-component']}>
                    <div>

                    </div>
                    <div className={styles['moc-center']}>
                        <ComingSoon/>
                    </div>
                    <div>

                    </div>
                </div>
            </div>
        </TrackingProvider>
    )
}