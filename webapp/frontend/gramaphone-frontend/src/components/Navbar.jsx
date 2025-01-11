import React from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useFirebase } from '../context/FirebaseContext'

const Navbar = () => {
  const { user, auth } = useFirebase();
  const navigate = useNavigate();
  const HandleLogout = async () => {
    try{
      await auth.signOut();
      navigate('/');
    }catch(err){
      console.log("Error");
    }
  }

  return (
    <nav className="bg-gray-900 shadow-md">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          <div className="flex-shrink-0">
            <h2 className="text-2xl font-bold text-green-500">GramaPhone</h2>
          </div>
          <div>
            {user ? (
              <Link to="/login">
                <button className="bg-gray-800 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded-md transition duration-300 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-opacity-50" onClick={HandleLogout}>
                  Logout
                </button>
              </Link>
            ) : (
              <Link to="/login">
                <button className="bg-green-500 hover:bg-green-600 text-white font-bold py-2 px-4 rounded-md transition duration-300 ease-in-out transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-green-500 focus:ring-opacity-50">
                  Login
                </button>
              </Link>
            )}
          </div>
        </div>
      </div>
    </nav>
  )
}

export default Navbar

