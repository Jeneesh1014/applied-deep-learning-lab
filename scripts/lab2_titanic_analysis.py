import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# load the dataset
def load_data():
    return pd.read_csv("data/titanic.csv")


# Task 2: First Look
def first_look(data):
    # Print rows and columns
    rows, columns = data.shape
    print("Rows:", rows)
    print("Columns:", columns)

    # Print column names
    print(data.columns)

    # Print first 5 rows
    print(data.head())

    # Average age of the passengers
    avg_age = data["Age"].mean()
    print("Average Age:", avg_age)

    # It returns basic math calculations basically summary statistics
    print(data.describe())


# Task 3: Cleaning Data
def clean_data(data):
    # Replace missing value with mean in age columns
    data["Age"] = data["Age"].fillna(data["Age"].mean())

    # Drop columns with more than 50% of missing values
    threshold = len(data) * 0.5
    data = data.dropna(thresh=threshold, axis=1)

    # Drop rows that contains missing values
    data = data.dropna()

    # To check if there are still any missing values
    print(data.isnull().sum())

    return data


# Task 4: Exploratory Filtering
def exploratory_filtering(data):
    # Passenger with the most expensive ticket Survived or not
    passenger_info = data.loc[data["Fare"].idxmax()]

    if passenger_info["Survived"] == 1:
        print("Passenger survived")
    else:
        print("Passenger not survived")

    # Name of the oldest survived person
    survived = data[data["Survived"] == 1]
    passenger_info = survived.loc[survived["Age"].idxmax()]
    print("Oldest survived passenger:", passenger_info["Name"])

    # Group the passengers by ticket class
    result = data.groupby("Pclass").agg({
        "Age": "mean",
        "Survived": "mean"
    })

    print(result)


# Task 5: Plotting
def plotting(data):
    grouped = data.groupby(["Sex", "Pclass"])["Survived"].mean().reset_index()
    print(grouped)

    sns.barplot(data=grouped, x="Pclass", y="Survived", hue="Sex")

    plt.title("Survival Rate by Sex and Ticket Class")
    plt.ylabel("Survival Rate")
    plt.xlabel("Ticket Class")

    plt.show()


# run everything from here
if __name__ == "__main__":
    data = load_data()

    # Task 2
    print("\nTask 2: First Look")
    first_look(data)

    # Task 3
    print("\nTask 3: Cleaning")
    data = clean_data(data)
    print("After cleaning:", data.shape)

    # Task 4
    print("\nTask 4: Exploratory Filtering")
    exploratory_filtering(data)

    # Task 5
    print("\nTask 5: Plotting")
    plotting(data)