//Austin Gore ayg9fh
//CS 3240 HW1 

#include <iostream>
#include "Point.h"
#include <string> 
#include <vector>
#include <sstream>
#include <fstream>
#include <stdlib.h>
using namespace std;

//Global vars - change for production
//Vector in which points from file will be stored
vector<Point*> allPoints;

//Forward function declarations
void prepForExit();

int main(int argc, char* argv[]){
	//Prompt user for values of K and numFromFile. 
	cout << "Please enter a value for K: "; 
	int k; 
	cin >> k; 
	cout << "Please enter the number of values to be read from file: "; 
	int numFromFile; 
	cin >> numFromFile;
	cout << "Please enter the filename to be read from: "; 
	string fileName; 
	cin >> fileName;

	//Vector in which points from file will be stored
	vector<Point*> allPoints;
	//Attempt to open the file
	string line;
	ifstream myfile(fileName.c_str());
	if(myfile.is_open()){
		//Variables used to hold converted data
		string category;
		float tempX;
		float tempY;
		//read numFromFile lines from the file
		for(int i=0; i<numFromFile; i++){
			if(getline(myfile, line)){
				//Convert this line into a Point
				istringstream iss(line);
				string sub;
				iss >> sub; 
				string category = sub;
				iss >> sub;
				tempX = stof(sub);
				iss>> sub;
				tempY = stof(sub);

				//create a new point
				Point * newPoint = new Point(tempX, tempY, category);
				allPoints.push_back(newPoint);
			}else{
				cout << "Something went wrong getting a line from the file. Exiting now." << endl;
				prepForExit();
			}
		}
		myfile.close();

		//Test reading the Points
		for(vector<Point*>::iterator it = allPoints.begin(); it != allPoints.end(); ++it){
		cout << "The category is: " << (*it)->getCategory() << endl;
	}

	}else{
		cout << "unable to open file.\n";
	}

	prepForExit();
}

void prepForExit(){
	//Free all the memory of Points in the vector
	for(vector<Point*>::iterator it = allPoints.begin(); it != allPoints.end(); ++it){
		delete *it;
	}
	exit();
}