# API Connection Debugging Guide

## Problem: "Failed to generate plan" on Vercel Deployment

This guide helps diagnose why the frontend (on Vercel) cannot connect to the backend (on Azure).

---

## Quick Diagnosis Steps

### Step 1: Find Your Vercel Deployment URL

1. Go to Vercel Dashboard: https://vercel.com/dashboard
2. Select your project: `ai_project_planner_agent`
3. Copy the **Deployment URL** (e.g., `https://ai-project-planner-abc123.vercel.app`)

### Step 2: Check Browser Console for Detailed Errors

1. Open your Vercel app in browser
2. Press `F12` to open Developer Tools
3. Go to **Console** tab
4. Try generating a plan
5. Look for error messages like:

```
🔌 API Base URL: https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net
📤 API Request: POST /plan/ ...
❌ API Error Details: {
  message: "Network Error" | "timeout" | etc
  status: 403 | 404 | 500 | etc
}
```

### Step 3: Test Backend Health Check

In browser console, run:

```javascript
fetch('https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net/health/')
  .then(r => r.json())
  .then(d => console.log('✅ Health:', d))
  .catch(e => console.error('❌ Health error:', e))
```

### Step 4: Test CORS Preflight

The browser sends an `OPTIONS` request first. Check Network tab:

1. Open DevTools → **Network** tab
2. Generate a plan
3. Look for an `OPTIONS` request to `/plan/`
4. Check the **Status** code:
   - ✅ **204 No Content** = CORS OK
   - ❌ **400 Bad Request** = CORS configuration issue
   - ❌ **403 Forbidden** = Not allowed by CORS

---

## Common Issues & Solutions

### Issue 1: CORS Error - "Access to XMLHttpRequest blocked"

**Error Message:**
```
Access to XMLHttpRequest at 'https://backend.azurewebsites.net/plan/' 
from origin 'https://your-vercel-app.vercel.app' blocked by CORS policy
```

**Root Causes:**

1. **Vercel URL not in CORS allowed list**
   - Solution: Add your Vercel URL to backend CORS configuration

2. **Backend restart needed**
   - Solution: Restart Azure App Service

**Fix:**

1. **On Azure Backend:**
   ```bash
   # Go to Azure Portal
   App Service → ai-project-planner-api-* → Configuration
   
   # Add/Update environment variable:
   FRONTEND_URL = https://your-vercel-project.vercel.app
   
   # Click Save
   # Go to Overview → Click Restart
   ```

2. **Verify CORS logs:**
   ```bash
   # In Azure Portal → App Service → Log stream
   # You should see:
   # 🔒 CORS Configuration - Environment: production
   # 🔒 Allowed Origins: ['https://your-vercel-project.vercel.app']
   ```

3. **Redeploy frontend on Vercel** to clear caches
   - Vercel Dashboard → Deployments → Click "..." → Redeploy

---

### Issue 2: Request Timeout

**Error Message:**
```
Request timeout - backend may be slow or unreachable.
```

**Root Causes:**

1. **Azure App Service asleep** (cold start)
   - Solution: Wait 30 seconds and try again
   - Or: Check Azure portal to ensure service is running

2. **Azure OpenAI API call hanging**
   - Solution: Check Azure OpenAI service status
   - Verify credentials are correct

3. **Network connectivity issue**
   - Solution: Check Azure backend is accessible

**Fix:**

```bash
# Test backend health from terminal
curl -v https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net/health/

# Expected response (within 5 seconds):
# {"status": "AI Project Planner Backend Running"}

# If slow or no response:
# 1. Go to Azure Portal
# 2. Click on your App Service
# 3. Click "Overview" → Check "Status" (should be "Running")
# 4. Click "Restart" button
# 5. Wait 2-3 minutes
# 6. Try again
```

---

### Issue 3: 404 Not Found

**Error Message:**
```
status: 404
detail: "Not Found"
```

**Root Causes:**

1. **Incorrect backend URL in environment variable**
2. **API endpoint path wrong**
3. **Backend not deployed**

**Fix:**

1. **Verify backend URL in Vercel:**
   ```bash
   # Go to Vercel Dashboard → Project Settings → Environment Variables
   # Check: VITE_API_BASE_URL = https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net
   # (should NOT have trailing slash)
   ```

2. **Verify API endpoint exists:**
   ```bash
   curl https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net/
   
   # Expected response:
   # {"message": "AI Project Planner API", "version": "0.1.0", "status": "running"}
   ```

3. **Check backend logs:**
   ```bash
   # Azure Portal → App Service → Log stream
   # Should show: "✅ FastAPI application initialized successfully"
   ```

---

### Issue 4: 500 Server Error

**Error Message:**
```
status: 500
detail: "Failed to generate plan: ..."
```

**Root Causes:**

1. **Azure OpenAI API credentials missing**
2. **Azure OpenAI API credentials invalid**
3. **Database connection error**
4. **Unhandled exception in code**

**Fix:**

1. **Check environment variables on Azure:**
   ```bash
   # Azure Portal → App Service → Configuration
   # Verify these are set:
   - AZURE_OPENAI_ENDPOINT
   - AZURE_OPENAI_API_KEY
   - AZURE_OPENAI_DEPLOYMENT
   - AZURE_OPENAI_API_VERSION
   ```

