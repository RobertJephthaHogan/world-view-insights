import { getConfig } from '../config/Constants'
import axios from 'axios'


const config = getConfig()

const apiInstance = axios.create({
    baseURL: `${config.apiUrl}/`,
    headers: {
        'Content-Type': 'application/json',
    },
})


export const dataService = {
    getMarketLeaderQuotes,
    getMajorIndicesOverview,
    getNotableQuotes,
    getGainersPriceTable
}

async function getMarketLeaderQuotes(limit) {
    return new Promise((resolve, reject) => {
        apiInstance
            .get(`/data/get_market_leader_quotes/${limit}`)
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

async function getMajorIndicesOverview() {
    return new Promise((resolve, reject) => {
        apiInstance
            .get(`/data/get_major_index_overview/`)
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

async function getNotableQuotes() {
    return new Promise((resolve, reject) => {
        apiInstance
            .get(`/data/get_notable_quotes/`)
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

async function getGainersPriceTable() {
    return new Promise((resolve, reject) => {
        apiInstance
            .get(`/data/gainers_price_table/`)
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