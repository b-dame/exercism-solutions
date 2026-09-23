#include "difference_of_squares.h"

unsigned int sum_of_squares(unsigned int number) {
    unsigned int sum = 0;
    for(unsigned int i = 1; i <= number; i++) {
        sum += i*i;
    }
    return sum;
}

unsigned int square_of_sum(unsigned int number) {
    unsigned int sum = 0;
    unsigned int square = 0;
    for(unsigned int i = 1; i <= number; i++) {
        sum += i;
    }
    square = sum*sum;
    return square;
}

unsigned int difference_of_squares(unsigned int number) {
    unsigned int sum1 = 0;
    unsigned int sum2 = 0;
    unsigned int difference = 0;
    sum1 = square_of_sum(number);
    sum2 = sum_of_squares(number);
    difference = sum1 - sum2;
    return difference;
}