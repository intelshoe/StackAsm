/*
*   A sample c++ program demonstrating chaning pointer values
*   Source: https://www.w3schools.com/cpp/cpp_examples.asp
*
*   This is used as a test script for compiling into 
*   assembly and running through StackAsm.
*/

#include <iostream>
#include <string>
using namespace std;

int main() {
	string food = "Pizza";
	string* ptr = &food;

	// Output the value of food
	cout << food << "\n";

	// Output the memory address of food
	cout << &food << "\n";

	// Access the memory address of food and output its value
	cout << *ptr << "\n";

	// Change the value of the pointer
	*ptr = "Hamburger";

	// Output the new value of the pointer
	cout << *ptr << "\n";

	// Output the new value of the food variable
	cout << food << "\n";
	return 0;
}
