#include <iostream>
#include <stdlib.h>
#include <ctime>
using namespace std;

int CheckPrediction(int choice){
   if (choice>6)
   {
        cout << "Choose a Number 1-6" << endl;
        for (int i=0; i<3; i++)
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
    
    // Lets roll 3 dice and get 3 predictions!
    // I will start it off

    // This is a for loop and i is our iterating variable
    // I will translate each part for clarification
    // int i=0;   This means initially i = 0
    // i<3;       "i" will always remain less than 3
    // i++        Every time it loops "i" will increase by an increment of 1
    // Note: When coding, numbers will start with 0 NOT 1

    
    // If you build and run this, you will see "i" being printed out as 0, 1, 2
    // We want to roll the dice 3 times and whatever you put into this loop will run 3 times
    // Happy hunting! 

    cout << "Enter prediction of dice roll" << endl; 
    cin >> choice;
    cout << "Dice Rolled!!" << endl;
    int roll = DiceRoll();
    for (int i=0; i<3; i++){
        cout << rand() % 6 + 1 << endl;
    }
    
    cout << "Your Prediction Was " << choice << endl;
    cout << "Your Roll Was " << roll << endl;
}
