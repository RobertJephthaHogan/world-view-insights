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
    "current mortgage rates",
    "best stocks to buy",
    "home buying tips",
    "real estate market analysis",
    "is now a good time to buy a house",
    "latest business news",
    "market updates",
    "stock market news",
    "technology updates",
    "tech industry news",
    "advanced stock scanner",
    "stock value checker",
    "stock price for XYZ", // replace XYZ with specific tickers
    "stock market charts",
    "interactive stock analysis",
    "investment opportunities",
    "financial market insights",
    "economic news",
    "stock trading tips",
    "tech stocks",
    "stock market trends",
    "real estate investment advice",
    "mortgage rate trends",
    "financial planning",
    "stock portfolio management",
    "technology sector analysis",
    "business strategy news",
    "stock market analysis tools",
    "personal finance tips"
];

export const metadata: Metadata = {
    title: "WorldView Insights",
    description: "All in one source for news, market data, investing tools, overall insights",
    keywords: keywordSearchTerms
};


export default function Homepage() {

    return (
        <TrackingProvider>
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
                        <NewsSection/>
                        <NewsSection/>
                        <NewsSection/>
                    </div>
                    <div className={styles['hpb-r']}>
                        <NotableQuotes/>
                    </div>
                </div>
            </div>
        </TrackingProvider>
    )
}