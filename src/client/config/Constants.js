


//const API_BASE_URL = 'http://127.0.0.1:8008/'
const PY_DS_API_BASE_URL = 'http://127.0.0.1:8007/'

const API_BASE_URL = 'https://api.worldviewinsights.com/'
// const PY_DS_API_BASE_URL = 'https://pydsapi.worldviewinsights.com/'




// const CLIENT_BASE_URL = 'http://localhost:3008/'
const CLIENT_BASE_URL = 'https://worldviewinsights.com/'

export function getConfig() {
    return {
        apiUrl: API_BASE_URL,
        pyDataServerApiUrl: PY_DS_API_BASE_URL,
        clientUrl: CLIENT_BASE_URL
    }
}