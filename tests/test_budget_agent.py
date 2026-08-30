import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agents.budget_agent import calculate_budget

# Test 1: normal valid case
result = calculate_budget(50000, 5, 2, "mid")
print("Test 1 (valid):", result)

# Test 2: infeasible budget
result2 = calculate_budget(5000, 5, 2, "mid")
print("Test 2 (too low):", result2)

# Test 3: bad casing — should still work due to normalization
result3 = calculate_budget(50000, 5, 2, "MID")
print("Test 3 (case-insensitive):", result3)