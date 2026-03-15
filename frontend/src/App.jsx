import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Home from "./pages/Home";
import PlanResult from "./pages/PlanResult";
import "./styles/index.css";

/**
 * Main application component for the AI Project Planner.
 * Acts as the root layout wrapper and handles the routing configuration
 * for the entire frontend using React Router.
 *
 * @returns {JSX.Element} The rendered application layout and routes.
 */
function App() {
  return (
    <Router>
      <div className="flex flex-col min-h-screen">
        <Header />
        <main className="flex-1">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/plan" element={<PlanResult />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
