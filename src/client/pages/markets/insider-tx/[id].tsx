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
import { formFourService } from '@/services/formFour.service';


const inter = Inter({ subsets: ["latin"] });




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

    
    // ToDo: Get the filing data from the backend
    const filingData = {}
  
    return {
        props: { filingData }, // Filing data passed to the page component as props
    };
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
                                <div>
                                    Right
                                </div>
                            </div>
                        </div>

                        Filing Page Content

                    </div>
                    <div>

                    </div>
                </div>
                
            </div>
        </TrackingProvider>
    );
};
  
export default FormFourPage;