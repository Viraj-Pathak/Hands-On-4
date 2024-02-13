# Hands-On-4 | Problem - 0

2.Time Complexity Analysis:
Let's denote the time complexity of fib(n) as T(n).

For each call to fib(n), it recursively calls fib(n-1) and fib(n-2). Therefore, the time complexity can be represented as:

T(n) = T(n-1) + T(n-2) + O(1)

This resembles the Fibonacci sequence itself, which has a time complexity of approximately O(2^n) due to repeated calculations.


3.Potential Improvements:
Memoization: To improve the performance of this recursive solution, we can use memoization. Memoization stores the results of expensive function calls and returns the cached result when the same inputs occur again. This would reduce the time complexity to O(n) by eliminating redundant calculations.

Iterative Solution: An iterative solution using a loop would be more efficient than the recursive solution, especially for large values of n. It would have a time complexity of O(n) and wouldn't suffer from the overhead of function calls.

Closed-form Formula: The Fibonacci sequence has a closed-form formula using the golden ratio. Implementing this formula directly would provide a constant time solution, greatly improving performance. However, this approach might suffer from precision issues for very large values of n due to limitations in floating-point arithmetic.

Dynamic Programming: Along with memoization, dynamic programming can be employed to solve the problem bottom-up, starting from the smallest subproblems and working towards the larger ones. This approach would also have a time complexity of O(n) and avoid the overhead of recursion.
