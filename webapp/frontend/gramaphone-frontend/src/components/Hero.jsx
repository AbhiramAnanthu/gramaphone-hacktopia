import React from 'react';
import { PhoneIcon, ServerIcon, ChatBubbleBottomCenterTextIcon } from '@heroicons/react/24/outline';

const Hero = () => {
  return (
    <div className="bg-gray-900 text-white">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 lg:py-24">
        <div className="lg:grid lg:grid-cols-2 lg:gap-8 items-center">
          <div className="mb-12 lg:mb-0">
            <h1 className="text-4xl sm:text-5xl font-extrabold tracking-tight mb-4">
              <span className="block text-green-500">GramaPhone</span>
              <span className="block">Bridging Rural Communities</span>
            </h1>
            <p className="text-xl text-gray-300 mb-8">
              Access government services with a simple phone call. No internet required.
            </p>
          </div>
          <div className="grid grid-cols-2 gap-4 sm:gap-6 lg:gap-8">
            <FeatureCard
              icon={<PhoneIcon className="h-8 w-8 text-green-500" />}
              title="Simple Phone Call"
              description="Access services by dialing a toll-free number"
            />
            <FeatureCard
              icon={<ServerIcon className="h-8 w-8 text-green-500" />}
              title="AI-Powered"
              description="Intelligent system handles your requests efficiently"
            />
            <FeatureCard
              icon={<ChatBubbleBottomCenterTextIcon className="h-8 w-8 text-green-500" />}
              title="Voice Interaction"
              description="Communicate naturally with our AI agent"
            />
            <FeatureCard
              icon={<ServerIcon className="h-8 w-8 text-green-500" />}
              title="No Internet Needed"
              description="Works with basic phone connections"
            />
          </div>
        </div>
      </div>
      <div className="bg-gray-800">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
          <div className="text-center">
            <p className="text-2xl font-semibold text-green-500">Empowering Rural Communities</p>
            <p className="mt-2 text-lg text-gray-300">
              GramaPhone eliminates the need for physical visits to government offices,
              making administration accessible to all.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

const FeatureCard = ({ icon, title, description }) => {
  return (
    <div className="bg-gray-800 p-6 rounded-lg shadow-lg transition duration-300 ease-in-out transform hover:scale-105">
      <div className="flex items-center justify-center w-12 h-12 bg-green-500 bg-opacity-10 rounded-md mb-4">
        {icon}
      </div>
      <h3 className="text-lg font-semibold mb-2">{title}</h3>
      <p className="text-gray-400">{description}</p>
    </div>
  );
};

export default Hero;

