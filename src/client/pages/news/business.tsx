import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';




export default function BusinessNews() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Business News | WorldView Insights
                </title>
            </Head>
            <div>
                Business News
            </div>
        </TrackingProvider>
    )
}