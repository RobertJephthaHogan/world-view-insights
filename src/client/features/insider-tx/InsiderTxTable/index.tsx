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
                    {record?.rptOwnerName}
                </div>
            ),
        },
        {
            title: 'Transaction type',
            dataIndex: 'transactionType',
            key: 'transactionType',
            render: (_: any, record: any) => (
                <div>
                    {record?.transactionType == 'P' ? 'Purchase': null}
                    {record?.transactionType == 'S' ? 'Sale': null}
                </div>
            ),
        },
        {
            title: 'isDirector',
            dataIndex: 'isDirector',
            key: 'isDirector',
            render: (_: any, record: any) => (
                <div>
                    {record?.isDirector ? 'true' : 'false'}
                </div>
            ),
        },
        {
            title: 'isOfficer',
            dataIndex: 'isOfficer',
            key: 'isOfficer',
            render: (_: any, record: any) => (
                <div>
                    {record?.isOfficer ? 'true' : 'false'}
                </div>
            ),
        },
        {
            title: 'isTenPercentOwner',
            dataIndex: 'isTenPercentOwner',
            key: 'isTenPercentOwner',
            render: (_: any, record: any) => (
                <div>
                    {record?.isTenPercentOwner ? 'true' : 'false'}
                </div>
            ),
        },
        {
            title: 'isOther',
            dataIndex: 'isOther',
            key: 'isOther',
            render: (_: any, record: any) => (
                <div>
                    {record?.isOther ? 'true' : 'false'}
                </div>
            ),
        },
        {
            title: 'Date',
            dataIndex: 'periodOfReport',
            key: 'periodOfReport',
            render: (_: any, record: any) => (
                <div>
                    <span className={styles['tx-date-txt']}>
                        {record?.periodOfReport}
                    </span>
                </div>
            ),
        },

    ];

    return (
        <div>
            <Table 
                dataSource={tableData} 
                columns={columns} 
                size='small'
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