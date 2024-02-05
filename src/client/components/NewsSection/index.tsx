import React from 'react';
import styles from '../../styles/components/NewsSection.module.css';



interface NewsSectionProps {
    sectionTitle?: any
    moreNewsTitle?: any
    articles?: any[]
}

export default function NewsSection(props: NewsSectionProps) {

    function formatEasyReadDate (date: any) {
        const options: Intl.DateTimeFormatOptions = { day: 'numeric', month: 'long', year: 'numeric' };
        return new Intl.DateTimeFormat('en-US', options).format(date);
    }


    return (
        <div className={styles['news-section']}>
            <div className={styles['news-section-category-bar']}>
                <div>
                    <span className={styles['ns-category-title']}>
                        {props.sectionTitle ? props.sectionTitle : "News"}
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
                            {
                                props.articles?.[0]?.title
                                ? props.articles?.[0]?.title
                                : (
                                    "Error Loading Article Title"
                                )
                            }
                            
                        </span>
                    </div>
                    <div className={styles['main-story-description-container']}>
                        <span className={styles['ms-description']}>
                            {
                                props.articles?.[0]?.content
                                ? props.articles?.[0]?.content
                                : (
                                    "Error Loading Article Content"
                                )
                            }
                        </span>
                    </div>
                    <div className={styles['main-story-date-container']}>
                        <span className={styles['ms-date-text']}>
                            {
                                props.articles?.[0]?.tickers
                                ? props.articles?.[0]?.tickers
                                : (
                                    "Ticker Error"
                                )
                            } - 
                            {
                                props.articles?.[0]?.datePosted
                                ? ` ${formatEasyReadDate(
                                    new Date(props.articles?.[0]?.datePosted)
                                )}`
                                : (
                                    "Error Loading Date Posted"
                                )
                            }
                        </span>
                    </div>
                </div>
            </div>
            <div className={styles['more-news-title-container']}>
                <span className={styles['more-news-title']}>
                    {props.moreNewsTitle ? props.moreNewsTitle : "More News"}
                </span>
            </div>
            <div className={styles['more-stories-container']}>


                {
                    props.articles?.slice(1,4)?.map((article: any, i: number) => {
                        return (
                            <div 
                                className={styles['story-row']}
                                key={`story-row-${i}`}
                            >
                                <div className={styles['sr-l']}>
                                    <div className={styles['sr-image']}></div>
                                </div>
                                <div className={styles['sr-r']}>
                                    <div className={styles['sr-r-t']}>
                                        <span className={styles['story-row-title']}>
                                            {
                                                article?.title
                                                ? article?.title
                                                : (
                                                    "Error Loading Article Title"
                                                )
                                            }
                                        </span>
                                        <span className={styles['story-row-date']}>
                                            {
                                                article?.tickers
                                                ? article?.tickers
                                                : (
                                                    "Ticker Error"
                                                )
                                            } - 
                                            {
                                                article?.datePosted
                                                ? ` ${formatEasyReadDate(
                                                    new Date(article?.datePosted)
                                                )}`
                                                : (
                                                    "Error Loading Date Posted"
                                                )
                                            }
                                        </span>
                                    </div>   
                                    <div className={styles['sr-r-b']}>
                                        <span className={styles['story-row-description']}>
                                            {
                                                article?.content
                                                ? article?.content
                                                : (
                                                    "Error Loading Article Content"
                                                )
                                            }
                                            {/* Intuitive Surgical (NASDAQ:ISRG), renowned for its robotic-assisted surgical technology, reported 
                                            its fourth-quarter earnings, exceeding analyst expectations. The company's total revenue for the 
                                            quart... */}
                                        </span>
                                    </div>   
                                </div>
                            </div>
                        )
                    }) || []
                }


                {/* <div className={styles['story-row']}>
                    <div className={styles['sr-l']}>
                        <div className={styles['sr-image']}></div>
                    </div>
                    <div className={styles['sr-r']}>
                        <div className={styles['sr-r-t']}>
                            <span className={styles['story-row-title']}>
                                {
                                    props.articles?.[1]?.title
                                    ? props.articles?.[1]?.title
                                    : (
                                        "Error Loading Article Title"
                                    )
                                }
                            </span>
                            <span className={styles['story-row-date']}>
                                {
                                    props.articles?.[1]?.tickers
                                    ? props.articles?.[1]?.tickers
                                    : (
                                        "Ticker Error"
                                    )
                                } - 
                                {
                                    props.articles?.[1]?.datePosted
                                    ? ` ${formatEasyReadDate(
                                        new Date(props.articles?.[1]?.datePosted)
                                    )}`
                                    : (
                                        "Error Loading Date Posted"
                                    )
                                }
                            </span>
                        </div>   
                        <div className={styles['sr-r-b']}>
                            <span className={styles['story-row-description']}>
                                {
                                    props.articles?.[1]?.content
                                    ? props.articles?.[1]?.content
                                    : (
                                        "Error Loading Article Content"
                                    )
                                }
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
                                {
                                    props.articles?.[2]?.title
                                    ? props.articles?.[2]?.title
                                    : (
                                        "Error Loading Article Title"
                                    )
                                }
                            </span>
                            <span className={styles['story-row-date']}>
                                {
                                    props.articles?.[2]?.tickers
                                    ? props.articles?.[2]?.tickers
                                    : (
                                        "Ticker Error"
                                    )
                                } - 
                                {
                                    props.articles?.[2]?.datePosted
                                    ? ` ${formatEasyReadDate(
                                        new Date(props.articles?.[2]?.datePosted)
                                    )}`
                                    : (
                                        "Error Loading Date Posted"
                                    )
                                }
                            </span>
                        </div>   
                        <div className={styles['sr-r-b']}>
                            <span className={styles['story-row-description']}>
                                {
                                    props.articles?.[2]?.content
                                    ? props.articles?.[2]?.content
                                    : (
                                        "Error Loading Article Content"
                                    )
                                }
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
                                {
                                    props.articles?.[3]?.title
                                    ? props.articles?.[3]?.title
                                    : (
                                        "Error Loading Article Title"
                                    )
                                }
                            </span>
                            <span className={styles['story-row-date']}>
                                {
                                    props.articles?.[3]?.tickers
                                    ? props.articles?.[3]?.tickers
                                    : (
                                        "Ticker Error"
                                    )
                                } - 
                                {
                                    props.articles?.[3]?.datePosted
                                    ? ` ${formatEasyReadDate(
                                        new Date(props.articles?.[3]?.datePosted)
                                    )}`
                                    : (
                                        "Error Loading Date Posted"
                                    )
                                }
                            </span>
                        </div>   
                        <div className={styles['sr-r-b']}>
                            <span className={styles['story-row-description']}>
                                {
                                    props.articles?.[3]?.content
                                    ? props.articles?.[3]?.content
                                    : (
                                        "Error Loading Article Content"
                                    )
                                }
                            </span>
                        </div>   
                    </div>
                </div> */}


            </div>
        </div>
    );
}
