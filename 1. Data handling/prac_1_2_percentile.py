import numpy as np
import pandas as pd


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 1.2: Print Elements Above the 75th Percentile")
    print("Made by Divyanshu Tiwari, Session 2026-27")
    print("=" * 60 + "\n")


def main():
    print_title()

    try:
        n = int(input("Enter total number of students/data points: "))
        if n <= 0:
            print("Number of students must be greater than 0.")
            return

        names = []
        marks = []

        print("\nEnter student details:")
        for i in range(n):
            name = input(f"Enter name of student {i+1}: ")
            mark = float(input(f"Enter marks for {name}: "))
            names.append(name)
            marks.append(mark)

        # Creating the Series from user inputs
        marks_series = pd.Series(marks, index=names)

        print("\n" + "-" * 40)
        print("--- Complete Marks Series ---")
        print(marks_series)
        print("-" * 40 + "\n")

        # Calculating the 75th percentile
        p75 = marks_series.quantile(0.75)
        print(f"Calculated 75th Percentile Value: {p75}")
        print("-" * 40 + "\n")

        # Filtering elements above the 75th percentile
        above_p75 = marks_series[marks_series > p75]

        print("--- Students Above the 75th Percentile ---")
        if above_p75.empty:
            print("No students found strictly above the 75th percentile.")
        else:
            print(above_p75)

    except ValueError:
        print("Invalid input! Please enter valid numbers for marks and counts.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
