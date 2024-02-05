import { TrackingProvider } from '@/providers/TrackingProvider'
import React, { useEffect, useState } from 'react'
import Head from 'next/head';
import Header from '@/components/Header';
import { Inter } from "next/font/google";
import { useRouter } from 'next/navigation'
import dynamic from 'next/dynamic';
import styles from '../../styles/pages/markets/leaders.module.css'
import PriceTable from '@/components/PriceTable';
import { dataService } from '@/services/data.service';

const inter = Inter({ subsets: ["latin"] });

const Radio = dynamic(() => import('antd').then(mod => mod.Radio));
const RadioButton = dynamic(() => import('antd').then(mod => mod.Radio.Button));
const RadioGroup = dynamic(() => import('antd').then(mod => mod.Radio.Group));


export default function MarketLeaders() {
    
    const [tableType, setTableType] = useState<string>('price')
    const [tableData, setTableData] = useState<any>([])
    const router = useRouter()


    const handleNavigationClick = (path: string) => {
        router.push(path);
    };

    const handleTableTypeChange = (e: any) => {
        setTableType(e?.target?.value)
    };

        
    useEffect(() => {
        // When the tableType changes we need to fetch the 
        // data for the new table.


        //if tableType === 'price', get table data from /data/leaders_price_table
        if (tableType === 'price') {
            dataService.getLeadersTable()
                .then((resp: any) => {
                    setTableData(resp)
                })
                .catch((error: any) => {
                    console.log('error', error)
                })
        }
        

        //TODO: if tableType === 'performance', get table data from /data/leaders_performance_table

        //TODO: if tableType === 'technical', get table data from /data/leaders_technicals_table

        //TODO: if tableType === 'fundamental', get table data from /data/leaders_fundamentals_table

    }, [tableType])


    
    return (
        <TrackingProvider>
            <Head>
                <title>
                    Market Leaders | WorldView Insights
                </title>
            </Head>
            <div className={inter.className}>
                <Header/>
                <div className={styles['leaders-component']}>
                    <div className={styles['lc-left']}>
                        {/* add left column content here */}
                    </div>
                    <div className={styles['lc-center']}>
                        <div>
                            <div className={styles['tlt-container']}>
                                <span className={styles['top-leaders-title']}>
                                    Top Leaders - United Stated Stocks
                                </span>
                            </div>
                            <div className={styles['tl-divider']}/>
                            <div className={styles['tld-container']}>
                                <span>
                                    Explore the market movers and top stock leaders 
                                    in the US stock market, capturing notable drops 
                                    in stock prices. Stay informed about these movers, 
                                    leveraging real-time data and historical trends 
                                    to make informed investment decisions.
                                </span>
                            </div>
                        </div>
                        <div className={styles['lc-menu-bar']}>
                            <div 
                                className={styles['lc-menu-item-active']}
                                onClick={() => handleNavigationClick('/markets/gainers')}
                            >
                                <span className={styles['lc-mi-title']}>
                                    Top Gainers
                                </span>
                            </div>
                            <div 
                                className={styles['lc-menu-item']}
                                onClick={() => handleNavigationClick('/markets/losers')}
                            >
                                <span className={styles['lc-mi-title']}>
                                    Top Losers
                                </span>
                            </div>
                            <div 
                                className={styles['lc-menu-item']}
                                onClick={() => handleNavigationClick('/markets/active')}
                            >
                                <span className={styles['lc-mi-title']}>
                                    Most Active
                                </span>
                            </div>
                            <div 
                                className={styles['lc-menu-item']}
                                onClick={() => handleNavigationClick('/markets/leaders')}
                            >
                                <span className={styles['lc-mi-title']}>
                                    Market Leaders
                                </span>
                            </div>
                            <div className={styles['lc-menu-fill']}>
                                
                            </div>
                        </div>
                        <div className={styles['table-type-selection-container']}>
                            <RadioGroup
                                onChange={handleTableTypeChange} 
                                defaultValue="price" 
                                value={tableType}
                            >
                                <RadioButton value="price">Price</RadioButton>
                                <RadioButton value="performance">Performance</RadioButton>
                                <RadioButton value="technical">Technical</RadioButton>
                                <RadioButton value="fundamental">Fundamental</RadioButton>
                            </RadioGroup>
                        </div>
                        <div className={styles['table-container']}>
                            {
                                tableType == 'price'
                                ? (
                                    <PriceTable
                                        tableData={tableData}
                                    />
                                ) : null
                            }
                            {
                                tableType == 'performance'
                                ? (
                                    'Coming Soon!'
                                ) : null
                            }
                            {
                                tableType == 'technical'
                                ? (
                                    'Coming Soon!'
                                ) : null
                            }
                            {
                                tableType == 'fundamental'
                                ? (
                                    'Coming Soon!'
                                ) : null
                            }
                        </div>
                    </div>
                    <div className={styles['lc-right']}>
                        {/* add right column content here */}
                    </div>
                </div> 
            </div>
        </TrackingProvider>
    )
}