import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';
import styles from '../../styles/pages/news/business.module.css'
import Header from '@/components/Header';
import TickerBanner from '@/components/TickerBanner';
import IndexBanner from '@/components/IndexBanner';
import { Inter } from "next/font/google";
import BusinessNew from '@/components/news/BusinessNews';

const inter = Inter({ subsets: ["latin"] });



export default function BusinessNews() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Business News | WorldView Insights
                </title>
                <meta
                    name="description"
                    content="Top Business News Stories - WorldView Insights"
                />
            </Head>
            <div className={inter.className}>
                <Header/>
                <TickerBanner/>
                <IndexBanner/>
                <div className={styles['business-news-component']}>
                    <div>

                    </div>
                    <div>
                        <div className={styles['bn-title-row']}>
                            <span className={styles['business-news-title']}>
                                Business News
                            </span>
                        </div>
                        <div className={styles['business-news-container']}>
                            <BusinessNew
                                page={4}
                            />
                            <BusinessNew
                                page={3}
                                sectionTitle={"More Business News"}
                            />
                            <BusinessNew
                                page={2}
                                sectionTitle={"More Business News"}
                            />
                            <BusinessNew
                                page={1}
                                sectionTitle={"More Business News"}
                            />
                        </div>
                    </div>
                    <div>

                    </div>
                </div>
            </div>
        </TrackingProvider>
    )
}