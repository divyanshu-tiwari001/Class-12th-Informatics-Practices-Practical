import matplotlib.pyplot as plt
import pandas as pd


def print_title():
    print("=" * 60)
    print("INFORMATICS PRACTICES PRACTICAL - CLASS 12 (INTERACTIVE)")
    print("Practical 2.2: Interactive City Weather Comparison Plot")
    print("Made by Divyanshu Tiwari, Session 2026-27")
    print("=" * 60 + "\n")


def main():
    print_title()

    try:
        n = int(input("Enter number of cities to record weather data for: "))
        if n <= 0:
            print("Number of cities must be greater than 0.")
            return

        cities = []
        temperatures = []
        humidities = []

        print("\nEnter weather details:")
        for i in range(n):
            print(f"\nCity {i+1}:")
            city = input("  Enter City Name: ")
            temp = float(input("  Enter Temperature (°C): "))
            hum = float(input("  Enter Humidity (%): "))

            cities.append(city)
            temperatures.append(temp)
            humidities.append(hum)

        # Creating DataFrame
        weather_df = pd.DataFrame({
            "City": cities,
            "Temperature": temperatures,
            "Humidity": humidities
        })

        print("\n--- Weather Dataset Summary ---")
        print(weather_df)
        print("\n" + "-" * 40 + "\n")

        # Plotting graphs interactively using subplots
        print("Generating weather subplots... Close the chart window to complete execution.")

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

        # Subplot 1: Temperature Bar Chart
        ax1.bar(weather_df["City"], weather_df["Temperature"], color="orange", edgecolor="black")
        ax1.set_title("Temperature Comparison (°C)", fontsize=12, fontweight="bold")
        ax1.set_xlabel("City", fontsize=10)
        ax1.set_ylabel("Temperature (°C)", fontsize=10)
        ax1.grid(axis="y", linestyle="--", alpha=0.7)

        # Subplot 2: Humidity Line/Marker Plot
        ax2.plot(weather_df["City"], weather_df["Humidity"], marker="o", color="blue", linewidth=2, markersize=8)
        ax2.set_title("Humidity Comparison (%)", fontsize=12, fontweight="bold")
        ax2.set_xlabel("City", fontsize=10)
        ax2.set_ylabel("Humidity (%)", fontsize=10)
        ax2.grid(True, linestyle="--", alpha=0.7)

        plt.suptitle("Interactive City Weather Analysis Dashboard", fontsize=14, fontweight="bold")
        plt.tight_layout()
        plt.show()

    except ValueError:
        print("Invalid input! Please enter proper numeric temperature/humidity values.")

    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
