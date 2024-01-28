import React, { useEffect, useState } from 'react'
import './styles.css'
import { dataService } from '../../services/data.service'





export default function TickerBanner() {

    const [bannerData, setBannerData] = useState<Array<any>|null>(null)


    useEffect(() => {

        console.log('hello')
        
        dataService.getMarketLeaderQuotes(10)
            .then((resp: any) => {
                console.log('resp', resp)
                setBannerData(resp)
            })
            .catch((error: any) => {
                console.log('error', error)
            })

    }, [])

    return (
        <div 
            className='ticker-banner'
            id='scroll-container'
        >
            <div 
                className='banner-rail'
                id='scroll-text'
            >
                {/* 
                    To create a seamless, continuous scroll without gaps between 
                    iterations, we need to duplicate the content within the 
                    scrolling element. This approach ensures that as one set of 
                    content goes off-screen, the identical set appears, creating 
                    an illusion of an endless scroll. Thats why there are two sets.
                */}
                
                {/* Set One */}

                {
                    bannerData &&
                    bannerData?.map((coData: any) => {
                        
                        return (
                            <div className='banner-item item'>
                                <span className='bi-info-text'>
                                    {coData?.symbol ?? "err"} - ${coData?.price}
                                </span>
                                <span className={
                                    `bi-change-text
                                    ${ coData?.changesPercentage < 0 ? 'bi-change-down-text' : 'bi-change-up-text'}
                                    `
                                }>
                                    {coData?.changesPercentage}%
                                </span>
                            </div>
                        )
                    })
                }

                {/* Set Two */}

                {
                    bannerData &&
                    bannerData?.map((coData: any) => {
                        
                        return (
                            <div className='banner-item item'>
                                <span className='bi-info-text'>
                                    {coData?.symbol ?? "err"} - ${coData?.price}
                                </span>
                                <span className={
                                    `bi-change-text
                                    ${ coData?.changesPercentage < 0 ? 'bi-change-down-text' : 'bi-change-up-text'}
                                    `
                                }>
                                    {coData?.changesPercentage}%
                                </span>
                            </div>
                        )
                    })
                }

            </div>
        </div>
    )
}