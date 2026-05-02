import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("AutoEDA/candy_crush.csv")
print(df.head())
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.info())
print(df.describe())
print(df.describe(include="all"))
print("Missing values per column:")
print(df.isnull().sum())
print("Number of duplicate rows:", df.duplicated().sum())
sns.set_style("whitegrid")
sns.set_palette("Set2")

# 1️⃣ Distribution of numeric columns (histograms)
df.hist(figsize=(12, 8), bins=20, edgecolor='black', color="skyblue")
plt.suptitle("Histograms of Numeric Columns", fontsize=16, fontweight="bold")
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

# 2️⃣ Countplot for Levels (categorical)
plt.figure(figsize=(10,5))
sns.countplot(data=df, x="level", hue="level", palette="Set3", legend=False)
plt.title("Count of Levels", fontsize=14, fontweight="bold")
plt.xticks(rotation=45)
plt.show()

# 3️⃣ Distribution of Number of Attempts
plt.figure(figsize=(8,5))
sns.histplot(df["num_attempts"], kde=True, bins=30, color="lightcoral")
plt.title("Distribution of Number of Attempts", fontsize=14, fontweight="bold")
plt.xlabel("Number of Attempts")
plt.ylabel("Frequency")
plt.show()

# 4️⃣ Distribution of Number of Successes
plt.figure(figsize=(8,5))
sns.histplot(df["num_success"], kde=True, bins=30, color="mediumseagreen")
plt.title("Distribution of Number of Successes", fontsize=14, fontweight="bold")
plt.xlabel("Number of Successes")
plt.ylabel("Frequency")
plt.show()

# 5️⃣ Boxplot: Attempts vs Level
plt.figure(figsize=(12,6))
sns.boxplot(data=df, x="level", y="num_attempts", hue="level", palette="Set2", legend=False)
plt.title("Attempts Distribution per Level", fontsize=14, fontweight="bold")
plt.xticks(rotation=45)
plt.show()

# 6️⃣ Boxplot: Successes vs Level
plt.figure(figsize=(12,6))
sns.boxplot(data=df, x="level", y="num_success", hue="level", palette="Set1", legend=False)
plt.title("Success Distribution per Level", fontsize=14, fontweight="bold")
plt.xticks(rotation=45)
plt.show()

# 7️⃣ Correlation Heatmap
plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap", fontsize=14, fontweight="bold")
plt.show()