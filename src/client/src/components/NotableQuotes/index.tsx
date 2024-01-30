import React, { useEffect, useState } from 'react'
import './styles.css'
import CaretRightOutlined from '@ant-design/icons/CaretRightOutlined'
import { dataService } from '../../services/data.service'



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
        <div className='notable-quotes'>
            <div className='quote-section'>
                <div className='quote-section-title-bar'>
                    <span className='quote-section-title'>
                        Market Leaders
                    </span>
                    <CaretRightOutlined
                         className='quote-section-caret'
                    />
                </div>
                <div className='section-quote-container'>

                    {
                        !quoteData?.marketLeaderQuotes &&
                        [0,0,0,0,0]?.map((quote: any) => {
                            return (
                                <div className='quote-skeleton-row'>
                                    <div className='quote-skeleton'>
                                        
                                    </div>
                                </div>
                            )
                        })
                    }

                    {
                        quoteData?.marketLeaderQuotes &&
                        quoteData?.marketLeaderQuotes?.map((quote: any) => {
                            return (
                                <div className='quote-row'>
                                    <div className='qrl'>
                                        <span className='quote-row-symbol'>
                                            {quote?.symbol}
                                        </span>
                                    </div>
                                    <div className='qrc'>
                                        <div className={
                                            `quote-change-chip
                                            ${ quote?.changesPercentage < 0 ? 'quote-change-down-chip' : 'quote-change-up-chip'}
                                            `
                                        }>
                                            <span className={
                                                `quote-change-text
                                                ${ quote?.changesPercentage < 0 ? 'quote-change-down-text' : 'quote-change-up-text'}
                                                `
                                            }>
                                                {quote?.changesPercentage.toFixed(2)}%
                                            </span>
                                        </div>
                                    </div>
                                    <div className='qrr'>
                                        <span className='quote-row-quote'>
                                            ${quote?.price?.toFixed(2)}
                                        </span>
                                    </div>
                                </div>
                            )
                        })
                    }

                </div>
            </div>
            <div className='quote-section mts'>
                <div className='quote-section-title-bar'>
                    <span className='quote-section-title'>
                        Gainers
                    </span>
                    <CaretRightOutlined
                         className='quote-section-caret'
                    />
                </div>
                <div className='section-quote-container'>

                    {
                        !quoteData?.gainerQuotes &&
                        [0,0,0,0,0]?.map((quote: any) => {
                            return (
                                <div className='quote-skeleton-row'>
                                    <div className='quote-skeleton'>
                                        
                                    </div>
                                </div>
                            )
                        })
                    }

                    {
                        quoteData?.gainerQuotes &&
                        quoteData?.gainerQuotes?.map((quote: any) => {
                            return (
                                <div className='quote-row'>
                                    <div className='qrl'>
                                        <span className='quote-row-symbol'>
                                            {quote?.symbol}
                                        </span>
                                    </div>
                                    <div className='qrc'>
                                        <div className={
                                            `quote-change-chip
                                            ${ quote?.changesPercentage < 0 ? 'quote-change-down-chip' : 'quote-change-up-chip'}
                                            `
                                        }>
                                            <span className={
                                                `quote-change-text
                                                ${ quote?.changesPercentage < 0 ? 'quote-change-down-text' : 'quote-change-up-text'}
                                                `
                                            }>
                                                {quote?.changesPercentage.toFixed(2)}%
                                            </span>
                                        </div>
                                    </div>
                                    <div className='qrr'>
                                        <span className='quote-row-quote'>
                                            ${quote?.price?.toFixed(2)}
                                        </span>
                                    </div>
                                </div>
                            )
                        })
                    }

                </div>
            </div>
            <div className='quote-section mts'>
                <div className='quote-section-title-bar'>
                    <span className='quote-section-title'>
                        Losers
                    </span>
                    <CaretRightOutlined
                         className='quote-section-caret'
                    />
                </div>
                <div className='section-quote-container'>

                    {
                        !quoteData?.loserQuotes &&
                        [0,0,0,0,0]?.map((quote: any) => {
                            return (
                                <div className='quote-skeleton-row'>
                                    <div className='quote-skeleton'>
                                        
                                    </div>
                                </div>
                            )
                        })
                    }

                    {
                        quoteData?.loserQuotes &&
                        quoteData?.loserQuotes?.map((quote: any) => {
                            return (
                                <div className='quote-row'>
                                    <div className='qrl'>
                                        <span className='quote-row-symbol'>
                                            {quote?.symbol}
                                        </span>
                                    </div>
                                    <div className='qrc'>
                                        <div className={
                                            `quote-change-chip
                                            ${ quote?.changesPercentage < 0 ? 'quote-change-down-chip' : 'quote-change-up-chip'}
                                            `
                                        }>
                                            <span className={
                                                `quote-change-text
                                                ${ quote?.changesPercentage < 0 ? 'quote-change-down-text' : 'quote-change-up-text'}
                                                `
                                            }>
                                                {quote?.changesPercentage.toFixed(2)}%
                                            </span>
                                        </div>
                                    </div>
                                    <div className='qrr'>
                                        <span className='quote-row-quote'>
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