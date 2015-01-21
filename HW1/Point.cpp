//Austin Gore ayg9fh
//Class body for Point

#include "Point.h"
#include <math.h>

using namespace std;
//Point constructor
Point::Point(float X, float Y, string category){
	_X = X;
	_Y = Y;
	_category = category;
	_Dist = 1000;
}

float Point::getX(){
	return _X;
}

float Point::getY(){
	return _Y;
}

float Point::getDist(){
	return _Dist;
}
void Point::computeDist(float X, float Y){
	float xDiff = X - _X;
	float yDiff = Y - _Y;
	_Dist = sqrt(pow(xDiff, 2)+pow(yDiff, 2));
	return;
}
void Point::clearDist(){
	_Dist = 1000;
	return;
}

string Point::getCategory(){
	return _category;
}

