import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';




export default function InsiderTransactions() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Insider Transactions | WorldView Insights
                </title>
            </Head>
            <div>
                Insider Transactions
            </div>
        </TrackingProvider>
    )
}