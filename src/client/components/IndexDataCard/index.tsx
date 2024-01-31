import React from 'react'
import styles from '../../styles/components/IndexDataCard.module.css'



interface IndexDataCardProps {
    title?: string
    displayPrice?: string
    grossChange: string
    percentChange: string
    chartData?: Array<any>
}

export default function IndexDataCard(props: IndexDataCardProps) {

    return (
        <div className={styles['index-data-card']}>
            <div className={styles['idc-left']}>
                <div className={styles['idc-l-top']}>
                    <span className={styles['index-title']}>
                        {props?.title}
                    </span>
                    <span className={styles['index-display-price']}>
                        {props?.displayPrice}
                    </span>
                </div>
                <div className={styles['idc-l-bottom']}>
                    <span className={`
                        ${styles['change-text']}
                        ${parseFloat(props?.percentChange) > 0 ? styles['change-up'] : ''}
                        ${parseFloat(props?.percentChange) < 0 ? styles['change-down'] : ''}
                    `}>
                        {parseFloat(props?.grossChange)?.toFixed(2)} ({parseFloat(props?.percentChange)?.toFixed(2)}%)
                    </span>
                </div>
            </div>
            <div className={styles['idc-right']}>
                <div className={styles['chart']}>
                    
                </div>
            </div>
        </div>
    )
}