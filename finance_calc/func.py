#!/usr/bin/env python3

def needs_budget(income: int, total_needs: int):
    remainder = 0
    needs = income * 0.5
    remainder = needs - total_needs
    return remainder

def wants_budget(income: int, total_wants: int):
    remainder_wants = 0
    wants = income * 0.3 
    remainder_wants = wants - total_wants
    return remainder_wants

def savings(income: int, total_savings: int):
    remainder_savings = 0
    savings = income * 0.2
    remainder_savings = savings - total_savings
    return remainder_savings

def display_account(income:int):
    print(f"Balance is {income}")

