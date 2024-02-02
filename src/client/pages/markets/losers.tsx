import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';
import Header from '@/components/Header';
import { Inter } from "next/font/google";


const inter = Inter({ subsets: ["latin"] });



export default function Losers() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Market Losers | WorldView Insights
                </title>
            </Head>
            <div className={inter.className}>
                <Header/>
                Losers 
            </div>
        </TrackingProvider>
    )
}