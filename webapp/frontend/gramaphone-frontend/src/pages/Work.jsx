import React, { useState } from "react";
import { useLocation } from "react-router-dom";

import { MapPin, FileText, Calendar, Plus } from 'lucide-react';
import Navbar from "../components/Navbar";

const Work = () => {
  const location = useLocation();
  const work = location.state?.data; // Assuming data is passed in `state`

  const [updateTitle, setUpdateTitle] = useState("");
  const [updateDesc, setUpdateDesc] = useState("");

  if (!work) {
    return (
      <div className="min-h-screen bg-gray-900 text-green-400 flex items-center justify-center">
        <div className="text-2xl font-bold">No work data found!</div>
      </div>
    );
  }

  const handleSubmit = (e) => {
    e.preventDefault();
    // Handle the update submission here
    console.log("Update submitted:", { updateTitle, updateDesc });
    // Reset form fields
    setUpdateTitle("");
    setUpdateDesc("");
  };

  return (
    <div className="min-h-screen bg-gray-900 text-green-400">
      <Navbar/>
      <div className="container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-6">Work Details</h1>
        <div className="bg-black rounded-lg shadow-lg p-6 mb-8">
          <div className="flex items-center mb-4">
            <MapPin className="w-6 h-6 mr-2 text-green-600" />
            <p className="text-xl font-semibold">{work.Work_title}</p>
          </div>
          <div className="flex items-start mb-4">
            <FileText className="w-6 h-6 mr-2 text-green-600 mt-1" />
            <p>{work.Work_description}</p>
          </div>
          <div className="border-t border-green-800 pt-4 mt-4">
            <h2 className="text-xl font-semibold mb-4">Updates</h2>
            {work.Updates.update_title ? (
              <div className="bg-gray-800 rounded-lg p-4">
                <p className="font-semibold mb-2">{work.Updates.update_title}</p>
                <p className="mb-2">{work.Updates.update_desc}</p>
                <div className="flex items-center text-green-600">
                  <Calendar className="w-4 h-4 mr-2" />
                  <span className="text-sm">{work.Updates.update_date}</span>
                </div>
              </div>
            ) : (
              <p className="text-green-600">No updates available</p>
            )}
          </div>
        </div>

        <div className="bg-black rounded-lg shadow-lg p-6">
          <h2 className="text-xl font-semibold mb-4">Add Update</h2>
          <form onSubmit={handleSubmit} className="space-y-4">
            <div>
              <label htmlFor="updateTitle" className="block mb-1">Update Title</label>
              <input
                type="text"
                id="updateTitle"
                value={updateTitle}
                onChange={(e) => setUpdateTitle(e.target.value)}
                className="w-full bg-gray-800 text-green-400 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-600"
                placeholder="Enter update title"
              />
            </div>
            <div>
              <label htmlFor="updateDesc" className="block mb-1">Update Description</label>
              <textarea
                id="updateDesc"
                value={updateDesc}
                onChange={(e) => setUpdateDesc(e.target.value)}
                className="w-full bg-gray-800 text-green-400 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-green-600"
                placeholder="Enter update description"
                rows="3"
              ></textarea>
            </div>
            <button
              type="submit"
              className="bg-green-600 text-black font-semibold py-2 px-4 rounded hover:bg-green-500 transition duration-300 flex items-center"
            >
              <Plus className="w-5 h-5 mr-2" />
              Add Update
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Work;

