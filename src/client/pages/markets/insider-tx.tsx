import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';
import Header from '@/components/Header';
import { Inter } from "next/font/google";
import styles from '../../styles/pages/markets/insider-tx.module.css'
import ComingSoon from '@/components/ComingSoon';


const inter = Inter({ subsets: ["latin"] });



export default function InsiderTransactions() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Insider Transactions | WorldView Insights
                </title>
                <meta
                    name="description"
                    content="Form 4 Filings - Insider Transactions - WorldView Insights"
                />
            </Head>
            <div className={inter.className}>
                <Header/>
                <div className={styles['insider-tx-component']}>
                    <div>

                    </div>
                    <div className={styles['itxc-center']}>
                        <ComingSoon/>
                    </div>
                    <div>

                    </div>
                </div>
            </div>
        </TrackingProvider>
    )
}