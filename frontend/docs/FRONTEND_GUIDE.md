# AI Project Planner Agent - Frontend

A modern, responsive React frontend for the AI Project Planner Agent that converts raw project ideas into structured development plans using AI.

## Features

- ✨ **Smart Project Form** - Describe your project idea with dynamic tech stack input
- 🏗️ **Architecture Visualization** - View your project's system architecture
- 📅 **Weekly Sprint Roadmap** - Timeline-based phase breakdown with tasks
- 📋 **Task Board** - Organized task cards with phase grouping
- 🐙 **GitHub-Ready Issues** - Auto-generated issues with copy-to-clipboard
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- ⚡ **Fast Development** - Built with Vite for instant HMR
- 🎨 **Beautiful UI** - Tailwind CSS for clean, modern styling

## Tech Stack

- **React 18** - UI library
- **Vite** - Build tool and dev server
- **React Router** - Client-side routing
- **Axios** - HTTP client
- **Tailwind CSS** - Utility-first CSS framework
- **PostCSS & Autoprefixer** - CSS processing

## Project Structure

```
frontend/
├── index.html
├── package.json
├── vite.config.js
├── tailwind.config.js
├── postcss.config.js
├── .env.example
├── .gitignore
├── src/
│   ├── main.jsx              # Entry point
│   ├── App.jsx               # Root component with routing
│   ├── api/
│   │   └── plannerApi.js     # API client wrapper functions
│   ├── components/
│   │   ├── Header.jsx        # Top navigation header
│   │   ├── Footer.jsx        # Footer component
│   │   ├── ProjectForm.jsx   # Main form component
│   │   ├── ArchitectureView.jsx
│   │   ├── WeeklyPlanView.jsx
│   │   ├── TaskBoard.jsx
│   │   ├── IssueList.jsx
│   │   └── LoadingSpinner.jsx
│   ├── pages/
│   │   ├── Home.jsx          # Home page with form
│   │   └── PlanResult.jsx    # Results display page
│   ├── services/
│   │   └── apiClient.js      # Axios instance configuration
│   └── styles/
│       └── index.css         # Global styles with Tailwind
└── README.md
```

## Getting Started

### Prerequisites

- Node.js 16+ and npm/yarn
- Backend running at `http://localhost:8000`

### Installation

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Create a `.env.local` file (optional, for custom backend URL):

   ```bash
   cp .env.example .env.local
   ```

   Edit `.env.local` if your backend runs on a different URL:

   ```
   VITE_API_BASE_URL=http://localhost:8000
   ```

### Development Server

Start the development server:

```bash
npm run dev
```

The application will be available at `http://localhost:5173`

The dev server includes:

- Hot Module Replacement (HMR) for instant code updates
- Fast refresh for React components
- Proxy configuration for backend API calls

### Building for Production

Build the project for production:

```bash
npm run build
```

The optimized build output will be in the `dist/` directory.

### Preview Production Build

Preview the production build locally:

```bash
npm run preview
```

## Integration with Backend

The frontend connects to the FastAPI backend using Axios. The API integration is handled in:

- `src/services/apiClient.js` - Axios client configuration
- `src/api/plannerApi.js` - API endpoint wrapper functions

### API Endpoints Used

- `GET /health` - Health check
- `POST /plan/` - Generate a new project plan
- `GET /plan/{plan_id}` - Retrieve a specific plan
- `GET /plan/` - List all plans

### Configuration

Backend URL is configured via:

1. Environment variable `VITE_API_BASE_URL`
2. Default fallback: `http://localhost:8000`

## Features in Detail

### Home Page (`/`)

The home page displays:

- Project overview and features
- Project submission form with fields:
  - Project Name (required)
  - Description (required)
  - Technology Stack (optional, dynamic list)
- How it works section
- Features list

### Plan Result Page (`/plan`)

After plan generation, displays:

1. **Architecture Overview** - System architecture summary with component breakdown
2. **Weekly Sprint Roadmap** - Timeline visualization of development phases with tasks
3. **Task Board** - Grid layout of all tasks grouped by phase, with checkboxes
4. **Git Issues** - Auto-generated GitHub issues with:
   - Title and description
   - Acceptance criteria
   - Labels
   - Copy-to-clipboard button

