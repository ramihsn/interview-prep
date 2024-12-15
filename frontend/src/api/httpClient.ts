import axios from 'axios'

const httpClient = axios.create({
  baseURL: `${import.meta.env.VITE_BASE_URL}/api` || 'http://localhost:8000',
  headers: {
    'Content-Type': 'application/json',
  },
})

export default httpClient
