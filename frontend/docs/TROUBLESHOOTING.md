# Troubleshooting & Common Issues Guide

## Installation Issues

### Issue: `npm install` fails

**Error:** `npm ERR!` or similar

**Solutions:**

```bash
# 1. Clear npm cache
npm cache clean --force

# 2. Delete node_modules and lock file
rm -rf node_modules package-lock.json

# 3. Reinstall
npm install

# 4. If still failing, check Node version
node --version  # Should be 16+
npm --version   # Should be 7+
```

### Issue: Permission denied during installation

**Solutions:**

```bash
# Use sudo carefully
sudo npm install

# Or fix npm permissions
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
export PATH=~/.npm-global/bin:$PATH
```

---

## Development Server Issues

### Issue: "Port 5173 already in use"

**Error:** `Error: listen EADDRINUSE: address already in use :::5173`

**Solutions:**

```bash
# 1. Use a different port
npm run dev -- --port 5174

# 2. Kill process using port 5173
# On Linux/Mac:
lsof -i :5173
kill -9 <PID>

# On Windows:
netstat -ano | findstr :5173
taskkill /PID <PID> /F
```

### Issue: Hot Module Replacement (HMR) not working

**Error:** Changes don't reflect, need to refresh manually

**Solutions:**

```bash
# 1. Clear browser cache
# Ctrl+Shift+Delete (or Cmd+Shift+Delete on Mac)

# 2. Hard refresh
# Ctrl+Shift+R (or Cmd+Shift+R on Mac)

# 3. Restart dev server
# Stop: Ctrl+C
# Start: npm run dev

# 4. Check vite.config.js has HMR enabled
```

### Issue: "ENOSPC: System limit for number of file watchers exceeded"

**Error:** On Linux systems with file watching

**Solutions:**

```bash
# Increase file watcher limit
echo fs.inotify.max_user_watches=582222 | sudo tee -a /etc/sysctl.conf
sudo sysctl -p

# Or run dev server without watching specific files
npm run dev
```

---

## Backend Connection Issues

### Issue: "Cannot GET /health" or API connection refused

**Error:** Network tab shows 404 or Connection refused

**Causes & Solutions:**

1. **Backend not running:**

   ```bash
   # Terminal 1 - Start backend
   cd backend
   python -m uvicorn app.main:app --reload

   # Should show:
   # Uvicorn running on http://127.0.0.1:8000
   ```

2. **Backend on different URL:**

   ```bash
   # Create .env.local in frontend directory
   VITE_API_BASE_URL=http://localhost:3000
   # or
   VITE_API_BASE_URL=http://192.168.1.100:8000
   ```

3. **CORS not enabled on backend:**

   Backend needs CORS middleware:

   ```python
   from fastapi.middleware.cors import CORSMiddleware

   app.add_middleware(
       CORSMiddleware,
       allow_origins=["http://localhost:5173", "http://localhost:3000"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

4. **Firewall blocking connection:**

   ```bash
   # Check if port is accessible
   curl http://localhost:8000/health

   # Should return: {"status":"ok"}
   ```

### Issue: Form submission hangs or times out

**Error:** Loading spinner never goes away

**Causes:**

1. **Backend endpoint doesn't exist:**
   - Verify `POST /plan/` endpoint exists
   - Check backend logs for errors

2. **Slow network:**
   - Check Network tab for request duration
   - Verify request/response size

3. **API timeout:**
   - Check axios timeout in `src/services/apiClient.js`
   - Increase if backend is slow

---

## Form & Input Issues

### Issue: Form validation not working

**Problem:** Can submit empty form

**Solutions:**

```jsx
// Check ProjectForm.jsx line with validation:
if (!formData.project_name.trim() || !formData.description.trim()) {
  setError('Please fill in all required fields')
  return
}

// Add HTML5 validation as backup
<input required type="text" ... />
```

### Issue: Tech stack input doesn't work

**Problem:** Can't add technologies

**Solutions:**

```bash
# 1. Check browser console for errors
# Press F12, go to Console tab

# 2. Verify handleAddTech function in ProjectForm.jsx

# 3. Try pressing Enter instead of clicking button
# The component listens to both

