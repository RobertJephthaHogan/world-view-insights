import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';




export default function MarketOverview() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Market Overview | WorldView Insights
                </title>
            </Head>
            <div>
                Market Overview
            </div>
        </TrackingProvider>
    )
}