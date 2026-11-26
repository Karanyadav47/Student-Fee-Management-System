"""
Student Fee Management System
PS No. 64 | Python 3

Concepts: Dictionaries, Functions, Conditions and File Handling.
"""

import csv
import os

DATA_FILE = "fees.txt"

# Course fees (course name: total fee)
COURSE_FEES = {
    "BCA": 45000,
    "BTech": 80000,
    "MBA": 80000
}

# Each student is stored as a dictionary in this list.
students = []


def calculate_due(student):
    """Return the remaining fee."""
    return student["TotalFee"] - student["Paid"]


def get_status(student):
    """Return Unpaid, Partial or Paid."""
    if student["Paid"] == 0:
        return "Unpaid"
    if calculate_due(student) == 0:
        return "Paid"
    return "Partial"


def search_student(roll):
    """Find a student by roll number; return None if not found."""
    for student in students:
        if student["Roll"] == roll:
            return student
    return None


def save_records():
    """Save records in fees.txt as Roll,Name,Course,Paid."""
    try:
        with open(DATA_FILE, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            for student in students:
                writer.writerow([
                    student["Roll"],
                    student["Name"],
                    student["Course"],
                    student["Paid"]
                ])
        return True
    except OSError as error:
        print(f"Error: Could not save records: {error}")
        return False


def load_records():
    """Load valid student records from fees.txt at startup."""
    students.clear()

    if not os.path.exists(DATA_FILE):
        return

    try:
        with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)
            for line_number, row in enumerate(reader, start=1):
                if not row:
                    continue

                if len(row) != 4:
                    print(f"Warning: Invalid record on line {line_number}; skipped.")
                    continue

                roll_text, name, course, paid_text = row
                name = name.strip()
                course = course.strip()

                try:
                    roll = int(roll_text)
                    paid = int(paid_text)
                except ValueError:
                    print(f"Warning: Invalid number on line {line_number}; skipped.")
                    continue

                if roll <= 0 or not name or course not in COURSE_FEES:
                    print(f"Warning: Invalid student data on line {line_number}; skipped.")
                    continue

                total_fee = COURSE_FEES[course]
                if paid < 0 or paid > total_fee:
                    print(f"Warning: Invalid payment on line {line_number}; skipped.")
                    continue

                if search_student(roll) is not None:
                    print(f"Warning: Duplicate roll number {roll}; later record skipped.")
                    continue

                students.append({
                    "Roll": roll,
                    "Name": name,
                    "Course": course,
                    "TotalFee": total_fee,
                    "Paid": paid
                })
    except OSError as error:
        print(f"Error: Could not read records: {error}")


def add_student():
    """Register a student with an unpaid course fee."""
    print("\n--- Add Student ---")
    try:
        roll = int(input("Roll: ").strip())
    except ValueError:
        print("Invalid roll number. Enter a whole number.")
        return

    if roll <= 0:
        print("Roll number must be greater than zero.")
        return
    if search_student(roll) is not None:
        print(f"Student with roll number {roll} already exists.")
        return

    name = input("Name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    print("Available courses:")
    for course, fee in COURSE_FEES.items():
        print(f"{course}: {fee}")

    course = input("Course: ").strip()
    if course not in COURSE_FEES:
        print("Invalid course. Choose BCA, BTech or MBA.")
        return

    student = {
        "Roll": roll,
        "Name": name,
        "Course": course,
        "TotalFee": COURSE_FEES[course],
        "Paid": 0
    }
    students.append(student)

    if not save_records():
        students.remove(student)
        print("Student was not added because the record could not be saved.")
        return

    print(
        f"Student added: {roll} | {name} | {course} | "
        f"Total Fee: {student['TotalFee']} | Paid: 0 | "
        f"Due: {calculate_due(student)} | Status: {get_status(student)}"
    )


def pay_fee():
    """Accept a payment only when it is positive and does not exceed the due."""
    print("\n--- Pay Fee ---")
    try:
        roll = int(input("Roll: ").strip())
    except ValueError:
        print("Invalid roll number. Enter a whole number.")
        return

    student = search_student(roll)
    if student is None:
        print(f"Student with roll number {roll} not found.")
        return

    due = calculate_due(student)
    if due == 0:
        print("No dues remaining. Student has already paid the total fee.")
        return

    try:
        amount = int(input("Amount: ").strip())
    except ValueError:
        print("Invalid amount. Enter a whole number.")
        return

    if amount <= 0:
        print("Payment rejected. Amount must be greater than zero.")
        return
    if amount > due:
        print(f"Amount exceeds due ({due}). Payment rejected.")
        return

    old_paid = student["Paid"]
    student["Paid"] += amount

    if not save_records():
        student["Paid"] = old_paid
        print("Payment was not recorded because the file could not be saved.")
        return

    print(
        f"Payment received. Paid: {student['Paid']} | "
        f"Due: {calculate_due(student)} | Status: {get_status(student)}"
    )


def search_by_roll():
    """Display a student's complete fee record."""
    print("\n--- Search Student ---")
    try:
        roll = int(input("Roll: ").strip())
    except ValueError:
        print("Invalid roll number. Enter a whole number.")
        return

    student = search_student(roll)
    if student is None:
        print("Student not found.")
        return

    print(
        f"Roll: {student['Roll']} | Name: {student['Name']} | "
        f"Course: {student['Course']} | Total Fee: {student['TotalFee']} | "
        f"Paid: {student['Paid']} | Due: {calculate_due(student)} | "
        f"Status: {get_status(student)}"
    )


def pending_dues():
    """Display all students who still have fees to pay."""
    print("\n--- Pending Dues ---")
    pending_students = [
        student for student in students if calculate_due(student) > 0
    ]

    if not pending_students:
        print("No pending dues.")
        return

    print("Roll | Name | Course | Total Fee | Paid | Due | Status")
    print("-" * 72)
    for student in pending_students:
        print(
            f"{student['Roll']} | {student['Name']} | {student['Course']} | "
            f"{student['TotalFee']} | {student['Paid']} | "
            f"{calculate_due(student)} | {get_status(student)}"
        )


def display_menu():
    """Display the application menu."""
    print("\n========== STUDENT FEE MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. Pay Fee")
    print("3. Search by Roll Number")
    print("4. Pending Dues")
    print("5. Exit")
    print("====================================================")


def main():
    """Load records and run the menu until the user exits."""
    load_records()
    print("Student Fee Management System")
    print(f"Records loaded: {len(students)}")

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            pay_fee()
        elif choice == "3":
            search_by_roll()
        elif choice == "4":
            pending_dues()
        elif choice == "5":
            if save_records():
                print("Records saved. Thank you for using the system.")
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    main()
