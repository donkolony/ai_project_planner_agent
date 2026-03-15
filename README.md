[![Live Demo](https://img.shields.io/badge/Demo-Video-red?style=for-the-badge&logo=youtube)](YOUR_VIDEO_LINK_HERE)
[![Frontend](https://img.shields.io/badge/Frontend-Live-blue?style=for-the-badge)](https://ai-project-planner-agent.vercel.app/)
[![Backend](https://img.shields.io/badge/API-Documentation-green?style=for-the-badge)](https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net/docs)

# AI Project Planner Agent

An AI-powered assistant that transforms raw project ideas into structured architecture designs, actionable task breakdowns, and clear execution plans to improve project delivery and team coordination.

---

## Problem Statement

Student and junior development teams often struggle with:

- Poor project planning and unclear architecture
- Large tasks that are not broken into manageable pieces
- Lack of structured weekly goals
- Inconsistent issue tracking in Git platforms
- Rushed implementation without proper roadmap

The **AI Project Planner Agent** solves this by automatically generating:

- High-level system architecture
- Feature-to-task breakdown
- Structured project roadmap
- Git-ready issue descriptions
- Clear deliverables per phase

---

## Architecture Overview

### System Flow

User Input ➡️ React/JavaScript Frontend ➡️ FastAPI Backend ➡️ AI Planning Engine ➡️ Structured JSON Output ➡️ Dashboard Rendering

### Core Components

1. **Frontend (React + JavaScript)**
   - Project idea submission form
   - Architecture display
   - Roadmap visualization
   - Task breakdown board

2. **Backend (FastAPI + Python)**
   - Prompt orchestration
   - AI response validation
   - JSON schema enforcement
   - REST API endpoints

3. **AI Layer**
   - Architecture generator
   - Task breakdown generator
   - Roadmap planner
   - Issue formatter

---

## Tech Stack

**Frontend:** React, JavaScript, Axios, Tailwind CSS
**Backend:** Python, FastAPI, Pydantic, Uvicorn
**AI Integration:** Azure OpenAI (gpt-4o-mini), Structured JSON prompt design

---

## Features

- Convert project ideas into structured plans
- Generate full project architecture
- Break features into small actionable tasks
- Create dynamic project roadmap based on duration
- Produce Git-ready issue descriptions
- Enforce structured JSON outputs

---

## API Documentation

### Base URL

```
http://localhost:8000
```

### Endpoints

- **GET /health/** — Health Check
- **GET /plan/** — Get All Plans
- **POST /plan/** — Generate Plan
- **GET /plan/{plan_id}** — Get Plan

### Sample Request

```json
{
  "project_name": "AI Task Manager",
  "description": "AI Task Manager is a productivity web application that helps users organize and manage tasks using artificial intelligence.",
  "tech_stack": [
    "React",
    "Next.js",
    "Tailwind CSS",
    "Node.js",
    "Express.js",
    "PostgreSQL",
    "Prisma",
    "OpenAI API",
    "JWT Authentication",
    "Docker",
    "Vercel"
  ]
}
```

### Sample Response

```json
{
  "summary": "AI Task Manager is a productivity web application that leverages artificial intelligence to help users organize and manage tasks effectively.",
  "phases": [
    {
      "name": "Planning",
      "tasks": [
        "Define project scope and requirements",
        "Gather user feedback and conduct market research",
        "Create wireframes and initial UI/UX designs"
      ]
    },
    {
      "name": "Design",
      "tasks": [
        "Develop system architecture and database schema",
        "Design API endpoints and data models",
        "Finalize UI/UX designs and user flows"
      ]
    }
  ]
}
```

---

## ▶ Running Locally

### Backend

**Option 1: Using Python venv and pip**

```bash
cd backend
python -m venv venv
source venv/bin/activate      # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
uvicorn app.main:app --reload
```

**Option 2: Using uv sync**

```bash
cd backend
uv sync
```

### Frontend

```bash
cd frontend
# Install dependencies (use npm ci for exact versions)
npm install
# or
npm ci

# Start the frontend development server
npm run dev
```

---

## Key Engineering Decisions

- Structured JSON outputs for reliability
- Backend as AI orchestrator for security
- Modular planning components for extensibility
- Frontend supports both React and JavaScript for flexibility

---

## Codebase Structure

```
backend/
├── app/
├── tests/
├── requirements.txt
├── main.py
└── docs/            # Backend-specific documentation (API.md, Database.md, Setup.md)

frontend/
├── src/
├── package.json
├── vite.config.js
└── docs/            # Frontend-specific documentation (Components.md, Deployment.md, Styling.md)

README.md            # Main project README
```

---

## Demo Flow (How to Test)

1. **Start backend:**
   Activate the virtual environment and run `uvicorn app.main:app --reload`

2. **Start frontend:**
   Navigate to `frontend` and run `npm run dev`

3. **Access app:**
   Open your browser at `http://localhost:5173` (Vite default)

4. **Test features:**
   - Submit a project idea
   - View generated architecture
   - Explore roadmap and task breakdown
   - Use API endpoints via Swagger UI (`http://localhost:8000/docs`)

---

## Future Improvements

### Feature Enhancements

- Implement the ability to **download project plans as JSON**
- Add **export to PDF** functionality for plans and reports
- Visualize **roadmap and weekly plans graphically**
- Include **tasks and issues visualization** in the frontend dashboard

### Platform Enhancements

- GitHub/GitLab **automatic issue creation**
- Multi-agent planning and review
- Persistent database storage for plans and tasks
- Authentication & team collaboration features
- Sprint analytics and performance dashboard

---

## Project Goal

To build an AI-powered planning system that improves project organization, task clarity, and execution discipline for students and junior developers.

**AI Project Planner Agent — Turning ideas into executable roadmaps.**
