'use client'

import React, { useState } from 'react'
import dynamic from 'next/dynamic';
//import { Button, Input } from 'antd'
import InfoCircleOutlined from '@ant-design/icons/InfoCircleOutlined'
import CaretDownOutlined from '@ant-design/icons/CaretDownOutlined'
import styles from '../../styles/components/Header.module.css'
import { useRouter } from 'next/navigation'
import { getConfig } from '@/config/Constants';
import { FaCaretDown } from 'react-icons/fa';
import { GoSearch } from "react-icons/go";
import { CiMenuBurger } from "react-icons/ci";


const Button = dynamic(
    () => import('antd').then(mod => mod.Button),
    { ssr: false }
);

const Modal = dynamic(
    () => import('antd').then(mod => mod.Modal),
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
    const [ searchModalOpen, setSearchModalOpen] = useState<boolean>(false)
    const router = useRouter()
    const config = getConfig()


    const handleNavigationClick = (event: any, path: string) => {
        //TODO: Integrate Analytics Tracking Here

        // Prevent the default href link behavior 
        event.preventDefault();

        router.push(path);
    };



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
                        
                        <Button
                            onClick={() => setSearchModalOpen(true)}
                        >
                            <GoSearch />
                        </Button>
                    </div>
                </div>
                <div className={styles['hc-right']}>
                    <div className={styles['mobile-menu-container']}>
                        <Button
                            onClick={() => console.log('clicked')}
                        >
                            <CiMenuBurger />
                        </Button>
                    </div>
                <div className={styles['hc-parent-menu']}>
                    <span className={styles['hc-parent-menu-title']}>
                        News
                    </span>
                    {/* <FaCaretDown /> */}
                    <FaCaretDown />
                    <div className={styles["dropdown-content"]}>
                        <a 
                            onClick={(e) => handleNavigationClick(e, '/news/latest')}
                            href={`${config.clientUrl}news/latest`}
                        >
                            <span className={styles["hc-menu-item"]}>
                                Latest News
                            </span>
                        </a>
                        <a 
                            onClick={(e) => handleNavigationClick(e, '/news/business')}
                            href={`${config.clientUrl}news/business`}
                        >
                            <span className={styles["hc-menu-item"]}>
                                Business News
                            </span>
                        </a>
                        <a 
                            onClick={(e) => handleNavigationClick(e, '/news/politics')}
                            href={`${config.clientUrl}news/politics`}
                        >
                            <span className={styles["hc-menu-item"]}>
                                Political News
                            </span>
                        </a>
                        <a 
                            onClick={(e) => handleNavigationClick(e, '/news/tech')}
                            href={`${config.clientUrl}news/tech`}
                        >
                            <span className={styles["hc-menu-item"]}>
                                Tech News
                            </span>
                        </a>
                    </div>
                </div>
                    <div className={styles['hc-parent-menu']}>
                        <span className={styles['hc-parent-menu-title']}>
                            Markets
                        </span>
                        <FaCaretDown />
                        <div className={styles["dropdown-content"]}>
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
                                    <span className={styles["hc-menu-item"]}>
                                        Market Leaders
                                    </span>
                                </a>
                                <a 
                                    onClick={(e) => handleNavigationClick(e, '/markets/active')}
                                    href={`${config.clientUrl}markets/active`}
                                >
                                    <span className={styles["hc-menu-item"]}>
                                        Most Active
                                    </span>
                                </a>
                                <a 
                                    onClick={(e) => handleNavigationClick(e, '/markets/gainers')}
                                    href={`${config.clientUrl}markets/gainers`}
                                >
                                    <span className={styles["hc-menu-item"]}>
                                        Gainers
                                    </span>
                                </a>
                                <a 
                                    onClick={(e) => handleNavigationClick(e, '/markets/losers')}
                                    href={`${config.clientUrl}markets/losers`}
                                >
                                    <span className={styles["hc-menu-item"]}>
                                        Losers
                                    </span>
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
                        </div>
                    </div>
                    <div className={styles['hc-parent-menu']}>
                        <span className={styles['hc-parent-menu-title']}>
                            Tools
                        </span>
                        <FaCaretDown />
                        <div className={styles["dropdown-content"]}>
                            <a 
                                onClick={(e) => handleNavigationClick(e, '/markets/insider-tx')}
                                href={`${config.clientUrl}markets/insider-tx`}
                            >
                                <span className={styles["hc-menu-item"]}>
                                    Insider Tx Viewer
                                </span>
                            </a>
                        </div>
                    </div>
                    {/* <div className='hc-parent-menu'>
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
            <Modal 
                title="Search Stocks or Website Resources" 
                open={searchModalOpen} 
                onOk={() => setSearchModalOpen(false)} 
                onCancel={() => setSearchModalOpen(false)}
            >
                <p>Search Coming Soon</p>
                
            </Modal>
        </div>
    )
}