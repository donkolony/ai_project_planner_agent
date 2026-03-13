# Azure Deployment Guide for AI Project Planner Agent

## Overview
This application consists of:
- **Backend**: FastAPI Python REST API (backend/)
- **Frontend**: React SPA with Vite (frontend/)

---

## Prerequisites

1. **Azure Account** with resource group access
2. **Azure CLI** installed (`az --version`)
3. **GitHub** repository connected to Azure (for CI/CD)
4. **Required Azure Resources**:
   - App Service (or Container Registry if using Docker)
   - SQL Database (optional, or use SQLite)
   - Azure OpenAI instance with deployment

---

## Pre-Deployment Checklist

✅ All tests passing:
```bash
cd backend && python -m pytest tests/ -v
```

✅ Frontend builds successfully:
```bash
cd frontend && npm run build
```

✅ Environment variables configured in GitHub Secrets/Azure Key Vault

✅ CORS configured for production domain

✅ Database migration ready

---

## Deployment Option 1: Using GitHub Actions + Azure App Service (RECOMMENDED)

### Step 1: Prepare Azure Resources

```bash
# Create resource group
az group create --name ai-planner-rg --location eastus

# Create App Service Plan
az appservice plan create \
  --name ai-planner-plan \
  --resource-group ai-planner-rg \
  --sku B1 \
  --is-linux

# Create App Service for Backend
az webapp create \
  --resource-group ai-planner-rg \
  --plan ai-planner-plan \
  --name ai-project-planner-api \
  --runtime "PYTHON|3.11"

# (Optional) Create Storage Account for Static Web Apps
az storage account create \
  --name aiplannerfe \
  --resource-group ai-planner-rg \
  --location eastus \
  --sku Standard_LRS
```

### Step 2: Configure GitHub Secrets

In your GitHub repository, add these secrets:

```
AZUREAPPSERVICE_PUBLISHPROFILE    -> App Service publish profile (downloaded from Azure)
AZURE_OPENAI_ENDPOINT             -> https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY              -> your-api-key
AZURE_OPENAI_DEPLOYMENT           -> deployment-name
AZURE_OPENAI_API_VERSION           -> 2024-02-15-preview
DATABASE_URL                       -> sqlite:///./plans.db (or Azure SQL connection string)
ENVIRONMENT                        -> production
DEBUG                              -> false
FRONTEND_URL                       -> https://ai-project-planner.azurewebsites.net
```

### Step 3: GitHub Actions Workflow

The workflow file `.github/workflows/dep-project_ai-project-planner-api.yml` is already configured to:
1. Build Python app
2. Create virtual environment
3. Install dependencies
4. Deploy to Azure App Service

**Trigger**: Push to `dep/project` branch automatically deploys.

### Step 4: Deploy

```bash
# Push to deployment branch
git checkout -b dep/project
git push origin dep/project

# Monitor deployment in GitHub Actions
# Once complete, verify: curl https://ai-project-planner-api.azurewebsites.net/health/
```

### Step 5: Configure Application Settings in Azure Portal

In Azure Portal > App Service > Configuration > Application Settings, add:

```
ENVIRONMENT=production
DEBUG=false
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=[secret value]
AZURE_OPENAI_DEPLOYMENT=gpt-4
AZURE_OPENAI_API_VERSION=2024-02-15-preview
DATABASE_URL=sqlite:///./plans.db
FRONTEND_URL=https://your-frontend-domain.com
```

---

## Deployment Option 2: Manual Deployment via Azure CLI

```bash
# Login to Azure
az login

# Create deployment package
cd backend
zip -r app.zip . -x ".venv/*" "__pycache__/*" ".git/*"

# Deploy
az webapp deployment source config-zip \
  --resource-group ai-planner-rg \
  --name ai-project-planner-api \
  --src-path app.zip

# Verify
curl https://ai-project-planner-api.azurewebsites.net/health/
```

---

## Frontend Deployment

### Option A: Serve from Same App Service

1. Build frontend: `npm run build` (creates `dist/` folder)
2. Copy `frontend/dist/*` to `backend/static/` or use a separate route
3. Configure App Service to serve static files

### Option B: Azure Static Web Apps (Recommended)