# 4. Clear browser data
# Settings → Privacy → Clear browsing data
```

### Issue: Special characters in form cause errors

**Problem:** Text with quotes, ampersands, etc. breaks

**Solution:**
API automatically handles encoding, but if issues persist:

```javascript
// In ProjectForm.jsx, sanitize input
const sanitize = (str) => {
  return str.replace(/[<>]/g, "").trim();
};
```

---

## API Response Issues

### Issue: "Plan not found" after generation

**Error:** 404 from backend

**Causes:**

1. Backend not saving plan to database
2. Wrong response structure from backend
3. Database connection issue

**Solution:**

```bash
# Check backend database
# Verify SQLite file exists: backend/planner.db
# Check database has data: sqlite3 planner.db "SELECT * FROM plan;"
```

### Issue: Malformed API response

**Error:** "Cannot read property 'summary' of undefined"

**Causes:**

1. **Backend returning wrong format:**

   ```python
   # Correct format:
   {
     "summary": "...",
     "phases": [
       {"name": "...", "tasks": ["...", "..."]}
     ]
   }
   ```

2. **Frontend not handling response:**
   ```javascript
   // Check src/api/plannerApi.js
   // Verify response.data structure
   ```

**Solution:**

```bash
# Test backend directly with curl
curl -X POST http://localhost:8000/plan/ \
  -H "Content-Type: application/json" \
  -d '{
    "project_name": "Test",
    "description": "Test project",
    "tech_stack": ["React"]
  }'
```

---

## Component Display Issues

### Issue: Tailwind CSS not applied (unstyled page)

**Error:** Page looks ugly, no colors or formatting

**Causes:**

1. Tailwind CSS not compiled
2. CSS file not imported
3. Build cache issue

**Solutions:**

```bash
# 1. Verify CSS import in App.jsx
import './styles/index.css'

# 2. Check tailwind.config.js has correct paths
content: [
  "./index.html",
  "./src/**/*.{js,jsx,ts,tsx}",
]

# 3. Restart dev server
npm run dev

# 4. Clear Vite cache
rm -rf node_modules/.vite
npm run dev
```

### Issue: Images or components not loading

**Error:** Blank spaces where content should be

**Solutions:**

```bash
# 1. Check browser console for 404 errors
# Press F12 > Console

# 2. Verify component imports
// Correct:
import Header from './components/Header'
// Incorrect:
import Header from './components/Header.jsx' // (might fail)

# 3. Check file paths are correct
# Components should be in: src/components/

# 4. Restart dev server
npm run dev
```

### Issue: Layout looks broken on mobile

**Error:** Single-column layout not working, text too small

**Solutions:**

```bash
# 1. Check viewport meta tag in index.html
<meta name="viewport" content="width=device-width, initial-scale=1.0" />

# 2. Test responsive design
# F12 > Toggle device toolbar > Select mobile device

# 3. Verify Tailwind breakpoints
# sm: 640px
# md: 768px
# lg: 1024px

# 4. Check components use responsive classes
# Correct:
className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3"
# Incorrect:
className="grid grid-cols-3" // (always 3 columns)
```

---

## Performance Issues

### Issue: Page loads slowly

**Error:** Slow first page load, noticeable delay

**Solutions:**

```bash
# 1. Check network tab for large assets
# F12 > Network tab > reload

# 2. Check backend response time
# Network tab > API call > Duration

# 3. Build and test production
npm run build
npm run preview

# 4. Check browser extensions blocking scripts
# Try in incognito mode
```

### Issue: Copy to clipboard doesn't work

**Error:** Button click doesn't copy issue text

**Solutions:**

```javascript
// Check copyToClipboard function in IssueList.jsx
navigator.clipboard.writeText(issueMarkdown).then(() => {
  // This requires HTTPS in production
  // or localhost in development
});

// If still failing:
// 1. Page must be HTTPS in production
// 2. Localhost works in development
// 3. Check browser console for errors
// 4. Use older clipboard API if needed
```

---

## Browser Compatibility Issues

### Issue: "React is not defined" error

**Error:** React component won't render

**Solutions:**

```jsx
// Add React import (may not be needed in newer versions)
import React from "react";

// Or ensure src/main.jsx has proper setup
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
```

### Issue: Feature works in Chrome but not Firefox

**Error:** Inconsistent behavior across browsers

**Solutions:**

```bash
# 1. Check browser compatibility
# Visit: https://caniuse.com/

# 2. Use standard APIs:
# ✓ Fetch
# ✓ localStorage
# ✓ clipboard
# ✗ Non-standard APIs

# 3. Add vendor prefixes (autoprefixer does this)

# 4. Test in multiple browsers:
# Chrome, Firefox, Safari, Edge
```

---

## Build & Deployment Issues

### Issue: `npm run build` fails

**Error:** Build process exits with error

**Solutions:**

```bash
# 1. Check for syntax errors
npm run build

