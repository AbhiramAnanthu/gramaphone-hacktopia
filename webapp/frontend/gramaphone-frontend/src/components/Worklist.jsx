import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Worklist = ({details}) => {
    const [works, setWorks] = useState([]);
    const navigate = useNavigate();
    useEffect(() => {
        const fetchData = async() => {
            try {
                const res = await axios.get(`http://127.0.0.1:5000/read_work/${details.ID}`)
                setWorks(res.data);
            } catch (error) {
                console.log(error);
            }
        }
        fetchData();
    }, [])

    const HandleClick = (work) =>{
      navigate(`/work/${work.ID}`, { state: { data: work } });
    }
    
  return (
    <>
      <div className="w-full bg-black shadow-lg rounded-lg overflow-hidden text-green-400">
      <div className="px-6 py-4 border-b border-green-800">
        <h2 className="text-xl font-bold text-green-400">Complaints</h2>
      </div>
      <div className="px-6 py-4">
        <table className="w-full">
          <thead>
            <tr className="text-left text-green-600">
              <th className="pb-2">Title</th>
              <th className="pb-2">Created Date</th>
            </tr>
          </thead>
          <tbody>
            {works.map((work) => (
              <tr key={work.ID} className="border-t border-green-800" onClick={() => HandleClick(work)}>
                <td className="py-2">{work.Work_title}</td>
                <td className="py-2">{work.Created_at}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
    </>
  )
}

export default Worklist
