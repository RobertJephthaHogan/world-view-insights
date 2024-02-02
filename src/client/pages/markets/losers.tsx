import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';




export default function Losers() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Market Losers | WorldView Insights
                </title>
            </Head>
            <div>
                Losers 
            </div>
        </TrackingProvider>
    )
}