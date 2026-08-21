import pandas as pd


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 1.4: Interactive DataFrame Exploration & Operations")
    print("Made by Divyanshu Tiwari, Session 2026-27")
    print("=" * 60 + "\n")


def main():
    print_title()

    try:
        n = int(input("Enter total number of student records to create (recommend 5+): "))
        if n <= 0:
            print("Number of records must be greater than 0.")
            return

        roll_nos = []
        names = []
        marks = []
        grades = []

        print("\nEnter student details:")
        for i in range(n):
            print(f"\nStudent {i+1}:")
            r = int(input("  Enter Roll No: "))
            name = input("  Enter Name: ")
            m = float(input("  Enter Marks: "))
            g = input("  Enter Grade: ")

            roll_nos.append(r)
            names.append(name)
            marks.append(m)
            grades.append(g)

        # Creating the DataFrame
        data = {
            "Roll_No": roll_nos,
            "Name": names,
            "Marks": marks,
            "Grade": grades
        }
        df = pd.DataFrame(data)

        while True:
            print("\n" + "=" * 40)
            print("--- DataFrame Operation Menu ---")
            print("1. View Complete DataFrame")
            print("2. View Top Records (head)")
            print("3. View Bottom Records (tail)")
            print("4. View DataFrame Attributes (shape, index, columns, dtypes)")
            print("5. Exit")
            
            choice = input("Enter your choice (1-5): ").strip()

            if choice == "1":
                print("\n--- Complete DataFrame ---")
                print(df)
            elif choice == "2":
                num = int(input("Enter number of rows from top to view: "))
                print(f"\n--- Top {num} Records ---")
                print(df.head(num))
            elif choice == "3":
                num = int(input("Enter number of rows from bottom to view: "))
                print(f"\n--- Bottom {num} Records ---")
                print(df.tail(num))
            elif choice == "4":
                print("\n--- DataFrame Attributes ---")
                print(f"Shape (Rows, Columns): {df.shape}")
                print(f"Index: {df.index}")
                print(f"Columns: {df.list if hasattr(df, 'list') else list(df.columns)}")
                print("\nData Types:")
                print(df.dtypes)
            elif choice == "5":
                print("Exiting DataFrame interactive menu.")
                break
            else:
                print("Invalid choice! Please choose between 1 and 5.")

    except ValueError:
        print("Invalid input! Please enter correct numeric values where required.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
