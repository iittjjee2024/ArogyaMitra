import React from 'react';
import { User, Mail, Phone, MapPin } from 'lucide-react';

const Profile = () => {
  const profile = {
    name: "John Doe",
    email: "john.doe@example.com",
    goal: "Weight Loss",
    weight: "75 kg",
    height: "178 cm"
  };

  return (
    <div className="max-w-4xl mx-auto space-y-6">
      <div className="bg-white rounded-xl shadow-sm border p-8 text-center">
        <div className="w-24 h-24 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center mx-auto mb-4 text-3xl font-bold">
          {profile.name.charAt(0)}
        </div>
        <h1 className="text-2xl font-bold">{profile.name}</h1>
        <p className="text-gray-500">{profile.goal}</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white p-6 rounded-xl border shadow-sm space-y-4">
          <h2 className="font-semibold text-lg border-b pb-2">Physical Attributes</h2>
          <div className="flex justify-between">
            <span className="text-gray-500">Weight</span>
            <span className="font-medium">{profile.weight}</span>
          </div>
          <div className="flex justify-between">
            <span className="text-gray-500">Height</span>
            <span className="font-medium">{profile.height}</span>
          </div>
        </div>
        
        <div className="bg-white p-6 rounded-xl border shadow-sm space-y-4">
          <h2 className="font-semibold text-lg border-b pb-2">Contact Information</h2>
          <div className="flex items-center gap-3 text-gray-600">
            <Mail className="w-4 h-4" /> {profile.email}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;
