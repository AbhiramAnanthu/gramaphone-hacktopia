import React from 'react'


const ProfileCard = ({details}) => {
  return (
    <>
      <div>
        <h2>Name: {details.Name}</h2>
        <h2>Address: {details.Address}</h2>
        <h2>Email: {details.Email}</h2>
        <h2>Position: {details.Position}</h2>
        <h2>Phone: {details.Phone_Number}</h2>
      </div>
    </>
  )
}

export default ProfileCard
