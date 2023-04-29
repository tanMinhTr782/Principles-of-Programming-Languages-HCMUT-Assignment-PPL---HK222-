#include <iostream> 


int main () { 
    int a = 10; 
    while (a < 100) {
        a = a + 1; 
        {
            break;
        }
    }
    std::cout << a; 
}