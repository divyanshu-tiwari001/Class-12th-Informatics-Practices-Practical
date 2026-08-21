import sqlite3


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12")
    print("Practical 3.7: Interactive Student Table Manager")
    print("Made by Divyanshu Tiwari, Session 2026-27")
    print("=" * 60 + "\n")


def initialize_database(cursor, conn):
    """Creates the student table and inserts sample records if empty."""
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS student (
            student_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            marks REAL NOT NULL
        );
        """
    )

    sample_data = [
        (101, "Aarav Sharma", 88.5),
        (102, "Vivaan Verma", 76.0),
        (103, "Aditya Singh", 91.0),
        (104, "Diya Patel", 65.5),
        (105, "Saanvi Gupta", 95.0),
    ]

    cursor.executemany(
        """
        INSERT OR IGNORE INTO student (student_id, name, marks) 
        VALUES (?, ?, ?);
        """,
        sample_data,
    )
    conn.commit()


def display_all_students(cursor):
    """Displays all records currently in the student table."""
    print("\n" + "--- Current Student Table Data ---")
    cursor.execute("SELECT student_id, name, marks FROM student;")
    rows = cursor.fetchall()

    if not rows:
        print("No records found in the database.")
        return

    print(f"{'ID':<10} | {'Name':<20} | {'Marks':<10}")
    print("-" * 46)
    for row in rows:
        print(f"{row[0]:<10} | {row[1]:<20} | {row[2]:<10}")
    print("-" * 46)


def add_student(cursor, conn):
    """Allows the user to insert a new student record interactively."""
    print("\n" + "--- Add New Student ---")
    try:
        student_id = int(input("Enter Student ID (e.g., 106): "))
        name = input("Enter Student Name: ").strip()
        marks = float(input("Enter Marks (e.g., 85.5): "))

        cursor.execute(
            """
            INSERT INTO student (student_id, name, marks) 
            VALUES (?, ?, ?);
            """,
            (student_id, name, marks),
        )
        conn.commit()
        print(f"Success: Student '{name}' added successfully!")
    except sqlite3.IntegrityError:
        print("Error: Student ID already exists. Please use a unique ID.")
    except ValueError:
        print("Error: Invalid input format. Please enter numeric values for ID and Marks.")


def sort_students(cursor):
    """Sorts and displays students by marks in either ascending or descending order."""
    print("\nSelect Sorting Order:")
    print("1. Descending Order (Highest to Lowest Marks)")
    print("2. Ascending Order (Lowest to Highest Marks)")

    choice = input("Enter your choice (1 or 2): ").strip()

    if choice == "1":
        order_query = "SELECT student_id, name, marks FROM student ORDER BY marks DESC;"
        title = "Student Table Ordered by Marks (Descending)"
    elif choice == "2":
        order_query = "SELECT student_id, name, marks FROM student ORDER BY marks ASC;"
        title = "Student Table Ordered by Marks (Ascending)"
    else:
        print("Invalid choice. Returning to main menu.")
        return

    cursor.execute(order_query)
    results = cursor.fetchall()

    print(f"\n--- {title} ---")
    print(f"{'Student ID':<12} | {'Name':<20} | {'Marks':<10}")
    print("-" * 48)
    for row in results:
        print(f"{row[0]:<12} | {row[1]:<20} | {row[2]:<10}")
    print("-" * 48)


def main():
    print_title()

    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    # Initialize table with default sample data
    initialize_database(cursor, conn)

    while True:
        print("\n" + "=" * 25 + " MENU " + "=" * 25)
        print("1. View All Students")
        print("2. Add a New Student")
        print("3. Sort Students by Marks")
        print("4. Exit")
        print("=" * 56)

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            display_all_students(cursor)
        elif choice == "2":
            add_student(cursor, conn)
        elif choice == "3":
            sort_students(cursor)
        elif choice == "4":
            print("\nExiting program. Thank you!")
            break
        else:
            print("\nInvalid choice! Please select a valid option from 1 to 4.")

    conn.close()
    print("=" * 60)


if __name__ == "__main__":
    main()
