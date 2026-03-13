#!/bin/bash

# Frontend Deployment Script for Azure Static Web Apps / App Service

set -e

echo "🚀 AI Project Planner Frontend - Azure Deployment Script"
echo "=================================================="

# Check if Node.js is installed
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install it first."
    exit 1
fi

echo "✅ Node.js version: $(node --version)"

# Navigate to frontend directory
cd "$(dirname "$0")/frontend" || { echo "❌ Frontend directory not found"; exit 1; }

echo ""
echo "📦 Installing dependencies..."
npm install

echo ""
echo "🔨 Building frontend..."
npm run build

echo ""
echo "✅ Build complete!"
echo ""
echo "📂 Build output is in: ./dist"
echo ""
echo "🚀 Next steps:"
echo ""
echo "Option 1: Deploy to Azure Static Web Apps"
echo "  az staticwebapp up --name ai-project-planner-frontend --location southafricanorth"
echo ""
echo "Option 2: Deploy to Azure App Service"
echo "  az webapp up --name ai-project-planner-frontend --runtime node"
echo ""
echo "Option 3: Deploy to Vercel"
echo "  npm install -g vercel"
echo "  vercel --prod"
echo ""
echo "=================================================="
echo "Build artifacts are ready for deployment!"
