# -*- coding:cp936 -*-

import arcpy,os,shutil

def changetifname(oldpath,newpath):
    raster=arcpy.Raster(oldpath)
    newname=str(int(raster.extent.YMax/1000))+"-"+str(int(raster.extent.XMax/1000))+".tif"
    newfullpath=os.path.join(newpath,newname)
    print newfullpath
    shutil.copy(oldpath,newfullpath)
    
basepath = r"C:\test\t"
newpath=r"C:\test\n";
for root,d,files in os.walk(basepath):
    for f in files:
        if f[-4:]=='.TIF':
            modpath=os.path.join(root,f)
            changetifname(modpath,newpath)



