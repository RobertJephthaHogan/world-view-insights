import { getConfig } from '../config/Constants'
import axios from 'axios'


const config = getConfig()

const apiInstance = axios.create({
    baseURL: `${config.pyDataServerApiUrl}/`,
    headers: {
        'Content-Type': 'application/json',
    },
})


export const formFourService = {
    getFormFours,
}

async function getFormFours(pageSize, page) {
    return new Promise((resolve, reject) => {
        apiInstance
            .get(`/form-four/get_paginated_form_fours/${page}/${pageSize}`)
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