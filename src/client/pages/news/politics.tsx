import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';
import Header from '@/components/Header';
import { Inter } from "next/font/google";
import styles from '../../styles/pages/news/politics.module.css'
import ComingSoon from '@/components/ComingSoon';


const inter = Inter({ subsets: ["latin"] });



export default function PoliticalNews() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Political News | WorldView Insights
                </title>
            </Head>
            <div className={inter.className}>
                <Header/>
                <div className={styles['political-news-component']}>
                    <div>

                    </div>
                    <div className={styles['pnc-center']}>
                        <ComingSoon/>
                    </div>
                    <div>

                    </div>
                </div>
            </div>
        </TrackingProvider>
    )
}