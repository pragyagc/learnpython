import matplotlib.pyplot as plt
import seaborn as sns

#line chart 
yield_apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
plt.plot(yield_apples)
plt.show()

#x axis labels
years =[2010, 2011, 2012, 2013, 2014, 2015]
plt.plot(years, yield_apples)
plt.show()

#axis labels and title
plt.plot(years, yield_apples)   
plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')
plt.title('Apple Yield Over Time')
plt.show()

#ploting multiple lines with legend
years = range(2000, 2012)
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896, ]
plt.plot(years, apples)
plt.plot(years, oranges)
plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')
plt.title('Apple and Orange Yield Over Time')
plt.legend(['Apples', 'Oranges'])
plt.show()


#line marker styles
plt.plot(years, apples, marker='o')
plt.plot(years, oranges, marker='x')

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges'])
plt.show()


#Styling lines and markers
plt.plot(years, apples, marker='s', c='b', ls='-', lw=2, ms=8, mew=2, mec='navy')
plt.plot(years, oranges, marker='o', c='r', ls='--', lw=3, ms=10, alpha=.5)

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges'])
plt.show()

#or
plt.plot(years, apples, 's-b')
plt.plot(years, oranges, 'o--r')

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges'])
plt.show()


#Changing the Figure Size
plt.figure(figsize=(12, 6))

plt.plot(years, oranges, 'or')
plt.title("Yield of Oranges (tons per hectare)");
plt.show()


#Improving Default Styles using Seaborn
plt.plot(years, apples, 's-b')
plt.plot(years, oranges, 'o--r')

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges'])
plt.show()

#or 
sns.set_style("darkgrid")
plt.plot(years, apples, 's-b')
plt.plot(years, oranges, 'o--r')

plt.xlabel('Year')
plt.ylabel('Yield (tons per hectare)')

plt.title("Crop Yields in Kanto")
plt.legend(['Apples', 'Oranges'])
plt.show()



# scatter plot   
# Load data into a Pandas dataframe
flowers_df = sns.load_dataset("iris")
print(flowers_df)

print(flowers_df.species.unique())
a=flowers_df['sepal_length']
b=flowers_df['sepal_width']
c=flowers_df['species']
sns.set_style("darkgrid")
plt.plot(a, b)
plt.show()

sns.scatterplot(x=a, y=b)
plt.show()

#adding hues
sns.scatterplot(x=a, y=b, hue=c, s=100)
plt.show()

#Plotting using Pandas Data Frames
plt.title('Sepal Dimensions')
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', s=100, data=flowers_df)
plt.show()

#histogram
plt.title("Distribution of Sepal Width")
plt.hist(flowers_df.sepal_width)
plt.show()

#Controlling the size and number of bins
# Specifying the number of bins
plt.hist(flowers_df.sepal_width, bins=5)
plt.show()

import numpy as np

# Specifying the boundaries of each bin
plt.hist(flowers_df.sepal_width, bins=np.arange(2, 5, 0.25))
plt.show()  


#Multiple Histograms
setosa_df = flowers_df[flowers_df.species == 'setosa']
versicolor_df = flowers_df[flowers_df.species == 'versicolor']
virginica_df = flowers_df[flowers_df.species == 'virginica']
plt.hist(setosa_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))
plt.hist(versicolor_df.sepal_width, alpha=0.4, bins=np.arange(2, 5, 0.25))
plt.show()


#We can also stack multiple histograms on top of one another.
plt.title('Distribution of Sepal Width')

plt.hist([setosa_df.sepal_width, versicolor_df.sepal_width, virginica_df.sepal_width], 
         bins=np.arange(2, 5, 0.25), 
         stacked=True)

plt.legend(['Setosa', 'Versicolor', 'Virginica'])
plt.show()


#Bar chart
years = range(2000, 2006)
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]

plt.bar(years, oranges)
plt.show()

plt.bar(years, apples)
plt.bar(years, oranges, bottom=apples)
plt.show()

#Bar Plots with Averages
tips_df = sns.load_dataset("tips")
print(tips_df)

sns.barplot(x='day', y='total_bill', data=tips_df)
plt.show()

