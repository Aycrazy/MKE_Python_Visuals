import geopandas as gp
from shapely.geometry import Point
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import cm

mil_link= 'neighborhood.shp'
mil = gp.read_file(mil_link)
%matplotlib inline



#colors
#https://matplotlib.org/gallery/color/colormap_reference.html

#cmap = ListedColormap(['winter'], name='winter')

fig,ax = plt.subplots(1, 1, figsize=(20,10))
mil.plot(color='darkgrey', ax =ax)

event_locs = gp.GeoDataFrame(df[['point']],
                            crs=mil.crs).rename(columns={'point':'geometry'})

event_locs.plot(ax=ax, 
                                color = 'blue', 
                                marker = '*',
                                markersize = 60)

ax.set(xlabel = 'Easting',
      ylabel='Northing',
      title="Milwaukee Rodents")
ax.set_axisbelow(True)
ax.yaxis.grid(color ='gray',
             linestyle='dashed')
ax.xaxis.grid(color ='gray',
             linestyle='dashed')
