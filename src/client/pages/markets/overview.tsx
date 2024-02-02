import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'




export default function MarketOverview() {
    return (
        <TrackingProvider>
            <div>
                Market Overview
            </div>
        </TrackingProvider>
    )
}