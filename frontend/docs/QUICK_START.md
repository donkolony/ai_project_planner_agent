# 🚀 Quick Start Guide - Frontend

## Installation & Setup (5 minutes)

### Step 1: Navigate to Frontend Directory

```bash
cd frontend
```

### Step 2: Install Dependencies

```bash
npm install
```

Expected output:

```
added X packages in Xs
```

### Step 3: Verify Backend is Running

Ensure your FastAPI backend is running on `http://localhost:8000`

```bash
# From backend directory in another terminal
cd backend
python -m uvicorn app.main:app --reload
```

### Step 4: Start Development Server

```bash
npm run dev
```

Output:

```
  VITE v5.0.0  ready in 123 ms

  ➜  Local:   http://localhost:5173/
  ➜  press h to show help
```

### Step 5: Open in Browser

Navigate to: **http://localhost:5173**

---

## 🎯 Using the Application

### Home Page

1. **Fill in Project Details:**
   - Project Name (required)
   - Description (required)
   - Technology Stack (optional - add as many as you want)

2. **Click "Generate Plan"**
   - Loading spinner appears
   - API processes your request

3. **View Results**
   - Automatically navigates to results page

### Results Page

View four sections:

1. **Architecture** - System design overview
2. **Roadmap** - Week-by-week development phases
3. **Tasks** - All tasks from phases in grid layout
4. **Issues** - GitHub-ready issues with copy button

---

## ⚙️ Configuration

### Environment Variables

Create `.env.local` file in frontend directory:

```bash
# Optional - defaults to http://localhost:8000
VITE_API_BASE_URL=http://localhost:8000
```

### Build Configuration Files

Files already configured and ready to use:

- ✅ `vite.config.js` - Vite build tool
- ✅ `tailwind.config.js` - Tailwind CSS
- ✅ `postcss.config.js` - PostCSS processing
- ✅ `index.html` - HTML entry point

---

## 📦 Available Commands

```bash
# Start development server (HMR enabled)
npm run dev

# Build for production
npm run build

# Preview production build locally
npm run preview

# Run linter (optional, configured but not required)
npm run lint
```

---

## 🔧 Troubleshooting

### Issue: "Port 5173 already in use"

**Solution:**

```bash
npm run dev -- --port 5174
```

### Issue: "Cannot find module 'react'"

**Solution:**

```bash
rm -rf node_modules package-lock.json
npm install
```

### Issue: "Backend connection failed"

**Solution:**

1. Verify backend is running: `http://localhost:8000/health`
2. Check network tab in browser DevTools
3. Ensure CORS is enabled on backend
4. Verify `VITE_API_BASE_URL` if using custom URL

### Issue: "Form submission doesn't work"

**Solution:**

1. Open browser console (F12)
2. Check for error messages
3. Verify backend endpoint: `POST /plan/`
4. Check request payload in Network tab

---

## 📁 File Structure Quick Reference

```
frontend/
├── src/
│   ├── api/plannerApi.js         ← API calls here
│   ├── components/               ← Reusable components
│   ├── pages/                    ← Full page components
│   ├── services/apiClient.js     ← Axios client
│   ├── styles/index.css          ← Global styles
│   ├── App.jsx                   ← Routing setup
│   └── main.jsx                  ← React DOM render
├── package.json                   ← Dependencies
├── vite.config.js                ← Build config
└── README.md                      ← Full documentation
```

---

## 🎨 Component Overview

### Pages

- **Home** - Form submission page
- **PlanResult** - Results display with tabs

### Components

- **Header** - Navigation bar
- **ProjectForm** - Input form with validation
- **ArchitectureView** - Architecture cards
- **WeeklyPlanView** - Timeline visualization
- **TaskBoard** - Grid of tasks
- **IssueList** - GitHub issues with copy button
- **Footer** - Footer section
- **LoadingSpinner** - Loading overlay

---

## 🌐 API Endpoints

The frontend calls these backend endpoints:

```
POST /plan/
  Body: {
    "project_name": "string",
    "description": "string",
    "tech_stack": ["string", ...]
  }
  Response: {
    "summary": "string",
    "phases": [
      {
        "name": "string",
        "tasks": ["string", ...]
      }
    ]
  }

GET /health
  Response: {"status": "ok"}
```

---

## ✨ Features Checklist

As you explore the app, check off these features:

- [ ] Home page loads and displays form
- [ ] Can enter project name
- [ ] Can enter description
- [ ] Can add technology stack items
- [ ] Form validation prevents empty submission
- [ ] Clicking "Generate Plan" calls API
- [ ] Loading spinner appears during generation
- [ ] Results page displays with plan data
- [ ] Architecture section shows summary
- [ ] Weekly roadmap shows timeline
- [ ] Task board displays all tasks
- [ ] Issue list shows generated issues
- [ ] Copy button works (button text changes to "✓ Copied")
- [ ] Can navigate back to home
- [ ] Responsive design works on mobile/tablet

---

## 💡 Tips

### For Development

- Use React DevTools extension for component inspection
- Check Network tab to see API calls
- Use Console for debugging
- Press `h` in terminal for Vite help

### For Styling

- Tailwind classes are already available
- Add new classes directly to JSX
- Refer to `tailwind.config.js` for custom colors
- Use IntelliSense for class suggestions

### For API Integration

- API client is in `src/services/apiClient.js`
- API functions are in `src/api/plannerApi.js`
- Add new endpoints to `plannerApi.js`

---

## 🚀 Next Steps

### After Verifying It Works:

1. **Build for Production:**

   ```bash
   npm run build
   ```

2. **Deploy to Hosting:**
   - Vercel: `vercel deploy`
   - Netlify: Drag & drop `dist/` folder
   - Docker: Build container with Dockerfile
   - AWS S3 + CloudFront
   - Any static host (dist/ is the output)

3. **Share with Team:**
   - Share frontend README
   - Set backend URL in environment
   - Team can run `npm install && npm run dev`

---

## 📚 Documentation

- **Full README:** `frontend/README.md`
- **Implementation Details:** `FRONTEND_IMPLEMENTATION.md` (root)
- **Structure Reference:** `FRONTEND_STRUCTURE.sh` (root)

---

## ✅ Everything Ready!

Your frontend is completely set up and ready to use:

✓ All dependencies configured
✓ All components implemented
✓ All pages created
✓ All API integration done
✓ Styling with Tailwind CSS
✓ Responsive design
✓ Error handling
✓ Loading states
✓ Documentation complete

**Start with:** `npm install && npm run dev`

Happy coding! 🎉
