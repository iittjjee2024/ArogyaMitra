import React from 'react';
import { Bell, Search, User } from 'lucide-react';

const Navbar = () => {
  return (
    <nav className="h-16 bg-white border-b flex items-center justify-between px-8 sticky top-0 z-10">
      <div className="relative w-96">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400 w-4 h-4" />
        <input 
          type="text" 
          placeholder="Search health metrics..." 
          className="w-full pl-10 pr-4 py-2 border rounded-lg bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>
      <div className="flex items-center space-x-4">
        <button className="p-2 hover:bg-gray-100 rounded-full text-gray-600">
          <Bell className="w-5 h-5" />
        </button>
        <div className="flex items-center space-x-2 border-l pl-4">
          <span className="text-sm font-medium">John Doe</span>
          <div className="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center text-white text-xs">JD</div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
