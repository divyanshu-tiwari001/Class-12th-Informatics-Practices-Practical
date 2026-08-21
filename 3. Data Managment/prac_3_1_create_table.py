import sqlite3


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 3.1: Interactive SQL Database Console")
    print("Made by Divyanshu Tiwari, Session 2026-27")
    print("=" * 60 + "\n")


def main():
    print_title()

    conn = sqlite3.connect("school_interactive.db")
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS student (
        student_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        marks REAL NOT NULL
    );
    """
    )
    conn.commit()

    while True:
        print("\n" + "=" * 50)
        print("--- STUDENT DATABASE MENU ---")
        print("1. View All Student Records")
        print("2. Insert a New Student (Practical 3.1 & 3.2)")
        print("3. Delete a Student by ID (Practical 3.3)")
        print("4. Select Students with Marks > 80 (Practical 3.4)")
        print("5. View Aggregate Statistics on Marks (Practical 3.5)")
        print("6. View Students Ordered by Marks Descending (Practical 3.7)")
        print("7. Exit & Close Database")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            cursor.execute("SELECT * FROM student;")
            rows = cursor.fetchall()
            print("\n--- Current Student Records ---")
            if not rows:
                print("No records found in database.")
            else:
                print(f"{'Student ID':<15} | {'Name':<20} | {'Marks':<10}")
                print("-" * 50)
                for row in rows:
                    print(f"{row[0]:<15} | {row[1]:<20} | {row[2]:<10}")

        elif choice == "2":
            try:
                sid = int(input("Enter Student ID (Integer): "))
                name = input("Enter Student Name: ").strip()
                marks = float(input("Enter Marks: "))

                cursor.execute(
                    "INSERT INTO student (student_id, name, marks) VALUES (?, ?, ?);",
                    (sid, name, marks),
                )
                conn.commit()
                print(f"Success! Student '{name}' added successfully.")
            except sqlite3.IntegrityError:
                print("Error: Student ID already exists! Please use a unique ID.")
            except ValueError:
                print("Invalid input! Please enter proper numeric values for ID and marks.")

        elif choice == "3":
            try:
                sid = int(input("Enter Student ID to delete: "))
                cursor.execute("DELETE FROM student WHERE student_id = ?;", (sid,))
                if cursor.rowcount > 0:
                    conn.commit()
                    print(f"Student with ID {sid} deleted successfully.")
                else:
                    print("No student found with that ID.")
            except ValueError:
                print("Invalid input! Please enter a valid numeric Student ID.")

        elif choice == "4":
            cursor.execute("SELECT * FROM student WHERE marks > 80;")
            rows = cursor.fetchall()
            print("\n--- Students with Marks > 80 ---")
            if not rows:
                print("No students found with marks greater than 80.")
            else:
                print(f"{'Student ID':<15} | {'Name':<20} | {'Marks':<10}")
                print("-" * 50)
                for row in rows:
                    print(f"{row[0]:<15} | {row[1]:<20} | {row[2]:<10}")

        elif choice == "5":
            cursor.execute(
                """
            SELECT MIN(marks), MAX(marks), SUM(marks), AVG(marks) FROM student;
            """
            )
            res = cursor.fetchone()
            print("\n--- Aggregate Statistics ---")
            if res[0] is None:
                print("No records available to compute aggregates.")
            else:
                print(f"Minimum Marks : {res[0]}")
                print(f"Maximum Marks : {res[1]}")
                print(f"Total Sum     : {res[2]}")
                print(f"Average Marks : {res[3]:.2f}")

        elif choice == "6":
            cursor.execute("SELECT student_id, name, marks FROM student ORDER BY marks DESC;")
            rows = cursor.fetchall()
            print("\n--- Students Ordered by Marks (Descending) ---")
            if not rows:
                print("No records found.")
            else:
                print(f"{'Student ID':<15} | {'Name':<20} | {'Marks':<10}")
                print("-" * 50)
                for row in rows:
                    print(f"{row[0]:<15} | {row[1]:<20} | {row[2]:<10}")

        elif choice == "7":
            print("Closing database connection. Goodbye!")
            conn.close()
            break
        else:
            print("Invalid choice! Please select an option between 1 and 7.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
