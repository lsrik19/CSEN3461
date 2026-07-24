#include <stdio.h>
#include <stdlib.h>

int modulus(int a, int b) {
    if (b == 0) {
        printf("Error: Modulus by zero is not allowed.\n");
        exit(1);
    }

    int quotient = a / b;
    int remainder = a - (quotient * b);

    if (remainder != 0 && ((a < 0) != (b < 0))) {
        remainder += b;
    }

    return remainder;
}

int main() {
    printf("Please Enter a and b: \n");
    int a, b;
    scanf("%d %d", &a, &b);
    int rem = modulus(a,b);
    printf("%d mod %d = %d\n", a, b, rem);
    return 0;
}