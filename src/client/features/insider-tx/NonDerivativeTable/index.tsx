import React from 'react'
import styles from '../../../styles/features/insider-tx/NonDerivativeTable.module.css'




export default function NonDerivativeTable(){ 

    return (
        <table 
            border="1"
            className={styles['non-derivative-table']}
        >
            <thead>
                <tr>
                    <th rowSpan="2">
                        1. Title of Security (Instr. 3)
                    </th>
                    <th rowSpan="2">
                        2. Transaction Date (Month/Day/Year)
                    </th>
                    <th rowSpan="2">
                        2A. Deemed Execution Date, if any (Month/Day/Year)
                    </th>
                    <th colSpan="2">
                        3. Transaction Code (Instr. 8)
                    </th>
                    <th colSpan="3">
                        4. Securities Acquired (A) or Disposed Of (D) (Instr. 3, 4 and 5)
                    </th>
                    <th rowSpan="2">
                        5. Amount of Securities Beneficially Owned Following Reported Transaction(s) (Instr. 3 and 4)	
                    </th>
                    <th rowSpan="2">
                        6. Ownership Form: Direct (D) or Indirect (I) (Instr. 4)	
                    </th>
                    <th rowSpan="2">
                        7. Nature of Indirect Beneficial Ownership (Instr. 4)
                    </th>
                </tr>
                <tr>
                    <th>Code</th>
                    <th>V</th>
                    <th>Amount</th>
                    <th>(A) or (D)</th>
                    <th>Price</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Title of Security 1</td>
                    <td>Transaction Date 1</td>
                    <td></td>
                    <td>S</td>
                    <td></td>
                    <td>D1</td>
                    <td>D2</td>
                    <td>D3</td>
                    <td></td>
                    <td>I</td>
                    <td></td>
                </tr>
                <tr>
                    <td>Title of Security 2</td>
                    <td>Transaction Date 2</td>
                    <td></td>
                    <td>S</td>
                    <td></td>
                    <td>D1</td>
                    <td>D2</td>
                    <td>D3</td>
                    <td></td>
                    <td>I</td>
                    <td></td>
                </tr>
            </tbody>
        </table>
    )
}