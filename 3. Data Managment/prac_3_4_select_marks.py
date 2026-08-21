import sqlite3


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 3.4: Select Students with Marks > 80")
    print("Made by Divyanshu Tiwari, Session 2026-27")
    print("=" * 60 + "\n")


def main():
    print_title()

    conn = sqlite3.connect("school_interactive.db")
    cursor = conn.cursor()

    # Ensuring table exists
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
        print("\n--- Select Filter Menu ---")
        print("1. View all student records")
        print("2. Filter students with marks > 80 (Standard Practical Query)")
        print("3. Filter students with a custom marks threshold")
        print("4. Exit filter utility")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            cursor.execute("SELECT * FROM student;")
            rows = cursor.fetchall()
            print("\n--- All Student Records ---")
            if not rows:
                print("No records found in database.")
            else:
                print(f"{'Student ID':<15} | {'Name':<20} | {'Marks':<10}")
                print("-" * 50)
                for row in rows:
                    print(f"{row[0]:<15} | {row[1]:<20} | {row[2]:<10}")

        elif choice == "2":
            query = "SELECT student_id, name, marks FROM student WHERE marks > 80;"
            cursor.execute(query)
            rows = cursor.fetchall()
            
            print("\n--- Students with Marks > 80 ---")
            if not rows:
                print("No students found with marks greater than 80.")
            else:
                print(f"{'Student ID':<15} | {'Name':<20} | {'Marks':<10}")
                print("-" * 50)
                for row in rows:
                    print(f"{row[0]:<15} | {row[1]:<20} | {row[2]:<10}")

        elif choice == "3":
            try:
                threshold = float(input("Enter custom marks threshold (e.g., 75): "))
                query = "SELECT student_id, name, marks FROM student WHERE marks > ?;"
                cursor.execute(query, (threshold,))
                rows = cursor.fetchall()

                print(f"\n--- Students with Marks > {threshold} ---")
                if not rows:
                    print(f"No students found with marks greater than {threshold}.")
                else:
                    print(f"{'Student ID':<15} | {'Name':<20} | {'Marks':<10}")
                    print("-" * 50)
                    for row in rows:
                        print(f"{row[0]:<15} | {row[1]:<20} | {row[2]:<10}")
            except ValueError:
                print("\n[Error] Invalid input! Please enter a valid numeric threshold.")

        elif choice == "4":
            print("Exiting filter utility.")
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")

    conn.close()
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
