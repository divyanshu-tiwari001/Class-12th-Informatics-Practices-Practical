import numpy as np
import pandas as pd


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 1.1: Create Pandas Series from User Input")
    print("Made by Divyanshu Tiwari, Session 2026-27")
    print("=" * 60 + "\n")


def main():
    print_title()

    # 1. Interactive Series from NumPy ndarray
    print("--- 1. Create Series from NumPy ndarray (e.g., Marks) ---")
    try:
        n = int(input("Enter the number of subjects/elements: "))
        arr_list = []
        index_list = []
        for i in range(n):
            sub = input(f"Enter name of subject {i+1}: ")
            val = float(input(f"Enter marks for {sub}: "))
            index_list.append(sub)
            arr_list.append(val)

        arr_data = np.array(arr_list)
        series_from_array = pd.Series(arr_data, index=index_list)

        print("\nResulting Series from ndarray:")
        print(series_from_array)
    except ValueError:
        print("Invalid input! Please enter numeric values for marks.")

    print("\n" + "-" * 40 + "\n")

    # 2. Interactive Series from a Dictionary
    print("--- 2. Create Series from Dictionary (e.g., Student Scores) ---")
    try:
        d_count = int(input("Enter the number of students to add: "))
        dict_data = {}
        for i in range(d_count):
            name = input(f"Enter student name {i+1}: ")
            score = float(input(f"Enter score for {name}: "))
            dict_data[name] = score

        series_from_dict = pd.Series(dict_data)

        print("\nResulting Series from Dictionary:")
        print(series_from_dict)
    except ValueError:
        print("Invalid input! Please enter numeric values for scores.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
