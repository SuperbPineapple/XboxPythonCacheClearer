import os

# define cachepaths, you can change these if your caches are different
cachePathE = r"E:\CACHE"
# cachePathX = r"X:"
# cachePathY = r"Y:"
# cachePathZ = r"Z:"
# There's no XYZ parititions on my version of Xemu, so these are disabled.
# TODO - readd them (for other version that don't hide XYZ for some reason)

# for if you play beta halos (you can comment this out if this folder doesn't appear)
betaHaloCache = r"E:\CACHEGSRV"

# remove E cache files
for eCache in os.listdir(cachePathE):
   clearECache = os.path.join(cachePathE, eCache)
   if os.path.isfile(clearECache):
      os.remove(clearECache)

# remove X cache files
# for filesInX in os.listdir(cachePathX):
   clearXCache = os.path.join(cachePathX, filesInX)
   if os.path.isfile(clearXCache):
      os.remove(clearXCache)

# remove Y cache files
# for filesInY in os.listdir(cachePathY):
   clearYCache = os.path.join(cachePathY, filesInY)
   if os.path.isfile(clearYCache):
      os.remove(clearYCache)

# remove Z cache files
# for filesInZ in os.listdir(cachePathZ):
   clearZCache = os.path.join(cachePathZ, filesInZ)
   if os.path.isfile(clearZCache):
      os.remove(clearZCache)

# remove halo cache files (you can comment this out if the folder doesn't appear)
for fileNameHalo in os.listdir(betaHaloCache):
   fileToRemoveHalo = os.path.join(betaHaloCache, fileNameHalo)
   if os.path.isfile(fileToRemoveHalo):
      os.remove(fileToRemoveHalo)

print("Cache cleared.")