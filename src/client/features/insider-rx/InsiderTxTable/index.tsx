import React from 'react'
import dynamic from 'next/dynamic';

const Table = dynamic(() => import('antd').then(mod => mod.Table));


interface InsiderTxTableProps {
    tableData?: any
}

export default function InsiderTxTable(props: InsiderTxTableProps) {



    const tableData = props.tableData?.map((item: any) => {
        return { ...item, key: item.symbol };
    }) || []

    const columns = [
        {
            title: 'Name',
            dataIndex: 'name',
            key: 'name',
            render: (_: any, record: any) => (
                <div>
                    {record?.name}
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