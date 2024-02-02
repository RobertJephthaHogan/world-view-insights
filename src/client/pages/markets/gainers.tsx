import { TrackingProvider } from '@/providers/TrackingProvider'
import React, { useEffect, useState } from 'react'
import Head from 'next/head';
import { Inter } from "next/font/google";
import Header from '@/components/Header';
import { useRouter } from 'next/navigation'
import dynamic from 'next/dynamic';
import styles from '../../styles/pages/markets/gainers.module.css'
import PriceTable from '@/components/PriceTable';
import { dataService } from '@/services/data.service';
// import { Radio } from 'antd';


const inter = Inter({ subsets: ["latin"] });

const Radio = dynamic(() => import('antd').then(mod => mod.Radio));
const RadioButton = dynamic(() => import('antd').then(mod => mod.Radio.Button));
const RadioGroup = dynamic(() => import('antd').then(mod => mod.Radio.Group));

export default function Gainers() {

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


        //TODO: if tableType === 'price', get table data from /data/gainers_price_table
        if (tableType === 'price') {
            dataService.getGainersPriceTable()
                .then((resp: any) => {
                    console.log(resp)
                    setTableData(resp)
                })
                .catch((error: any) => {
                    console.log('error', error)
                })
        }
        

        //TODO: if tableType === 'performance', get table data from /data/gainers_performance_table

        //TODO: if tableType === 'technical', get table data from /data/gainers_technicals_table

        //TODO: if tableType === 'fundamental', get table data from /data/gainers_fundamentals_table

    }, [tableType])


    return (
        <TrackingProvider>
            <Head>
                <title>
                    WorldView Insights | Gainers
                </title>
            </Head>
            <div className={inter.className}>
                <Header/>
                <div className={styles['gainers-component']}>
                    <div className={styles['gc-left']}>
                        {/* add left column content here */}
                    </div>
                    <div className={styles['gc-center']}>
                        <div>
                            <div className={styles['tgt-container']}>
                                <span className={styles['top-gainers-title']}>
                                    Top Gainers - United Stated Stocks
                                </span>
                            </div>
                            <div className={styles['tg-divider']}/>
                            <div className={styles['tgd-container']}>
                                <span>
                                    Explore the market movers and top stock gainers 
                                    in the US stock market, capturing notable surges 
                                    in stock prices. Stay informed about these movers, 
                                    leveraging real-time data and historical trends 
                                    to make informed investment decisions.
                                </span>
                            </div>
                        </div>
                        <div className={styles['gc-menu-bar']}>
                            <div 
                                className={styles['gc-menu-item-active']}
                                onClick={() => handleNavigationClick('/markets/gainers')}
                            >
                                <span className={styles['gc-mi-title']}>
                                    Top Gainers
                                </span>
                            </div>
                            <div 
                                className={styles['gc-menu-item']}
                                onClick={() => handleNavigationClick('/markets/losers')}
                            >
                                <span className={styles['gc-mi-title']}>
                                    Top Losers
                                </span>
                            </div>
                            <div 
                                className={styles['gc-menu-item']}
                                onClick={() => handleNavigationClick('/markets/active')}
                            >
                                <span className={styles['gc-mi-title']}>
                                    Most Active
                                </span>
                            </div>
                            <div 
                                className={styles['gc-menu-item']}
                                onClick={() => handleNavigationClick('/markets/leaders')}
                            >
                                <span className={styles['gc-mi-title']}>
                                    Market Leaders
                                </span>
                            </div>
                            <div className={styles['gc-menu-fill']}>
                                
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
                    <div className={styles['gc-right']}>
                        {/* add right column content here */}
                    </div>
                </div> 
            </div>
        </TrackingProvider>
    )
}