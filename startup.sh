#!/bin/bash

# ============================================================================
# AI Project Planner Agent - Setup Script
# ============================================================================
# This script automates the setup process for both frontend and backend
# Usage: bash setup.sh
# ============================================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Functions
print_header() {
    echo -e "\n${BLUE}========================================${NC}"
    echo -e "${BLUE}$1${NC}"
    echo -e "${BLUE}========================================${NC}\n"
}

print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠ $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ $1${NC}"
}

# Check if running from project root
if [ ! -f "backend/requirements.txt" ] || [ ! -f "frontend/package.json" ]; then
    print_error "This script must be run from the project root directory"
    echo "Please navigate to the AI Project Planner Agent directory and try again."
    exit 1
fi

print_header "AI Project Planner Agent - Setup Script"

# ============================================================================
# Step 1: Check Prerequisites
# ============================================================================
print_header "Step 1: Checking Prerequisites"

# Check Python
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1 | awk '{print $2}')
    print_success "Python $PYTHON_VERSION is installed"
else
    print_error "Python 3 is not installed. Please install Python 3.11 or higher."
    exit 1
fi

# Check Node.js
if command -v node &> /dev/null; then
    NODE_VERSION=$(node --version)
    print_success "Node.js $NODE_VERSION is installed"
else
    print_error "Node.js is not installed. Please install Node.js 16 or higher."
    exit 1
fi

# Check npm
if command -v npm &> /dev/null; then
    NPM_VERSION=$(npm --version)
    print_success "npm $NPM_VERSION is installed"
else
    print_error "npm is not installed. Please install npm."
    exit 1
fi

# ============================================================================
# Step 2: Backend Setup
# ============================================================================
print_header "Step 2: Setting Up Backend"

cd backend

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    print_info "Creating Python virtual environment..."
    python3 -m venv venv
    print_success "Virtual environment created"
else
    print_info "Virtual environment already exists"
fi

# Activate virtual environment
print_info "Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
print_info "Upgrading pip..."
pip install --upgrade pip -q

# Install dependencies
print_info "Installing Python dependencies..."
pip install -r requirements.txt -q
print_success "Python dependencies installed"

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    print_info "Creating .env file from template..."
    cp .env.example .env
    print_warning "Please update .env with your Azure OpenAI credentials"
    print_info "Edit: backend/.env"
else
    print_info ".env file already exists"
fi

cd ..

print_success "Backend setup completed"

# ============================================================================
# Step 3: Frontend Setup
# ============================================================================
print_header "Step 3: Setting Up Frontend"

cd frontend

# Install npm dependencies
print_info "Installing npm dependencies..."
npm install -q
print_success "npm dependencies installed"

# Create .env.production if it doesn't exist
if [ ! -f ".env.production" ]; then
    print_info "Creating .env.production file..."
    cat > .env.production << 'EOF'
VITE_API_BASE_URL=https://ai-project-planner-api-hufwf8agddd4a2h6.southafricanorth-01.azurewebsites.net
EOF
    print_success ".env.production created"
else
    print_info ".env.production already exists"
fi

# Create .env.local for development
if [ ! -f ".env.local" ]; then
    print_info "Creating .env.local for development..."
    cat > .env.local << 'EOF'
VITE_API_BASE_URL=http://localhost:8000
EOF
    print_success ".env.local created"
else
    print_info ".env.local already exists"
fi

cd ..

print_success "Frontend setup completed"

# ============================================================================
# Step 4: Database Setup (Optional)
# ============================================================================
print_header "Step 4: Database Setup"

read -p "Initialize database tables? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    cd backend
    source venv/bin/activate
    print_info "Initializing database..."
    python -c "from app.core.database import init_db; init_db()"
    print_success "Database initialized"
    cd ..
else
    print_info "Skipping database initialization"
fi

# ============================================================================
# Step 5: Run Tests (Optional)
# ============================================================================
print_header "Step 5: Running Tests"

read -p "Run backend tests? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    cd backend
    source venv/bin/activate
    print_info "Running pytest..."
    python -m pytest tests/ -v --tb=short
    print_success "Tests completed"
    cd ..
else
    print_info "Skipping tests"
fi

# ============================================================================
# Step 6: Start Servers (Optional)
# ============================================================================
print_header "Step 6: Start Development Servers"

read -p "Start development servers? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    print_info "Starting backend server in background..."
    cd backend
    source venv/bin/activate
    python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000 &
    BACKEND_PID=$!
    print_success "Backend running on http://localhost:8000 (PID: $BACKEND_PID)"
    cd ..
    
    sleep 2
    
    print_info "Starting frontend server..."
    cd frontend
    print_success "Frontend will run on http://localhost:5173"
    npx vite --host
    cd ..
else
    print_info "Skipping server startup"
    print_info "\nTo start servers manually:"
    echo -e "${YELLOW}Backend:${NC}  cd backend && source venv/bin/activate && python -m uvicorn app.main:app --reload"
    echo -e "${YELLOW}Frontend:${NC} cd frontend && npx vite --host"
fi

print_header "Setup Complete! 🎉"

echo -e "${GREEN}Your AI Project Planner Agent is ready to use!${NC}\n"

echo -e "${YELLOW}Next Steps:${NC}"
echo "1. Update backend/.env with your Azure OpenAI credentials"
echo "2. Start the backend: cd backend && source venv/bin/activate && python -m uvicorn app.main:app --reload"
echo "3. Start the frontend: cd frontend && npx vite --host"
echo "4. Open http://localhost:5173 in your browser"
echo ""
echo -e "${BLUE}Documentation:${NC}"
echo "- Backend: backend/README.md"
echo "- Frontend: frontend/README.md"
echo "- Deployment: docs/AZURE_DEPLOYMENT_GUIDE.md"
echo ""