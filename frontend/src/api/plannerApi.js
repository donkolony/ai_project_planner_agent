import apiClient from '../services/apiClient'

export const checkHealth = async () => {
  const response = await apiClient.get('/health/')
  return response.data
}

export const createPlan = async (planRequest) => {
  const response = await apiClient.post('/plan/', planRequest)
  return response.data
}

export const getPlan = async (planId) => {
  const response = await apiClient.get(`/plan/${planId}`)
  return response.data
}

export const listPlans = async () => {
  const response = await apiClient.get('/plan/')
  return response.data
}
