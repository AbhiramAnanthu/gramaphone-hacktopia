import React from "react";
import { Navigate } from "react-router-dom"; // For React Router v6
import { useFirebase } from "../context/FirebaseContext"; // Your authentication context

const ProtectedRoute = ({ children }) => {
  const { user } = useFirebase(); // Get user from context or authentication state

  if (!user) {
    // Redirect to login if not authenticated
    return <Navigate to="/login" />;
  }

  return children; // Render the protected component if authenticated
};

export default ProtectedRoute;
