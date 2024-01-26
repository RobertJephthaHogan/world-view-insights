import React from 'react'
import './styles.css'
import IndexDataCard from '../IndexDataCard'


export default function IndexBanner() {

    const componentData = [
        {
            title: "S&P 500",
            displayPrice: "$4870.5",
            grossChange: "+1.95",
            percentChange: "+0.04%",
            chartData: []
        },
        {
            title: "DOW 30",
            displayPrice: "$37817.5",
            grossChange: "+10.86",
            percentChange: "+0.03%",
            chartData: []
        },
        {
            title: "NASDAQ",
            displayPrice: "$15444.5",
            grossChange: "-37.78",
            percentChange: "-0.24%",
            chartData: []
        },
        {
            title: "Bitcoin",
            displayPrice: "$39745.62",
            grossChange: "-37.78",
            percentChange: "-0.24%",
            chartData: []
        },
        {
            title: "EUR/USD",
            displayPrice: "$1.08",
            grossChange: "+0.0005",
            percentChange: "+0.48%",
            chartData: []
        },
    ]

    return (
        <div className='index-banner'>
            <div className='index-card-container'>
                <IndexDataCard
                    title={componentData?.[0]?.title}
                    displayPrice={componentData?.[0]?.displayPrice}
                    grossChange={componentData?.[0]?.grossChange}
                    percentChange={componentData?.[0]?.percentChange}
                    chartData={componentData?.[0]?.chartData}
                />
                <IndexDataCard
                    title={componentData?.[1]?.title}
                    displayPrice={componentData?.[1]?.displayPrice}
                    grossChange={componentData?.[1]?.grossChange}
                    percentChange={componentData?.[1]?.percentChange}
                    chartData={componentData?.[1]?.chartData}
                />
                <IndexDataCard
                    title={componentData?.[2]?.title}
                    displayPrice={componentData?.[2]?.displayPrice}
                    grossChange={componentData?.[2]?.grossChange}
                    percentChange={componentData?.[2]?.percentChange}
                    chartData={componentData?.[2]?.chartData}
                />
                <IndexDataCard
                    title={componentData?.[3]?.title}
                    displayPrice={componentData?.[3]?.displayPrice}
                    grossChange={componentData?.[3]?.grossChange}
                    percentChange={componentData?.[3]?.percentChange}
                    chartData={componentData?.[3]?.chartData}
                />
                <IndexDataCard
                    title={componentData?.[4]?.title}
                    displayPrice={componentData?.[4]?.displayPrice}
                    grossChange={componentData?.[4]?.grossChange}
                    percentChange={componentData?.[4]?.percentChange}
                    chartData={componentData?.[4]?.chartData}
                />
            </div>
        </div>
    )
}


