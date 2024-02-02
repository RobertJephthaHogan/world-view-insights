import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';




export default function InterestRates() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Interest Rates | WorldView Insights
                </title>
            </Head>
            <div>
                Interest Rates 
            </div>
        </TrackingProvider>
    )
}