import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';




export default function Currencies() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Currencies | WorldView Insights
                </title>
            </Head>
            <div>
                Currencies Overview
            </div>
        </TrackingProvider>
    )
}