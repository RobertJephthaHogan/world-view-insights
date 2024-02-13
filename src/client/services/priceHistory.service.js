import { getConfig } from '../config/Constants'
import axios from 'axios'


const config = getConfig()

const apiInstance = axios.create({
    baseURL: `${config.apiUrl}/`,
    headers: {
        'Content-Type': 'application/json',
    },
})


export const priceHistoryService = {
    getStockPriceHistory,
}

async function getStockPriceHistory(symbol) {
    return new Promise((resolve, reject) => {
        apiInstance
            .get(`/price-history/get_stock_price_history/${symbol}`)
            .then((response) => {
                const resp = response.data
                return resolve(resp)
            })
            .catch((error) => {
                console.error(error)
                reject(error)
            })
    })
}