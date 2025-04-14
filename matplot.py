import matplotlib.pyplot as plt                                     
# Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a line plot
plt.plot(x, y)

# Add labels and title
plt.xlabel('Time')
plt.ylabel('Temp')
plt.title('Temp Plot')

# Display the plot
plt.show()


# Data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a scatter plot
plt.scatter(x, y)

# Add labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot')

# Display the plot
plt.show()

# create a bar plot of top ten climbers of Mt. Everest
# Data
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 15, 25]

# Create a bar plot
plt.bar(categories, values)

# Add labels and title
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Plot')

# Display the plot
plt.show()
import pandas as pd
df = pd.read_csv('../2. Fundamentals of NumPy and Pandas/mt_everest.csv')
df.columns
plt.bar(df['NAME'].value_counts().index[:10], df['NAME'].value_counts().values[:10])

plt.xticks(rotation=90)
# Add labels and title
plt.xlabel('Climbers')
plt.ylabel('No of times')
plt.title('Top Ten Mt. Everest Climber')

# Display the plot
plt.show()