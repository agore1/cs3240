//Austin Gore ayg9fh
//Class body for Point

#include "Point.h"

using namespace std;
//Point constructor
Point::Point(float X, float Y, string category){
	_X = X;
	_Y = Y;
	_category = category;
}

float Point::getX(){
	return _X;
}

float Point::getY(){
	return _Y;
}

string Point::getCategory(){
	return _category;
}