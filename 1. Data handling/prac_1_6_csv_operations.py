import os
import pandas as pd


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 1.6: Interactive CSV Import & Export")
    print("Made by Divyanshu Tiwari, Session 2026-27")
    print("=" * 60 + "\n")


def main():
    print_title()

    try:
        # Prompting for a custom file name
        csv_file_name = input("Enter custom CSV file name (e.g., 'my_data.csv'): ").strip()
        if not csv_file_name.endswith(".csv"):
            csv_file_name += ".csv"

        n = int(input("Enter number of records to create and export: "))
        if n <= 0:
            print("Number of records must be greater than 0.")
            return

        roll_nos, names, marks, grades = [], [], [] ,[]

        print("\nEnter record details:")
        for i in range(n):
            print(f"\nRecord {i+1}:")
            r = int(input("  Enter Roll No / ID: "))
            name = input("  Enter Name: ")
            m = float(input("  Enter Marks: "))
            g = input("  Enter Grade: ")

            roll_nos.append(r)
            names.append(name)
            marks.append(m)
            grades.append(g)

        # Creating the original DataFrame
        df_original = pd.DataFrame({
            "Roll_No": roll_nos,
            "Name": names,
            "Marks": marks,
            "Grade": grades
        })

        print("\n--- Original DataFrame to Export ---")
        print(df_original)

        # Exporting to CSV
        df_original.to_csv(csv_file_name, index=False)
        print(f"\nSuccess! DataFrame exported to '{csv_file_name}'.")

        while True:
            print("\n" + "=" * 40)
            print("--- CSV Operation Menu ---")
            print("1. Read/Import Data Back from CSV File")
            print("2. Read CSV and Filter Records (e.g., Marks > specific value)")
            print("3. Delete/Cleanup the CSV file from disk and Exit")
            print("4. Exit without deleting file")

            choice = input("Enter your choice (1-4): ").strip()

            if choice == "1":
                if os.path.exists(csv_file_name):
                    df_imported = pd.read_csv(csv_file_name)
                    print(f"\n--- Data Successfully Imported from '{csv_file_name}' ---")
                    print(df_imported)
                else:
                    print("Error: File not found on disk!")

            elif choice == "2":
                if os.path.exists(csv_file_name):
                    df_imported = pd.read_csv(csv_file_name)
                    threshold = float(input("Enter marks threshold to filter students above: "))
                    filtered_df = df_imported[df_imported["Marks"] > threshold]
                    print(f"\n--- Students with Marks > {threshold} ---")
                    if filtered_df.empty:
                        print("No records match this condition.")
                    else:
                        print(filtered_df)
                else:
                    print("Error: File not found on disk!")

            elif choice == "3":
                if os.path.exists(csv_file_name):
                    os.remove(csv_file_name)
                    print(f"File '{csv_file_name}' deleted successfully from disk.")
                else:
                    print("File already removed or does not exist.")
                print("Exiting program.")
                break

            elif choice == "4":
                print(f"Exiting program. Note: '{csv_file_name}' remains saved on your disk.")
                break
            else:
                print("Invalid choice! Please select between 1 and 4.")

    except ValueError:
        print("Invalid input! Please enter proper data types.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
