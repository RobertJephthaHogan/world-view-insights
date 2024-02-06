import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';
import Header from '@/components/Header';
import { Inter } from "next/font/google";
import styles from '../../styles/pages/news/tech.module.css'
import ComingSoon from '@/components/ComingSoon';


const inter = Inter({ subsets: ["latin"] });



export default function TechNews() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Tech News | WorldView Insights
                </title>
                <meta
                    name="description"
                    content="Top Technology News Stories - WorldView Insights"
                />
            </Head>
            <div className={inter.className}>
                <Header/>
                <div className={styles['tech-news-component']}>
                    <div>

                    </div>
                    <div className={styles['tnc-center']}>
                        <ComingSoon/>
                    </div>
                    <div>

                    </div>
                </div>
            </div>
        </TrackingProvider>
    )
}