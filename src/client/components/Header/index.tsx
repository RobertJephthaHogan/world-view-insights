'use client'

import React, { useState } from 'react'
import dynamic from 'next/dynamic';
//import { Button, Input } from 'antd'
import InfoCircleOutlined from '@ant-design/icons/InfoCircleOutlined'
// import CaretDownOutlined from '@ant-design/icons/CaretDownOutlined'
import styles from '../../styles/components/Header.module.css'
import { useRouter } from 'next/navigation'
import { getConfig } from '@/config/Constants';


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

const CaretDownOutlined = dynamic(() => import('@ant-design/icons').then((mod) => mod.CaretDownOutlined), {
    ssr: false,
});

// const { Search } = Input;




export default function Header() {

    const [searchText, setSearchText] = useState<string>('')
    const router = useRouter()
    const config = getConfig()


    const handleNavigationClick = (event: any, path: string) => {
        //TODO: Integrate Analytics Tracking Here

        // Prevent the default href link behavior 
        event.preventDefault();

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
                    onClick={(e) => handleNavigationClick(e, '/')}
                >
                        <div className={styles['wvi-icon-dark']}/>
                        <div>
                            <span className={styles['wvi-logo-text']}>
                                WorldView Insights
                            </span>
                            <span className={styles['wvi-beta-text']}>
                                Beta
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
                    {/* <CaretDownOutlined className={styles['hc-mi-caret']}/> */}
                    <CaretDownOutlined />
                    <div className={styles["dropdown-content"]}>
                        <a 
                            onClick={(e) => handleNavigationClick(e, '/news/latest')}
                            href={`${config.clientUrl}news/latest`}
                        >
                            Latest News
                        </a>
                        <a 
                            onClick={(e) => handleNavigationClick(e, '/news/business')}
                            href={`${config.clientUrl}news/business`}
                        >
                            Business News
                        </a>
                        <a 
                            onClick={(e) => handleNavigationClick(e, '/news/politics')}
                            href={`${config.clientUrl}news/politics`}
                        >
                            Political News
                        </a>
                        <a 
                            onClick={(e) => handleNavigationClick(e, '/news/tech')}
                            href={`${config.clientUrl}news/tech`}
                        >
                            Tech News
                        </a>
                    </div>
                </div>
                    <div className={styles['hc-menu-item']}>
                        <span>
                            Markets
                        </span>
                        <CaretDownOutlined />
                        <div className={styles["dropdown-content"]}>
                            <div className={styles['dropdown-panel']}>
                                <div>
                                    {/* <a 
                                        onClick={(e) => handleNavigationClick(e, '/markets/overview')}
                                        href={`${config.clientUrl}markets/overview`}
                                    >
                                        Overview
                                    </a>
                                    <a 
                                        onClick={(e) => handleNavigationClick(e, '/markets/currencies')}
                                        href={`${config.clientUrl}markets/currencies`}
                                    >
                                        Currencies
                                    </a> */}
                                    {/* <a 
                                        onClick={(e) => handleNavigationClick(e, '/markets/sectors')}
                                        href={`${config.clientUrl}markets/sectors`}
                                    >
                                        Sectors
                                    </a>
                                    <a 
                                        onClick={(e) => handleNavigationClick(e, '/markets/interest-rates')}
                                        href={`${config.clientUrl}markets/interest-rates`}
                                    >
                                        Interest Rates
                                    </a> */}
                                    {/* <a 
                                        onClick={(e) => handleNavigationClick(e, '/markets/insider-tx')}
                                        href={`${config.clientUrl}markets/insider-tx`}
                                    >
                                        Insider Tx Viewer
                                    </a> */}
                                    <a 
                                        onClick={(e) => handleNavigationClick(e, '/markets/leaders')}
                                        href={`${config.clientUrl}markets/leaders`}
                                    >
                                        Market Leaders
                                    </a>
                                    <a 
                                        onClick={(e) => handleNavigationClick(e, '/markets/active')}
                                        href={`${config.clientUrl}markets/active`}
                                    >
                                        Most Active
                                    </a>
                                    <a 
                                        onClick={(e) => handleNavigationClick(e, '/markets/gainers')}
                                        href={`${config.clientUrl}markets/gainers`}
                                    >
                                        Gainers
                                    </a>
                                    <a 
                                        onClick={(e) => handleNavigationClick(e, '/markets/losers')}
                                        href={`${config.clientUrl}markets/losers`}
                                    >
                                        Losers
                                    </a>
                                    {/* <a 
                                        onClick={(e) => handleNavigationClick(e, '/markets/updates')}
                                        href={`${config.clientUrl}markets/updates`}
                                    >
                                        Market Updates
                                    </a> */}
                                    {/* <a 
                                        onClick={(e) => handleNavigationClick(e, '/markets/stocks')}
                                        href={`${config.clientUrl}markets/stocks`}
                                    >
                                        Stocks
                                    </a> */}
                                    {/* <a href="#markets1">Mortgage Data</a> */}
                                </div>
                                {/* <div className={styles['dp-col']}>
                                    <a 
                                        onClick={(e) => handleNavigationClick(e, '/markets/leaders')}
                                        href={`${config.clientUrl}markets/leaders`}
                                    >
                                        Market Leaders
                                    </a>
                                    <a 
                                        onClick={(e) => handleNavigationClick(e, '/markets/active')}
                                        href={`${config.clientUrl}markets/active`}
                                    >
                                        Most Active
                                    </a>
                                </div> */}
                            </div>
                        </div>
                    </div>
                    <div className={styles['hc-menu-item']}>
                        <span>
                            Tools
                        </span>
                        <CaretDownOutlined />
                        <div className={styles["dropdown-content"]}>
                            <a 
                                onClick={(e) => handleNavigationClick(e, '/markets/insider-tx')}
                                href={`${config.clientUrl}markets/insider-tx`}
                            >
                                Insider Tx Viewer
                            </a>
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