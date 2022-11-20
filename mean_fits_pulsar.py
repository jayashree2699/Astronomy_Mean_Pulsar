from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
# mean_fits function
def mean_fits(images):
  length = len(images)
  for l in range(0, length):
    if l==0:
      hduList = fits.open(images[l])
      data = np.zeros_like(hduList[0].data)
    hduList = fits.open(images[l])
    data += hduList[0].data
  meanVal = data/length
  return meanVal
if __name__ == '__main__':
  
  # Test your function with examples
  data  = mean_fits(['image0.fits', 'image1.fits', 'image2.fits'])
  print(data[100, 100])

  #Plot the result:
  import matplotlib.pyplot as plt
  plt.imshow(data.T, cmap=plt.cm.viridis)
  plt.colorbar()
  plt.show()