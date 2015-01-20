//Austin Gore ayg9fh
//Scratchwork file for CS3240 HW1

#include <iostream>
#include "Point.h"
using namespace std;

int main(int argc, char* argv[]){
	float f; 
	cout << "Please enter a float: ";
	cin >> f;
	cout << "The value for f is: " << f << "\n";



	Point testPoint(f, 4, "hello"); 
	cout << "testPoint has values" << testPoint.getX() << ", " << testPoint.getY() << ", " << testPoint.getCategory() << endl;

	return 0;
}