import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np
import os

ndvi_list = list()
for dataset in np.sort(os.listdir('../datasets/')):
	print(dataset) 
	#import bands as separate 1 band raster
	band4 = rasterio.open('../datasets/' + dataset +'/' + dataset + '_B4.TIF') #red
	band5 = rasterio.open('../datasets/' + dataset +'/' + dataset + '_B5.TIF') #nir
	red = band4.read(1).astype('float64')
	nir = band5.read(1).astype('float64')

	#ndvi calculation, empty cells or nodata cells are reported as 0
	ndvi=np.where(
	    (nir+red)==0., 
	    0, 
	    (nir-red)/(nir+red))
	ndvi[:5,:5]
	ndvi_list.append(np.average(ndvi))
	ndviImage = rasterio.open('../Outputs/' + dataset + '_ndviImage.tiff','w',driver='Gtiff',
                          width=band4.width, 
                          height = band4.height, 
                          count=1, crs=band4.crs, 
                          transform=band4.transform, 
                          dtype='float64')
	ndviImage.write(ndvi,1)
	ndviImage.close()
	ndvi = rasterio.open('../Outputs/' + dataset + '_ndviImage.tiff')
	fig = plt.figure(figsize=(18,12))
	plot.show(ndvi, cmap='rainbow_r')

plt.plot(ndvi_list)
plt.title("Change in NDVI over time")
plt.show()
