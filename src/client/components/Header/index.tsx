'use client'

import React, { useState } from 'react'
import dynamic from 'next/dynamic';
//import { Button, Input } from 'antd'
import InfoCircleOutlined from '@ant-design/icons/InfoCircleOutlined'
import CaretDownOutlined from '@ant-design/icons/CaretDownOutlined'
import styles from '../../styles/components/Header.module.css'
import { useRouter } from 'next/navigation'


const Button = dynamic(
    () => import('antd').then(mod => mod.Button),
    { ssr: false }
);

const Input = dynamic(
    () => import('antd').then(mod => mod.Input),
    { ssr: false }
);

const Search = dynamic(
    () => import('antd').then(mod => mod.Input.Search),
    { ssr: false }
);

// const { Search } = Input;




export default function Header() {

    const [searchText, setSearchText] = useState<string>('')
    const router = useRouter()

    const handleNavigationClick = (path: string) => {
        router.push(path);
    };

    function onSearch() {
        console.log('onSearch!', searchText)
    }

    function handleSearchTextChange(value: string) {
        setSearchText(value)
    }

    return (
        <div className={styles['header']}>
            <div className={styles['header-content']}>
            <div className={styles['hc-left']}>
                <div 
                    className={styles['logo-container']}
                    onClick={() => handleNavigationClick('/')}
                >
                        <div className={styles['wvi-icon-dark']}/>
                        <div>
                            <span className={styles['wvi-logo-text']}>
                                WorldView Insights
                            </span>
                        </div>
                    </div>
                    <div className={styles['search-container']}>
                        <Search 
                            placeholder="Search Site Resource or Stock" 
                            onSearch={onSearch} 
                            value={searchText}
                            onChange={(e) => handleSearchTextChange(e?.target?.value)}
                        />
                    </div>
                </div>
                <div className={styles['hc-right']}>
                <div className={styles['hc-menu-item']}>
                    <span>News</span>
                    <CaretDownOutlined className={styles['hc-mi-caret']}/>
                    <div className={styles["dropdown-content"]}>
                        <a onClick={() => handleNavigationClick('/news/latest')}>
                            Latest News
                        </a>
                        <a onClick={() => handleNavigationClick('/news/business')}>
                            Business News
                        </a>
                        <a onClick={() => handleNavigationClick('/news/politics')}>
                            Political News
                        </a>
                        <a onClick={() => handleNavigationClick('/news/tech')}>
                            Tech News
                        </a>
                    </div>
                </div>
                    <div className={styles['hc-menu-item']}>
                        <span>
                            Markets
                        </span>
                        <CaretDownOutlined className={styles['hc-mi-caret']}/>
                        <div className={styles["dropdown-content"]}>
                            <div className={styles['dropdown-panel']}>
                                <div>
                                    <a onClick={() => handleNavigationClick('/markets/overview')}>
                                        Overview
                                    </a>
                                    <a onClick={() => handleNavigationClick('/markets/currencies')}>
                                        Currencies
                                    </a>
                                    <a onClick={() => handleNavigationClick('/markets/stocks')}>
                                        Stocks
                                    </a>
                                    <a onClick={() => handleNavigationClick('/markets/sectors')}>
                                        Sectors
                                    </a>
                                    <a onClick={() => handleNavigationClick('/markets/interest-rates')}>
                                        Interest Rates
                                    </a>
                                    <a onClick={() => handleNavigationClick('/markets/insider-tx')}>
                                        Insider Tx Viewer
                                    </a>
                                    <a onClick={() => handleNavigationClick('/markets/updates')}>
                                        Market Updates
                                    </a>
                                    <a href="#markets1">Mortgage Data</a>
                                </div>
                                <div className={styles['dp-col']}>
                                    <a onClick={() => handleNavigationClick('/markets/leaders')}>
                                        Market Leaders
                                    </a>
                                    <a onClick={() => handleNavigationClick('/markets/gainers')}>
                                        Gainers
                                    </a>
                                    <a onClick={() => handleNavigationClick('/markets/losers')}>
                                        Losers
                                    </a>
                                    <a onClick={() => handleNavigationClick('/markets/active')}>
                                        Most Active
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className={styles['hc-menu-item']}>
                        <span>
                            Tools
                        </span>
                        <CaretDownOutlined className={styles['hc-mi-caret']}/>
                        <div className={styles["dropdown-content"]}>
                            <a href="#markets1">Calculators</a>
                        </div>
                    </div>
                    {/* <div className='hc-menu-item'>
                        <span>
                            Mortgages
                        </span>
                        <CaretDownOutlined className='hc-mi-caret'/>
                    </div> */}
                    <div className={styles['hc-login-item']}>
                        <Button className={styles['login-btn']}>
                            <span className={styles['login-btn-text']}>
                                Login
                            </span>
                        </Button>
                    </div>
                </div>
            </div>
        </div>
    )
}