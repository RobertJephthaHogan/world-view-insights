import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';




export default function Sectors() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Market Sectors | WorldView Insights
                </title>
            </Head>
            <div>
                Sectors 
            </div>
        </TrackingProvider>
    )
}