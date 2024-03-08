import Head from 'next/head';
import Header from '@/components/Header';
import TickerBanner from '@/components/TickerBanner';
import { TrackingProvider } from '@/providers/TrackingProvider';
import { GetServerSideProps, NextPage } from 'next';
import { Inter } from "next/font/google";
import { useEffect, useState } from 'react';
import dynamic from 'next/dynamic';
import styles from '../../../styles/pages/markets/insider-tx.module.css'
import SnippetsOutlined from '@ant-design/icons/SnippetsOutlined'
import LinkOutlined from '@ant-design/icons/LinkOutlined'
import { formFourService } from '@/services/formFour.service';
import Link from 'next/link';
import CustomLink from '@/components/CustomLink';


const inter = Inter({ subsets: ["latin"] });

const Button = dynamic(() => import('antd').then(mod => mod.Button));



export const getServerSideProps: GetServerSideProps = async (context) => {
    const { id } = context.params!;

    console.log('filing ID', id)


    try {
        const resp = await formFourService.getFormFourById(id)
	
		return {
			props: { filingData: resp?.data }, 
		};
	} catch (error) {
		console.error('Error Getting Form Four By ID', error);
	
		return {
			props: { filingData: null }
		};
	}

    
}
  

const FormFourPage: NextPage<any> = ({ filingData }: any) => {

    console.log('filingData', filingData)

    return (
        <TrackingProvider>
            <Head>
                <title>
                    Four Four | Insider Transaction Details
                </title>
                <meta
                    name="description"
                    content={`Four Four | Insider Transaction Details`}
                />
            </Head>
            <div className={inter.className}>
                <Header/>
                <TickerBanner/>
                <div className={styles['insider-tx-filing-component']}>
                    <div>

                    </div>
                    <div className={styles['itxfc-center']}>
                        <div className={styles['itxfc-topbar']}>
                            <div className={styles['itxfc-topbar-content']}>
                                <div className={styles['itxfc-tc-left']}>
                                    <div>
                                        <SnippetsOutlined  className={styles['itxfc-tc-left-logo']}/>
                                    </div>
                                    <div>
                                        <span className={styles['itxfc-tc-left-title']}>
                                            SEC - Form 4 - {filingData?._id}
                                        </span>
                                    </div>
                                </div>
                                <div className={styles['itxfc-tc-right']}>
                                    <CustomLink href={`/stock/${filingData?.issuerTradingSymbol}`}>
                                        <Button className={styles['itxfc-tcr-btn']}>
                                            <LinkOutlined/>
                                            See Company Info
                                        </Button>
                                    </CustomLink>
                                    <CustomLink href={filingData?.link}>
                                        <Button>
                                            <LinkOutlined/>
                                            Go To SEC Filing
                                        </Button>
                                    </CustomLink>
                                </div>
                            </div>
                        </div>
                        <div  className={styles['itxfc-filing-details-container']}>
                            <div className={styles['itxfc-fd']}>
                                <div className={styles['itxfc-fd-tb']}>
                                    <span className={styles['itxfc-fd-tb-title']}>
                                        Filing Details
                                    </span>
                                </div>
                                <div className={styles['itxfc-fd-info-grid-container']}>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Period of Report
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            03-12-2024
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Is Director?
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            False
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Reporting Owner Name
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            ROSS TERRY D
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Is Officer?
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            False
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Reporting Owner CIK
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            0026541235
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Is 10% Owner?
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            False
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Relationship
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            GROUP PRESIDENT, PR
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Is Other?
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            False
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Issuer Name
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            Enovis CORP
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Officer Title
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            GROUP PRESIDENT, PR
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Issuer Trading Symbol
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            ENOV
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Other Title
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            ----
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Issuer CIK
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            0001420800
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Shares Remaining After Transaction
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            23,0213,123
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Total Transaction Shares
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            500
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Accession Number
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            000095017024026786
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Transaction Price
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            $59.81
                                        </span>
                                    </div>
                                    <div className={styles['itxfc-grid-item']}>
                                        <span className={styles['itxfc-grid-item-label']}>
                                            Total Transaction Size
                                        </span>
                                        <span className={styles['itxfc-grid-item-value']}>
                                            $26,495.83
                                        </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className={styles['non-derivative-table-container']}>
                            Non Derivative Table Container
                        </div>
                        <div className={styles['derivative-table-container']}>
                            Derivative Table Container
                        </div>
                        

                    </div>
                    <div>

                    </div>
                </div>
                
            </div>
        </TrackingProvider>
    );
};
  
export default FormFourPage;