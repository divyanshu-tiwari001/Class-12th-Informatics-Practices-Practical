import pandas as pd


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 1.5: Interactive DataFrame Modifications")
    print("Made by Divyanshu Tiwari, Session 2026-27")
    print("=" * 60 + "\n")


def main():
    print_title()

    try:
        n = int(input("Enter number of initial employee records to create: "))
        if n <= 0:
            print("Number of records must be greater than 0.")
            return

        emp_ids, names, departments, salaries = [], [], [], []

        print("\nEnter employee details:")
        for i in range(n):
            print(f"\nEmployee {i+1}:")
            emp_id = int(input("  Enter Emp ID: "))
            name = input("  Enter Name: ")
            dept = input("  Enter Department: ")
            sal = float(input("  Enter Salary: "))

            emp_ids.append(emp_id)
            names.append(name)
            departments.append(dept)
            salaries.append(sal)

        df = pd.DataFrame({
            "Emp_ID": emp_ids,
            "Name": names,
            "Department": departments,
            "Salary": salaries
        })

        while True:
            print("\n" + "=" * 40)
            print("--- DataFrame Modification Menu ---")
            print("1. View Current DataFrame")
            print("2. Extract/Select a Specific Column")
            print("3. Insert a New Column (e.g., Bonus or Experience)")
            print("4. Modify Values in a Column")
            print("5. Drop/Delete a Column")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ").strip()

            if choice == "1":
                print("\n--- Current DataFrame ---")
                print(df)

            elif choice == "2":
                print(f"Available columns: {list(df.columns)}")
                col = input("Enter column name to extract: ").strip()
                if col in df.columns:
                    print(f"\n--- Data in column '{col}' ---")
                    print(df[col])
                else:
                    print("Column not found!")

            elif choice == "3":
                col_name = input("Enter new column name: ").strip()
                val_type = input("Do you want to fill it with a single default value for all rows? (y/n): ").strip().lower()
                
                if val_type == 'y':
                    val = float(input("Enter numeric value to fill: "))
                    df[col_name] = val
                else:
                    print(f"Enter values for {n} rows one by one:")
                    col_vals = []
                    for i in range(len(df)):
                        v = float(input(f"  Value for row {i} ({df.loc[i, 'Name']}): "))
                        col_vals.append(v)
                    df[col_name] = col_vals
                print(f"\nColumn '{col_name}' added successfully!")
                print(df)

            elif choice == "4":
                print(f"Available columns: {list(df.columns)}")
                col = input("Enter column name to modify: ").strip()
                if col in df.columns:
                    row_idx = int(input(f"Enter row index (0 to {len(df)-1}) to modify: "))
                    if 0 <= row_idx < len(df):
                        new_val = input(f"Enter new value for row {row_idx}: ")
                        # Simple type conversion check
                        try:
                            if "." in new_val:
                                new_val = float(new_val)
                            else:
                                new_val = int(new_val)
                        except ValueError:
                            pass # Keep as string
                        
                        df.loc[row_idx, col] = new_val
                        print("\nDataFrame updated successfully!")
                        print(df)
                    else:
                        print("Invalid row index!")
                else:
                    print("Column not found!")

            elif choice == "5":
                print(f"Available columns: {list(df.columns)}")
                col = input("Enter column name to drop/delete: ").strip()
                if col in df.columns:
                    df = df.drop(columns=[col])
                    print(f"\nColumn '{col_name if 'col_name' in locals() else col}' dropped successfully!")
                    print(df)
                else:
                    print("Column not found!")

            elif choice == "6":
                print("Exiting interactive modification menu.")
                break
            else:
                print("Invalid choice! Please choose between 1 and 6.")

    except ValueError:
        print("Invalid input! Please enter proper numeric/text data types.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
