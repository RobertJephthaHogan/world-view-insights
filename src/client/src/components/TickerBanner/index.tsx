import React from 'react'
import './styles.css'





// TODO: REFACTOR BANNER ITEMS WITH DYNAMIC COMPONENT
export default function TickerBanner() {

    return (
        <div className='ticker-banner'>
            <div className='banner-item'>
                <span className='bi-info-text'>
                    AAPL - $193.55
                </span>
                <span className='bi-change-down-text'>
                    -0.28%
                </span>
            </div>
            <div className='banner-item'>
                <span className='bi-info-text'>
                    MSFT - $403.25
                </span>
                <span className='bi-change-up-text'>
                    -0.18%
                </span>
            </div>
            <div className='banner-item'>
                <span className='bi-info-text'>
                    NVDA - $612.25
                </span>
                <span className='bi-change-down-text'>
                    -0.32%
                </span>
            </div>
            <div className='banner-item'>
                <span className='bi-info-text'>
                    WBA - $22.89
                </span>
                <span className='bi-change-up-text'>
                    +0.14%
                </span>
            </div>
            <div className='banner-item'>
                <span className='bi-info-text'>
                    META - $403.25
                </span>
                <span className='bi-change-up-text'>
                    +0.14%
                </span>
            </div>
            <div className='banner-item'>
                <span className='bi-info-text'>
                    AAPL - $193.55
                </span>
                <span className='bi-change-down-text'>
                    -0.28%
                </span>
            </div>
            <div className='banner-item'>
                <span className='bi-info-text'>
                    MSFT - $403.25
                </span>
                <span className='bi-change-up-text'>
                    -0.18%
                </span>
            </div>
            <div className='banner-item'>
                <span className='bi-info-text'>
                    NVDA - $612.25
                </span>
                <span className='bi-change-down-text'>
                    -0.32%
                </span>
            </div>
            <div className='banner-item'>
                <span className='bi-info-text'>
                    WBA - $22.89
                </span>
                <span className='bi-change-up-text'>
                    +0.14%
                </span>
            </div>
            <div className='banner-item'>
                <span className='bi-info-text'>
                    META - $403.25
                </span>
                <span className='bi-change-up-text'>
                    +0.14%
                </span>
            </div>
        </div>
    )
}