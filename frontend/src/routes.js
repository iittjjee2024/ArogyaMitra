import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import WorkoutPlanner from './pages/WorkoutPlanner';
import NutritionGuide from './pages/NutritionGuide';
import HealthCoach from './pages/HealthCoach';
import Profile from './pages/Profile';

const AppRoutes = () => (
  <Routes>
    <Route path="/" element={<Dashboard />} />
    <Route path="/workouts" element={<WorkoutPlanner />} />
    <Route path="/nutrition" element={<NutritionGuide />} />
    <Route path="/ai-coach" element={<HealthCoach />} />
    <Route path="/profile" element={<Profile />} />
  </Routes>
);

export default AppRoutes;
