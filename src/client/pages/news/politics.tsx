import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';




export default function PoliticalNews() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Political News | WorldView Insights
                </title>
            </Head>
            <div>
                Political News
            </div>
        </TrackingProvider>
    )
}