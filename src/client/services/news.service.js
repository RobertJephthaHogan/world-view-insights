import { getConfig } from '../config/Constants'
import axios from 'axios'


const config = getConfig()

const apiInstance = axios.create({
    baseURL: `${config.apiUrl}/`,
    headers: {
        'Content-Type': 'application/json',
    },
})


export const newsService = {
    getBusinessNewsArticles,
    getArticleById,
}

async function getBusinessNewsArticles(limit) {
    return new Promise((resolve, reject) => {
        apiInstance
            .get(`/news/get_business_news_articles/${limit}`)
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


async function getArticleById(id) {
    return new Promise((resolve, reject) => {
        apiInstance
            .get(`/news/get_article_by_id/${id}`)
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