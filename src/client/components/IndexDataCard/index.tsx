import React from 'react'
import { Line } from 'react-chartjs-2';
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    Filler
} from 'chart.js';
// Register the components
ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend,
    Filler
);
import styles from '../../styles/components/IndexDataCard.module.css'



interface IndexDataCardProps {
    title?: string
    displayPrice?: string
    grossChange: string
    percentChange: string
    chartData?: Array<any>
}

export default function IndexDataCard(props: IndexDataCardProps) {


    const chartData = {
        labels: ['1', '2', '3', '4', '5', '6'],
        datasets: [
            {
                label: 'Price',
                backgroundColor: 'rgba(255, 99, 132, 0.2)',
                borderColor: 'rgba(255, 99, 132, 1)',
                borderWidth: 1,
                data: [65, 59, 80, 81, 56, 55, 40],
                fill: true, // Enables area fill
                pointRadius: 0, // Removes the dots on each datapoint
            },
        ],
    };

    const chartOptions = {
        scales: {
            x: {
                display: false, // Hides the x-axis label and scale
                },
            y: {
                display: false, // Hides the y-axis label and scale
            }
        },
        layout: {
            padding: 0, // Adjusts padding around the chart. Set to 0 or an object {top, right, bottom, left} for fine control
        },
        plugins: {
            legend: {
                display: false, // Optionally, hide the legend if you also want to remove that
            },
            tooltip: {
                enabled: false, // Disable tooltips
            },
        },
        //maintainAspectRatio: false // This is optional based on your responsiveness needs
    };

    return (
        <div className={styles['index-data-card']}>
            <div className={styles['idc-left']}>
                <div className={styles['idc-l-top']}>
                    <span className={styles['index-title']}>
                        {props?.title}
                    </span>
                    <span className={styles['index-display-price']}>
                        {props?.displayPrice}
                    </span>
                </div>
                <div className={styles['idc-l-bottom']}>
                    <span className={`
                        ${styles['change-text']}
                        ${parseFloat(props?.percentChange) > 0 ? styles['change-up'] : ''}
                        ${parseFloat(props?.percentChange) < 0 ? styles['change-down'] : ''}
                    `}>
                        {parseFloat(props?.grossChange)?.toFixed(2)} ({parseFloat(props?.percentChange)?.toFixed(2)}%)
                    </span>
                </div>
            </div>
            <div className={styles['idc-right']}>
                <div className={styles['chart']}>
                    <Line 
                        data={chartData} 
                        options={chartOptions}
                        height={60}
                        width={60}
                    />
                </div>
            </div>
        </div>
    )
}