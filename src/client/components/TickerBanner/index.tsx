'use client'

import React, { useEffect, useState } from 'react'
import { dataService } from '../../services/data.service'
import styles from '../../styles/components/TickerBanner.module.css'
//import './styles.css'





export default function TickerBanner() {

    const [bannerData, setBannerData] = useState<Array<any>|null>(null)


    useEffect(() => {
        
        dataService.getMarketLeaderQuotes(10)
            .then((resp: any) => {
                setBannerData(resp)
            })
            .catch((error: any) => {
                console.log('error', error)
            })

    }, [])

    return (
        <div 
            className={styles['ticker-banner']}
            id={styles['scroll-container']}
        >
            <div 
                className={styles['banner-rail']}
                id={styles['scroll-text']}
            >
                {/* 
                    To create a seamless, continuous scroll without gaps between 
                    iterations, we need to duplicate the content within the 
                    scrolling element. This approach ensures that as one set of 
                    content goes off-screen, the identical set appears, creating 
                    an illusion of an endless scroll. Thats why there are two sets.
                */}
                
                
                {/* Loader Skeleton */}
                {
                    !bannerData &&
                    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]?.map((coData: any, i: number) => {
                        
                        return (
                            <div className={styles['banner-item']} key={`ticker-skeleton-${i}`}>
                                <div className={styles['banner-skeleton']}/>
                            </div>
                        )
                    })
                }

                {/* Set One */}
                {
                    bannerData &&
                    bannerData?.map((coData: any, i: number) => {
                        
                        return (
                            <div className={styles['banner-item']} key={`ticker-banner-item-${i}`}>
                                <span className={styles['bi-info-text']}>
                                    {coData?.symbol ?? "err"} - ${coData?.price?.toFixed(2)}
                                </span>
                                <span className={`${styles['bi-change-text']} ${coData?.changesPercentage < 0 ? styles['bi-change-down-text'] : styles['bi-change-up-text']}`}>
                                    {coData?.changesPercentage?.toFixed(2)}%
                                </span>
                            </div>
                        )
                    })
                }

                {/* Set Two */}

                {
                    bannerData &&
                    bannerData?.map((coData: any, i: number) => {
                        
                        return (
                            <div className={styles['banner-item']} key={`ticker-banner-item-${i}`}>
                                <span className={styles['bi-info-text']}>
                                    {coData?.symbol ?? "err"} - ${coData?.price?.toFixed(2)}
                                </span>
                                <span className={`${styles['bi-change-text']} ${coData?.changesPercentage < 0 ? styles['bi-change-down-text'] : styles['bi-change-up-text']}`}>
                                    {coData?.changesPercentage?.toFixed(2)}%
                                </span>
                            </div>
                        )
                    })
                }

            </div>
        </div>
    )
}