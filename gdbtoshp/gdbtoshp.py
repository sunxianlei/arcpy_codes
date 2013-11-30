# -*- coding:gbk -*-
import arcpy,os
from arcpy import env

def gdbtoshp(outfolder):
    fcs=arcpy.ListFeatureClasses()
    for fc in fcs:
        arcpy.CopyFeatures_management(fc,outfolder +os.sep+ str(fc))
        print fc
        
inputfolder=r"E:\1"
outputfolder=r"E:\11"

for r,ds,fs in os.walk(inputfolder):
    newpath=r.replace(inputfolder,outputfolder)
    if not os.path.exists(newpath):
        os.mkdir(newpath)
    if r[-4:]==".gdb":
        env.workspace=r
        mdbpath=r.replace(inputfolder,outputfolder)
        print mdbpath
        gdbtoshp(str(mdbpath))
