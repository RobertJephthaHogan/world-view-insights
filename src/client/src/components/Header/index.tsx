import React, { useState } from 'react'
import './styles.css'
import { Input, Tooltip } from 'antd'
import InfoCircleOutlined from '@ant-design/icons/InfoCircleOutlined'


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
                    Right
                </div>
            </div>
        </div>
    )
}