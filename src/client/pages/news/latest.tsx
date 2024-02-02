import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';



export default function LatestNews() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Latest News | WorldView Insights
                </title>
            </Head>
            <div>
                Latest News
            </div>
        </TrackingProvider>
    )
}