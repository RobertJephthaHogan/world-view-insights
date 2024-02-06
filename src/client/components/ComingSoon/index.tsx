import React from 'react'
import styles from '../../styles/components/ComingSoon.module.css'


export default function ComingSoon() {

    return (
        <div className={styles['coming-soon']}>
            <div className={styles['coming-soon-row']}>
                <div className={styles['coming-soon-pigeon']}>
                    
                </div>
            </div>
            <div className={styles['coming-soon-row']}>
                <span className={styles['tfi-text']}>
                    This Feature Is
                </span>
            </div>
            <div className={styles['coming-soon-row']}>
                <span className={styles['otw-text']}>
                    On The Way
                </span>
            </div>
            <div className={styles['coming-soon-row']}>
                <span className={styles['cptip-text']}>
                    We are growing quickly - Check back in a few days.
                </span>
            </div>
        </div>
    )
}