#!/usr/bin/env python3
import subprocess

test_cases = [
    "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0",
    "5 * X^0 + 4 * X^1 = 4 * X^0", 
    "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0",
    "6 * X^0 = 6 * X^0",
    "10 * X^0 = 15 * X^0",
    "1 * X^0 + 2 * X^1 + 5 * X^2 = 0"
]

python_path = "/home/weaz/42/computerv1/.venv/bin/python"
script_path = "/home/weaz/42/computerv1/main.py"

for i, test_case in enumerate(test_cases, 1):
    print(f"$>./computor \"{test_case}\"")
    result = subprocess.run([python_path, script_path, test_case],
                            capture_output=True, text=True)
    print(result.stdout.strip())
    if i < len(test_cases):
        print()
