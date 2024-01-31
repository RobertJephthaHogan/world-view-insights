'use client'

import React, { useEffect, useState } from 'react'
import CaretRightOutlined from '@ant-design/icons/CaretRightOutlined'
import { dataService } from '../../services/data.service'
import styles from '../../styles/components/NotableQuotes.module.css'




export default function NotableQuotes() {

    const [quoteData, setQuoteData] = useState<any|null>(null)

    useEffect(() => {
        
        dataService.getNotableQuotes()
            .then((resp: any) => {
                setQuoteData(resp)
            })
            .catch((error: any) => {
                console.log('error', error)
            })

    }, [])

    return (
        <div className={styles['notable-quotes']}>
            <div className={styles['quote-section']}>
                <div className={styles['quote-section-title-bar']}>
                    <span className={styles['quote-section-title']}>
                        Market Leaders
                    </span>
                    <CaretRightOutlined
                         className={styles['quote-section-caret']}
                    />
                </div>
                <div className={styles['section-quote-container']}>

                    {
                        !quoteData?.marketLeaderQuotes &&
                        [0,0,0,0,0]?.map((quote: any) => {
                            return (
                                <div className={styles['quote-skeleton-row']}>
                                    <div className={styles['quote-skeleton']}>
                                        
                                    </div>
                                </div>
                            )
                        })
                    }

                    {
                        quoteData?.marketLeaderQuotes &&
                        quoteData?.marketLeaderQuotes?.map((quote: any) => {
                            return (
                                <div className={styles['quote-row']}>
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
                            )
                        })
                    }

                </div>
            </div>
            <div className={`${styles['quote-section']} ${styles['mts']}`}>
                <div className={styles['quote-section-title-bar']}>
                    <span className={styles['quote-section-title']}>
                        Gainers
                    </span>
                    <CaretRightOutlined
                         className={styles['quote-section-caret']}
                    />
                </div>
                <div className={styles['section-quote-container']}>

                    {
                        !quoteData?.gainerQuotes &&
                        [0,0,0,0,0]?.map((quote: any) => {
                            return (
                                <div className={styles['quote-skeleton-row']}>
                                    <div className={styles['quote-skeleton']}>
                                        
                                    </div>
                                </div>
                            )
                        })
                    }

                    {
                        quoteData?.gainerQuotes &&
                        quoteData?.gainerQuotes?.map((quote: any) => {
                            return (
                                <div className={styles['quote-row']}>
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
                            )
                        })
                    }

                </div>
            </div>
            <div className={`${styles['quote-section']} ${styles['mts']}`}>
                <div className={styles['quote-section-title-bar']}>
                    <span className={styles['quote-section-title']}>
                        Losers
                    </span>
                    <CaretRightOutlined
                         className={styles['quote-section-caret']}
                    />
                </div>
                <div className={styles['section-quote-container']}>

                    {
                        !quoteData?.loserQuotes &&
                        [0,0,0,0,0]?.map((quote: any) => {
                            return (
                                <div className={styles['quote-skeleton-row']}>
                                    <div className={styles['quote-skeleton']}>
                                        
                                    </div>
                                </div>
                            )
                        })
                    }

                    {
                        quoteData?.loserQuotes &&
                        quoteData?.loserQuotes?.map((quote: any) => {
                            return (
                                <div className={styles['quote-row']}>
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
                            )
                        })
                    }

                </div>
            </div>
        </div>
    )
}