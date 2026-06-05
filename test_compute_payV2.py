import pytest
from compute_payV2 import compute_pay
import sys
import os

print("\n--- DEBUG INFO ---")
print("Where Python is looking for files (sys.path):")
for path in sys.path:
    print(f"  - {path}")
print("------------------\n")


def test_reg_hours():
    # Test a normal 40-hour work week
    assert compute_pay(40, 10.50) == 420.00


def test_ot_hours():
    # Test 45 hours
    assert compute_pay(45, 10.50) == 498.75


def test_negative_values_raise_error():
    # Test that the function correctly raises a ValueError for bad inputs
    with pytest.raises(ValueError):
        compute_pay(-5, 10)
