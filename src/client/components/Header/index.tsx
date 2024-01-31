'use client'

import React, { useState } from 'react'
import { Button, Input } from 'antd'
import InfoCircleOutlined from '@ant-design/icons/InfoCircleOutlined'
import CaretDownOutlined from '@ant-design/icons/CaretDownOutlined'
import styles from '../../styles/components/Header.module.css'


const { Search } = Input;


export default function Header() {

    const [searchText, setSearchText] = useState<string>('')

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
                <div className={styles['logo-container']}>
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
                        <a href="#news1">Latest News</a>
                        <a href="#news2">Business News</a>
                        <a href="#news3">Political News</a>
                        <a href="#news4">Tech News</a>
                    </div>
                </div>
                    <div className={styles['hc-menu-item']}>
                        <span>
                            Markets
                        </span>
                        <CaretDownOutlined className={styles['hc-mi-caret']}/>
                        <div className={styles["dropdown-content"]}>
                            <a href="#markets1">Overview</a>
                            <a href="#markets1">Currencies</a>
                            <a href="#markets1">Stocks</a>
                            <a href="#markets1">Sectors</a>
                            <a href="#markets1">Interest Rates</a>
                            <a href="#markets1">Market Updates</a>
                            <a href="#markets1">Mortgage Data</a>
                        </div>
                    </div>
                    <div className={styles['hc-menu-item']}>
                        <span>
                            Tools
                        </span>
                        <CaretDownOutlined className={styles['hc-mi-caret']}/>
                        <div className={styles["dropdown-content"]}>
                            <a href="#markets1">Insider Tx Viewer</a>
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