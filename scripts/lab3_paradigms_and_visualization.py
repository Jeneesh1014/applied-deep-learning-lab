#lab3 workimport seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset("penguins")


# Task 1

penguins_task1 = penguins.dropna(subset=["body_mass_g"])

sns.lineplot(x=penguins_task1.index, y="body_mass_g", data=penguins_task1)
plt.title("Line Plot of Body Mass")
plt.show()

# this is misleading because line plot is used for time series data
# here there is no order so it creates false trend

sns.histplot(data=penguins_task1, x="body_mass_g", bins=20)
plt.title("Distribution of Body Mass")
plt.show()

# histogram is correct because it shows distribution of the data


# Task 2

penguins_task2 = penguins.dropna(subset=["flipper_length_mm", "bill_length_mm"])

sns.barplot(data=penguins_task2, x="flipper_length_mm", y="bill_length_mm")
plt.xticks(rotation=90)
plt.title("Bar plot flipper vs bill length")
plt.show()

# overcrowded because too many values on x axis
# difficult to read and hides details

sns.scatterplot(data=penguins_task2, x="flipper_length_mm", y="bill_length_mm")
plt.title("Scatter plot flipper vs bill length")
plt.show()

# scatter plot shows relationship clearly and also shows clusters and outliers


# Task 3

penguins_task3 = penguins.dropna(subset=["species", "body_mass_g"])

penguins_task3.groupby("species")["body_mass_g"].sum().plot.pie(autopct='%1.1f%%')
plt.title("Pie Chart of Body Mass per Species")
plt.show()

# poor choice because total mass depends on number of penguins
# it does not show average weight

sns.boxplot(data=penguins_task3, x="species", y="body_mass_g")
plt.title("Box Plot of Body Mass per Species")
plt.show()

# box plot shows median, spread and outliers so it is better


# Task 4

penguins_task4 = penguins.dropna(subset=["flipper_length_mm", "bill_length_mm", "species"])

species_list = penguins_task4["species"].unique()

for sp in species_list:
    subset = penguins_task4[penguins_task4["species"] == sp]
    
    sns.scatterplot(data=subset, x="flipper_length_mm", y="bill_length_mm")
    plt.title(f"Scatter Plot for {sp}")
    plt.show()

# separate plots are harder to compare

sns.scatterplot(
    data=penguins_task4,
    x="flipper_length_mm",
    y="bill_length_mm",
    hue="species"
)

plt.title("Flipper vs Bill colored by species")
plt.show()

# hue helps to compare all species in one plot
# overall trend is similar but each species forms its own cluster