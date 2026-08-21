import sqlite3


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 3.6: Customers Count by Country Using GROUP BY")
    print("Made by Divyanshu Tiwari, Session 2026-27")
    print("=" * 60 + "\n")


def main():
    print_title()

    conn = sqlite3.connect("school_interactive.db")
    cursor = conn.cursor()

    # Ensuring customer table exists and has sample default records
    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS customer (
        customer_id INTEGER PRIMARY KEY,
        customer_name TEXT NOT NULL,
        country TEXT NOT NULL
    );
    """
    )
    
    # Adding a few default sample records if table is empty
    cursor.execute("SELECT COUNT(*) FROM customer;")
    if cursor.fetchone()[0] == 0:
        sample_customers = [
            (1, "Aarav Sharma", "India"),
            (2, "John Smith", "USA"),
            (3, "Priya Patel", "India"),
            (4, "Emma Watson", "UK"),
            (5, "Liam Brown", "USA"),
            (6, "Rohan Verma", "India")
        ]
        cursor.executemany(
            "INSERT INTO customer (customer_id, customer_name, country) VALUES (?, ?, ?);",
            sample_customers
        )
        conn.commit()

    while True:
        print("\n--- Customer GROUP BY Menu ---")
        print("1. View all customer records")
        print("2. Insert a new customer record")
        print("3. Run GROUP BY Query: Total customers from each country")
        print("4. Exit utility")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            cursor.execute("SELECT * FROM customer;")
            rows = cursor.fetchall()
            print("\n--- All Customer Records ---")
            if not rows:
                print("No customer records found.")
            else:
                print(f"{'Customer ID':<15} | {'Customer Name':<20} | {'Country':<15}")
                print("-" * 55)
                for row in rows:
                    print(f"{row[0]:<15} | {row[1]:<20} | {row[2]:<15}")

        elif choice == "2":
            try:
                cid = int(input("Enter Customer ID (Integer): "))
                cname = input("Enter Customer Name: ").strip()
                country = input("Enter Country Name: ").strip()

                cursor.execute(
                    "INSERT INTO customer (customer_id, customer_name, country) VALUES (?, ?, ?);",
                    (cid, cname, country),
                )
                conn.commit()
                print(f"\n[Success] Customer '{cname}' from '{country}' added successfully!")
            except sqlite3.IntegrityError:
                print("\n[Error] Customer ID already exists! Please use a unique ID.")
            except ValueError:
                print("\n[Error] Invalid input! Please enter a numeric Customer ID.")

        elif choice == "3":
            # Core Practical Query using GROUP BY
            query = """
            SELECT country, COUNT(customer_id) 
            FROM customer 
            GROUP BY country;
            """
            cursor.execute(query)
            rows = cursor.fetchall()

            print("\n" + "=" * 45)
            print("--- Total Customers From Each Country ---")
            print(f"{'Country':<20} | {'Total Customers':<15}")
            print("-" * 45)
            for row in rows:
                print(f"{row[0]:<20} | {row[1]:<15}")
            print("=" * 45)

        elif choice == "4":
            print("Exiting utility.")
            break
        else:
            print("Invalid choice! Please select between 1 and 4.")

    conn.close()
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
