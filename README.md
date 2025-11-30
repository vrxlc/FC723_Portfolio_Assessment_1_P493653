# FC723 Euclidean Algorithm Project

Euclidean & Extended Euclidean Algorithms

Student ID: P493653
Tutor: Sophie Norman

📌 Project Description

This project implements both the Euclidean Algorithm and the Extended Euclidean Algorithm using Python.
The goal is to show understanding of encapsulation, input validation, algorithm implementation, and progressive versioning across multiple improvements (V1, V2, V3).

The program can:

Calculate the Greatest Common Divisor (GCD) of two positive integers

Calculate Bézout coefficients (x, y) such that:

𝑎
𝑥
+
𝑏
𝑦
=
gcd
⁡
(
𝑎
,
𝑏
)
ax+by=gcd(a,b)

Each version builds on the previous one to demonstrate iterative enhancement, good coding practice, and clear documentation.

📦 Versions Overview

Version 1 – Basic Euclidean Algorithm

- Implemented a simple calculate_gcd() method

- Added encapsulation using a class

- Introduced a main program to accept user input

- Provided basic output formatting

Version 2 – Improved Euclidean Algorithm

- Added a helper function get_valid_input() to accept only positive integers

- Refactored the main program to use validated user input

- Introduced error messages for invalid input

- Added explanatory comments for clarity

Version 3 – Extended Euclidean Algorithm

- Added ExtendedEuclideanAlgorithm class

Implemented extended_gcd() to compute:

- GCD

- Bézout coefficients

- Added user input and validation

- Added detailed comments explaining the algorithm step-by-step

This version demonstrates how the extended algorithm tracks remainders and coefficient changes in each loop iteration, making it suitable for cryptographic applications (e.g., modular inverses).

▶️ How to Run the Program

1. Ensure you have Python 3 installed.

2. Open a terminal or command prompt.

3. Navigate to the folder containing the .py file.

4. Run:

python main.py


Enter two positive integers when prompted.
