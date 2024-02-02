import React from 'react'
import dynamic from 'next/dynamic';
import styles from '../../styles/components/PriceTable.module.css'
import { formatNumber, formatTimestampAsTime } from '@/utils/formatters';

const Table = dynamic(() => import('antd').then(mod => mod.Table));



interface PriceTableProps {
    tableData?: any
}

export default function PriceTable(props: PriceTableProps) {

    console.log('props.tableData', props.tableData)

    const tableData = props.tableData.map((item: any) => {
        return { ...item, key: item.symbol };
    });

    function determineChangeStyling(pctChange: any) {

        if (pctChange > 0) {
            return 'change-up'
        }

        if (pctChange < 0) {
            return 'change-down'
        }

        return 'no-change' // default case
    }
    
    const columns = [
        {
            title: 'Name',
            dataIndex: 'name',
            key: 'name',
            render: (_: any, record: any) => (
                <div>
                    <span className={styles['ti-name']}>
                        {record?.name}
                    </span>
                </div>
            ),
        },
        {
            title: 'Price',
            dataIndex: 'price',
            key: 'price',
            render: (_: any, record: any) => (
                <div>
                    <span>
                        ${record?.price}
                    </span>
                </div>
            ),
        },
        {
            title: 'Percent Change',
            dataIndex: 'changesPercentage',
            key: 'changesPercentage',
            render: (_: any, record: any) => (
                <div>
                    <span className={
                        styles[determineChangeStyling(record.changesPercentage)]
                    }>
                        {record?.changesPercentage?.toFixed(2)}%
                    </span>
                </div>
            ),
        },
        {
            title: 'Change',
            dataIndex: 'change',
            key: 'change',
            render: (_: any, record: any) => (
                <div>
                    <span className={
                        styles[determineChangeStyling(record.changesPercentage)]
                    }>
                        ${record?.change?.toFixed(2)}
                    </span>
                </div>
            ),
        },
        {
            title: 'Day High',
            dataIndex: 'dayHigh',
            key: 'dayHigh',
            render: (_: any, record: any) => (
                <div>
                    <span>
                        ${record?.dayHigh?.toFixed(2)}
                    </span>
                </div>
            ),
        },
        {
            title: 'Day Low',
            dataIndex: 'dayLow',
            key: 'dayLow',
            render: (_: any, record: any) => (
                <div>
                    <span>
                        ${record?.dayLow?.toFixed(2)}
                    </span>
                </div>
            ),
        },
        {
            title: 'Volume',
            dataIndex: 'volume',
            key: 'volume',
            render: (_: any, record: any) => (
                <div>
                    <span>
                        {formatNumber(record?.volume)}
                    </span>
                </div>
            ),
        },
        {
            title: 'Symbol',
            dataIndex: 'symbol',
            key: 'symbol',
        },
        {
            title: 'Average Volume',
            dataIndex: 'avgVolume',
            key: 'avgVolume',
            render: (_: any, record: any) => (
                <div>
                    <span>
                        {formatNumber(record?.avgVolume)}
                    </span>
                </div>
            ),
        },
        {
            title: 'Time',
            dataIndex: 'time',
            key: 'time',
            render: (_: any, record: any) => (
                <div>
                    <span className={styles['ti-time']}>
                        {formatTimestampAsTime(record?.time)}
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
            />
        </div>
    )
}