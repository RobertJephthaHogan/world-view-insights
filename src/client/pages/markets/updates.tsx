import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';
import Header from '@/components/Header';
import { Inter } from "next/font/google";
import styles from '../../styles/pages/markets/updates.module.css'
import ComingSoon from '@/components/ComingSoon';


const inter = Inter({ subsets: ["latin"] });



export default function MarketUpdates() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Stocks | WorldView Insights
                </title>
            </Head>
            <div className={inter.className}>
                <Header/>
                <div className={styles['updates-component']}>
                    <div>

                    </div>
                    <div className={styles['uc-center']}>
                        <ComingSoon/>
                    </div>
                    <div>

                    </div>
                </div>
            </div>
        </TrackingProvider>
    )
}