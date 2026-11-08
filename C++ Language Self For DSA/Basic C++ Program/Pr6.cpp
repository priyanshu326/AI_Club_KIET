// Size of int, float, double, char
#include <iostream>
using namespace std;
int main()
{
    int a;
    float b;
    double c;
    char ch;

    cout << "Enter integer Value " ;
    cin >>  a;
    cout << "Enter float Value " ;
    cin >> b;
    cout << "Enter double float Value " ;
    cin >> c;
    cout << "Enter character Value " ;
    cin >> ch;

    cout << "Size of Integer" << sizeof(a) << endl;
    cout << "Size of Float" << sizeof(b) << endl;
    cout << "Size of Double Float" << sizeof(c) << endl;
    cout << "Size of Character" << sizeof(ch) << endl;

}