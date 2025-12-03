import os

# define cachepaths, you can change these if your cache path is different
cachePath = r"E:\CACHE"

# for if you play beta halos (you can comment this out if you don't play it)
betaHaloCache = r"E:\CACHEGSRV"

# remove cache files
for fileName in os.listdir(cachePath):
   fileToRemove = os.path.join(cachePath, fileName)
   if os.path.isfile(fileToRemove):
      os.remove(fileToRemove)

# remove halo cache files (you can comment this out if you don't play it)
for fileNameHalo in os.listdir(betaHaloCache):
   fileToRemoveHalo = os.path.join(betaHaloCache, fileNameHalo)
   if os.path.isfile(fileToRemoveHalo):
      os.remove(fileToRemoveHalo)

