import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';



export default function TechNews() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Tech News | WorldView Insights
                </title>
            </Head>
            <div>
                Tech News
            </div>
        </TrackingProvider>
    )
}