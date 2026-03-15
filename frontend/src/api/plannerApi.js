/**
 * API service module for interacting with the AI Project Planner backend endpoints.
 */
import apiClient from "../services/apiClient";

/**
 * Pings the backend to check if the API is currently running and accessible.
 * * @returns {Promise<Object>} A promise resolving to the health status data.
 */
export const checkHealth = async () => {
  const response = await apiClient.get("/health/");
  return response.data;
};

/**
 * Submits a new project plan request to the AI generation engine.
 * * @param {Object} planRequest - The payload containing the user's project requirements.
 * @returns {Promise<Object>} A promise resolving to the newly generated project plan data.
 */
export const createPlan = async (planRequest) => {
  const response = await apiClient.post("/plan/", planRequest);
  return response.data;
};

/**
 * Retrieves a specific, previously generated project plan.
 * * @param {string} planId - The unique identifier (e.g., UUID) of the plan to retrieve.
 * @returns {Promise<Object>} A promise resolving to the detailed project plan data.
 */
export const getPlan = async (planId) => {
  const response = await apiClient.get(`/plan/${planId}`);
  return response.data;
};

/**
 * Fetches a list of all project plans stored in the database.
 * * @returns {Promise<Array>} A promise resolving to an array of project plan objects.
 */
export const listPlans = async () => {
  const response = await apiClient.get("/plan/");
  return response.data;
};
