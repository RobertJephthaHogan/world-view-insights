import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';
import Header from '@/components/Header';
import { Inter } from "next/font/google";


const inter = Inter({ subsets: ["latin"] });

export default function ActiveStocks() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Active Stocks | WorldView Insights
                </title>
            </Head>
            <div className={inter.className}>
                <Header/>
                Active Stocks
            </div>
        </TrackingProvider>
    )
}