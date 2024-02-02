import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';




export default function Stocks() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Stocks | WorldView Insights
                </title>
            </Head>
            <div>
                Stocks 
            </div>
        </TrackingProvider>
    )
}