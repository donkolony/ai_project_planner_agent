# 🎬 User Journey & Application Flow

## Complete User Workflow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         HOME PAGE (/)                                   │
│                                                                         │
│  ╔═══════════════════════════════════════════════════════════════╗    │
│  ║  AI PROJECT PLANNER AGENT                                    ║    │
│  ║  Transform ideas into structured plans                       ║    │
│  ╚═══════════════════════════════════════════════════════════════╝    │
│                                                                         │
│  ┌────────────────────┐  ┌────────────────────┐  ┌────────────────────┐│
│  │ 💡 Smart Planning  │  │ 📋 Task Breakdown  │  │ 🐙 GitHub Ready    ││
│  │                    │  │                    │  │                    ││
│  │ AI-powered analysis│  │ Detailed lists &   │  │ Auto-generated     ││
│  │ into phases        │  │ deliverables       │  │ GitHub issues      ││
│  └────────────────────┘  └────────────────────┘  └────────────────────┘│
│                                                                         │
│  ╔═══════════════════════════════════════════════════════════════╗    │
│  ║             CREATE YOUR PROJECT PLAN                          ║    │
│  ║                                                               ║    │
│  ║  Project Name:  [_____________________________]               ║    │
│  ║  Description:   [_____________________________]               ║    │
│  ║                 [_____________________________]               ║    │
│  ║  Tech Stack:    [React] [Node.js] [MongoDB]  [+Add]          ║    │
│  ║                                                               ║    │
│  ║  [              GENERATE PLAN              ]                 ║    │
│  ╚═══════════════════════════════════════════════════════════════╝    │
│                                                                         │
│  How it Works:                      Features:                          │
│  1️⃣ Fill in project details        ✓ Architecture visualization       │
│  2️⃣ Let AI create plan             ✓ Weekly sprint roadmap           │
│  3️⃣ Review results                 ✓ Task board with grouping        │
│  4️⃣ Copy issues to GitHub          ✓ Git-ready issues               │
│                                     ✓ Copy to clipboard               │
│                                     ✓ Responsive design               │
│                                                                         │
│  ⬇️  User fills form and clicks "Generate Plan"                      │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                    LOADING STATE                                        │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────┐      │
│  │                    🔄 Generating Plan...                    │      │
│  │                                                             │      │
│  │                    ◯ (spinning circle)                      │      │
│  │                                                             │      │
│  │              AI is analyzing your project                  │      │
│  └─────────────────────────────────────────────────────────────┘      │
│                                                                         │
│  ⬇️  API returns plan data                                             │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                    PLAN RESULT PAGE (/plan)                            │
│                                                                         │
│  ← Back to Home                                                        │
│                                                                         │
│  AI Study Planner - Development Plan                                  │
│  Your AI-generated project plan with architecture, phases, and issues │
│                                                                         │
│  ┌──────────────┬──────────────┬──────────────┬──────────────┐       │
│  │ Architecture │ Roadmap      │ Tasks        │ Issues       │       │
│  └──────────────┴──────────────┴──────────────┴──────────────┘       │
│                                                                         │
│  ╔═══════════════════════════════════════════════════════════════╗    │
│  ║  🏗️  ARCHITECTURE OVERVIEW                                     ║    │
│  ║                                                               ║    │
│  ║  System architecture and design patterns...                  ║    │
│  ║                                                               ║    │
│  ║  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌──────┐ ║   │
│  ║  │   Frontend  │  │   Backend   │  │  Database   │  │ APIs │ ║   │
│  ║  └─────────────┘  └─────────────┘  └─────────────┘  └──────┘ ║   │
│  ╚═══════════════════════════════════════════════════════════════╝    │
│                                                                         │
│  ╔═══════════════════════════════════════════════════════════════╗    │
│  ║  📅 WEEKLY SPRINT ROADMAP                                      ║    │
│  ║                                                               ║    │
│  ║  Phase 1: Foundation                                        ║    │
│  ║  ◉────────────────────────                                   ║    │
│  ║  • Setup project structure                                  ║    │
│  ║  • Configure database                                       ║    │
│  ║  • Implement API routes                                     ║    │
│  ║                                                               ║    │
│  ║  Phase 2: Core Features                                     ║    │
│  ║  ────◉──────────────────────                                 ║    │
│  ║  • Create models and schemas                                ║    │
│  ║  • Implement business logic                                 ║    │
│  ║  • Add authentication                                       ║    │
│  ║                                                               ║    │
│  ║  Phase 3: Integration                                       ║    │
│  ║  ────────◉────────────────                                   ║    │
│  ║  • Connect frontend and backend                             ║    │
│  ║  • Implement API client                                     ║    │
│  ║  • Add error handling                                       ║    │
│  ║                                                               ║    │
│  ║  Phase 4: Polish & Deploy                                   ║    │
│  ║  ────────────◉──────────────                                 ║    │
│  ║  • Write tests and documentation                            ║    │
│  ║  • Optimize performance                                     ║    │
│  ║  • Deploy to production                                     ║    │
│  ╚═══════════════════════════════════════════════════════════════╝    │
│                                                                         │
│  ╔═══════════════════════════════════════════════════════════════╗    │
│  ║  📋 TASK BREAKDOWN                                             ║    │
│  ║                                                               ║    │
│  ║  ┌─────────────────────┐  ┌─────────────────────┐            ║    │
│  ║  │ ☐ Setup backend     │  │ ☐ Create models     │            ║    │
│  ║  │ [Phase 1: Foundation]│  │ [Phase 2: Core]     │            ║    │
│  ║  └─────────────────────┘  └─────────────────────┘            ║    │
│  ║                                                               ║    │
│  ║  ┌─────────────────────┐  ┌─────────────────────┐            ║    │
│  ║  │ ☐ API routes        │  │ ☐ Error handling    │            ║    │
│  ║  │ [Phase 1: Foundation]│  │ [Phase 3: Integration]          ║    │
│  ║  └─────────────────────┘  └─────────────────────┘            ║    │
│  ║                                                               ║    │
│  ║  Total Tasks: 24        Phases: 4                            ║    │
│  ╚═══════════════════════════════════════════════════════════════╝    │
│                                                                         │
│  ╔═══════════════════════════════════════════════════════════════╗    │
│  ║  🐙 GIT-READY ISSUES                                           ║    │
│  ║                                                               ║    │
│  ║  [Phase 1] Setup and Planning                       [Copy]   ║    │
│  ║  Initialize Phase 1 for AI Study Planner                    ║    │
│  ║  Labels: phase, setup, foundation                          ║    │
│  ║                                                               ║    │
│  ║  Setup backend services                             [Copy]   ║    │
│  ║  Task from Phase 1 phase                                   ║    │
│  ║  Labels: foundation, task                                  ║    │
│  ║                                                               ║    │
│  ║  Create database models                             [Copy]   ║    │
│  ║  Task from Phase 2 phase                                   ║    │
│  ║  Labels: core, task                                        ║    │
│  ║                                                               ║    │
│  ║  ... more issues ...                                        ║    │
│  ║                                                               ║    │
│  ║  Total Issues: 28                                          ║    │
│  ╚═══════════════════════════════════════════════════════════════╝    │
│                                                                         │
│  ╔═══════════════════════════════════════════════════════════════╗    │
│  ║  💾 EXPORT & CONTINUE                                         ║    │
│  ║  [📥 Download as JSON] [📄 Export as PDF] [➕ Create New]     ║    │
│  ╚═══════════════════════════════════════════════════════════════╝    │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Data Flow Diagram

