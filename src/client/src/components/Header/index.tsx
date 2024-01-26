import React from 'react'
import './styles.css'


export default function Header() {

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
                        search
                    </div>
                </div>
                <div className='hc-right'>
                    Right
                </div>
            </div>
        </div>
    )
}