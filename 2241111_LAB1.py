import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# Load the dataset
file_path = "C:\\Users\\joshy\\Desktop\\archive (1)\\retail_sales_dataset.csv" 
data = pd.read_csv(file_path)

# Display basic information about the dataset
print(data.info())
print(data.head())

# Convert Date column to datetime format
data['Date'] = pd.to_datetime(data['Date'])

# Check for missing values
data.isnull().sum()

# Ensure numeric columns are of the correct type
numeric_columns = ['Age', 'Quantity', 'Price per Unit', 'Total Amount']
for col in numeric_columns:
    data[col] = pd.to_numeric(data[col])

# Drop or handle rows with missing or invalid numeric values
data = data.dropna(subset=numeric_columns)
# Basic statistics
print(data[numeric_columns].describe())
for col in numeric_columns:
    plt.figure(figsize=(6, 4))
    sns.histplot(data[col], kde=True, bins=20, color='skyblue')
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.show()

    # Plot boxplots
for col in numeric_columns:
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=data[col], color='orange')
    plt.title(f'Box Plot of {col}')
    plt.show()


# Correlation heatmap
plt.figure(figsize=(8, 6))
correlation_matrix = data[numeric_columns].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap')
plt.show()

# Pairplot for numeric columns
sns.pairplot(data[numeric_columns], diag_kind='kde')
plt.suptitle('Pairwise Relationships', y=1.02)
plt.show()
