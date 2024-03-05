import React from 'react'
import dynamic from 'next/dynamic';
import styles from '../../../styles/features/insider-tx/InsiderTxTable.module.css'
import { getConfig } from '@/config/Constants'
import { useRouter } from 'next/navigation'

const Table = dynamic(() => import('antd').then(mod => mod.Table));


interface InsiderTxTableProps {
    tableData?: any
}

export default function InsiderTxTable(props: InsiderTxTableProps) {

    const config = getConfig()
    const router = useRouter()


    const handleNavigationClick = (event: any, path: string) => {
        // Prevent the default href link behavior 
        event.preventDefault();
    
        // TODO: Implement tracking logic here
    
        // Navigate to the URL after tracking
        //window.location.href = url;
        router.push(path);
    };


    // Create a new Intl.NumberFormat object for US English, displaying as currency
    const currencyFormatter = new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        // Specify rounding to a maximum of 2 decimal places
        maximumFractionDigits: 2,
    });
    

    // Create a new Intl.NumberFormat object for US English, displaying as currency
    const usNumberFormatter = new Intl.NumberFormat('en-US', {
        //style: 'currency',
        currency: 'USD',
        // Specify rounding to a maximum of 2 decimal places
        maximumFractionDigits: 2,
    });


    const tableData = props.tableData?.map((item: any) => {
        return { ...item, key: item._id };
    }) || []

    const columns = [
        {
            title: 'Symbol',
            dataIndex: 'symbol',
            key: 'symbol',
            render: (_: any, record: any) => (
                <a
                    className={styles['tx-trading-symbol-anchor']}
                    href={`${config.clientUrl}stock/${record?.issuerTradingSymbol}`}
                    onClick={(e) => handleNavigationClick(e, `/stock/${record?.issuerTradingSymbol}`)}
                >
                    <span className={styles['tx-trading-symbol']}>
                        {record?.issuerTradingSymbol}
                    </span>
                </a>
            ),
        },
        {
            title: 'Reporting Owner Name',
            dataIndex: 'rptOwnerName',
            key: 'rptOwnerName',
            render: (_: any, record: any) => (
                <div>
                    <span className={styles['rptOwnerName-txt']}>
                        {record?.rptOwnerName}
                    </span>
                </div>
            ),
        },
        {
            title: 'Relationship',
            dataIndex: 'relationship',
            key: 'relationship',
            render: (_: any, record: any) => (
                <div>
                    <span className={styles['relationship-txt']}>
                        {record?.relationship}
                    </span>
                </div>
            ),
        },
        {
            title: 'Transaction type',
            dataIndex: 'transactionType',
            key: 'transactionType',
            render: (_: any, record: any) => (
                <div>
                    <span className={styles['transactionType-txt']}>
                        {record?.transactionType == 'P' ? 'Purchase': null}
                        {record?.transactionType == 'S' ? 'Sale': null}
                    </span>
                </div>
            ),
        },
        {
            title: 'Tx Price',
            dataIndex: 'transactionPrice',
            key: 'transactionPrice',
            render: (_: any, record: any) => (
                <div>
                    <span className={styles['transactionPrice-txt']}>
                        {currencyFormatter.format(record?.transactionPrice)}
                    </span>
                </div>
            ),
        },
        {
            title: '# Shares',
            dataIndex: 'totalTransactionShares',
            key: 'totalTransactionShares',
            render: (_: any, record: any) => (
                <div>
                    <span className={styles['totalTransactionShares-txt']}>
                        {usNumberFormatter.format(record?.totalTransactionShares)}
                    </span>
                </div>
            ),
        },
        {
            title: 'Trade Value',
            dataIndex: 'totalTransactionSize',
            key: 'totalTransactionSize',
            render: (_: any, record: any) => (
                <div>
                    <span className={styles['totalTransactionSize-txt']}>
                        {currencyFormatter.format(record?.totalTransactionSize)}
                    </span>
                </div>
            ),
        },
        {
            title: 'isDirector',
            dataIndex: 'isDirector',
            key: 'isDirector',
            render: (_: any, record: any) => (
                <div>
                    <span className={styles['isDirector-txt']}>
                        {record?.isDirector ? 'true' : 'false'}
                    </span>
                </div>
            ),
        },
        {
            title: 'isOfficer',
            dataIndex: 'isOfficer',
            key: 'isOfficer',
            render: (_: any, record: any) => (
                <div>
                    <span className={styles['isOfficer-txt']}>
                        {record?.isOfficer ? 'true' : 'false'}
                    </span>
                </div>
            ),
        },
        {
            title: 'isTenPercentOwner',
            dataIndex: 'isTenPercentOwner',
            key: 'isTenPercentOwner',
            render: (_: any, record: any) => (
                <div>
                    <span className={styles['isTenPercentOwner-txt']}>
                        {record?.isTenPercentOwner ? 'true' : 'false'}
                    </span>
                </div>
            ),
        },
        {
            title: 'isOther',
            dataIndex: 'isOther',
            key: 'isOther',
            render: (_: any, record: any) => (
                <div>
                    <span className={styles['isOther-txt']}>
                        {record?.isOther ? 'true' : 'false'}
                    </span>
                </div>
            ),
        },
        {
            title: 'Date',
            dataIndex: 'periodOfReport',
            key: 'periodOfReport',
            render: (_: any, record: any) => (
                <a
                    className={styles['date-link-anchor']}
                    href={record?.link?.replace(/\s+/g, '')}
                    target="_blank"
                >
                    <span className={styles['tx-date-txt']}>
                        {record?.periodOfReport}
                    </span>
                </a>
            ),
        },

    ];

    return (
        <div>
            <Table 
                dataSource={tableData} 
                columns={columns} 
                size='small'
                className={styles['insider-tx-table']}
                rowClassName={(record) => {
                    switch (record.transactionType) {
                        case 'P':
                            return styles['transaction-buy'];
                        case 'S':
                            return styles['transaction-sell'];
                        // Add more cases for other transaction types if needed here
                        default:
                            return '';
                    }
                }}
            />
        </div>
    )
}