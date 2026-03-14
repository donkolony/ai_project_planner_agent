# Vercel Deployment Guide - AI Project Planner

Complete step-by-step instructions for deploying the AI Project Planner frontend to Vercel and configuring it to work with your Azure backend API.

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Frontend Deployment to Vercel](#frontend-deployment-to-vercel)
3. [Environment Configuration](#environment-configuration)
4. [Backend API Configuration](#backend-api-configuration)
5. [Post-Deployment Testing](#post-deployment-testing)
6. [Troubleshooting](#troubleshooting)
7. [Custom Domain Setup](#custom-domain-setup)
8. [CI/CD Pipeline](#cicd-pipeline)

---

## Prerequisites

Before you begin, ensure you have:

- ✅ **Vercel Account**: Sign up at [vercel.com](https://vercel.com)
- ✅ **GitHub Account**: Repository with code pushed to GitHub
- ✅ **Git**: Version control system installed
- ✅ **Node.js**: v18 or higher (`node --version`)
- ✅ **npm**: Package manager (`npm --version`)
- ✅ **Backend Running**: Azure backend accessible at its public URL
- ✅ **Environment Variables**: List of all required env vars prepared

---

## Frontend Deployment to Vercel

### Step 1: Push Code to GitHub

Ensure all your code is pushed to your GitHub repository on the `main` branch:

```bash
cd /home/yamkelamacwili/Desktop/porfolio_projects/ai_project_planner_agent
git status
git add .
git commit -m "Ready for Vercel deployment"
git push origin main
```

**Verify** your code is on GitHub by visiting: `https://github.com/donkolony/ai_project_planner_agent`

### Step 2: Connect GitHub to Vercel

1. **Sign in to Vercel**: Go to [vercel.com](https://vercel.com) and click **Sign In**
2. **Select GitHub**: Choose "Continue with GitHub"
3. **Authorize Vercel**: Grant permissions to access your GitHub repositories
4. **Select Repository**: Find and click on `ai_project_planner_agent`

### Step 3: Configure Project Settings

Vercel will auto-detect that this is a monorepo with `frontend/` and `backend/` directories.

**Settings to Configure:**

- **Framework Preset**: `Vite`
- **Root Directory**: `./frontend` (IMPORTANT - specify this!)
- **Build Command**: `npm run build`
- **Output Directory**: `dist`
- **Install Command**: `npm install`

**Configure in Vercel Dashboard:**

1. Click **Settings** tab
2. Under **Build & Development Settings**:
   - Root Directory: `./frontend`
   - Framework: `Vite`
   - Build Command: `npm run build`
   - Output Directory: `dist`

3. Click **Save**

### Step 4: Set Environment Variables

In Vercel Dashboard:

1. Go to **Settings** → **Environment Variables**
2. Add the following environment variables:

```
VITE_API_BASE_URL = https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net
```

**For each environment** (Production, Preview, Development):
- Select which environments this applies to
- Usually apply to: **Production**, **Preview**, **Development**

3. Click **Save**

### Step 5: Deploy

After configuring environment variables:

1. Click **Deploy** button in Vercel Dashboard
2. Wait for build to complete (usually 2-3 minutes)
3. You'll see a **Success** message with a deployment URL

**Your frontend is now live!** 🎉

---

## Environment Configuration

### Frontend Environment Variables

The frontend requires the backend API URL to be set:

**File**: `frontend/.env.production` (created automatically by Vercel)

```env
VITE_API_BASE_URL=https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net
```

**How Vercel uses this**:
- Vercel reads `VITE_API_BASE_URL` from Dashboard → Environment Variables
- Vite embeds this into the build during compilation
- Frontend uses `import.meta.env.VITE_API_BASE_URL` in the code

### Accessing Environment Variables in Frontend Code

In `frontend/src/services/apiClient.js`:

```javascript
const baseURL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000';

const apiClient = axios.create({
  baseURL,
  headers: {
    'Content-Type': 'application/json',
  },
});
```

---

## Backend API Configuration

### Important: Update CORS on Backend

Your Azure backend must allow requests from your Vercel domain.

**Update** `backend/app/main.py`:

```python
if settings.environment == "development":
    allow_origins = [
        "http://localhost:3000",
        "http://localhost:5173",
        # ... dev ports
    ]
else:
    # Production: Allow Vercel frontend domain
    frontend_urls = os.getenv(
        "FRONTEND_URL",
        "https://your-vercel-project.vercel.app"  # Replace with your Vercel URL
    )
    allow_origins = [url.strip() for url in frontend_urls.split(",")]
```

**Steps**:

1. After your Vercel deployment succeeds, note your **Deployment URL** (e.g., `https://ai-project-planner-abc123.vercel.app`)
2. Update `FRONTEND_URL` environment variable on Azure backend:
   - Go to Azure Portal → App Service → Configuration
   - Add/Update: `FRONTEND_URL = https://ai-project-planner-abc123.vercel.app`
   - Click **Save**
3. Restart your Azure App Service for changes to take effect

### Backend Health Check

Verify your backend is accessible:

```bash
curl https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net/health/
```

Expected response:
```json
{"status": "AI Project Planner Backend Running"}
```

---

## Post-Deployment Testing

### Test 1: Frontend Access

1. Visit your Vercel deployment URL: `https://your-project.vercel.app`
2. **Check**:
   - ✅ Logo appears in header
   - ✅ Form loads with all fields
   - ✅ No console errors (open DevTools: F12)

### Test 2: Health Check API Call

1. In the frontend, the health check should happen automatically
2. **Check** in browser DevTools (Network tab):
   - Request to: `/health/` succeeds with 200 OK
   - Response: `{"status": "..."}`

### Test 3: Form Submission

1. Fill out the form:
   - Project Name: "Test Project"
   - Description: "Testing deployment"
   - Tech Stack: "React, FastAPI"
2. Click **Generate Plan**
3. **Verify**:
   - ✅ Loading spinner appears
   - ✅ Plan generates successfully (or error message appears)
   - ✅ No CORS errors in DevTools Console

### Test 4: Check Console Logs

Open DevTools (F12 → Console) and verify:

```javascript
// Should show
VITE_API_BASE_URL = "https://ai-project-planner-api-..."

// Should NOT show CORS errors like:
// "Access to XMLHttpRequest at '...' from origin '...' blocked by CORS"
```

---

## Troubleshooting

### Issue 1: Blank Page or 404 on Vercel

**Cause**: Root directory not set correctly

**Solution**:
1. Vercel Dashboard → Settings → Build & Development Settings
2. Set **Root Directory** to `./frontend`
3. Redeploy

### Issue 2: Environment Variable Not Loading

**Error**: API calls fail, shows `Cannot POST to undefined`

**Solution**:
1. Verify `VITE_API_BASE_URL` is set in Vercel Dashboard
2. In code, use: `import.meta.env.VITE_API_BASE_URL`
3. Redeploy after changing env vars

### Issue 3: CORS Error - "Access to XMLHttpRequest blocked"

**Error**: 
```
Access to XMLHttpRequest at 'https://backend.azurewebsites.net/plan/'
from origin 'https://your-vercel-app.vercel.app' blocked by CORS policy
```

**Solution**:
1. Update `FRONTEND_URL` on Azure backend to include your Vercel URL
2. Restart Azure App Service
3. Wait 2-3 minutes for changes to propagate
4. Test again

### Issue 4: 502 Bad Gateway or Timeout

**Cause**: Backend API not responding or Azure service issue

**Solution**:
1. Check backend health: `curl https://backend-url.azurewebsites.net/health/`
2. Check Azure status: Azure Portal → App Service → Health check
3. Check backend logs: Azure Portal → App Service → Log stream
4. Restart the App Service if needed

### Issue 5: Build Fails with "Module not found"

**Error**: `npm ERR! Module not found: '@vitejs/plugin-react'`

**Solution**:
1. Ensure `package.json` is in the `frontend/` directory
2. Vercel Build Command should be: `npm run build`
3. Root Directory should be: `./frontend`

---

## Custom Domain Setup

### Add Custom Domain to Vercel

1. **Go to Vercel Dashboard** → Your Project → Settings → Domains
2. **Add Domain**: Click "Add" and enter your domain (e.g., `planner.yourdomain.com`)
3. **Configure DNS**: Vercel provides DNS instructions
4. **Wait**: DNS propagation can take 24-48 hours

### Update Backend CORS for Custom Domain

Update `FRONTEND_URL` on Azure backend to include your custom domain:

```
FRONTEND_URL = https://planner.yourdomain.com,https://your-project.vercel.app
```

(Keep both the custom domain and Vercel URL to support both)

---

## CI/CD Pipeline

### Automatic Deployments

Vercel automatically deploys when you push to GitHub:

- **Push to `main`** → Deploys to Production
- **Create PR** → Deploys Preview (separate URL)
- **Push to other branches** → No deploy (optional)

### Redeployment

To manually redeploy:

1. Vercel Dashboard → Deployments tab
2. Click "..." on any deployment
3. Select "Redeploy"

Or push a new commit:
```bash
git commit --allow-empty -m "Trigger Vercel redeploy"
git push origin main
```

---

## Production Checklist

Before going live, verify:

- [ ] Frontend deployed on Vercel
- [ ] Deployment URL accessible: `https://your-project.vercel.app`
- [ ] `VITE_API_BASE_URL` set to Azure backend URL
- [ ] Backend `FRONTEND_URL` includes Vercel domain
- [ ] Health check endpoint responds with 200 OK
- [ ] Form submission works end-to-end
- [ ] No CORS errors in browser console
- [ ] No sensitive data in environment variables (all keys/secrets on Azure only)
- [ ] Custom domain configured (if applicable)
- [ ] Analytics enabled (optional): Vercel → Settings → Analytics
- [ ] Monitoring configured (optional): Vercel → Monitoring

---

## Useful Commands

```bash
# Check Node version (Vercel requires v18+)
node --version

# Build locally to test before deploy
cd frontend
npm run build
npm run preview

# View build output
ls -la frontend/dist/

# Check git status
git status
git log --oneline -5

# Push to trigger Vercel deploy
git push origin main
```

---

## Vercel Dashboard Quick Links

| Section | URL |
|---------|-----|
| Projects | `vercel.com/dashboard/projects` |
| Project Settings | `vercel.com/[project]/settings` |
| Environment Variables | `vercel.com/[project]/settings/environment-variables` |
| Deployments | `vercel.com/[project]/deployments` |
| Analytics | `vercel.com/[project]/analytics` |
| Domains | `vercel.com/[project]/settings/domains` |

---

## Support & Resources

- **Vercel Docs**: https://vercel.com/docs
- **Vite Docs**: https://vitejs.dev
- **React Docs**: https://react.dev
- **Azure App Service**: https://azure.microsoft.com/services/app-service

---

## Next Steps

After successful deployment:

1. **Monitor Performance**: Check Vercel Analytics
2. **Set up Error Tracking**: Integrate Sentry or similar
3. **Configure Email Notifications**: Get alerts for deployment failures
4. **Backup Strategy**: Regular backups of Azure database
5. **Security**: Review CORS, HTTPS, and authentication

---

**Deployment Date**: March 14, 2026  
**Frontend Framework**: React 18.2 + Vite 5.0  
**Backend API**: FastAPI on Azure App Service  
**Status**: ✅ Ready for Production