# 2. Clear cache and rebuild
rm -rf dist node_modules/.vite
npm run build

# 3. Check for missing dependencies
npm install

# 4. Review error message carefully
# Look for file paths and line numbers
```

### Issue: Production build doesn't work

**Error:** Works in `npm run dev` but not after `npm run build`

**Causes:**

1. Missing environment variables
2. API URL not configured correctly
3. Asset paths wrong

**Solutions:**

```bash
# 1. Set environment variable before building
VITE_API_BASE_URL=http://localhost:8000 npm run build

# 2. Or create .env.production
VITE_API_BASE_URL=https://api.example.com

# 3. Check dist/index.html is correct
# Should reference bundled JS/CSS

# 4. Test locally first
npm run build
npm run preview
# Open http://localhost:4173
```

### Issue: Production API calls fail

**Error:** Backend works in dev, fails in production

**Solutions:**

```bash
# 1. Verify API URL is set correctly
# In .env.production or deployment config

# 2. Check CORS on backend
# Must allow production frontend URL

# 3. Verify backend is accessible from internet
curl https://api.example.com/health

# 4. Check browser console for actual error
# Production might hide errors
```

---

## Debugging Tips

### Enable Console Logging

```javascript
// In src/services/apiClient.js
apiClient.interceptors.response.use(
  (response) => {
    console.log("✓ API Response:", response);
    return response;
  },
  (error) => {
    console.error("✗ API Error:", error);
    return Promise.reject(error);
  },
);
```

### Check Network Requests

```
Press F12 > Network tab
1. Reload page
2. Look for API calls
3. Check status: 200 (good), 404 (not found), 500 (server error)
4. Click request to see details
5. Check Response tab for actual data
```

### Browser DevTools Shortcuts

```
F12 or Ctrl+Shift+I     Open DevTools
Ctrl+Shift+C            Inspect element
Ctrl+Shift+J            Open console
Ctrl+Shift+K            Toggle console
Ctrl+Shift+E            Open inspector
Ctrl+Shift+N            Toggle network log
```

### React DevTools

```
Install extension: "React Developer Tools"
1. Open DevTools
2. Go to "Components" tab
3. Select any component
4. View props and state on right panel
5. Modify state to test behavior
```

---

## Clean Start (Nuclear Option)

If all else fails, completely clean and reinstall:

```bash
# 1. Delete all generated files
rm -rf node_modules package-lock.json dist

# 2. Clear npm cache
npm cache clean --force

# 3. Reinstall from scratch
npm install

# 4. Verify backend is running
curl http://localhost:8000/health

# 5. Start fresh
npm run dev

# 6. Test with simple request
# Open http://localhost:5173
# Try to submit form
```

---

## Getting Help

If you're still stuck:

1. **Check error message carefully**
   - Copy exact error text
   - Google the error message

2. **Review documentation**
   - frontend/README.md
   - QUICK_START.md
   - This troubleshooting guide

3. **Check backend logs**
   - Backend terminal shows request details
   - Look for tracebacks
   - Verify endpoint exists

4. **Isolate the problem**
   - Does homepage load? (Network issue?)
   - Does form work? (API issue?)
   - Are results displayed? (Data parsing issue?)

5. **Test manually**
   ```bash
   # Test backend directly
   curl http://localhost:8000/health
   curl -X POST http://localhost:8000/plan/ \
     -H "Content-Type: application/json" \
     -d '{"project_name":"Test","description":"Test","tech_stack":["React"]}'
   ```

---

## Common Patterns & Solutions

| Problem           | Check            | Solution                       |
| ----------------- | ---------------- | ------------------------------ |
| Page blank        | Console          | Missing import, syntax error   |
| No styling        | Network tab      | CSS file not loading           |
| API fails         | Backend terminal | Backend not running            |
| Form hangs        | Backend logs     | Endpoint doesn't exist         |
| Layout broken     | Device toolbar   | Missing responsive classes     |
| Copy doesn't work | Browser console  | Check clipboard API support    |
| Build fails       | Error message    | Check syntax, dependencies     |
| CORS error        | Network tab      | Add CORS middleware to backend |

---

## Support Resources

- **Vite Docs:** https://vitejs.dev/guide/
- **React Docs:** https://react.dev/
- **Tailwind Docs:** https://tailwindcss.com/docs
- **Axios Docs:** https://axios-http.com/docs/intro
- **MDN Web Docs:** https://developer.mozilla.org/en-US/

---

Good luck troubleshooting! Most issues have simple solutions. 🚀
