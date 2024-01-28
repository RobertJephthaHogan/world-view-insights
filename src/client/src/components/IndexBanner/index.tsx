import React, { useEffect, useState } from 'react'
import './styles.css'
import IndexDataCard from '../IndexDataCard'
import { dataService } from '../../services/data.service'


export default function IndexBanner() {
    
    const [bannerData, setBannerData] = useState<Array<any>|null>(null)

    useEffect(() => {
        
        dataService.getMajorIndicesOverview()
            .then((resp: any) => {
                console.log('resp', resp)
                setBannerData(resp)
            })
            .catch((error: any) => {
                console.log('error', error)
            })

    }, [])


    const componentData = [
        {
            title: "S&P 500",
            displayPrice: "$4870.5",
            grossChange: "+1.95",
            percentChange: "+0.04%",
            chartData: []
        },
        {
            title: "DOW 30",
            displayPrice: "$37817.5",
            grossChange: "+10.86",
            percentChange: "+0.03%",
            chartData: []
        },
        {
            title: "NASDAQ",
            displayPrice: "$15444.5",
            grossChange: "-37.78",
            percentChange: "-0.24%",
            chartData: []
        },
        {
            title: "Bitcoin",
            displayPrice: "$39745.62",
            grossChange: "-37.78",
            percentChange: "-0.24%",
            chartData: []
        },
        {
            title: "EUR/USD",
            displayPrice: "$1.08",
            grossChange: "+0.0005",
            percentChange: "+0.48%",
            chartData: []
        },
    ]

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


