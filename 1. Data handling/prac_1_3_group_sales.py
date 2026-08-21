import pandas as pd


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 1.3: Grouping Quarterly Sales Data by Category")
    print("Made by Divyanshu Tiwari, Session 2026-27")
    print("=" * 60 + "\n")


def main():
    print_title()

    try:
        n = int(input("Enter the number of sales records you want to add: "))
        if n <= 0:
            print("Number of records must be greater than 0.")
            return

        categories = []
        items = []
        expenditures = []

        print("\nEnter sales details:")
        for i in range(n):
            print(f"\nRecord {i+1}:")
            cat = input("  Enter Item Category (e.g., Electronics, Stationery): ")
            item = input("  Enter Item Name: ")
            exp = float(input("  Enter Expenditure amount: "))
            
            categories.append(cat)
            items.append(item)
            expenditures.append(exp)

        # Creating the DataFrame from user inputs
        sales_data = {
            "Item Category": categories,
            "Item Name": items,
            "Expenditure": expenditures
        }
        df_sales = pd.DataFrame(sales_data)

        print("\n" + "-" * 40)
        print("--- Original Quarterly Sales DataFrame ---")
        print(df_sales)
        print("-" * 40 + "\n")

        # Grouping by 'Item Category' and calculating total expenditure
        grouped_sales = df_sales.groupby("Item Category")["Expenditure"].sum()

        print("--- Total Expenditure Per Category ---")
        print(grouped_sales)

    except ValueError:
        print("Invalid input! Please enter valid numeric values for expenditure and counts.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
