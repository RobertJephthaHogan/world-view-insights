import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'




export default function InsiderTransactions() {
    return (
        <TrackingProvider>
            <div>
                Insider Transactions
            </div>
        </TrackingProvider>
    )
}