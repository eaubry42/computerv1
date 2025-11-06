#!/usr/bin/env python3
"""
Demo script showing both command line and STDIN usage of the polynomial solver
"""
import subprocess

python_path = "/home/weaz/42/computerv1/.venv/bin/python"
script_path = "/home/weaz/42/computerv1/main.py"

print("=== Polynomial Solver Demo ===\n")

print("1. Command Line Usage:")
print("$>./computor \"5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0\"")
result = subprocess.run([python_path, script_path, "5 * X^0 + 4 * X^1 - 9.3 * "
                        "X^2 = 1 * X^0"], capture_output=True, text=True)
print(result.stdout.strip())

print("\n2. STDIN Usage:")
print("$>echo \"6 * X^0 = 6 * X^0\" | ./computor")
result = subprocess.run([python_path, script_path],
                        input="6 * X^0 = 6 * X^0",
                        capture_output=True, text=True)
print(result.stdout.strip())

print("\n3. Error Handling - Empty Input:")
print("$>echo \"\" | ./computor")
result = subprocess.run([python_path, script_path],
                        input="",
                        capture_output=True, text=True)
print(result.stdout.strip())

print("\n4. Error Handling - Too Many Arguments:")
print("$>./computor \"arg1\" \"arg2\"")
result = subprocess.run([python_path, script_path, "arg1", "arg2"],
                        capture_output=True, text=True)
print(result.stdout.strip())

print("\nBoth command line arguments and STDIN input are now supported!")
