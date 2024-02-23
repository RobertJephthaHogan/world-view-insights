import React from 'react'
import dynamic from 'next/dynamic';

const Table = dynamic(() => import('antd').then(mod => mod.Table));


interface InsiderTxTableProps {
    tableData?: any
}

export default function InsiderTxTable(props: InsiderTxTableProps) {



    const tableData = props.tableData?.map((item: any) => {
        return { ...item, key: item._id };
    }) || []

    const columns = [
        {
            title: 'Symbol',
            dataIndex: 'symbol',
            key: 'symbol',
            render: (_: any, record: any) => (
                <div>
                    {record?.symbol}
                </div>
            ),
        },
        {
            title: 'Reporting Ownder Name',
            dataIndex: 'rptOwnerName',
            key: 'rptOwnerName',
            render: (_: any, record: any) => (
                <div>
                    {record?.rptOwnerName}
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
                    {record?.periodOfReport}
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