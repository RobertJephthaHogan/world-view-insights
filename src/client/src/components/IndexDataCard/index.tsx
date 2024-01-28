import React from 'react'
import './styles.css'


interface IndexDataCardProps {
    title?: string
    displayPrice?: string
    grossChange?: string
    percentChange?: string
    chartData?: Array<any>
}

export default function IndexDataCard(props: IndexDataCardProps) {

    return (
        <div className='index-data-card'>
            <div className='idc-left'>
                <div className='idc-l-top'>
                    <span className='index-title'>
                        {props?.title}
                    </span>
                    <span className='index-display-price'>
                        {props?.displayPrice}
                    </span>
                </div>
                <div className='idc-l-bottom'>
                    <span className={
                        `change-text 
                        ${ props?.percentChange?.[0] === '+' && 'change-up'}
                        ${ props?.percentChange?.[0] === '-' && 'change-down'}
                        `
                        }>
                        {props?.grossChange} ({props.percentChange})
                    </span>
                </div>
            </div>
            <div className='idc-right'>
                <div className='chart'>
                    
                </div>
            </div>
        </div>
    )
}