//Austin Gore ayg9fh
//CS 3240 HW1 

#include <iostream>
#include "Point.h"
#include <string> 
#include <vector>
#include <sstream>
#include <fstream>
using namespace std;

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

	//Attempt to open the file
	string line;
	ifstream myfile(fileName.c_str());
	if(myfile.is_open()){
		while(getline(myfile, line)){
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

	


}