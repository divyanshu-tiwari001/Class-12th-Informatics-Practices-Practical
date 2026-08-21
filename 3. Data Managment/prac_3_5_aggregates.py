import sqlite3


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 3.5: Aggregate Functions on Marks (Min, Max, Sum, Avg)")
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
        print("\n--- Aggregate Calculator Menu ---")
        print("1. View all student records")
        print("2. Calculate Aggregate Statistics (Min, Max, Sum, Avg)")
        print("3. Exit aggregate utility")

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
            query = """
            SELECT MIN(marks), MAX(marks), SUM(marks), AVG(marks), COUNT(marks) 
            FROM student;
            """
            cursor.execute(query)
            res = cursor.fetchone()

            print("\n" + "=" * 40)
            print("--- Aggregate Statistics Report ---")
            if res[4] == 0 or res[0] is None:
                print("No student records available to calculate aggregates.")
            else:
                print(f"Total Students Evaluated : {res[4]}")
                print(f"Minimum Marks            : {res[0]}")
                print(f"Maximum Marks            : {res[1]}")
                print(f"Total Sum of Marks       : {res[2]}")
                print(f"Average Marks            : {res[3]:.2f}")
            print("=" * 40)

        elif choice == "3":
            print("Exiting aggregate utility.")
            break
        else:
            print("Invalid choice! Please select between 1 and 3.")

    conn.close()
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
