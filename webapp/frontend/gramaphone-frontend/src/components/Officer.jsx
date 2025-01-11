import React, { useEffect, useState } from 'react'
import ProfileCard from './ProfileCard'
import axios from 'axios';
import Worklist from './Worklist';
import { useFirebase } from '../context/FirebaseContext';

const Officer = () => {
  const {user} = useFirebase();
 // console.log(user.email);
 const [details, setDetails] = useState({});
  useEffect(() => {
  
  
    const fetchData = async () => {
      try {
        
        const res = await axios.get(`http://127.0.0.1:5000/officers/${user.email}`);
        setDetails(res.data);
        //console.log(res.data.Name);
        //console.log(res.data);
      } catch (error) {
        console.log(error);
      }
    }

    fetchData();
  }, [])
  //console.log(details.name);
  return (
    <>
      <ProfileCard details={details}/>
      <Worklist details={details}/>
    </>
  )
}

export default Officer
