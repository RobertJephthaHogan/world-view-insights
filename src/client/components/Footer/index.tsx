import React from 'react'
import styles from '../../styles/components/Footer.module.css'
import { getConfig } from '@/config/Constants'
import { useRouter } from 'next/navigation'



export default function Footer() {

    const router = useRouter()
    const config = getConfig()

    
    const handleMenuItemClick = (event: any, path: string) => {
        //TODO: Integrate Analytics Tracking Here

        // Prevent the default href link behavior 
        event.preventDefault();

        router.push(path);
    };


    return (
        <div className={styles['homepage-footer']}>
            <div className={styles['footer-top']}>
                <div className={styles['footer-top-content-wrapper']}>
                    <div className={styles['ft-left']}>
                        <a 
                            className={styles['logo-container-anchor']}
                            href={`${config.clientUrl}`}
                            onClick={(e) => handleMenuItemClick(e, '/')}
                        >
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
                        </a>
                    </div>
                    <div className={styles['ft-right']}>
                        <div className={styles['ft-menu']}>
                            <div className={styles['ft-menu-title-container']}>
                                <span className={styles['ft-menu-title']}>
                                    Platform
                                </span>
                            </div>
                            <div className={styles['ft-menu-option-container']}>
                                <a
                                    className={styles['ft-mo-anchor']}
                                    href={`${config.clientUrl}`}
                                    onClick={(e) => handleMenuItemClick(e, '/')}
                                >
                                    <span>
                                        Homepage
                                    </span>
                                </a>
                                <a
                                    className={styles['ft-mo-anchor']}
                                    href={`${config.clientUrl}about`}
                                    onClick={(e) => handleMenuItemClick(e, '/about')}
                                >
                                    <span>
                                        About
                                    </span>
                                </a>
                                <a
                                    className={styles['ft-mo-anchor']}
                                    href={`${config.clientUrl}privacy-policy`}
                                    onClick={(e) => handleMenuItemClick(e, '/privacy-policy')}
                                >
                                    <span>
                                        Privacy Policy
                                    </span>
                                </a>
                            </div>
                        </div>
                        <div className={styles['ft-menu']}>
                            <div className={styles['ft-menu-title-container']}>
                                <span className={styles['ft-menu-title']}>
                                    News
                                </span>
                            </div>
                            <div className={styles['ft-menu-option-container']}>
                                <a
                                    className={styles['ft-mo-anchor']}
                                    href={`${config.clientUrl}news/latest`}
                                    onClick={(e) => handleMenuItemClick(e, '/news/latest')}
                                >
                                    <span>
                                        Latest News
                                    </span>
                                </a>
                                <a
                                    className={styles['ft-mo-anchor']}
                                    href={`${config.clientUrl}news/business`}
                                    onClick={(e) => handleMenuItemClick(e, '/news/business')}
                                >
                                    <span>
                                        Business News
                                    </span>
                                </a>
                                <a
                                    className={styles['ft-mo-anchor']}
                                    href={`${config.clientUrl}news/tech`}
                                    onClick={(e) => handleMenuItemClick(e, '/news/tech')}
                                >
                                    <span>
                                        Tech News
                                    </span>
                                </a>
                            </div>
                        </div>
                        <div className={styles['ft-menu']}>
                            <div className={styles['ft-menu-title-container']}>
                                <span className={styles['ft-menu-title']}>
                                    Markets
                                </span>
                            </div>
                            <div className={styles['ft-menu-option-container']}>
                                <a
                                    className={styles['ft-mo-anchor']}
                                    href={`${config.clientUrl}markets/overview`}
                                    onClick={(e) => handleMenuItemClick(e, '/markets/overview')}
                                >
                                    <span className={styles['ft-menu-option']}>
                                        Overview
                                    </span>
                                </a>
                                <a
                                    className={styles['ft-mo-anchor']}
                                    href={`${config.clientUrl}markets/stocks`}
                                    onClick={(e) => handleMenuItemClick(e, '/markets/stocks')}
                                >
                                    <span className={styles['ft-menu-option']}>
                                        Stocks
                                    </span>
                                </a>
                                <a
                                    className={styles['ft-mo-anchor']}
                                    href={`${config.clientUrl}markets/insider-tx`}
                                    onClick={(e) => handleMenuItemClick(e, '/markets/insider-tx')}
                                >
                                    <span className={styles['ft-menu-option']}>
                                        Insider Transactions
                                    </span>
                                </a>
                            </div>
                        </div>
                        <div className={styles['ft-menu']}>
                            <div className={styles['ft-menu-title-container']}>
                                <span className={styles['ft-menu-title']}>
                                    Company
                                </span>
                            </div>
                            <div className={styles['ft-menu-option-container']}>
                                <a
                                    className={styles['ft-mo-anchor']}
                                    href={`${config.clientUrl}about`}
                                    onClick={(e) => handleMenuItemClick(e, '/about')}
                                >
                                    <span className={styles['ft-menu-option']}>
                                        About
                                    </span>
                                </a>
                                <a
                                    className={styles['ft-mo-anchor']}
                                    href={`${config.clientUrl}contact`}
                                    onClick={(e) => handleMenuItemClick(e, '/contact')}
                                >
                                    <span className={styles['ft-menu-option']}>
                                        Contact
                                    </span>
                                </a>
                                <a
                                    className={styles['ft-mo-anchor']}
                                    href={`${config.clientUrl}contact`}
                                    onClick={(e) => handleMenuItemClick(e, '/contact')}
                                >
                                    <span className={styles['ft-menu-option']}>
                                        Support
                                    </span>
                                </a>
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
                    <a
                        className={styles['ps-anchor']}
                        href={`${config.clientUrl}privacy-policy`}
                        onClick={(e) => handleMenuItemClick(e, '/privacy-policy')}
                    >
                        <span className={styles['fbl-pp-text']}>
                            Privacy Settings
                        </span>
                    </a>
                </div>
            </div>
        </div>
    )
}