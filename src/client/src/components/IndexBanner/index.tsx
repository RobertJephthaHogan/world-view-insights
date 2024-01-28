import React, { useEffect, useState } from 'react'
import './styles.css'
import IndexDataCard from '../IndexDataCard'
import { dataService } from '../../services/data.service'


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
        <div className='index-banner'>
            <div className='index-card-container'>

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


