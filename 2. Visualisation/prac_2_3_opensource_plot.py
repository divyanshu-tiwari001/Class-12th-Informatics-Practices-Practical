import matplotlib.pyplot as plt
import pandas as pd


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 2.3: Interactive Data Aggregation & Plotting")
    print("Made by Divyanshu Tiwari, Session 2026-27")
    print("=" * 60 + "\n")


def main():
    print_title()

    print("Choose Data Source:")
    print("1. Enter custom dataset interactively")
    print("2. Load built-in open-source sample dataset (Smartphone Market Share)")
    
    choice = input("Enter choice (1 or 2): ").strip()

    try:
        if choice == "1":
            n = int(input("Enter number of categories: "))
            if n <= 0:
                print("Number of categories must be greater than 0.")
                return

            categories = []
            values = []

            print("\nEnter category details:")
            for i in range(n):
                cat = input(f"  Enter Category {i+1} Name: ")
                val = float(input(f"  Enter Value/Share for {cat}: "))
                categories.append(cat)
                values.append(val)

            df = pd.DataFrame({
                "Category": categories,
                "Value": values
            })
            chart_title = "Custom Open-Source Dataset Analysis"

        else:
            # Built-in open-source sample data
            data = {
                "Category": ["Android", "iOS", "Windows", "Others"],
                "Value": [71.5, 27.6, 0.4, 0.5]
            }
            df = pd.DataFrame(data)
            chart_title = "Global Smartphone OS Market Share Analysis"
            print("\nLoaded sample open-source dataset (Smartphone Market Share).")

        print("\n--- Dataset Summary ---")
        print(df)
        print("\n" + "-" * 40 + "\n")

        # Summary statistics
        total_sum = df["Value"].sum()
        max_val = df["Value"].max()
        min_val = df["Value"].min()

        print("--- Aggregated Metrics ---")
        print(f"Total Sum : {total_sum}")
        print(f"Maximum   : {max_val}")
        print(f"Minimum   : {min_val}")
        print("\n" + "-" * 40 + "\n")

        # Plotting choice
        print("Choose Plot Type:")
        print("1. Pie Chart")
        print("2. Bar Chart")
        plot_choice = input("Enter choice (1 or 2): ").strip()

        print("\nGenerating plot visualization... Close the chart window to complete execution.")

        plt.figure(figsize=(8, 6))

        if plot_choice == "1":
            plt.pie(
                df["Value"], 
                labels=df["Category"], 
                autopct="%1.1f%%", 
                startangle=140, 
                colors=["#ff9999","#66b3ff","#99ff99","#ffcc99"]
            )
            plt.title(f"{chart_title} (Pie Chart)", fontsize=14, fontweight="bold")
        else:
            df.plot(kind="bar", x="Category", y="Value", color="teal", edgecolor="black", ax=plt.gca(), legend=False)
            plt.title(f"{chart_title} (Bar Chart)", fontsize=14, fontweight="bold")
            plt.xlabel("Categories", fontsize=12)
            plt.ylabel("Values / Shares", fontsize=12)
            plt.xticks(rotation=0)
            plt.grid(axis="y", linestyle="--", alpha=0.7)

        plt.tight_layout()
        plt.show()

    except ValueError:
        print("Invalid input! Please enter proper numbers where required.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
