import React from 'react';
import { Play, Clock, Flame } from 'lucide-react';

const WorkoutCard = ({ title, duration, calories, difficulty }) => {
  return (
    <div className="bg-white p-4 rounded-xl border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
      <h3 className="font-bold text-gray-900 mb-2">{title}</h3>
      <div className="flex items-center space-x-4 text-sm text-gray-500 mb-4">
        <span className="flex items-center"><Clock className="w-4 h-4 mr-1" /> {duration}m</span>
        <span className="flex items-center"><Flame className="w-4 h-4 mr-1" /> {calories} kcal</span>
      </div>
      <button className="w-full bg-blue-600 text-white py-2 rounded-lg flex items-center justify-center hover:bg-blue-700">
        <Play className="w-4 h-4 mr-2" /> Start Workout
      </button>
    </div>
  );
};

export default WorkoutCard;
