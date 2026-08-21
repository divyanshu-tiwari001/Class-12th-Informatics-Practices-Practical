import sqlite3


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 3.2: Insert Details of a New Student")
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
        print("\n--- Insert Student Record Menu ---")
        print("1. Insert a new student record")
        print("2. View all student records")
        print("3. Exit to main menu / Finish")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            try:
                sid = int(input("Enter Student ID (e.g., 101): "))
                name = input("Enter Student Name: ").strip()
                marks = float(input("Enter Marks: "))

                cursor.execute(
                    "INSERT INTO student (student_id, name, marks) VALUES (?, ?, ?);",
                    (sid, name, marks),
                )
                conn.commit()
                print(f"\n[Success] Student '{name}' inserted successfully!")

            except sqlite3.IntegrityError:
                print("\n[Error] Student ID already exists! Please use a unique ID.")
            except ValueError:
                print("\n[Error] Invalid input! Please enter proper numeric values for ID and marks.")

        elif choice == "2":
            cursor.execute("SELECT * FROM student;")
            rows = cursor.fetchall()
            print("\n--- Current Student Records in Database ---")
            if not rows:
                print("No records found.")
            else:
                print(f"{'Student ID':<15} | {'Name':<20} | {'Marks':<10}")
                print("-" * 50)
                for row in rows:
                    print(f"{row[0]:<15} | {row[1]:<20} | {row[2]:<10}")

        elif choice == "3":
            print("Exiting insertion utility.")
            break
        else:
            print("Invalid choice! Please select between 1 and 3.")

    conn.close()
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
