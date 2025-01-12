import React from 'react'
import { MapPin, Mail, Briefcase, Phone } from 'lucide-react'

const ProfileCard = ({ details }) => {
  return (
    <div className="w-full max-w-sm bg-white shadow-lg rounded-lg overflow-hidden text-green-400">
      <div className="px-6 py-4">
        <div className="flex items-center gap-4">
          <div className="w-16 h-16 bg-green-800 rounded-full overflow-hidden">
              <div className="w-full h-full flex items-center justify-center text-2xl font-bold text-green-400 bg-green-900">
                {details.Name.charAt(0)}
              </div>
          </div>
          <div>
            <h2 className="text-xl font-bold text-green-400">{details.Name}</h2>
            <p className="text-sm text-green-600">{details.Position}</p>
          </div>
        </div>
      </div>
      <div className="px-6 py-4 border-t border-green-800">
        <div className="grid gap-2">
          <div className="flex items-center gap-2">
            <MapPin className="h-4 w-4 text-green-600" />
            <span className="text-sm text-green-400">{details.Address}</span>
          </div>
          <div className="flex items-center gap-2">
            <Mail className="h-4 w-4 text-green-600" />
            <span className="text-sm text-green-400">{details.Email}</span>
          </div>
          <div className="flex items-center gap-2">
            <Briefcase className="h-4 w-4 text-green-600" />
            <span className="text-sm text-green-400">{details.Position}</span>
          </div>
          <div className="flex items-center gap-2">
            <Phone className="h-4 w-4 text-green-600" />
            <span className="text-sm text-green-400">{details.Phone_Number}</span>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ProfileCard

