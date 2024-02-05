import type { Metadata } from "next";
import Header from '../components/Header'
import TickerBanner from '../components/TickerBanner'
import IndexBanner from '../components/IndexBanner'
import NotableQuotes from '../components/NotableQuotes'
import NewsSection from '../components/NewsSection'
import styles from '../styles/page.module.css'
import "../styles/globals.css";
import { Inter } from "next/font/google";
import { TrackingProvider } from "@/providers/TrackingProvider";

const inter = Inter({ subsets: ["latin"] });


const keywordSearchTerms = [
    "Stock Market Data",
    "Market Gainers Today",
    "Market Losers Today",
    "Stock Prices"
];

export const metadata: Metadata = {
    title: "WorldView Insights | Homepage",
    description: "All in one source for news, market data, investing tools, overall insights",
    keywords: keywordSearchTerms
};


export default function Homepage() {

    return (
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
                    {/* <NewsSection/>
                    <NewsSection/>
                    <NewsSection/> */}
                </div>
                <div className={styles['hpb-r']}>
                    <NotableQuotes/>
                </div>
            </div>
        </div>
    )
}