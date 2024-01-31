'use client'

import React, { useEffect, useState } from 'react'
import IndexDataCard from '../IndexDataCard'
import { dataService } from '../../services/data.service'
import styles from '../../styles/components/IndexBanner.module.css'


export default function IndexBanner() {
    
    const [bannerData, setBannerData] = useState<Array<any>|null>(null)

    useEffect(() => {
        
        dataService.getMajorIndicesOverview()
            .then((resp: any) => {
                setBannerData(resp)
            })
            .catch((error: any) => {
                console.log('error', error)
            })

    }, [])


    return (
        <div className={styles['index-banner']}>
            <div className={styles['index-card-container']}>

                {
                    !bannerData &&
                    [0,0,0,0,0]?.map((entry: any) => {
                        return (
                            <div className={styles['index-card-skeleton']}/>
                        )
                    })
                }

                {
                    bannerData &&
                    bannerData?.map((entry: any) => {
                        return (
                            <IndexDataCard
                                title={entry?.title}
                                displayPrice={entry?.current_price}
                                grossChange={entry?.price_change_24h}
                                percentChange={entry?.price_change_percentage_24h}
                                chartData={entry?.intraday_price_history}
                            />
                        )
                    })
                }

            </div>
        </div>
    )
}


