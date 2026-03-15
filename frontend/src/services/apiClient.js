import axios from "axios";

const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "http://localhost:8000";

/**
 * Pre-configured Axios HTTP client instance for communicating with the backend API.
 * Automatically handles the base URL routing via environment variables (development vs. production)
 * and includes a global response interceptor for unified error logging.
 * * @type {import("axios").AxiosInstance}
 */
const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    "Content-Type": "application/json",
  },
});

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    console.error("API Error:", error);
    return Promise.reject(error);
  },
);

export default apiClient;