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

int DiceRoll(){
    int roll = rand() % 6 + 1;
    return roll;
}

int main ()
{
    int choice;
    srand(time(NULL));
    
    for (int i=0; i<3; i++){
        cout << "Enter prediction of dice roll" << endl; 
        cin >> choice;
        CheckPrediction(choice);    
        cout << "Dice Rolled!!" << endl;
        int roll = DiceRoll();

        cout << "Your Prediction Was " << choice << endl;
        cout << "Your Roll Was " << roll << endl;
    }
}
    

    

