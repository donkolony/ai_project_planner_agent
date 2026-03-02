# AI Project Planner Agent

An AI-powered assistant that transforms raw project ideas into
structured architecture designs, actionable task breakdowns, and clear
weekly execution plans to improve project delivery and team
coordination.

------------------------------------------------------------------------

## 📌 Problem Statement

Student and junior development teams often struggle with:

-   Poor project planning and unclear architecture
-   Large tasks that are not broken into manageable pieces
-   Lack of structured weekly goals
-   Inconsistent issue tracking in Git platforms
-   Rushed implementation without proper roadmap

The **AI Project Planner Agent** solves this by automatically
generating:

-   High-level system architecture
-   Feature-to-task breakdown
-   5-week sprint plan
-   Git-ready issue descriptions
-   Clear deliverables per week

------------------------------------------------------------------------

## Architecture Overview

### System Flow

User Input → React Frontend → FastAPI Backend → AI Planning Engine →
Structured JSON Output → Dashboard Rendering

### Core Components

1.  Frontend (React)
    -   Project idea submission form
    -   Architecture display
    -   Weekly roadmap visualization
    -   Task breakdown board

2.  Backend (FastAPI)
    -   Prompt orchestration
    -   AI response validation
    -   JSON schema enforcement
    -   REST API endpoints

3.  AI Layer
    -   Architecture generator
    -   Task breakdown generator
    -   Weekly sprint planner
    -   Issue formatter

------------------------------------------------------------------------

## Tech Stack

Frontend: - React - Axios - Tailwind CSS

Backend: - Python - FastAPI - Pydantic - Uvicorn

AI Integration: - Azure OpenAI or OpenAI API - Structured JSON prompt
design

------------------------------------------------------------------------

## Features

-   Convert project ideas into structured plans
-   Generate full project architecture
-   Break features into small actionable tasks
-   Create 5-week sprint roadmap
-   Produce Git-ready issue descriptions
-   Enforce structured JSON outputs

------------------------------------------------------------------------

## API Documentation

### Base URL

http://localhost:8000

### POST /plan

Request Body: { "project_name": "AI Study Planner", "description": "An
AI tool that helps students plan assignments and deadlines",
"duration_weeks": 5 }

Response: { "architecture": {}, "weekly_plan": \[\], "tasks": \[\],
"issues": \[\] }

### GET /health

Response: { "status": "ok" }

------------------------------------------------------------------------

## ▶ Running Locally

### Backend

cd backend python -m venv venv source venv/bin/activate pip install -r
requirements.txt uvicorn main:app --reload

### Frontend

cd frontend npm install npm start

------------------------------------------------------------------------

## Key Engineering Decisions

-   Structured JSON outputs for reliability
-   Backend as AI orchestrator for security
-   Modular planning components for extensibility

------------------------------------------------------------------------

## Codebase Structure

backend/ app/ main.py api/ services/ schemas/ core/ tests/
requirements.txt

frontend/ src/ components/ pages/ services/ App.jsx package.json

------------------------------------------------------------------------

## Testing

-   Validate JSON structure
-   Test API endpoints
-   Mock AI responses
-   Ensure proper error handling

------------------------------------------------------------------------

## Future Improvements

-   GitHub/GitLab automatic issue creation
-   Multi-agent planning and review
-   Persistent database storage
-   Authentication & team collaboration
-   Sprint analytics dashboard

------------------------------------------------------------------------

## Project Goal

To build an AI-powered planning system that improves project
organization, task clarity, and execution discipline for students and
junior developers.

**AI Project Planner Agent --- Turning ideas into executable roadmaps.**
