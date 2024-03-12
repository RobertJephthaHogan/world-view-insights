import React, { useEffect, useState } from 'react'
import styles from '../../../styles/features/insider-tx/NonDerivativeTable.module.css'


interface NonDerivativeTableProps {
    nonDerivativeTable?: any
}

export default function NonDerivativeTable(props: NonDerivativeTableProps){ 

    const [tableData, setTableData] = useState<any>([])


    useEffect(() => {
        // format transactions into table entries
        const entries = Object.values(props.nonDerivativeTable?.nonDerivativeTransactions)
        setTableData(entries)
    }, [props.nonDerivativeTable])

    return (
        <table 
            className={styles['non-derivative-table']}
        >
            <thead>
                <tr key={'ndt-top-header'}>
                    <th rowSpan={2}>
                        1. Title of Security (Instr. 3)
                    </th>
                    <th rowSpan={2}>
                        2. Transaction Date (Month/Day/Year)
                    </th>
                    <th rowSpan={2}>
                        2A. Deemed Execution Date, if any (Month/Day/Year)
                    </th>
                    <th colSpan={2}>
                        3. Transaction Code (Instr. 8)
                    </th>
                    <th colSpan="3">
                        4. Securities Acquired (A) or Disposed Of (D) (Instr. 3, 4 and 5)
                    </th>
                    <th rowSpan={2}>
                        5. Amount of Securities Beneficially Owned Following Reported Transaction(s) (Instr. 3 and 4)	
                    </th>
                    <th rowSpan={2}>
                        6. Ownership Form: Direct (D) or Indirect (I) (Instr. 4)	
                    </th>
                    <th rowSpan={2}>
                        7. Nature of Indirect Beneficial Ownership (Instr. 4)
                    </th>
                </tr>
                <tr key={'ndt-bottom-header'}>
                    <th>Code</th>
                    <th>V</th>
                    <th>Amount</th>
                    <th>(A) or (D)</th>
                    <th>Price</th>
                </tr>
            </thead>
            <tbody>
                {
                    tableData?.map((filing: any, i: number) => {

                        return (
                            <tr key={i}>
                                <td>
                                    {filing?.securityTitle}
                                </td>
                                <td>
                                    {filing?.transactionDate}
                                </td>
                                <td>
                                    {filing?.deemedExecutionDate}
                                </td>
                                <td>
                                    {filing?.transactionCode}
                                </td>
                                <td>
                                    {/* TODO: Determine V */}
                                </td>
                                <td>
                                    {filing?.transactionShares}
                                </td>
                                <td>
                                    {filing?.transactionAcquiredDisposedCode}
                                </td>
                                <td>
                                    {filing?.transactionPricePerShare}
                                </td>
                                <td>
                                    {filing?.sharesOwnedFollowingTransaction}
                                </td>
                                <td>
                                    {filing?.directOrIndirectOwnership}
                                </td>
                                <td>
                                    {/* TODO: ADD NATURE OF BENEFICIAL OWNERSHIP */}
                                </td>
                            </tr>
                        )
                    })
                }
            </tbody>
        </table>
    )
}