//Austin Gore ayg9fh
//Class header for Point

#ifndef POINT_H
#define POINT_H

#include <string>

class Point{
	private:
		float _X;
		float _Y;
		float _Dist;
		std::string _category;
	
	public:
		Point(float X, float Y, std::string category);
		float getX();
		float getY();
		float getDist();
		void computeDist(float X, float Y);
		void clearDist();
		std::string getCategory();
		
};

#endif