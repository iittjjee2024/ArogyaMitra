import React from 'react';
import HealthStats from '../components/HealthStats';
import WorkoutCard from '../components/WorkoutCard';
import { Activity, Heart, Zap } from 'lucide-react';

const Dashboard = () => {
  return (
    <div className="space-y-8">
      <header>
        <h1 className="text-3xl font-bold text-gray-900">Welcome Back, John!</h1>
        <p className="text-gray-500">Here is your health summary for today.</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <HealthStats title="Heart Rate" value="72 bpm" icon={Heart} color="text-red-500" />
        <HealthStats title="Active Calories" value="450 kcal" icon={Zap} color="text-yellow-500" />
        <HealthStats title="Sleep Quality" value="85%" icon={Activity} color="text-blue-500" />
      </div>

      <section>
        <h2 className="text-xl font-semibold mb-4">Recommended Workouts</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
          <WorkoutCard title="Morning Yoga" duration="20" calories="120" />
          <WorkoutCard title="High Intensity Interval" duration="45" calories="400" />
        </div>
      </section>
    </div>
  );
};

export default Dashboard;
