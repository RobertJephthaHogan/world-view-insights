import React from 'react'
import styles from '../../../styles/features/insider-tx/DerivativeTable.module.css'



export default function DerivativeTable() {

    // TODO: Ensure Overflow scroll works properly

    return (
        <table 
            border="1"
            className={styles['derivative-table']}
        >
            <thead>
                <tr>
                    <th rowSpan="2">
                        1. Title of Derivative Security (Instr. 3)
                    </th>
                    <th rowSpan="2">
                        2. Conversion or Exercise Price of Derivative Security
                    </th>
                    <th rowSpan="2">
                        3. Transaction Date (Month/Day/Year)	
                    </th>
                    <th rowSpan="2">
                        3A. Deemed Execution Date, if any (Month/Day/Year)	
                    </th>
                    <th colSpan="2">
                        4. Transaction Code (Instr. 8)	
                    </th>
                    <th colSpan="2">
                        5. Number of Derivative Securities Acquired (A) or Disposed of (D) (Instr. 3, 4 and 5)	
                    </th>
                    <th colSpan="2">
                        6. Date Exercisable and Expiration Date (Month/Day/Year)	
                    </th>
                    <th colSpan="2">
                        7. Title and Amount of Securities Underlying Derivative Security (Instr. 3 and 4)	
                    </th>
                    <th rowSpan="2">
                        8. Price of Derivative Security (Instr. 5)	
                    </th>
                    <th rowSpan="2">
                        9. Number of derivative Securities Beneficially Owned Following Reported Transaction(s) (Instr. 4)	
                    </th>
                    <th rowSpan="2">
                        10. Ownership Form: Direct (D) or Indirect (I) (Instr. 4)	
                    </th>
                    <th rowSpan="2">
                        11. Nature of Indirect Beneficial Ownership (Instr. 4)
                    </th>
                </tr>
                <tr>
                    <th>Code</th>
                    <th>V</th>
                    <th>(A)</th>
                    <th>(D)</th>
                    <th>Date Exercisable</th>
                    <th>Expiration Date	</th>
                    <th>Title</th>
                    <th>Amount or Number of Shares</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Title</td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
                <tr>
                    <td>Title</td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
            </tbody>
        </table>
    )
}