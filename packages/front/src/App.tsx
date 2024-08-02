import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Header from './components/header';
import Footer from './components/footer';
import Home from './pages/Home';
import SignUp from './pages/SignUp';
import Login from './pages/Login';
import Test from './pages/Test';
import Background from './components/background';
import Guard from './auth/guard';

const App: React.FC = () => {
  return (
    <Router>
      <div>
        <Header />
        <Background componentChildren={
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/sign-up" element={<SignUp />} />
            <Route path="/login" element={<Login />} />
            <Route path="/test" element={<Guard><Test /></Guard>} />
            <Route path="*" element={<p>404</p>} />
          </Routes>
        } />
        <Footer />
      </div>
    </Router>
  );
};

export default App;
