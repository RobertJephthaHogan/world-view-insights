import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import type { Metadata } from "next";



const keywordSearchTerms = [
    "insights",
];

export const metadata: Metadata = {
    title: "WorldView Insights",
    description: "All in one source for news, market data, investing tools, overall insights",
    keywords: keywordSearchTerms
};

export default function About() {

    return (
        <TrackingProvider>
            <div>
                About
            </div>
        </TrackingProvider>
    )
}