import { TrackingProvider } from '@/providers/TrackingProvider'
import React, { useEffect, useState } from 'react'
import Head from 'next/head';
import Header from '@/components/Header';
import TickerBanner from '@/components/TickerBanner';
import { Inter } from "next/font/google";
import styles from '../../../styles/pages/markets/insider-tx.module.css'
import ComingSoon from '@/components/ComingSoon';
import {formFourService} from '@/services/formFour.service';
import InsiderTxTable from '@/features/insider-tx/InsiderTxTable';

const inter = Inter({ subsets: ["latin"] });


export default function InsiderTransactions() {

    const [transactions, setTransactions] = useState<any[]>([])

    useEffect(() => {

        formFourService.getPurchasesAndSales(200, 1)
            .then((resp: any) => {
                console.log('form fours:', resp)
                setTransactions(resp.data)
            })
            .catch((error: any) => {
                console.error("error getting form fours", error)
            })

    }, [])

    return (
        <TrackingProvider>
            <Head>
                <title>
                    Insider Transactions | WorldView Insights
                </title>
                <meta
                    name="description"
                    content="Form 4 Filings - Insider Transactions "
                />
            </Head>
            <div className={inter.className}>
                <Header/>
                <TickerBanner/>
                <div className={styles['insider-tx-component']}>
                    <div>

                    </div>
                    <div className={styles['itxc-center']}>
                        <div className={styles['itxc-topbar']}>
                            <div className={styles['itxc-topbar-title-container']}>
                                <span className={styles['itxc-topbar-title']}>
                                    Latest Insider Transactions
                                </span>
                            </div>
                            {/* <a className={styles['itxc-tb-btn-anchor']}>
                                <div className={styles['itxc-tb-btn']}>
                                    <span className={styles['tb-btn-txt']}>
                                        Latest Insider Transactions
                                    </span>
                                </div>
                            </a>
                            <a className={styles['itxc-tb-btn-anchor']}>
                                <div className={styles['itxc-tb-btn']}>
                                    <span className={styles['tb-btn-txt']}>
                                        Top Insider Transactions This Week
                                    </span>
                                </div>
                            </a>
                            <a className={styles['itxc-tb-btn-anchor']}>
                                <div className={styles['itxc-tb-btn']}>
                                    <span className={styles['tb-btn-txt']}>
                                        Top 10% Owner Transactions This Week
                                    </span>
                                </div>
                            </a> */}
                        </div>
                        <div className={styles['itxc-table-container']}>
                            <InsiderTxTable
                                tableData={transactions}
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