```
User Input
    ↓
┌─────────────────────┐
│  ProjectForm        │
│  - Validation       │
│  - Form state       │
│  - Tech stack mgmt  │
└─────────────────────┘
    ↓
Submit Form
    ↓
┌─────────────────────┐
│  createPlan()       │
│  (API call)         │
│  POST /plan/        │
└─────────────────────┘
    ↓
┌─────────────────────┐
│  Loading Spinner    │
│  (Overlay)          │
└─────────────────────┘
    ↓
API Response
    ↓
┌─────────────────────┐
│  Plan Data          │
│  - summary          │
│  - phases[]         │
└─────────────────────┘
    ↓
Navigate to /plan
    ↓
┌──────────────────────────────────────────────┐
│  PlanResult Page                             │
│  ├─ ArchitectureView (summary)               │
│  ├─ WeeklyPlanView (phases)                  │
│  ├─ TaskBoard (generate from phases)         │
│  └─ IssueList (generate from phases/tasks)   │
└──────────────────────────────────────────────┘
```

---

## Component Interaction Flow

```
App (Router)
│
├── Header (always visible)
│   └── Navigation & branding
│
├── Routes
│   ├── / (Home page)
│   │   ├── Home component
│   │   │   ├── Feature cards
│   │   │   └── ProjectForm
│   │   │       ├── Input: project_name
│   │   │       ├── Input: description
│   │   │       ├── Input: tech_stack (array)
│   │   │       ├── State: formData
│   │   │       ├── State: loading
│   │   │       ├── State: error
│   │   │       └── Action: onSubmit → API call → navigate
│   │   │
│   │   └── If loading
│   │       └── LoadingSpinner
│   │
│   └── /plan (Results page)
│       ├── PlanResult component
│       ├── Receives: plan (from location state)
│       │   ├── summary (string)
│       │   └── phases (array of {name, tasks})
│       │
│       ├── ArchitectureView
│       │   └── Displays: summary text
│       │
│       ├── WeeklyPlanView
│       │   ├── Maps: phases
│       │   └── Displays: timeline + tasks
│       │
│       ├── TaskBoard
│       │   ├── Generates: task array from phases
│       │   └── Displays: grid of tasks
│       │
│       └── IssueList
│           ├── Generates: issues from phases/tasks
│           ├── State: copiedIndex (for feedback)
│           └── Action: Copy to clipboard
│
└── Footer (always visible)
    └── Links & info
```

