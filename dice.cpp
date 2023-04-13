#include <iostream>
#include <stdlib.h>
#include <ctime>
using namespace std;

int CheckPrediction(){
    int choice=0;
    cin >> choice;
   if (choice>6)
   {
        cout << "Choose a Number 1-6" << endl;
        CheckPrediction();
    }
    return choice; 
    
}
int main ()
{
    cout << "Enter Predictions!" << endl; 
    int choice;
    cin >> choice;
    CheckPrediction();
    srand(time(NULL));
    cout <<"Dice Rolled!!" << endl;
    int roll = 0;
    roll= rand() % 6 + 1;
    cout <<"Your Prediction Was " << choice << endl;
    cout << "Your Roll Was " << roll << endl;
}