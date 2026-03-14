import axios from 'axios'

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

// Log the API base URL for debugging
console.log('🔌 API Base URL:', API_BASE_URL)

const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
  timeout: 30000, // 30 second timeout
})

apiClient.interceptors.request.use(
  (config) => {
    console.log('📤 API Request:', {
      method: config.method?.toUpperCase(),
      url: config.baseURL + config.url,
      data: config.data,
    })
    return config
  },
  (error) => {
    console.error('❌ Request Error:', error)
    return Promise.reject(error)
  }
)

apiClient.interceptors.response.use(
  (response) => {
    console.log('✅ API Response:', {
      status: response.status,
      url: response.config.url,
      data: response.data,
    })
    return response
  },
  (error) => {
    console.error('❌ API Error Details:', {
      message: error.message,
      status: error.response?.status,
      statusText: error.response?.statusText,
      data: error.response?.data,
      url: error.config?.url,
      baseURL: error.config?.baseURL,
    })
    return Promise.reject(error)
  }
)

export default apiClient
