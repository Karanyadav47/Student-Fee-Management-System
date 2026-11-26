# Student Fee Management System

**PS No. 64 — Bachelor of Computer Application**  
**Language:** Python 3  
**Concepts:** Dictionaries, Functions, Conditions and File Handling

A menu-driven console application to register students, collect course fees, search student records and display pending dues. Records are stored locally in `fees.txt`.

## Course fee structure

| Course | Total fee |
|---|---:|
| BCA | ₹45,000 |
| BTech | ₹80,000 |
| MBA | ₹80,000 |

## Features

- Add/register a student with roll number, name and course.
- Accept full or partial fee payments.
- Reject zero, negative and over-due payments.
- Search student details by roll number.
- List all students with pending dues.
- Calculate due amount and status automatically: Unpaid, Partial or Paid.
- Load records at startup and save after every successful change.
- Prevent duplicate roll numbers and skip malformed records.
- Use CSV handling so names containing commas are safely stored.

## Requirements

- Python 3.x
- No external packages are required.

## Run

Open a terminal in this project folder:

```bash
python main.py
```

On Windows, you can also use:

```bash
py main.py
```

The application creates `fees.txt` automatically when the first student is added. Keep it in the same folder as `main.py` to retain saved records.

## Menu

1. Add Student
2. Pay Fee
3. Search by Roll Number
4. Pending Dues
5. Exit

## Data file format

Each record in `fees.txt` contains:

```text
Roll,Name,Course,Paid
```

The total fee is calculated from the course-fee dictionary and is not duplicated in the file.

## Validation

- Roll number must be a positive whole number and unique.
- Student name cannot be empty.
- Course must be BCA, BTech or MBA.
- Payment must be a positive whole number.
- Payment cannot exceed the student's current due.
- Failed file writes do not leave an unsaved student/payment in memory.

## College test cases

| Test | Input / action | Expected result |
|---|---|---|
| 1. Normal input | Add roll 101, Riya, BCA | Total ₹45,000; Paid ₹0; Due ₹45,000; Unpaid |
| 2. Boundary input | Pay ₹45,000 for roll 101 | Paid ₹45,000; Due ₹0; Paid |
| 3. Invalid input | Pay ₹50,000 when due is ₹45,000 | Rejected; saved record unchanged |
| 4. Different valid scenario | Add roll 102, Aman, BTech; pay ₹20,000 | Paid ₹20,000; Due ₹60,000; Partial; appears in Pending Dues |

## Verification

The four college scenarios were executed using Python 3.13.5 in isolated temporary directories. The test run also checked that records persist after restarting the program. All five checks passed.

## Project report

See [PROJECT_REPORT.md](PROJECT_REPORT.md) for the project write-up, function descriptions, test-case results and limitations.

## Scope and limitation

This is an academic console application. It does not connect to a real payment gateway, database server or institution ERP.
