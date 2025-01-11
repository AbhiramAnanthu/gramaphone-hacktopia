import React from 'react'
import { Link } from 'react-router-dom'
const Navbar = () => {
  return (
    <>
      <div className='flex flex-row justify-between px-7 py-3 bg-black'>
        <h2 className='text-[25px] text-white'>GramaPhone</h2>
        <Link to ='/login'>
        <button className='border bg-black text-white px-4 rounded-xl'>Login</button>
        </Link>
      </div>
    </>
  )
}

export default Navbar
