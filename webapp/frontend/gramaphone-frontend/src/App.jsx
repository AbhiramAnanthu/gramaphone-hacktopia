import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Login from './pages/Login'
import { FirebaseProvider } from './context/FirebaseContext'
import Dashboard from './pages/Dashboard'
function App() {
  return (
    <>
      <FirebaseProvider>

      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/dashboard" element={<Dashboard/>}/>
        </Routes>
      </Router>
      </FirebaseProvider>
    </>
  )
}

export default App