```bash
# Create Static Web App
az staticwebapp create \
  --name ai-planner-frontend \
  --resource-group ai-planner-rg \
  --source https://github.com/your-org/ai_project_planner_agent \
  --location eastus \
  --branch feat/frontend

# Configure API backend URL in frontend
# Update frontend/.env.example with backend API URL
```

### Option C: Azure Blob Storage + CDN

1. Upload built frontend to blob storage
2. Configure CDN endpoint
3. Enable CORS on blob storage

---

## Post-Deployment Verification

### 1. Test Health Endpoint
```bash
curl https://ai-project-planner-api.azurewebsites.net/health/
# Expected: {"status":"AI Project Planner Backend Running"}
```

### 2. Test Plan Generation
```bash
curl -X POST https://ai-project-planner-api.azurewebsites.net/plan/ \
  -H "Content-Type: application/json" \
  -d '{
    "project_name": "Test",
    "description": "Test project",
    "tech_stack": ["Python", "FastAPI"]
  }'
```

### 3. Check Logs
```bash
# Stream logs from App Service
az webapp log tail --name ai-project-planner-api --resource-group ai-planner-rg
```

### 4. Test from Frontend
- Visit your frontend URL
- Fill form and submit
- Verify plan generation works
- Check for CORS errors in browser console

---

## Monitoring & Maintenance

### Application Insights Integration

```bash
# Enable Application Insights
az webapp config appsettings set \
  --name ai-project-planner-api \
  --resource-group ai-planner-rg \
  --settings APPINSIGHTS_INSTRUMENTATIONKEY=[key]
```

### View Metrics
- Azure Portal > App Service > Metrics
- Monitor: CPU, Memory, Response Time, Failed Requests

### Scaling

```bash
# Scale up to S1 if needed
az appservice plan update \
  --name ai-planner-plan \
  --sku S1 \
  --resource-group ai-planner-rg
```

---

## Troubleshooting

### 502 Bad Gateway
- Check startup logs: `az webapp log tail --name ai-project-planner-api`
- Verify Python version (should be 3.11)
- Check if dependencies are installed

### CORS Errors
- Verify `FRONTEND_URL` environment variable
- Check `main.py` CORS configuration matches frontend domain
- Clear browser cache

### Database Connection Issues
- For SQLite: Ensure `/tmp/` directory is writable on App Service
- For Azure SQL: Verify connection string format
- Check firewall rules if using Azure SQL

### Azure OpenAI API Errors
- Verify API key and endpoint in Application Settings
- Check deployment name matches
- Verify API version is supported

---

## Database Migration to Azure SQL (Optional)

### Create Azure SQL Database
```bash
az sql server create \
  --name aiplannerdb \
  --resource-group ai-planner-rg \
  --admin-user sqladmin \
  --admin-password [SecurePassword]

az sql db create \
  --server aiplannerdb \
  --name plans_db \
  --resource-group ai-planner-rg
```

### Update Connection String
```
mssql+pyodbc://sqladmin:password@aiplannerdb.database.windows.net/plans_db?driver=ODBC+Driver+17+for+SQL+Server
```

### Install ODBC Driver
```bash
# Update startup.sh to install ODBC driver
apt-get update && apt-get install -y odbc-mssql
```

---

## Security Recommendations

1. ✅ Use Azure Key Vault for secrets (not App Settings)
2. ✅ Enable HTTPS only (default in App Service)
3. ✅ Configure WAF (Web Application Firewall)
4. ✅ Enable authentication (AAD/Managed Identity)
5. ✅ Set restrictive CORS origins (not `*`)
6. ✅ Enable logging and monitoring
7. ✅ Regular security updates for dependencies

---

## Cost Optimization

- Use **B1 App Service Plan** for low traffic ($10-15/month)
- Set **auto-shutdown** for dev/staging environments
- Use **shared hosting** if not mission-critical
- Monitor usage with **Application Insights**

---

## Support & Next Steps

1. Review Azure Python documentation: https://learn.microsoft.com/en-us/azure/app-service/quickstart-python
2. Implement CI/CD pipeline improvements
3. Add application monitoring and alerting
4. Plan scaling strategy for production load
5. Set up staging environment for testing

---

**Deployment Status**: ✅ Ready for Production

All checks passed. Application is ready to deploy to Azure.
