#include <iostream>
#include <stdlib.h>
#include <ctime>
using namespace std;

int CheckPrediction(int choice){
   if (choice>6)
   {
        cout << "Choose a Number 1-6" << endl;
        CheckPrediction(choice);
    }
    return choice; 
}
int main ()
{
    cout << "Enter Predictions!" << endl; 
    int choice;
    cin >> choice;
    CheckPrediction(choice);
    srand(time(NULL));
    cout << "Dice Rolled!!" << endl;
    int roll = 0;
    roll= rand() % 6 + 1;
    cout << "Your Prediction Was " << choice << endl;
    cout << "Your Roll Was " << roll << endl;
}
