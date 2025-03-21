import react from "react"
import { BrowserRouter, Routes, Route, Navigate} from "react-router-dom"
import Login from "./pages/Login"
import Register from "./pages/Register"
import Home from "./pages/Home"
import Notfound from "./pages/NotFound"
import ProtectedRoute from "./guards/ProtectedRoute"
import Header from './components/Header';
import Footer from './components/Footer';
import Background from './components/Background';
import "./styles/style.css"

function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {
  return (
    <BrowserRouter>
      <div>
        <Header />
        <Background componentChildren={
          <Routes>
            {/* <Route 
              path="/"
              element={
                <ProtectedRoute>
                  <Home />
                </ProtectedRoute>
              }
            /> */}
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/logout" element={<Logout />} />
            <Route path="/register" element={<RegisterAndLogout />} />
            <Route path="*" element={<Notfound />}></Route>
          </Routes>
        } />
        <Footer />
      </div>
    </BrowserRouter>
  )
}

export default App
