# Immediate Action Steps to Fix "Failed to generate plan"

## 📋 Quick Checklist

Follow these steps in order to diagnose and fix the connection issue.

---

## Step 1: Find Your Vercel URL (1 minute)

1. Go to: https://vercel.com/dashboard/projects
2. Click on: `ai_project_planner_agent`
3. **Copy your Deployment URL** - it looks like: `https://ai-project-planner-abc123xyz.vercel.app`
4. **Save this URL** - you'll need it in the next step

---

## Step 2: Redeploy Frontend with Updated Code (2 minutes)

The debugging code was pushed to GitHub. Now trigger a new Vercel build:

**Option A: Automatic (Recommended)**
```bash
cd /home/yamkelamacwili/Desktop/porfolio_projects/ai_project_planner_agent
git push origin main  # This triggers automatic Vercel deployment
```

**Option B: Manual in Vercel Dashboard**
1. Go to Vercel Dashboard → Deployments
2. Click the "..." menu on the latest deployment
3. Click "Redeploy"

**Wait 2-3 minutes** for build to complete.

---

## Step 3: Check Vercel Environment Variable (2 minutes)

1. Go to Vercel Dashboard → Settings → Environment Variables
2. **Verify** `VITE_API_BASE_URL` is set to:
   ```
   https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net
   ```
   (without trailing slash)

3. Make sure it's enabled for: **Production**, **Preview**, **Development**

✅ **If changed**: Click "Redeploy" again after updating

---

## Step 4: Update Azure Backend CORS (3 minutes)

This is the **most common fix** for "Failed to generate plan"!

1. Go to Azure Portal: https://portal.azure.com
2. Find your App Service: `ai-project-planner-api-*`
3. Click **Configuration** (left sidebar)
4. Find or Add environment variable: `FRONTEND_URL`
5. Set value to your Vercel URL (from Step 1):
   ```
   https://ai-project-planner-abc123xyz.vercel.app
   ```
6. Click **Save**
7. Go to **Overview** → Click **Restart** button
8. **Wait 2-3 minutes** for service to restart

---

## Step 5: Test the Connection (2 minutes)

Open your Vercel app and **open Browser DevTools** (Press `F12`):

1. Go to **Console** tab
2. Try filling out the form and clicking **Generate Plan**
3. **Look for these success messages:**
   ```
   🔌 API Base URL: https://ai-project-planner-api-...
   📤 API Request: POST /plan/ ...
   ✅ API Response: {"summary": "...", "phases": ...}
   ```

4. **If you see these, it's working!** ✅

---

## Step 6: Troubleshoot If Still Not Working (5-10 minutes)

### Check Error Message in Console

Look for error logs like:
- **"Network Error"** → Backend unreachable
- **"Request timeout"** → Backend too slow
- **"status: 404"** → Wrong backend URL
- **"status: 500"** → Backend error (check Azure logs)
- **"CORS blocked"** → Frontend URL not in CORS allowed list

### Check DevTools Network Tab

1. Open DevTools → **Network** tab
2. Click **Generate Plan**
3. Look for the **OPTIONS** request to `/plan/`:
   - ✅ **Status 204** = CORS working
   - ❌ **Status 400** or **403** = CORS not configured

### Check Azure Backend Status

```bash
# Test health endpoint
curl https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net/health/

# Should respond with (within 5 seconds):
# {"status": "AI Project Planner Backend Running"}
```

### Check Azure Logs

1. Go to Azure Portal
2. Click on App Service → **Log stream** (left sidebar)
3. Look for:
   - ✅ `🔒 CORS Configuration` messages (shows allowed origins)
   - ✅ `📋 Generating plan` messages
   - ❌ Error messages starting with `❌`

---

## 🚀 Expected Working State

When everything is working, you should see:

**Console Output:**
```javascript
🔌 API Base URL: https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net
📤 API Request: {
  method: "POST",
  url: "https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net/plan/",
  data: {...}
}
✅ API Response: {
  status: 200,
  url: "/plan/",
  data: {
    summary: "...",
    phases: [...]
  }
}
```

**Network Tab:**
- OPTIONS /plan/ → Status: **204**
- POST /plan/ → Status: **200**

**Page Display:**
- Plan results show successfully ✅
- No error messages ✅

---

## 🆘 Still Having Issues?

Follow the detailed guide: **`DEBUGGING_API_CONNECTION.md`** in project root

Or try these:

1. **Clear browser cache:**
   ```bash
   # In browser DevTools: Clear site data
   # Or: Ctrl+Shift+Delete (Windows) / Cmd+Shift+Delete (Mac)
   ```

2. **Check if API is actually working locally:**
   ```bash
   cd backend
   python -m uvicorn app.main:app --reload
   
   # In another terminal:
   curl -X POST http://localhost:8000/plan/ \
     -H "Content-Type: application/json" \
     -d '{
       "project_name": "Test",
       "description": "Test description",
       "tech_stack": ["Python"]
     }'
   ```

3. **Restart Azure App Service:**
   - Go to Azure Portal
   - App Service → Overview → Click "Restart"
   - Wait 5 minutes

4. **Restart Vercel:**
   - Vercel Dashboard → Deployments
   - Click "..." → "Redeploy"

---

## Summary

| Step | Time | What | Why |
|------|------|------|-----|
| 1 | 1m | Get Vercel URL | Need for next steps |
| 2 | 2m | Redeploy frontend | Apply debugging code |
| 3 | 2m | Update CORS on backend | Most common issue! |
| 4 | 3m | Restart Azure service | Apply CORS changes |
| 5 | 2m | Test in browser | Verify it works |
| **Total** | **~10 mins** | **Full Fix** | **Should work!** |

---

## Contact Info

If you're stuck on any step, check:
- **DEBUGGING_API_CONNECTION.md** - Detailed troubleshooting guide
- **VERCEL_DEPLOYMENT.md** - Full deployment documentation
- Backend logs in Azure Portal Log stream
- Browser DevTools Console and Network tabs

Good luck! 🚀
