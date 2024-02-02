import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';
import { Inter } from "next/font/google";
import Header from '@/components/Header';


const inter = Inter({ subsets: ["latin"] });


export default function Gainers() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    WorldView Insights | Gainers
                </title>
            </Head>
            <div className={inter.className}>
                <Header/>
                Gainers 
            </div>
        </TrackingProvider>
    )
}