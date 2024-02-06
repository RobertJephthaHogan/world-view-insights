import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import type { Metadata } from "next";
import Head from 'next/head';




export default function About() {

    return (
        <TrackingProvider>
            <Head>
                <title>
                    About | WorldView Insights
                </title>
                <meta
                    name="description"
                    content="About WorldView Insights"
                />
            </Head>
            <div>
                About
            </div>
        </TrackingProvider>
    )
}