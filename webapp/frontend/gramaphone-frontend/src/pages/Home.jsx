import React from 'react'
import Navbar from '../components/Navbar'
import Hero from '../components/Hero'
import { useFirebase } from '../context/FirebaseContext'
import Dashboard from './Dashboard'

const Home = () => {
  const {user} = useFirebase()
  return (
    <>
      <Navbar/>
      {user ? (
        // <Dashboard/>
        <Hero/>
      ):
      (
        <Hero/>

      )}
    </>
  )
}

export default Home
