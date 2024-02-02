import { TrackingProvider } from '@/providers/TrackingProvider'
import React, { useState } from 'react'
import Head from 'next/head';
import { Inter } from "next/font/google";
import Header from '@/components/Header';
import { useRouter } from 'next/navigation'
import dynamic from 'next/dynamic';
import styles from '../../styles/pages/markets/gainers.module.css'
// import { Radio } from 'antd';


const inter = Inter({ subsets: ["latin"] });

const Radio = dynamic(() => import('antd').then(mod => mod.Radio));
const RadioButton = dynamic(() => import('antd').then(mod => mod.Radio.Button));
const RadioGroup = dynamic(() => import('antd').then(mod => mod.Radio.Group));

export default function Gainers() {

    const [tableType, setTableType] = useState<string>('price')
    const router = useRouter()


    const handleNavigationClick = (path: string) => {
        router.push(path);
    };

    const handleTableTypeChange = (e: any) => {
        setTableType(e?.target?.value)
    };

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
                        <div>
                            {
                                tableType == 'price'
                                ? (
                                    'Price Table'
                                ) : null
                            }
                            {
                                tableType == 'performance'
                                ? (
                                    'Performance Table'
                                ) : null
                            }
                            {
                                tableType == 'technical'
                                ? (
                                    'Technical Table'
                                ) : null
                            }
                            {
                                tableType == 'fundamental'
                                ? (
                                    'Fundamental Table'
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