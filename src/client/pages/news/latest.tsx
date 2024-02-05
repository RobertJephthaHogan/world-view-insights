import { TrackingProvider } from '@/providers/TrackingProvider'
import React from 'react'
import Head from 'next/head';
import styles from '../../styles/pages/news/latest.module.css'
import Header from '@/components/Header';
import TickerBanner from '@/components/TickerBanner';
import IndexBanner from '@/components/IndexBanner';
import { Inter } from "next/font/google";
import BusinessNew from '@/components/news/BusinessNews';


const inter = Inter({ subsets: ["latin"] });



export default function LatestNews() {
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Latest News | WorldView Insights
                </title>
                <meta
                    name="description"
                    content="Top Latest News Stories - WorldView Insights"
                />
            </Head>
            <div className={inter.className}>
                <Header/>
                <TickerBanner/>
                <IndexBanner/>
                <div className={styles['latest-news-component']}>
                    <div>

                    </div>
                    <div>
                        <div className={styles['ln-title-row']}>
                            <span className={styles['latest-news-title']}>
                                Latest News
                            </span>
                        </div>
                        <div className={styles['news-container']}>
                            <BusinessNew
                                page={1}
                            />
                            <BusinessNew
                                page={2}
                                sectionTitle={"More Business News"}
                            />
                            <BusinessNew
                                page={3}
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