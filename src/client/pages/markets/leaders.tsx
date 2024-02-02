import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';




export default function MarketLeaders() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Market Leaders | WorldView Insights
                </title>
            </Head>
            <div>
                Market Leaders 
            </div>
        </TrackingProvider>
    )
}