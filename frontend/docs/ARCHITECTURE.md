# 🏗️ Frontend Architecture Diagram

## System Architecture

```
╔════════════════════════════════════════════════════════════════════════╗
║                         BROWSER / CLIENT SIDE                         ║
╚════════════════════════════════════════════════════════════════════════╝

                              index.html
                                  ↓
                          ┌───────────────┐
                          │   React App   │
                          │   (main.jsx)  │
                          └───────┬───────┘
                                  ↓
                        ┌─────────────────────┐
                        │   App.jsx (Router)  │
                        └──────────┬──────────┘
                                   ↓
                    ┌──────────────┴──────────────┐
                    ↓                             ↓
            ┌───────────────┐           ┌───────────────┐
            │  Home Page    │           │ PlanResult    │
            │    (/)        │           │   Page (/plan)│
            └─────┬─────────┘           └───────┬───────┘
                  ↓                             ↓
        ┌────────────────────┐      ┌────────────────────────┐
        │  Header Component  │      │  Header Component      │
        │  ProjectForm       │      │  ArchitectureView      │
        │  Feature Cards     │      │  WeeklyPlanView        │
        │  How it Works      │      │  TaskBoard             │
        │  Features List     │      │  IssueList             │
        │  Footer Component  │      │  Footer Component      │
        └────────┬───────────┘      └──────────┬─────────────┘
                 ↓                             ↓
        ┌───────────────────┐        ┌─────────────────────┐
        │ Form Submission   │        │  Display Plan Data  │
        │ (State & Hooks)   │        │  (Props-based)      │
        └────────┬──────────┘        └──────────────────────┘
                 ↓
        ┌──────────────────────────┐
        │  axios / apiClient.js    │
        │  HTTP Request Handler    │
        └────────────┬─────────────┘
                     ↓
        ╔════════════════════════════════════╗
        ║   HTTP REQUEST TO BACKEND          ║
        ║   POST http://localhost:8000/plan/ ║
        ╚════════════╤═══════════════════════╝
                     ↓

╔════════════════════════════════════════════════════════════════════════╗
║                         FASTAPI BACKEND SERVER                        ║
╚════════════════════════════════════════════════════════════════════════╝

              POST /plan/ endpoint
                     ↓
        ┌────────────────────────────┐
        │ Pydantic Request Validation │
        │ (PlanRequest Model)         │
        └────────────┬───────────────┘
                     ↓
        ┌────────────────────────────┐
        │  AIPlanner Service         │
        │  - Analyzes project        │
        │  - Calls OpenAI/Azure API  │
        │  - Generates phases/tasks  │
        └────────────┬───────────────┘
                     ↓
        ┌────────────────────────────┐
        │ Database Layer (SQLite)    │
        │ - Save to PlanDB table     │
        │ - Return saved record      │
        └────────────┬───────────────┘
                     ↓
        ┌────────────────────────────┐
        │ PlanResponse Model         │
        │ (JSON serialization)       │
        └────────────┬───────────────┘
                     ↓
        ╔════════════════════════════════════╗
        ║   HTTP RESPONSE (JSON)             ║
        ║   {                                ║
        ║     "summary": "...",              ║
        ║     "phases": [...]                ║
        ║   }                                ║
        ╚════════════╤═══════════════════════╝
                     ↓

╔════════════════════════════════════════════════════════════════════════╗
║                         BROWSER / CLIENT SIDE (CONT)                  ║
╚════════════════════════════════════════════════════════════════════════╝

        ┌──────────────────────────┐
        │  Response Handler        │
        │  - Parse JSON            │
        │  - Update state          │
        │  - Navigate to /plan     │
        │  - Pass data via props   │
        └────────────┬─────────────┘
                     ↓
        ┌──────────────────────────┐
        │  PlanResult Page         │
        │  - Renders components    │
        │  - Displays all sections │
        │  - User interaction      │
        └──────────────────────────┘
```

---

## Component Hierarchy

```
App (Root Component)
│
├── Header
│   └── Navigation & Branding
│
├── Routes
│   │
│   ├── Route: /
│   │   │
│   │   └── Home
│   │       ├── ProjectForm
│   │       │   ├── Input: project_name
│   │       │   ├── Input: description
│   │       │   ├── Input: tech_stack
│   │       │   └── Button: Generate Plan
│   │       │
│   │       ├── Feature Cards (3 columns)
│   │       │   ├── Smart Planning
│   │       │   ├── Task Breakdown
│   │       │   └── GitHub Ready
│   │       │
│   │       ├── How it Works (4 steps)
│   │       │
│   │       └── Features List
│   │
│   └── Route: /plan
│       │
│       └── PlanResult
│           ├── Navigation: Back Button
│           │
│           ├── Tab Navigation
│           │   ├── Architecture Tab
│           │   ├── Roadmap Tab
│           │   ├── Tasks Tab
│           │   └── Issues Tab
│           │
│           ├── ArchitectureView
│           │   ├── Summary Text
│           │   └── Component Cards (4 items)
│           │       ├── Frontend
│           │       ├── Backend
│           │       ├── Database
│           │       └── AI Services
│           │
│           ├── WeeklyPlanView
│           │   └── Timeline (Multiple Phases)
│           │       └── Each Phase:
│           │           ├── Phase Name
│           │           ├── Phase Number/Icon
│           │           └── Task List
│           │
│           ├── TaskBoard
│           │   └── Grid Layout (3 columns on desktop)
│           │       └── Task Cards (Multiple)
│           │           ├── Checkbox
│           │           ├── Task Description
│           │           └── Phase Label
│           │
│           └── IssueList
│               └── Issue Cards (Multiple, scrollable)
│                   ├── Title
│                   ├── Description
│                   ├── Labels
│                   ├── Details (collapsible)
│                   │   └── Acceptance Criteria
│                   └── Copy Button
│
└── Footer
    ├── About Section
    ├── Technology Section
    ├── Links Section
    └── Copyright
```

