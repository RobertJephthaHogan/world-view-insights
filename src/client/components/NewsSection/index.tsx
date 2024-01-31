import React from 'react';
import styles from '../../styles/components/NewsSection.module.css';

export default function NewsSection() {
    return (
        <div className={styles['news-section']}>
            <div className={styles['news-section-category-bar']}>
                <div>
                    <span className={styles['ns-category-title']}>
                        Markets
                    </span>
                </div>
                <div className={styles['nsc-divider-container']}>
                    <div className={styles['nsc-divider']}></div>
                </div>
            </div>
            <div className={styles['ns-main-story']}>
                <div className={styles['ns-ms-l']}>
                    <div className={styles['ns-ms-image']}></div>
                </div>
                <div className={styles['ns-ms-r']}>
                    <div className={styles['main-story-title-container']}>
                        <span className={styles['ms-title']}>
                            Texas Instruments Shares Drops 3% 
                            on Weak Q4 Results & Guidance
                        </span>
                    </div>
                    <div className={styles['main-story-description-container']}>
                        <span className={styles['ms-description']}>
                            Texas Instruments (NASDAQ:TXN) saw its shares drop over 3% intra-day 
                            today, following a Q4 report that fell short of analysts' revenue and 
                            guidance expectations. The semiconductor manufacturer reported an 
                            EPS of $1.49 for the fourth quarter, a decrease from $2.13 in the same 
                            period last year. Its re...
                        </span>
                    </div>
                    <div className={styles['main-story-date-container']}>
                        <span className={styles['ms-date-text']}>
                            TXN - 24 January 2024
                        </span>
                    </div>
                </div>
            </div>
            <div className={styles['more-news-title-container']}>
                <span className={styles['more-news-title']}>
                    More Market News
                </span>
            </div>
            <div className={styles['more-stories-container']}>
                <div className={styles['story-row']}>
                    <div className={styles['sr-l']}>
                        <div className={styles['sr-image']}></div>
                    </div>
                    <div className={styles['sr-r']}>
                        <div className={styles['sr-r-t']}>
                            <span className={styles['story-row-title']}>
                                Intuitive Surgical Beats Q4 Expectations
                            </span>
                            <span className={styles['story-row-date']}>
                                ISRG - 24 January 2024
                            </span>
                        </div>   
                        <div className={styles['sr-r-b']}>
                            <span className={styles['story-row-description']}>
                                Intuitive Surgical (NASDAQ:ISRG), renowned for its robotic-assisted surgical technology, reported 
                                its fourth-quarter earnings, exceeding analyst expectations. The company's total revenue for the 
                                quart...
                            </span>
                        </div>   
                    </div>
                </div>
                <div className={styles['story-row']}>
                    <div className={styles['sr-l']}>
                        <div className={styles['sr-image']}></div>
                    </div>
                    <div className={styles['sr-r']}>
                        <div className={styles['sr-r-t']}>
                            <span className={styles['story-row-title']}>
                                Intuitive Surgical Beats Q4 Expectations
                            </span>
                            <span className={styles['story-row-date']}>
                                ISRG - 24 January 2024
                            </span>
                        </div>   
                        <div className={styles['sr-r-b']}>
                            <span className={styles['story-row-description']}>
                                Intuitive Surgical (NASDAQ:ISRG), renowned for its robotic-assisted surgical technology, reported 
                                its fourth-quarter earnings, exceeding analyst expectations. The company's total revenue for the 
                                quart...
                            </span>
                        </div>   
                    </div>
                </div>
                <div className={styles['story-row']}>
                    <div className={styles['sr-l']}>
                        <div className={styles['sr-image']}></div>
                    </div>
                    <div className={styles['sr-r']}>
                        <div className={styles['sr-r-t']}>
                            <span className={styles['story-row-title']}>
                                Intuitive Surgical Beats Q4 Expectations
                            </span>
                            <span className={styles['story-row-date']}>
                                ISRG - 24 January 2024
                            </span>
                        </div>   
                        <div className={styles['sr-r-b']}>
                            <span className={styles['story-row-description']}>
                                Intuitive Surgical (NASDAQ:ISRG), renowned for its robotic-assisted surgical technology, reported 
                                its fourth-quarter earnings, exceeding analyst expectations. The company's total revenue for the 
                                quart...
                            </span>
                        </div>   
                    </div>
                </div>
            </div>
        </div>
    );
}
