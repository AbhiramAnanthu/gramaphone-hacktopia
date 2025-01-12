import React, { useEffect, useState } from 'react'
import axios from 'axios';

const Worklist = ({details}) => {
    const [work, setWork] = useState([]);
    useEffect(() => {
        const fetchData = async() => {
            try {
                const res = await axios.get(`http://127.0.0.1:5000/read_work/${details.ID}`)
                setWork(res.data);
            } catch (error) {
                console.log(error);
            }
        }
        fetchData();
    }, [])
    
  return (
    <>
      <div>
        <h1>Worklist</h1>
        <ul>
           
        </ul>
      </div>
    </>
  )
}

export default Worklist