---

## API Call Sequence

```
┌─────────────────┐
│  User Submits   │
│  Project Form   │
└────────┬────────┘
         │
         ↓
┌────────────────────┐
│ Form Validation    │
│ (Client side)      │
└────────┬───────────┘
         │
         ↓
┌────────────────────────┐
│ Show Loading Spinner   │
└────────┬───────────────┘
         │
         ↓
┌───────────────────────────────────────┐
│ axios.post('/plan/', {                │
│   project_name: string,               │
│   description: string,                │
│   tech_stack: string[]                │
│ })                                    │
└────────┬────────────────────────────┘
         │
         ↓ (Network request)
         │
    ┌─────────────────┐
    │  FastAPI        │
    │  Backend        │
    │  POST /plan/    │
    └────────┬────────┘
             │
             ↓ (Process with AI)
             │
    ┌────────────────────┐
    │ Save to Database   │
    │ Generate Response  │
    └────────┬───────────┘
             │
             ↓ (Send response)
             │
         ┌─────────────────────┐
         │ Response Received   │
         │ {                   │
         │   summary: "...",   │
         │   phases: [...]     │
         │ }                   │
         └────────┬────────────┘
                  │
                  ↓
         ┌─────────────────────┐
         │ Hide Spinner        │
         │ Parse Response      │
         │ Navigate to /plan   │
         │ Pass data via state │
         └────────┬────────────┘
                  │
                  ↓
         ┌─────────────────────┐
         │ PlanResult Page     │
         │ Displays Plan Data  │
         └─────────────────────┘
```

---

## State Management Model

```
ProjectForm Component:
├── formData
│   ├── project_name: ""
│   ├── description: ""
│   └── tech_stack: []
├── techInput: ""
├── loading: false
├── error: null

PlanResult Component:
├── location.state.plan
│   ├── summary: "..."
│   └── phases: [{name, tasks}, ...]

IssueList Component:
├── copiedIndex: null
└── Auto-generates from phases

Navigation:
├── Route: /
├── Route: /plan
└── State passed via navigate(path, {state: {...}})
```

---

## Error Handling Flow

```
┌──────────────────────┐
│  Form Submission     │
└─────────┬────────────┘
          │
          ↓
┌──────────────────────────────────┐
│  Try API Call                    │
└─────────┬────────────────────────┘
          │
    ┌─────┴─────┐
    │           │
    ↓           ↓
 Success      Error
    │           │
    │           ↓
    │      ┌─────────────────────┐
    │      │ catch (err)         │
    │      │ - Network error     │
    │      │ - Server error      │
    │      │ - Validation error  │
    │      └────────┬────────────┘
    │               │
    │               ↓
    │      ┌──────────────────────┐
    │      │ setError(message)    │
    │      │ Display to user      │
    │      └──────────────────────┘
    │
    └─────────────┬──────────────────┐
                  │                  │
         ┌────────↓───────┐   ┌──────↓────────┐
         │ Navigate /plan │   │ Stay on page  │
         └────────────────┘   │ Show error msg│
                              └───────────────┘
```

---

## Mobile Responsive Behavior

```
Mobile (< 640px):
┌─────────────────┐
│ Header          │
├─────────────────┤
│ Content         │
│ (Single col)    │
│                 │
│                 │
├─────────────────┤
│ Footer          │
└─────────────────┘

Tablet (640px - 1024px):
┌─────────────────────────────┐
│ Header                      │
├─────────────────────────────┤
│ Content (2 cols)            │
│                             │
│                             │
├─────────────────────────────┤
│ Footer                      │
└─────────────────────────────┘

Desktop (> 1024px):
┌──────────────────────────────────────┐
│ Header                               │
├──────────────────────────────────────┤
│                                      │
│ Content (3-4 cols)                   │
│                                      │
│                                      │
├──────────────────────────────────────┤
│ Footer                               │
└──────────────────────────────────────┘
```

---

## Feature Checklist During Usage

After generating a plan, verify these features work:

```
Architecture Section:
  ☐ Summary text displays
  ☐ Component cards visible
  ☐ Color coding applied
  ☐ Responsive layout

Weekly Roadmap:
  ☐ Timeline dots visible
  ☐ Phases listed in order
  ☐ Tasks under each phase
  ☐ Responsive stacking

Task Board:
  ☐ Grid layout adapts
  ☐ Checkboxes functional
  ☐ Phase labels visible
  ☐ Statistics accurate

Issues:
  ☐ Issues generated
  ☐ Copy button works
  ☐ Feedback on copy
  ☐ Details expandable
  ☐ Labels visible

Overall:
  ☐ Page responsive
  ☐ Navigation works
  ☐ Back button returns home
  ☐ Create new plan button works
```

---

This comprehensive workflow ensures users can easily:
1. Submit their project idea
2. Receive AI-generated development plans
3. Review comprehensive plan details
4. Export issues to GitHub

The application is designed for smooth, intuitive interaction!