---

## Data Flow Diagram

```
┌────────────────────────────────────────────────────────────────────────┐
│ USER INTERACTION FLOW                                                  │
└────────────────────────────────────────────────────────────────────────┘

User Opens App
    ↓
┌─────────────────────────────────┐
│ Home Page Loads                 │
│ - Display form                  │
│ - Feature cards                 │
│ - How it works                  │
│ - Footer                        │
└─────────────────────────────────┘
    ↓
User Fills Form
    ↓
┌─────────────────────────────────┐
│ Form State Updates              │
│ - formData state                │
│ - Input validation              │
│ - Tech stack array              │
└─────────────────────────────────┘
    ↓
User Clicks Submit
    ↓
┌─────────────────────────────────┐
│ Form Validation                 │
│ - Check required fields         │
│ - Show error if invalid         │
└─────────────────────────────────┘
    ↓ (Valid)
┌─────────────────────────────────┐
│ Show Loading Spinner            │
│ - Overlay with spinner          │
│ - Set loading state             │
└─────────────────────────────────┘
    ↓
┌─────────────────────────────────┐
│ API Call                        │
│ - createPlan(formData)          │
│ - POST /plan/                   │
│ - Wait for response             │
└─────────────────────────────────┘
    ↓
┌────────────────┬────────────────┐
│                │                │
↓                ↓                ↓
Success        Error         Timeout
│              │               │
│              ↓               ↓
│         ┌──────────┐    ┌──────────┐
│         │Show Error│    │Show Error│
│         │Message   │    │Message   │
│         └──────────┘    └──────────┘
│              │               │
│              └───────┬───────┘
│                      ↓
│                 Keep on Page
│
└──────────────────────┬──────────────────────┐
                       ↓
          ┌────────────────────────────┐
          │ Parse Response             │
          │ - Extract plan data        │
          │ - summary string           │
          │ - phases array             │
          └────────────────────────────┘
                       ↓
          ┌────────────────────────────┐
          │ Navigate to /plan          │
          │ - Pass data via state      │
          │ - location.state.plan      │
          └────────────────────────────┘
                       ↓
          ┌────────────────────────────┐
          │ PlanResult Page Renders    │
          │ - Receives plan data       │
          │ - Displays all sections    │
          └────────────────────────────┘
                       ↓
          ┌────────────────────────────┐
          │ User Reviews Plan          │
          │ - Scrolls through sections │
          │ - Reads tasks              │
          │ - Views issues             │
          └────────────────────────────┘
                       ↓
          ┌────────────────────────────┐
          │ User Copies Issues         │
          │ - Click copy button        │
          │ - Clipboard updated        │
          │ - Paste to GitHub          │
          └────────────────────────────┘
                       ↓
          ┌────────────────────────────┐
          │ User Creates New Plan      │
          │ - Click "Create New"       │
          │ - Navigate back to /       │
          └────────────────────────────┘
```

---

## State Management Overview

```
ProjectForm Component State:
├── formData
│   ├── project_name: string
│   ├── description: string
│   └── tech_stack: string[]
├── techInput: string
├── loading: boolean
└── error: string | null

PlanResult Page State:
├── plan: {
│   ├── summary: string
│   └── phases: [{
│       ├── name: string
│       └── tasks: string[]
│   }]
└── }

IssueList Component State:
└── copiedIndex: number | null
    (for feedback when copy button clicked)

App/Router State:
├── Current route: "/" or "/plan"
└── Location state: { plan: {...} }
```

---

## API Integration Layer

