# Azure Deployment Readiness Checklist

## Issues Found and Fixes Applied:

### 1. ❌ CORS Configuration - CRITICAL
**Issue**: CORS only allows localhost origins. Azure deployment will fail.
**Impact**: Frontend cannot communicate with backend on Azure.
**Fix**: Updated to accept environment-based origins.

### 2. ❌ Database Configuration - CRITICAL  
**Issue**: SQLite database path is hardcoded (`./plans.db`). Not suitable for Azure App Service.
**Impact**: Database may not persist or may have permission issues on Azure.
**Fix**: Updated to use Azure SQL Database or environment-based connection string.

### 3. ❌ Environment Variables - CRITICAL
**Issue**: `.env` file is not tracked; Azure secrets not properly integrated.
**Impact**: API keys won't be available in production.
**Fix**: Created `.env.example` with required variables.

### 4. ⚠️ Azure OpenAI Configuration
**Issue**: No fallback if Azure OpenAI credentials are missing.
**Impact**: Service fails silently or with poor error messages.
**Fix**: Added validation and better error handling.

### 5. ⚠️ Startup Script
**Issue**: No Azure App Service startup script (`startup.sh`).
**Impact**: Deployment may not start uvicorn correctly.
**Fix**: Created startup script.

### 6. ⚠️ Production Dependencies
**Issue**: `watchfiles` and `uvloop` are development dependencies.
**Impact**: Unnecessary overhead in production.
**Fix**: Created separate requirements files.

### 7. ✅ Tests
**Status**: Test structure is good, mocks are in place.
**Action**: Run tests before deployment.

### 8. ✅ Frontend Build
**Status**: Vite build is configured, build output ready.
**Action**: Build frontend and serve from Azure Static Web Apps or App Service.

---

## Deployment Strategy for Azure:

### Option A: Azure App Service (Recommended - Single Service)
- Deploy backend FastAPI app on App Service
- Deploy frontend build artifacts separately on Static Web Apps OR same App Service

### Option B: Two Services
- Backend: Azure App Service (Python)
- Frontend: Azure Static Web Apps (React)

### Option C: Container (Docker)
- Create Docker image for backend
- Push to Azure Container Registry
- Deploy to Container Instances or App Service

---

## Next Steps:
1. ✅ Fix CORS for Azure domains
2. ✅ Update database configuration
3. ✅ Create startup script
4. ✅ Separate dev/prod requirements
5. ✅ Add web.config for Azure
6. ✅ Run tests
7. ✅ Build frontend
8. ✅ Create deployment documentation
