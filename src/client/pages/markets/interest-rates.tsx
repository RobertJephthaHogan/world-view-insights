import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';
import Header from '@/components/Header';
import { Inter } from "next/font/google";
import styles from '../../styles/pages/markets/interest-rates.module.css'
import ComingSoon from '@/components/ComingSoon';


const inter = Inter({ subsets: ["latin"] });




export default function InterestRates() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Interest Rates | WorldView Insights
                </title>
                <meta
                    name="description"
                    content="United Treasure Interest Rate Data - WorldView Insights"
                />
            </Head>
            <div className={inter.className}>
                <Header/>
                <div className={styles['interest-rates-component']}>
                    <div>

                    </div>
                    <div className={styles['irc-center']}>
                        <ComingSoon/>
                    </div>
                    <div>

                    </div>
                </div>
            </div>
        </TrackingProvider>
    )
}