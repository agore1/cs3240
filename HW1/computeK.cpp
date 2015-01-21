//Austin Gore ayg9fh
//CS 3240 HW1 

#include <iostream>
#include "Point.h"
#include <string> 
#include <vector>
#include <sstream>
#include <fstream>		//ifstream
#include <stdlib.h>
#include <algorithm> 	//sort
#include <map>
using namespace std;

//Global vars - change for production
//Vector in which points from file will be stored
vector<Point*> allPoints;

//Forward function declarations
void prepForExit();
bool comparePoints(Point* p1, Point* p2);

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
				exit(EXIT_FAILURE);
			}
		}
		myfile.close();

		//Test reading the Points
		for(vector<Point*>::iterator it = allPoints.begin(); it != allPoints.end(); ++it){
		cout << "The category is: " << (*it)->getCategory() << endl;
		}

	}else{
		cout << "Unable to open file.\n";
		return 0;
	}

	cout << "Input data successfully interpreted. \nPlease enter point to classify: ";
	//Scan for input
	string input = "";
	string sub = "0.0";
	// getline(cin, input);
	// cin >> input;
	// cout << input << endl;
	cin.ignore();	//clear newline character from cin, which can confuse getline. 
	while(getline(cin, input)){
		if(input == "1.0 1.0"){
			cout <<"Read terminating sequence, exiting now.\n";
			prepForExit();
			return 0;
		}
		cout << input << endl;
		istringstream iss(input);
		iss >> sub;
		float inputX = stof(sub);
		iss >> sub;
		float inputY =stof(sub); 

		//Compute distance for all points
		for(vector<Point*>::iterator it = allPoints.begin(); it != allPoints.end(); ++it){
			(*it)->computeDist(inputX, inputY);
		}

		//Sort points
		sort(allPoints.begin(), allPoints.end(), comparePoints);

		//Print K nearest points and add to dictionary
		map<string, int> Votes;
		for(int i=0; i<k; i++){
			cout << allPoints[i]->getCategory() << " " << allPoints[i]->getX() << " " << allPoints[i]->getY()<< " " << allPoints[i]->getDist() << endl;
			if(Votes.find(allPoints[i]->getCategory()) == Votes.end()){		//if the category isn't present
				Votes[allPoints[i]->getCategory()] = 1;
				cout << "Adding category: " << allPoints[i]->getCategory() << endl;
			}else{
				Votes[allPoints[i]->getCategory()]++;
				cout << "The value of " << allPoints[i]->getCategory() << " was incremented to : " << Votes[allPoints[i]->getCategory()] << endl;
			}
		}

		//Vote on K nearest points
		string maxCategory;
		int max = 0;
		for( map<string, int>::iterator voteIt = Votes.begin(); voteIt != Votes.end(); ++voteIt){
			if((*voteIt).second >= max){
				maxCategory = (*voteIt).first;
				max = (*voteIt).second;
			}
		}
		cout << "With " << max << " votes, the max category was: " << maxCategory << endl; 

		//clear the Distance attributes of all the points to prepare for next input
		for(vector<Point*>::iterator it = allPoints.begin(); it != allPoints.end(); ++it){
			(*it)->clearDist();
		}
		cout << "Please enter another point: ";
	}

	prepForExit();
	return 0;
}

void prepForExit(){
	//Free all the memory of Points in the vector
	for(vector<Point*>::iterator it = allPoints.begin(); it != allPoints.end(); ++it){
		delete *it;
	}
}

bool comparePoints(Point* p1, Point* p2){
	return p1->getDist() < p2->getDist();
}