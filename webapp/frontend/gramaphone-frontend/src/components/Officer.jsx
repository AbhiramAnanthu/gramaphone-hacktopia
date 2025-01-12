import React, { useEffect, useState } from 'react'
import ProfileCard from './ProfileCard'
import axios from 'axios';
import Worklist from './Worklist';
import { useFirebase } from '../context/FirebaseContext';

const Officer = () => {
  const {user} = useFirebase();
  console.log(user.email);
 const [details, setDetails] = useState({});
 
  useEffect(() => {
  
  
    const fetchData = async () => {
      try {
        const res = await axios.get(`http://127.0.0.1:5000/officers/${user.email}`);
        setDetails(res.data);
        //console.log(res.data);
        //console.log(res.data);
      } catch (error) {
        console.log(error);
      }
    }

    fetchData();
  }, [])
  console.log(details.Name);
  return (
    <>
      <div className="container mx-auto px-4 py-8 bg-gray-800 min-h-screen min-w-full">
      {
        details && details.Name ? (
          <div className="flex flex-col lg:flex-row gap-8">
      <div className="lg:w-3/4">
        <Worklist details={details} />
      </div>
      <div className="lg:w-1/4">
        <ProfileCard details={details} />
      </div>
    </div>
        ):(
          <div className="text-center text-2xl text-green-400">Loading...</div>
        )
      }
  </div>
    </>
  );  
}
export default Officer
