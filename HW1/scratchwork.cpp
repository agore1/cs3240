//Austin Gore ayg9fh
//Scratchwork file for CS3240 HW1

#include <iostream>
#include "Point.h"
#include <fstream>
#include <sstream>
using namespace std;

int main(int argc, char* argv[]){
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