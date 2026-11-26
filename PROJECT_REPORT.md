# Project Report — Student Fee Management System

**Institution:** Rungta International Skills University  
**School:** School of Information Technology  
**Programme:** Bachelor of Computer Application  
**Problem Statement:** PS No. 64  
**Project Title:** Student Fee Management System  
**Language:** Python 3

## 1. Introduction

The Student Fee Management System is a menu-driven console application developed in Python 3. It maintains student fee records, accepts fee payments, searches student records by roll number and displays students who have pending dues. Records are stored locally in `fees.txt`.

## 2. Objectives

- Register students with roll number, name and course.
- Calculate course fees, amount paid and remaining dues.
- Accept valid full or partial payments and reject invalid payments.
- Search student records by roll number.
- Display students with pending fee balances.
- Load saved records at startup and save changes to `fees.txt`.

## 3. Course Fee Structure

| Course | Total fee |
|---|---:|
| BCA | ₹45,000 |
| BTech | ₹80,000 |
| MBA | ₹80,000 |

## 4. Data Structures and File Handling

The `COURSE_FEES` dictionary stores the fee for each course. Student records are stored as dictionaries inside the `students` list. Each student dictionary contains `Roll`, `Name`, `Course`, `TotalFee` and `Paid`.

The file `fees.txt` stores each record as `Roll,Name,Course,Paid`. The total fee is recalculated from `COURSE_FEES` when records are loaded. Python's CSV module handles commas in names safely.

## 5. Main Functions

| Function | Purpose |
|---|---|
| `calculate_due(student)` | Calculates TotalFee minus Paid. |
| `get_status(student)` | Returns Unpaid, Partial or Paid. |
| `search_student(roll)` | Finds a student using roll number. |
| `add_student()` | Registers a student after validating inputs. |
| `pay_fee()` | Accepts a valid payment and saves the updated record. |
| `search_by_roll()` | Displays the selected student's fee details. |
| `pending_dues()` | Lists students whose remaining fee is greater than zero. |
| `load_records()` / `save_records()` | Loads records at startup and saves changes. |

## 6. Menu Options

1. Add Student
2. Pay Fee
3. Search by Roll Number
4. Pending Dues
5. Exit

## 7. Input Validation

- Roll number must be a positive integer and unique.
- Student name cannot be blank.
- Course must be BCA, BTech or MBA.
- Payment amount must be a positive integer.
- Payment greater than the current due is rejected.
- Malformed, duplicate or invalid records in the data file are skipped with a warning.
- If saving fails, the in-memory change is rolled back.

## 8. Test Cases and Execution Results

| Test | Input | Expected result | Execution |
|---|---|---|---|
| 1. Normal input | Add 101, Riya, BCA | Total 45000; Paid 0; Due 45000; Unpaid | PASS |
| 2. Boundary input | Pay 45000 for roll 101 | Paid 45000; Due 0; Paid | PASS |
| 3. Invalid input | Pay 50000 when due is 45000 | Payment rejected; file unchanged | PASS |
| 4. Partial payment | Add 102, Aman, BTech; pay 20000 | Paid 20000; Due 60000; Partial | PASS |
| 5. Persistence | Restart after saving | Previously saved record loads | PASS |

**Verification environment:** Python 3.13.5. The four college scenarios and a restart/persistence scenario were executed in isolated temporary working directories. All assertions passed.

## 9. How to Run

1. Install Python 3.x.
2. Keep `main.py` in a project folder.
3. Open a terminal in that folder.
4. Run `python main.py`.
5. Select a menu option and follow the prompts.

The program creates `fees.txt` automatically when a student is first saved.

## 10. Limitations

This is an academic console application. It does not connect to a real payment gateway, database server or institution ERP. The text file is intended for local, single-user use.

## 11. Conclusion

The project demonstrates Python dictionaries, lists, functions, conditional statements and file handling to manage student fee records. The required menu operations, payment validations, pending-dues report and file persistence were implemented and executed against the supplied test scenarios.
