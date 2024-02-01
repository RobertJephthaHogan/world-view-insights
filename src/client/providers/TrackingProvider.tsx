'use client'

import React, { useEffect, createContext, useContext } from 'react';
import { useRouter } from 'next/router';
import ReactGA from 'react-ga4';

const TrackingContext = createContext(null);

export const useTracking = () => useContext(TrackingContext);

export const TrackingProvider = ({ children }: any) => {
    const router = useRouter();

    useEffect(() => {
        // Initialize Google Analytics with your GA4 measurement ID
        ReactGA.initialize('G-LN9CBDS31C');

        const handleRouteChange = (url: string) => {
            // Use send method with pageview event for tracking
            ReactGA.send({ hitType: "pageview", page: url });
        };

        // Track the initial pageview
        ReactGA.send({ hitType: "pageview", page: router.asPath });

        // Add event listeners to track pageviews on route change
        router.events.on('routeChangeComplete', handleRouteChange);

        // Remove event listeners on cleanup
        return () => {
            router.events.off('routeChangeComplete', handleRouteChange);
        };
    }, [router.events, router.asPath]);

    return (
        <TrackingContext.Provider value={null}>
            {children}
        </TrackingContext.Provider>
    );
};