//Austin Gore ayg9fh
//Class header for Point

#ifndef POINT_H
#define POINT_H

#include <string>

class Point{
	private:
		float _X;
		float _Y;
		std::string _category;
	
	public:
		Point(float X, float Y, std::string category);
		float getX();
		float getY();
		std::string getCategory();
};

#endif