import React, { useEffect, useState } from 'react'
import './styles.css'
import { dataService } from '../../services/data.service'





// TODO: REFACTOR BANNER ITEMS WITH DYNAMIC COMPONENT
export default function TickerBanner() {

    const [bannerData, setBannerData] = useState<Array<any>|null>(null)


    useEffect(() => {
        //TODO: get banner data from backend and set to state

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

                {/* <div className='banner-item item'>
                    <span className='bi-info-text'>
                        AAPL - $193.55
                    </span>
                    <span className='bi-change-down-text'>
                        -0.28%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        MSFT - $403.25
                    </span>
                    <span className='bi-change-up-text'>
                        -0.18%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        NVDA - $612.25
                    </span>
                    <span className='bi-change-down-text'>
                        -0.32%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        WBA - $22.89
                    </span>
                    <span className='bi-change-up-text'>
                        +0.14%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        META - $403.25
                    </span>
                    <span className='bi-change-up-text'>
                        +0.14%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        AAPL - $193.55
                    </span>
                    <span className='bi-change-down-text'>
                        -0.28%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        MSFT - $403.25
                    </span>
                    <span className='bi-change-up-text'>
                        -0.18%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        NVDA - $612.25
                    </span>
                    <span className='bi-change-down-text'>
                        -0.32%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        WBA - $22.89
                    </span>
                    <span className='bi-change-up-text'>
                        +0.14%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        META - $403.25
                    </span>
                    <span className='bi-change-up-text'>
                        +0.14%
                    </span>
                </div> */}

                {/* Set Two */}
                {/* <div className='banner-item item'>
                    <span className='bi-info-text'>
                        AAPL - $193.55
                    </span>
                    <span className='bi-change-down-text'>
                        -0.28%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        MSFT - $403.25
                    </span>
                    <span className='bi-change-up-text'>
                        -0.18%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        NVDA - $612.25
                    </span>
                    <span className='bi-change-down-text'>
                        -0.32%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        WBA - $22.89
                    </span>
                    <span className='bi-change-up-text'>
                        +0.14%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        META - $403.25
                    </span>
                    <span className='bi-change-up-text'>
                        +0.14%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        AAPL - $193.55
                    </span>
                    <span className='bi-change-down-text'>
                        -0.28%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        MSFT - $403.25
                    </span>
                    <span className='bi-change-up-text'>
                        -0.18%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        NVDA - $612.25
                    </span>
                    <span className='bi-change-down-text'>
                        -0.32%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        WBA - $22.89
                    </span>
                    <span className='bi-change-up-text'>
                        +0.14%
                    </span>
                </div>
                <div className='banner-item item'>
                    <span className='bi-info-text'>
                        META - $403.25
                    </span>
                    <span className='bi-change-up-text'>
                        +0.14%
                    </span>
                </div> */}

            </div>
        </div>
    )
}