2. **Check backend logs:**
   ```bash
   # Azure Portal → App Service → Log stream
   # Look for error messages starting with ❌
   ```

3. **Test locally first:**
   ```bash
   # On your machine, start backend
   cd backend
   python -m uvicorn app.main:app --reload
   
   # Test health endpoint
   curl http://localhost:8000/health/
   
   # Test plan endpoint (from another terminal)
   curl -X POST http://localhost:8000/plan/ \
     -H "Content-Type: application/json" \
     -d '{
       "project_name": "Test",
       "description": "Test description",
       "tech_stack": ["Python"]
     }'
   ```

---

### Issue 5: Backend URL Not Set in Environment

**Error Message in Console:**
```
🔌 API Base URL: http://localhost:8000
```

**Problem:** Frontend is using fallback localhost instead of Azure backend

**Fix:**

1. **Update Vercel environment variable:**
   ```bash
   # Vercel Dashboard → Settings → Environment Variables
   # Variable: VITE_API_BASE_URL
   # Value: https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net
   # Scopes: Production, Preview, Development
   ```

2. **Redeploy on Vercel:**
   - After updating env vars, click "Redeploy" on a previous deployment
   - Or push a new commit to trigger rebuild

3. **Verify in browser console:**
   ```
   🔌 API Base URL: https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net
   ```

---

## Complete Checklist for Connection

- [ ] **Frontend Deployed**: Vercel deployment URL working and accessible
- [ ] **Backend Running**: Azure App Service status = "Running"
- [ ] **Environment Variable Set**: `VITE_API_BASE_URL` configured in Vercel Dashboard
- [ ] **CORS Configured**: Azure backend `FRONTEND_URL` includes Vercel domain
- [ ] **Azure Service Restarted**: After updating `FRONTEND_URL`, restart App Service
- [ ] **Health Check Passes**: Can curl backend `/health/` endpoint
- [ ] **CORS Preflight OK**: OPTIONS request returns 204, not 400/403
- [ ] **No Network Errors**: Browser console shows successful API requests
- [ ] **Timeout Not Exceeded**: Requests complete within 30 seconds
- [ ] **Credentials Valid**: Azure OpenAI credentials are correct

---

## Network Flow Diagram

```
┌─────────────────────┐
│  Your Browser       │
│ (on Vercel domain)  │
└──────────┬──────────┘
           │
           ├─→ 1. Loads Frontend JS from Vercel CDN ✅
           │
           ├─→ 2. Reads VITE_API_BASE_URL from env ✅
           │
           ├─→ 3. You fill form & click "Generate Plan"
           │
           ├─→ 4. Browser sends OPTIONS preflight
           │     │
           │     └─→ Azure Backend CORS check
           │         ├─ Is origin in allow_origins? 
           │         ├─ YES → 204 No Content ✅
           │         └─ NO  → 400/403 error ❌
           │
           ├─→ 5. If CORS OK, sends POST /plan/
           │     │
           │     └─→ Backend Processes Request
           │         ├─ Call Azure OpenAI API
           │         ├─ Save to Database
           │         └─ Return Result
           │
           └─→ 6. Frontend displays result or error ✅
```

---

## Advanced Debugging

### Enable Verbose Logging on Backend

1. **Update `backend/app/main.py`:**
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)  # More verbose
   ```

2. **Check logs:**
   ```bash
   # Azure Portal → App Service → Log stream
   # You'll see every request and response
   ```

### Use Network Tab to Inspect Request/Response

1. Open DevTools → **Network** tab
2. Try generating a plan
3. Click on the **`plan`** POST request
4. Check:
   - **Headers** tab: See request headers sent
   - **Response** tab: See server response
   - **Timing** tab: See request duration

### Test with curl from Terminal

```bash
# Test health
curl -v https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net/health/

# Test plan generation (replace your-vercel-domain with actual domain)
curl -X POST https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net/plan/ \
  -H "Content-Type: application/json" \
  -H "Origin: https://your-vercel-domain.vercel.app" \
  -d '{
    "project_name": "Debug Test",
    "description": "Testing API from curl",
    "tech_stack": ["Python", "React"]
  }' \
  -v
```

---

## Getting Help

If you're still stuck:

1. **Share console errors** from DevTools
2. **Share backend logs** from Azure Log stream
3. **Verify** all environment variables are set
4. **Restart** Azure App Service
5. **Redeploy** on Vercel after making changes

---

## Summary

**Most common fix (90% of cases):**

1. Note your Vercel deployment URL
2. Add it to Azure backend `FRONTEND_URL` environment variable
3. Restart Azure App Service
4. Redeploy on Vercel
5. Wait 2 minutes
6. Test again

**Expected working state:**

- ✅ Console shows: `🔌 API Base URL: https://ai-project-planner-api-...`
- ✅ Console shows: `📤 API Request: POST /plan/ ...`
- ✅ Console shows: `✅ API Response: {"summary": ..., "phases": ...}`
- ✅ Plan displays on screen without errors

