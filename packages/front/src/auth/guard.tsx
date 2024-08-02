import React from 'react';
import { Navigate } from 'react-router-dom';
import { isAuthenticated } from './auth';

const Guard: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  if (!isAuthenticated()) {
    return <Navigate to="/login" />;
  }
  return <>{children}</>;
};

export default Guard;
