# AI Project Planner Agent

An AI-powered assistant that transforms raw project ideas into structured architecture designs, actionable task breakdowns, and clear weekly execution plans to improve project delivery and team coordination.

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
- Project duration-based sprint plan
- Git-ready issue descriptions
- Clear deliverables per week

---

## Architecture Overview

### System Flow

User Input → Frontend → Backend → AI Planning Engine → Structured JSON Output → Dashboard Rendering

### Core Components

1. Frontend (React + JavaScript)
   - Project idea submission form
   - Architecture display
   - Weekly roadmap visualization
   - Task breakdown board

2. Backend (FastAPI)
   - Prompt orchestration
   - AI response validation
   - JSON schema enforcement
   - REST API endpoints

3. AI Layer
   - Architecture generator
   - Task breakdown generator
   - Weekly sprint planner
   - Issue formatter

---

## Tech Stack

Frontend: React, JavaScript, Axios, Tailwind CSS

Backend: Python, FastAPI, Pydantic, Uvicorn

AI Integration: Azure OpenAI (gpt-4o-mini) or OpenAI API, Structured JSON prompt design

Hosting: Azure App Services (backend), Vercel (frontend)

---

## Features

- Convert project ideas into structured plans
- Generate full project architecture
- Break features into small actionable tasks
- Create 5-week sprint roadmap
- Produce Git-ready issue descriptions
- Enforce structured JSON outputs

---

## API Documentation

### Base URL

http://localhost:8000

### Endpoints

**Health**

- GET /health/ : Health check

**Planner**

- GET /plan/ : Get all plans
- POST /plan/ : Generate plan
- GET /plan/{plan_id} : Get a specific plan

**Default**

- GET / : Root

### Example Request (POST /plan/)

Request Body:

```json
{
  "project_name": "AI Task Manager",
  "description": "AI Task Manager is a productivity web application that helps users organize and manage tasks using artificial intelligence. Users can create tasks, set deadlines, and categorize work. The AI analyzes task descriptions, deadlines, and workload to automatically prioritize tasks, suggest schedules, and convert natural language inputs into structured tasks with priorities, tags, and due dates.",
  "tech_stack": [
    "React",
    "JavaScript",
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

Response:

```json
{
  "summary": "AI Task Manager is a productivity web application that leverages artificial intelligence to help users organize and manage their tasks effectively.",
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
    },
    {
      "name": "Development",
      "tasks": [
        "Set up project repository and development environment",
        "Implement front-end components using React and JavaScript",
        "Develop back-end services using Node.js and Express.js",
        "Integrate PostgreSQL database with Prisma",
        "Implement AI features using OpenAI API",
        "Set up JWT authentication for user management"
      ]
    },
    {
      "name": "Testing",
      "tasks": [
        "Conduct unit testing for individual components",
        "Perform integration testing for the complete application",
        "Gather user feedback through beta testing"
      ]
    },
    {
      "name": "Deployment",
      "tasks": [
        "Containerize application using Docker",
        "Deploy application on Vercel",
        "Set up monitoring and logging for the application"
      ]
    },
    {
      "name": "Maintenance",
      "tasks": [
        "Monitor application performance and user feedback",
        "Implement updates and bug fixes",
        "Plan for future enhancements and feature additions"
      ]
    }
  ]
}
```

---

## Running Locally

### Backend

**Option 1: Using Python venv and pip**
```bash
cd backend
python -m venv venv
source venv/bin/activate      # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
uvicorn app.main:app --reload
```
**Option 2: Using uvsync**
```bash
cd backend
uv sync
```


### Frontend

```bash
cd frontend
npm install
npm run dev  # Start the frontend development server
```

---

## Key Engineering Decisions

- Structured JSON outputs for reliability
- Backend as AI orchestrator for security
- Modular planning components for extensibility
- Frontend uses React with JavaScript for interactive UI

---

## Demo Flow Instructions for Judges

1. Navigate to the frontend URL (Vercel deployment or localhost)
2. Enter a project name, description, and select the tech stack
3. Click 'Generate Plan'
4. Observe the generated architecture, task breakdown, and 5-week roadmap
5. Optionally, use the Swagger UI to test API endpoints:
   - GET /health/
   - GET /plan/
   - POST /plan/
   - GET /plan/{plan_id}

---

## Codebase Structure

```
backend/
  app/
    main.py
    api/
    services/
    schemas/
    core/
    tests/
  requirements.txt

frontend/
  src/
    components/
    pages/
    services/
  App.jsx
  package.json
```

---

## Testing

- Validate JSON structure
- Test API endpoints
- Mock AI responses
- Ensure proper error handling

---

## Future Improvements

- GitHub/GitLab automatic issue creation
- Multi-agent planning and review
- Persistent database storage
- Authentication & team collaboration
- Sprint analytics dashboard

---

## Project Goal

To build an AI-powered planning system that improves project organization, task clarity, and execution discipline for students and junior developers.

**AI Project Planner Agent — Turning ideas into executable roadmaps.**
