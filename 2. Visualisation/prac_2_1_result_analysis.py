import matplotlib.pyplot as plt
import pandas as pd


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 2.1: Interactive School Result Analysis & Plotting")
    print("Made by Divyanshu Tiwari, Session 2026-27")
    print("=" * 60 + "\n")


def main():
    print_title()

    try:
        n = int(input("Enter number of data entries to add: "))
        if n <= 0:
            print("Number of entries must be greater than 0.")
            return

        classes = []
        subjects = []
        avg_marks = []

        print("\nEnter record parameters:")
        for i in range(n):
            print(f"\nEntry {i+1}:")
            cls = input("  Enter Class name (e.g., 12A): ")
            sub = input("  Enter Subject name (e.g., Math, Physics, IP): ")
            marks = float(input("  Enter Average Marks: "))

            classes.append(cls)
            subjects.append(sub)
            avg_marks.append(marks)

        # Creating DataFrame
        df = pd.DataFrame({
            "Class": classes,
            "Subject": subjects,
            "Average_Marks": avg_marks
        })

        print("\n--- School Result Dataset Summary ---")
        print(df)
        print("\n" + "-" * 40 + "\n")

        # Grouping by Subject to calculate average performance
        subject_performance = df.groupby("Subject")["Average_Marks"].mean()

        print("--- Subject-wise Average Performance Summary ---")
        print(subject_performance)
        print("\n" + "-" * 40 + "\n")

        # Plotting chart interactively
        print("Generating bar chart visualization... Close the chart window to complete execution.")
        
        plt.figure(figsize=(8, 5))
        subject_performance.plot(kind="bar", color=["skyblue", "salmon", "lightgreen", "gold", "plum"], edgecolor="black")

        plt.title("Interactive Subject-wise Performance Analysis", fontsize=14, fontweight="bold")
        plt.xlabel("Subjects", fontsize=12)
        plt.ylabel("Average Marks", fontsize=12)
        plt.xticks(rotation=0)
        plt.grid(axis="y", linestyle="--", alpha=0.7)

        plt.tight_layout()
        plt.show()

    except ValueError:
        print("Invalid input! Please enter proper numeric marks or counts.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
