import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import { FirebaseProvider } from './context/FirebaseContext'
import Dashboard from './pages/Dashboard'
import ProtectedRoute from './components/ProtectedRoute'
import Work from './pages/Work'
function App() {
  return (
    <>
      <FirebaseProvider>

      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/work/:id" element={<Work/>}/>
          {/* <Route path="/dashboard" element={<Dashboard/>}/> */}
          <Route
          path="/dashboard"
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />
        </Routes>
      </Router>
      </FirebaseProvider>
    </>
  )
}

export default App
