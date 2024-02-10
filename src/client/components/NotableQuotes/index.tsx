'use client'

import React, { useEffect, useState } from 'react'
import CaretRightOutlined from '@ant-design/icons/CaretRightOutlined'
import { dataService } from '../../services/data.service'
import { useRouter } from 'next/navigation'
import styles from '../../styles/components/NotableQuotes.module.css'
import { getConfig } from '@/config/Constants'




export default function NotableQuotes() {

    const [quoteData, setQuoteData] = useState<any|null>(null)
    const router = useRouter()
    const config = getConfig()


    useEffect(() => {
        
        dataService.getNotableQuotes()
            .then((resp: any) => {
                setQuoteData(resp)
            })
            .catch((error: any) => {
                console.log('error', error)
            })

    }, [])

    const handleNavigationClick = (event: any, path: string) => {
        // Prevent the default href link behavior 
        event.preventDefault();
    
        // TODO: Implement tracking logic here
    
        // Navigate to the URL after tracking
        //window.location.href = url;
        router.push(path);
    };


    return (
        <div className={styles['notable-quotes']}>
            <div className={styles['quote-section']}>
                <a 
                    className={styles['market-leaders-title-anchor']}
                    href={`${config.clientUrl}markets/leaders`}
                    onClick={(e) => handleNavigationClick(e, '/markets/leaders')}
                >
                    <div 
                        className={styles['quote-section-title-bar']}
                    >
                        <span className={styles['quote-section-title']}>
                            Market Leaders
                        </span>
                        <CaretRightOutlined
                            className={styles['quote-section-caret']}
                        />
                    </div>
                </a>
                <div className={styles['section-quote-container']}>

                    {
                        !quoteData?.marketLeaderQuotes &&
                        [0,0,0,0,0]?.map((quote: any, i: number) => {
                            return (
                                <div 
                                    className={styles['quote-skeleton-row']}
                                    key={`market-quote-skeleton-${i}`}
                                >
                                    <div className={styles['quote-skeleton']}>
                                        
                                    </div>
                                </div>
                            )
                        })
                    }

                    {
                        quoteData?.marketLeaderQuotes &&
                        quoteData?.marketLeaderQuotes?.map((quote: any, i: number) => {
                            return (
                                <a
                                    className={styles['quote-row-anchor']}
                                    href={`${config.clientUrl}stock/${quote?.symbol}`}
                                    onClick={(e) => handleNavigationClick(e, `/stock/${quote?.symbol}`)}
                                >
                                    <div 
                                        className={styles['quote-row']}
                                        key={`market-quote-row-${i}`}
                                    >
                                        <div className={styles['qrl']}>
                                            <span className={styles['quote-row-symbol']}>
                                                {quote?.symbol}
                                            </span>
                                        </div>
                                        <div className={styles['qrc']}>
                                            <div className={
                                                `${styles['quote-change-chip']}
                                                ${ quote?.changesPercentage < 0 ? styles['quote-change-down-chip'] : ''}
                                                ${ quote?.changesPercentage > 0 ? styles['quote-change-up-chip'] : ''}
                                                `
                                            }>
                                                <span className={
                                                    `${styles['quote-change-text']}
                                                    ${ quote?.changesPercentage < 0 ? styles['quote-change-down-text'] : ''}
                                                    ${ quote?.changesPercentage > 0 ? styles['quote-change-up-text'] : ''}
                                                    `
                                                }>
                                                    {quote?.changesPercentage.toFixed(2)}%
                                                </span>
                                            </div>
                                        </div>
                                        <div className={styles['qrr']}>
                                            <span className={styles['quote-row-quote']}>
                                                ${quote?.price?.toFixed(2)}
                                            </span>
                                        </div>
                                    </div>
                                </a>
                            )
                        })
                    }

                </div>
            </div>
            <div className={`${styles['quote-section']} ${styles['mts']}`}>
                <a
                    className={styles['market-gainers-title-anchor']}
                    href={`${config.clientUrl}markets/gainers`}
                    onClick={(e) => handleNavigationClick(e, '/markets/gainers')}
                >
                    <div className={styles['quote-section-title-bar']}>
                        <span className={styles['quote-section-title']}>
                            Gainers
                        </span>
                        <CaretRightOutlined
                            className={styles['quote-section-caret']}
                        />
                    </div>
                </a>
                <div className={styles['section-quote-container']}>

                    {
                        !quoteData?.gainerQuotes &&
                        [0,0,0,0,0]?.map((quote: any, i: number) => {
                            return (
                                <div 
                                    className={styles['quote-skeleton-row']}
                                    key={`gainer-quote-skeleton-${i}`}
                                >
                                    <div className={styles['quote-skeleton']}>
                                        
                                    </div>
                                </div>
                            )
                        })
                    }

                    {
                        quoteData?.gainerQuotes &&
                        quoteData?.gainerQuotes?.map((quote: any, i: number) => {
                            return (
                                <a
                                    className={styles['quote-row-anchor']}
                                    href={`${config.clientUrl}stock/${quote?.symbol}`}
                                    onClick={(e) => handleNavigationClick(e, `/stock/${quote?.symbol}`)}
                                >
                                    <div 
                                        className={styles['quote-row']}
                                        key={`gainer-quote-row-${i}`}
                                    >
                                        <div className={styles['qrl']}>
                                            <span className={styles['quote-row-symbol']}>
                                                {quote?.symbol}
                                            </span>
                                        </div>
                                        <div className={styles['qrc']}>
                                            <div className={
                                                `${styles['quote-change-chip']}
                                                ${ quote?.changesPercentage < 0 ? styles['quote-change-down-chip'] : ''}
                                                ${ quote?.changesPercentage > 0 ? styles['quote-change-up-chip'] : ''}
                                                `
                                            }>
                                                <span className={
                                                    `${styles['quote-change-text']}
                                                    ${ quote?.changesPercentage < 0 ? styles['quote-change-down-text'] : ''}
                                                    ${ quote?.changesPercentage > 0 ? styles['quote-change-up-text'] : ''}
                                                    `
                                                }>
                                                    {quote?.changesPercentage.toFixed(2)}%
                                                </span>
                                            </div>
                                        </div>
                                        <div className={styles['qrr']}>
                                            <span className={styles['quote-row-quote']}>
                                                ${quote?.price?.toFixed(2)}
                                            </span>
                                        </div>
                                    </div>
                                </a>
                            )
                        })
                    }

                </div>
            </div>
            <div className={`${styles['quote-section']} ${styles['mts']}`}>
                <a
                    className={styles['market-losers-title-anchor']}
                    href={`${config.clientUrl}markets/losers`}
                    onClick={(e) => handleNavigationClick(e, '/markets/losers')}
                >
                    <div className={styles['quote-section-title-bar']} >
                        <span className={styles['quote-section-title']}>
                            Losers
                        </span>
                        <CaretRightOutlined
                            className={styles['quote-section-caret']}
                        />
                    </div>
                </a>
                <div className={styles['section-quote-container']}>

                    {
                        !quoteData?.loserQuotes &&
                        [0,0,0,0,0]?.map((quote: any, i: number) => {
                            return (
                                <div 
                                    className={styles['quote-skeleton-row']}
                                    key={`loser-quote-skeleton-${i}`}
                                >
                                    <div className={styles['quote-skeleton']}>
                                        
                                    </div>
                                </div>
                            )
                        })
                    }

                    {
                        quoteData?.loserQuotes &&
                        quoteData?.loserQuotes?.map((quote: any, i: number) => {
                            return (
                                <a
                                    className={styles['quote-row-anchor']}
                                    href={`${config.clientUrl}stock/${quote?.symbol}`}
                                    onClick={(e) => handleNavigationClick(e, `/stock/${quote?.symbol}`)}
                                >
                                    <div 
                                        className={styles['quote-row']}
                                        key={`loser-quote-row-${i}`}
                                    >
                                        <div className={styles['qrl']}>
                                            <span className={styles['quote-row-symbol']}>
                                                {quote?.symbol}
                                            </span>
                                        </div>
                                        <div className={styles['qrc']}>
                                            <div className={
                                                `${styles['quote-change-chip']}
                                                ${ quote?.changesPercentage < 0 ? styles['quote-change-down-chip'] : ''}
                                                ${ quote?.changesPercentage > 0 ? styles['quote-change-up-chip'] : ''}
                                                `
                                            }>
                                                <span className={
                                                    `${styles['quote-change-text']}
                                                    ${ quote?.changesPercentage < 0 ? styles['quote-change-down-text'] : ''}
                                                    ${ quote?.changesPercentage > 0 ? styles['quote-change-up-text'] : ''}
                                                    `
                                                }>
                                                    {quote?.changesPercentage.toFixed(2)}%
                                                </span>
                                            </div>
                                        </div>
                                        <div className={styles['qrr']}>
                                            <span className={styles['quote-row-quote']}>
                                                ${quote?.price?.toFixed(2)}
                                            </span>
                                        </div>
                                    </div>
                                </a>
                            )
                        })
                    }

                </div>
            </div>
        </div>
    )
}