```
┌──────────────────────────────────────────────────────────┐
│ src/services/apiClient.js                               │
│ - Axios instance configuration                          │
│ - Base URL: http://localhost:8000                       │
│ - Headers: Content-Type: application/json               │
│ - Interceptors: Error handling                          │
└──────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│ src/api/plannerApi.js                                   │
│ - Wrapper functions for API calls                       │
│                                                          │
│ Functions:                                               │
│ ├── checkHealth()        → GET /health                  │
│ ├── createPlan(data)     → POST /plan/                  │
│ ├── getPlan(id)          → GET /plan/{id}               │
│ └── listPlans()          → GET /plan/                   │
└──────────────────────────────────────────────────────────┘
                         ↓
┌──────────────────────────────────────────────────────────┐
│ Axios HTTP Client                                       │
│ - Handles actual HTTP requests                          │
│ - Manages headers, timeouts, retries                    │
│ - Parses JSON responses                                 │
└──────────────────────────────────────────────────────────┘
                         ↓
         ┌───────────────────────────────────┐
         │ Network Layer (Browser)            │
         │ - HTTP/HTTPS Protocol              │
         │ - TCP/IP Connection                │
         └───────────────────────────────────┘
                         ↓
       ╔═══════════════════════════════════╗
       ║    FastAPI Backend Server         ║
       ║    http://localhost:8000          ║
       ╚═══════════════════════════════════╝
```

---

## File Structure & Dependencies

```
frontend/
│
├── package.json
│   └── Dependencies:
│       ├── react@18
│       ├── react-dom@18
│       ├── react-router-dom@6
│       ├── axios@1.6
│       └── Dev: vite, tailwindcss, postcss, autoprefixer
│
├── vite.config.js
│   └── Configures: React plugin, dev server, build options
│
├── tailwind.config.js
│   └── Configures: Colors, spacing, responsive breakpoints
│
├── postcss.config.js
│   └── Plugins: tailwindcss, autoprefixer
│
├── index.html
│   └── Entry point: <div id="root"></div>
│
└── src/
    │
    ├── main.jsx
    │   └── ReactDOM.createRoot() → renders <App />
    │
    ├── App.jsx
    │   └── BrowserRouter with Routes:
    │       ├── / → <Home />
    │       └── /plan → <PlanResult />
    │
    ├── api/
    │   └── plannerApi.js
    │       └── Exports: checkHealth, createPlan, getPlan, listPlans
    │
    ├── components/
    │   ├── Header.jsx
    │   ├── Footer.jsx
    │   ├── ProjectForm.jsx
    │   ├── ArchitectureView.jsx
    │   ├── WeeklyPlanView.jsx
    │   ├── TaskBoard.jsx
    │   ├── IssueList.jsx
    │   └── LoadingSpinner.jsx
    │
    ├── pages/
    │   ├── Home.jsx
    │   └── PlanResult.jsx
    │
    ├── services/
    │   └── apiClient.js
    │       └── Axios instance with interceptors
    │
    └── styles/
        └── index.css
            └── Tailwind directives + custom component classes
```

---

## Error Handling Flow

```
┌──────────────────────────────┐
│ Try Form Submission          │
└──────────────┬───────────────┘
               ↓
       ┌───────────────┐
       │ Catch Error   │
       └───────┬───────┘
               │
    ┌──────────┴──────────┐
    │                     │
    ↓                     ↓
Validation Error    Network/API Error
    │                     │
    ↓                     ↓
setError(msg)          setError(msg)
    │                     │
    └──────────┬──────────┘
               ↓
       ┌───────────────────────┐
       │ Render Error Message  │
       │ in UI (Red banner)    │
       └───────────────────────┘
               ↓
       ┌───────────────────────┐
       │ User sees error       │
       │ Can retry or fix form │
       └───────────────────────┘
```

---

## Responsive Design Breakpoints

```
Mobile (< 640px):
├── Single column layouts
├── Full width inputs
├── Stacked cards
└── Hamburger menus (if added)

Tablet (640px - 1024px):
├── Two column grids
├── Flexible spacing
├── Readable text
└── Touch-friendly buttons

Desktop (> 1024px):
├── Three+ column grids
├── Full features visible
├── Optimized spacing
└── Mouse-friendly interactions

Tailwind Breakpoints Used:
├── sm: 640px (mobile to tablet)
├── md: 768px (tablet to small desktop)
└── lg: 1024px (desktop and beyond)
```

---

## CSS Architecture

```
Global Styles (src/styles/index.css):
├── @tailwind base
│   └── HTML element resets
├── @tailwind components
│   ├── .card (reusable card style)
│   ├── .btn-primary (primary button)
│   ├── .btn-secondary (secondary button)
│   ├── .input-field (form input)
│   └── .label (form label)
├── @tailwind utilities
│   └── All Tailwind utility classes
└── Custom Styles
    ├── Body background
    ├── Font family
    └── Box sizing

Component Styling:
├── Inline Tailwind classes in JSX
├── Dynamic classes with classNames (if used)
└── Responsive classes (sm:, md:, lg:)

Color System:
├── Primary: Blue (#0284c7, #0ea5e9)
├── Neutral: Slate (multiple shades)
├── Success: Green
├── Warning: Orange
└── Error: Red
```

---

This comprehensive architecture documentation shows how every piece
of the frontend application works together to create a seamless,
professional user experience.

🎉 Application is production-ready!
