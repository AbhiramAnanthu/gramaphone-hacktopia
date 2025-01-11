import React from 'react'
import { useFirebase } from '../context/FirebaseContext'
import Navbar from '../components/Navbar';
import Officer from '../components/Officer';
import Department from '../components/Department';

const Dashboard = () => {
    const {user} = useFirebase();
    
  return (
    <>
        <Navbar/>
        {
            user ? (
                <Officer/>
            ):(
                <Department/>
            )
        }
    </>
  )
}

export default Dashboard
