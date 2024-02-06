import React from 'react'
import styles from '../../styles/components/Footer.module.css'



export default function Footer() {

    return (
        <div className={styles['homepage-footer']}>
            <div className={styles['footer-top']}>
                <div className={styles['footer-top-content-wrapper']}>
                    <div className={styles['ft-left']}>
                        <div 
                            className={styles['logo-container']}
                            //onClick={() => handleLogoClick()}
                        >
                            <div className={styles['logo-container-left']}>
                                <div className={styles['logo-img']}>

                                </div>
                            </div>
                            <div className={styles['logo-title-container']}>
                                <div>
                                    <span  className={styles['title-text-top']}>
                                        WorldView
                                    </span>
                                </div>
                                <div>
                                    <span className={styles['title-text-bottom']}>
                                        Insights
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className={styles['ft-right']}>
                        <div className={styles['ft-menu']}>
                            <div className={styles['ft-menu-title-container']}>
                                <span className={styles['ft-menu-title']}>
                                    Platform
                                </span>
                            </div>
                            <div className={styles['ft-menu-option-container']}>
                                <span 
                                    className={styles['ft-menu-option']}
                                    //onClick={() => handleAboutSectionNavigation('inbox')}
                                >
                                    Homepage
                                </span>
                                <span 
                                    className={styles['ft-menu-option']}
                                    //onClick={() => handleAboutSectionNavigation('contacts')}
                                >
                                    About
                                </span>
                                <span 
                                    className={styles['ft-menu-option']}
                                    //onClick={() => handleAboutSectionNavigation('campaigns')}
                                >
                                    Privacy Policy
                                </span>
                            </div>
                        </div>
                        <div className={styles['ft-menu']}>
                            <div className={styles['ft-menu-title-container']}>
                                <span className={styles['ft-menu-title']}>
                                    News
                                </span>
                            </div>
                            <div className={styles['ft-menu-option-container']}>
                                <span 
                                    className={styles['ft-menu-option']}
                                    //onClick={() => handleAboutSectionNavigation('email')}
                                >
                                    Latest News
                                </span>
                                <span 
                                    className={styles['ft-menu-option']}
                                    //onClick={() => handleAboutSectionNavigation('sms')}
                                >
                                    Business News
                                </span>
                                <span 
                                    className={styles['ft-menu-option']}
                                    //onClick={() => handleAboutSectionNavigation('voice')}
                                >
                                    Tech News
                                </span>
                            </div>
                        </div>
                        <div className={styles['ft-menu']}>
                            <div className={styles['ft-menu-title-container']}>
                                <span className={styles['ft-menu-title']}>
                                    Markets
                                </span>
                            </div>
                            <div className={styles['ft-menu-option-container']}>
                                <span className={styles['ft-menu-option']}>
                                    Overview
                                </span>
                                <span className={styles['ft-menu-option']}>
                                    Stocks
                                </span>
                                <span className={styles['ft-menu-option']}>
                                    Insider Transactions
                                </span>
                            </div>
                        </div>
                        <div className={styles['ft-menu']}>
                            <div className={styles['ft-menu-title-container']}>
                                <span className={styles['ft-menu-title']}>
                                    Company
                                </span>
                            </div>
                            <div className={styles['ft-menu-option-container']}>
                                <span className={styles['ft-menu-option']}>
                                    About
                                </span>
                                <span className={styles['ft-menu-option']}>
                                    Contact
                                </span>
                                <span className={styles['ft-menu-option']}>
                                    Support
                                </span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div className={styles['footer-divider']}/>
            <div className={styles['footer-bottom']}>
                <div className={styles['footer-bottom-left']}>
                    <span className={styles['fbl-cr-text']}>
                        © 2024 WorldView Insights. All rights reserved.
                    </span>
                </div>
                <div className={styles['footer-bottom-right']}>
                    <span className={styles['fbl-pp-text']}>
                        Privacy Settings
                    </span>
                </div>
            </div>
        </div>
    )
}