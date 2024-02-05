import type { Metadata } from "next";
import Head from 'next/head';
import Header from '../components/Header'
import TickerBanner from '../components/TickerBanner'
import IndexBanner from '../components/IndexBanner'
import NotableQuotes from '../components/NotableQuotes'
import NewsSection from '../components/NewsSection'
import styles from '../styles/page.module.css'
import "../styles/globals.css";
import { Inter } from "next/font/google";
import { TrackingProvider } from "@/providers/TrackingProvider";
import BusinessNew from "@/components/news/BusinessNews";

const inter = Inter({ subsets: ["latin"] });




export default function Homepage() {

    return (
        <TrackingProvider>
            <Head>
                <title>
                    WorldView Insights | Homepage
                </title>
                <meta
                    name="description"
                    content="Top news, market data, investing tools, overall insights"
                />
            </Head>
            <div className={inter.className}>
                <Header/>
                <TickerBanner/>
                <IndexBanner/>
                <div className={styles['homepage-body']}>
                    <div className={styles['hpb-l']}>
                        <div className={styles['hpb-l-title-container']}>
                            <span className={styles['latest-news-title']}>
                                Latest News
                            </span>
                        </div>
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
                    <div className={styles['hpb-r']}>
                        <NotableQuotes/>
                    </div>
                </div>
            </div>
        </TrackingProvider>
    )
}