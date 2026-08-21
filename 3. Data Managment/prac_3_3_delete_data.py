import sqlite3


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 3.3: Delete Details of a Student")
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
        print("\n--- Delete Student Record Menu ---")
        print("1. View all current student records")
        print("2. Delete a student by Student ID")
        print("3. Exit deletion utility")

        choice = input("Enter your choice (1-3): ").strip()

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
            # Show records first to help the user choose an ID
            cursor.execute("SELECT student_id, name FROM student;")
            rows = cursor.fetchall()
            if not rows:
                print("\n[Notice] No records available to delete.")
                continue

            print("\nAvailable Students:")
            for row in rows:
                print(f"  ID: {row[0]} | Name: {row[1]}")

            try:
                sid = int(input("\nEnter Student ID to delete: "))
                
                # Check if student exists before deleting
                cursor.execute("SELECT name FROM student WHERE student_id = ?;", (sid,))
                student = cursor.fetchone()

                if student:
                    confirm = input(f"Are you sure you want to delete '{student[0]}' (ID: {sid})? (y/n): ").strip().lower()
                    if confirm == 'y':
                        cursor.execute("DELETE FROM student WHERE student_id = ?;", (sid,))
                        conn.commit()
                        print(f"\n[Success] Student with ID {sid} deleted successfully!")
                    else:
                        print("\nDeletion cancelled.")
                else:
                    print(f"\n[Error] No student found with ID {sid}.")

            except ValueError:
                print("\n[Error] Invalid input! Please enter a valid numeric Student ID.")

        elif choice == "3":
            print("Exiting deletion utility.")
            break
        else:
            print("Invalid choice! Please select between 1 and 3.")

    conn.close()
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
