#include <stdio.h>
#include <stdlib.h>

int gcd(float x, float y) {
    int a, b, temp;
    
    if (x != (int)x || y != (int)y) {
        printf("Enter only integers");
        exit(1);
    }
    
    a = abs((int)x);
    b = abs((int)y);
    
    if (a==0 && b==0){
        printf("GCD is undefined");
        exit(1);
    }
    
    while (b != 0) {
        temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    printf("Please enter a and b: \n");
    float a, b;
    scanf("%f %f", &a, &b);
    a = gcd(a, b);
    printf("GCD = %.1f \n", a);
    return 0;
}