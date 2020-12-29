#include <iostream>
#include <fstream>
#include <vector>
using namespace std;


// This function receives text and shift and 
// returns the encrypted text 
string encrypt(string text, int s) 
{ 
    string result = ""; 
  
    // traverse text 
    for (int i=0;i<text.length();i++) 
    { 
        // apply transformation to each character 
        // Encrypt Uppercase letters 
        if (isupper(text[i])) 
            result += char(int(text[i]+s-65)%26 +65); 
  
    // Encrypt Lowercase letters 
    else
        result += char(int(text[i]+s-97)%26 +97); 
    } 
  
    // Return the resulting string 
    return result; 
} 



//  writing input in terminal after running code:  ./a.exe
int main()
{
    ifstream Usernamefile("username.txt");// input file stream object
    ifstream Passwordfile("password.txt");// input file stream object
    vector<string> usernames; // var. to store all names 
    //login var.
    string username;
    string password;
    string Crypassword;
    bool vaild = false;
    string usernameInput;
    string passwordInput;
    
    Usernamefile >> usernameInput; //read the username in text file
    Passwordfile >> passwordInput; //read the password in text file
    
    while(!vaild) //loops until user is vaildated
    {
        cout << "Enter username\n";
        cin  >> username;
        cout << "Enter password\n";
        cin  >> password;
         
    
        
        if(username == usernameInput && encrypt(password,4) == "teww") //checks to see if the user writes the correct username and password that are stored in the text files- username.txt/ password/txt
        {
            cout << "Login in Sucessful!";
            vaild = true;
        }
        else 
        {
            cout << "Wrong Username and password! Please Enter again:\n";
        }
    }

    return 0;
}