## Component Documentation

### ProjectForm Component

Handles the initial project input with:

- Form validation
- Dynamic tech stack management
- Loading states
- Error handling
- Navigation to results page

### ArchitectureView Component

Displays architectural overview with component cards for:

- Frontend
- Backend
- Database
- AI Services

### WeeklyPlanView Component

Timeline-based visualization showing:

- Phases with visual indicators
- Tasks organized by phase
- Linear timeline design

### TaskBoard Component

Task grid display with:

- Phase-based grouping
- Checkbox interactions
- Task statistics

### IssueList Component

GitHub issue generation with:

- Automatic issue creation from phases and tasks
- Copy to clipboard functionality
- Issue template with acceptance criteria
- Collapsible details

## Styling

The application uses **Tailwind CSS** for styling with custom configuration:

### Color Scheme

- **Primary**: Blue (`primary-600` for main actions)
- **Neutral**: Slate (various shades for text and backgrounds)
- **Success**: Green (checkmarks and success states)
- **Feedback**: Red, Yellow, Orange for alerts and warnings

### Component Classes

Reusable Tailwind component classes defined in `src/styles/index.css`:

- `.card` - Standard card container
- `.btn-primary` - Primary action button
- `.btn-secondary` - Secondary action button
- `.input-field` - Form input styling
- `.label` - Form label styling

## Error Handling

The application handles:

1. **API Errors** - Displayed as user-friendly messages
2. **Network Errors** - Retry prompts
3. **Form Validation** - Real-time feedback
4. **Loading States** - Spinner overlay during API calls

## Performance

### Optimizations

- Code splitting with React Router
- Lazy loading of pages
- Efficient re-renders with React hooks
- Production build optimization with Vite

### Bundle Size

Production build is optimized for:

- Fast initial page load
- Minimal JavaScript payload
- Efficient CSS minification

## Browser Support

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Deployment

### Static Hosting (Vercel, Netlify, etc.)

1. Build the project:

   ```bash
   npm run build
   ```

2. Deploy the `dist/` directory to your hosting service

3. Set environment variable on hosting platform:
   ```
   VITE_API_BASE_URL=https://your-backend-url.com
   ```

### Docker

Create a Dockerfile for containerized deployment:

```dockerfile
FROM node:18-alpine
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build
EXPOSE 3000
CMD ["npm", "run", "preview"]
```

## Development Tips

### Component Development

1. Use functional components with hooks
2. Keep components focused and single-responsibility
3. Extract reusable logic into custom hooks
4. Use proper prop types validation

### Debugging

- Use React DevTools browser extension
- Check Network tab for API calls
- Use console for debugging
- Leverage Vite's error reporting

### Code Style

The project uses:

- ES6+ JavaScript features
- JSX for component templates
- Functional React patterns
- Modern CSS with Tailwind utilities

## Troubleshooting

### Backend Connection Issues

**Problem**: API calls fail with CORS errors

**Solution**: Ensure backend has CORS enabled:

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Port Already in Use

**Problem**: Port 5173 is already in use

**Solution**: Specify a different port:

```bash
npm run dev -- --port 5174
```

### Build Failures

**Problem**: Build command fails

**Solution**:

1. Clear node_modules and reinstall:
   ```bash
   rm -rf node_modules package-lock.json
   npm install
   ```
2. Check Node version compatibility
3. Review error messages in build output

## Contributing

1. Create a feature branch
2. Make your changes
3. Test the application
4. Commit with clear messages
5. Push and create a pull request

## License

This project is part of the AI Project Planner Agent system.

## Support

For issues and questions:

1. Check existing documentation
2. Review backend API responses
3. Check browser console for errors
4. Verify backend is running and accessible

## Future Enhancements

- [ ] Dark mode theme
- [ ] Plan history and versioning
- [ ] Real-time collaboration
- [ ] Export to various formats (PDF, Word, etc.)
- [ ] Plan editing and customization
- [ ] Team management features
- [ ] Advanced filtering and search
- [ ] Analytics and insights dashboard
