import React, { useState } from 'react'
import './styles.css'
import { Button, Input } from 'antd'
import InfoCircleOutlined from '@ant-design/icons/InfoCircleOutlined'
import CaretDownOutlined from '@ant-design/icons/CaretDownOutlined'


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
        <div className='header'>
            <div className='header-content'>
                <div className='hc-left'>
                    <div className='logo-container'>
                        <div className='wvi-icon-dark'/>
                        <div>
                            <span className='wvi-logo-text'>
                                WorldView Insights
                            </span>
                        </div>
                    </div>
                    <div className='search-container'>
                        <Search 
                            placeholder="Search Site Resource or Stock" 
                            onSearch={onSearch} 
                            value={searchText}
                            onChange={(e) => handleSearchTextChange(e?.target?.value)}
                        />
                    </div>
                </div>
                <div className='hc-right'>
                <div className='hc-menu-item'>
                    <span>News</span>
                    <CaretDownOutlined className='hc-mi-caret'/>
                    <div className="dropdown-content">
                        <a href="#news1">Latest News</a>
                        <a href="#news2">Business News</a>
                        <a href="#news3">Political News</a>
                        <a href="#news4">Tech News</a>
                    </div>
                </div>
                    <div className='hc-menu-item'>
                        <span>
                            Markets
                        </span>
                        <CaretDownOutlined className='hc-mi-caret'/>
                        <div className="dropdown-content">
                            <a href="#markets1">Overview</a>
                            <a href="#markets1">Currencies</a>
                            <a href="#markets1">Stocks</a>
                            <a href="#markets1">Sectors</a>
                            <a href="#markets1">Interest Rates</a>
                            <a href="#markets1">Market Updates</a>
                            <a href="#markets1">Mortgage Data</a>
                        </div>
                    </div>
                    <div className='hc-menu-item'>
                        <span>
                            Tools
                        </span>
                        <CaretDownOutlined className='hc-mi-caret'/>
                        <div className="dropdown-content">
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
                    <div className='hc-login-item'>
                        <Button className='login-btn'>
                            <span className='login-btn-text'>
                                Login
                            </span>
                        </Button>
                    </div>
                </div>
            </div>
        </div>
    )
}