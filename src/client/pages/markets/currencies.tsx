import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';
import Header from '@/components/Header';
import { Inter } from "next/font/google";
import styles from '../../styles/pages/markets/currencies.module.css'
import ComingSoon from '@/components/ComingSoon';


const inter = Inter({ subsets: ["latin"] });



export default function Currencies() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Currencies | WorldView Insights
                </title>
                <meta
                    name="description"
                    content="Global Currencies Data - WorldView Insights"
                />
            </Head>
            <div className={inter.className}>
                <Header/>
                <div className={styles['currencies-component']}>
                    <div>

                    </div>
                    <div className={styles['cc-center']}>
                        <ComingSoon/>
                    </div>
                    <div>

                    </div>
                </div>
            </div>
        </TrackingProvider>
    )
}