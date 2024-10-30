#include <iostream>
#include <chrono>

long long recfibonacci(int n) {
    if (n == 0) return 0;
    else if  (n == 1) return 1;
    else return recfibonacci(n-1) + recfibonacci(n-2);
}

int fibonacci(int n) {
    long long x, y, z;
    x = 0;
    y = 1;

    for (int i = 1; i < n; i++) {
        z = x + y;
        x = y;
        y = z;
    }
    return z;
}

int main() {
    auto t1 = std::chrono::high_resolution_clock::now();
    std::cout << fibonacci(25) << std::endl;
    auto t2 = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double, std::milli> ms_double = t2 - t1;
    std::cout << "iterative: " << ms_double.count() << std::endl;

    t1 = std::chrono::high_resolution_clock::now();
    std::cout << recfibonacci(25) << std::endl;
    t2 = std::chrono::high_resolution_clock::now();
    std::cout << "recursive: " << ms_double.count() << std::endl;
} 
