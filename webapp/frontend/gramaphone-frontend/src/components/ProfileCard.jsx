import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { useFirebase } from '../context/FirebaseContext';

const ProfileCard = () => {
 const {user} = useFirebase();
 // console.log(user.email);
 const [details, setDetails] = useState({});
  useEffect(() => {
  
  
    const fetchData = async () => {
      try {
        
        const res = await axios.get(`http://127.0.0.1:5000/officers/${user.email}`);
        setDetails(res.data);
        console.log(res.data.Name);
        console.log(res.data);
      } catch (error) {
        console.log(error);
      }
    }

    fetchData();
  }, [])
  console.log(details.name);
  return (
    <>
      <div>
        <h2>Name: {details.Name}</h2>
        <h2>Address: {details.Address}</h2>
        <h2>Email: {user.email}</h2>
        <h2>Position: {details.Position}</h2>
        <h2>Phone: {details.Phone_Number}</h2>
      </div>
    </>
  )
}

export default ProfileCard
