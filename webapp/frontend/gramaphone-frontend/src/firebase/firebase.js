// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAnalytics } from "firebase/analytics";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyD0rAUdh83XsL6-1sEZWxvUfbc8f-W9exk",
  authDomain: "test-project-a21f7.firebaseapp.com",
  projectId: "test-project-a21f7",
  storageBucket: "test-project-a21f7.firebasestorage.app",
  messagingSenderId: "235901443090",
  appId: "1:235901443090:web:b10270de2acd1eabdacccb",
  measurementId: "G-FPX2J6J7DX"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);
export {auth};