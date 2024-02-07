import { getConfig } from '../config/Constants'
import axios from 'axios'


const config = getConfig()

const apiInstance = axios.create({
    baseURL: `${config.apiUrl}/`,
    headers: {
        'Content-Type': 'application/json',
    },
})


export const stockService = {
    getStockPageData,
}

async function getStockPageData(symbol) {
    return new Promise((resolve, reject) => {
        apiInstance
            .get(`/stock/get_stock_page_data/${symbol}`)
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