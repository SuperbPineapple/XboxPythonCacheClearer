import os

# you can change these if your caches are different
cachePathE = r"E:\CACHE"

# X, Y, and Z caches don't appear usually on XBMC-type dashes
# You can uncomment the XYZ caches if you've enabled them.

# cachePathX = r"X:"
# cachePathY = r"Y:"
# cachePathZ = r"Z:"

# for if you play beta halos (you can comment this out if this directory doesn't appear)
betaHaloCache = r"E:\CACHEGSRV"

for eCache in os.listdir(cachePathE):
    clearECache = os.path.join(cachePathE, eCache)
    if os.path.isfile(clearECache):
        os.remove(clearECache)
"""

for filesInX in os.listdir(cachePathX):
   clearXCache = os.path.join(cachePathX, filesInX)
   if os.path.isfile(clearXCache):
     os.remove(clearXCache)

for filesInY in os.listdir(cachePathY):
  clearYCache = os.path.join(cachePathY, filesInY)
  if os.path.isfile(clearYCache):
     os.remove(clearYCache)

 for filesInZ in os.listdir(cachePathZ):
  clearZCache = os.path.join(cachePathZ, filesInZ)
  if os.path.isfile(clearZCache):
     os.remove(clearZCache)
"""
# you can comment this out if the directory doesn't appear
for fileNameHalo in os.listdir(betaHaloCache):
    fileToRemoveHalo = os.path.join(betaHaloCache, fileNameHalo)
    if os.path.isfile(fileToRemoveHalo):
        os.remove(fileToRemoveHalo)


print("Cache cleared.")

