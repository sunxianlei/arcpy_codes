# -*- coding:gbk -*-

import arcpy,os,shutil

def mdbReProject(oPath,tPath):
    try:
        arcpy.env.workspace=oPath
        outCS = arcpy.SpatialReference(r"E:\20130924mdb数据去除带号\code\Xian.prj")
        fcs=arcpy.ListFeatureClasses()
        for fc in fcs:
            print fc
            outfc=tPath + os.sep + str(fc.encode('gbk'))
            arcpy.Project_management(fc,outfc,outCS)
    except:
        print "---------------------------------------"

    

originPath=r"E:\20130622河道处mdb数据添加投影\有问题\二期\new"#源地址
targetPath=r"E:\20130924mdb数据去除带号\有问题\二期"#目标地址
modelMdbPath=r"E:\20130924mdb数据去除带号\code\model.mdb"#空白数据库地址

for r,ds,fs in os.walk(originPath):
    for f in fs:
        if f[-4:]=='.mdb':
            originMdbPath=os.path.join(r,f)
            targetMdbPath=os.path.join(targetPath,f)
            shutil.copy(modelMdbPath,targetMdbPath)
            print targetMdbPath
            mdbReProject(originMdbPath,targetMdbPath)
            print "done"
            
