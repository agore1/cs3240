//Austin Gore ayg9fh
//Scratchwork file for CS3240 HW1

#include <iostream>
#include "Point.h"
#include <fstream>
#include <sstream>
#include <vector>
using namespace std;

int main(int argc, char* argv[]){
	string input;
	getline(cin, input);
	cout << input <<endl;
	
	vector<Point*> allPoints; 
	Point* point1 = new Point(1.0, 1.0, "TestA");
	allPoints.push_back(point1);
	Point* point2 = new Point(3.0, 4.0, "TestB");
	allPoints.push_back(point2);
	cout <<"The value of point2 is: " << point2->getCategory() << endl;

	for(int i = 0; i < 2; i++){
		cout << allPoints[i]->getCategory() << allPoints[i]->getDist() << endl;

	}

	allPoints[0]->computeDist(2.0, 2.0);
	cout << "The distance of the point is: " << allPoints[0]->getDist();

	//Free the Points in allPoints
	cout << "Freeing points now." << endl;
	for(vector<Point*>::iterator it = allPoints.begin(); it != allPoints.end(); ++it){
		delete *it;
	}

	cout <<"The value of point2 is: " << point2->getCategory() << endl;


	string line;
	ifstream myfile("testData.txt");
	if(myfile.is_open()){
		while ( getline(myfile, line)){
			istringstream iss(line);
			string sub;
			while(iss >> sub){
				cout << "Substring: " << sub << endl;	
			}
			cout << "The whole line was: " << line << "\n";
		}
		myfile.close();
	}else{
		cout << "unable to open file.\n";
	}



	float f; 
	cout << "Please enter a float: ";
	cin >> f;
	cout << "The value for f is: " << f << "\n";



	Point testPoint(f, 4, "hello"); 
	cout << "testPoint has values" << testPoint.getX() << ", " << testPoint.getY() << ", " << testPoint.getCategory() << endl;



	return 0;
}