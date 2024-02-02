import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';



export default function Gainers() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    WorldView Insights | Gainers
                </title>
            </Head>
            <div>
                Gainers 
            </div>
        </TrackingProvider>
    )
}