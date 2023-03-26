!pip install geopandas matplotlib descartes


import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))


world.plot()
plt.show()


#country list

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
countries = world['name'].sort_values()

for country in countries:
    print(country)

    # Define countries you want to color
selected_countries = ['United States', 'India', 'China']

# Assign a color to the selected countries and grey to the rest
world['color'] = 'green'
world.loc[world['name'].isin(selected_countries), 'color'] = 'red'


world.plot(color=world['color'])
plt.show()



# Example data: Country population (not actual data)
data = pd.DataFrame({
    'country': ['United States', 'India', 'China', 'Brazil', 'France'],
    'population': [330, 1390, 1440, 212, 67]
})

# Merge data with the world data
world = world.merge(data, left_on='name', right_on='country', how='left')

# Plot the world map with countries colored according to population
world.boundary.plot(ax=world.plot(column='population', cmap='viridis', legend=True), linewidth=1)
plt.title('Country Population')
plt.show()


world['data'] = np.random.rand(len(world))
fig, ax = plt.subplots(1, 1, figsize=(12, 6))
world.plot(column='data', cmap='coolwarm', legend=True, ax=ax)
ax.set_title('World Map - Colored by Data Values')
plt.show()

