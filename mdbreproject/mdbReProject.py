# -*- coding:gbk -*-

import arcpy,os,shutil

def mdbReProject(oPath,tPath):
    try:
        arcpy.env.workspace=oPath
        outCS = arcpy.SpatialReference(r"E:\20130924mdb����ȥ������\code\Xian.prj")
        fcs=arcpy.ListFeatureClasses()
        for fc in fcs:
            print fc
            outfc=tPath + os.sep + str(fc.encode('gbk'))
            arcpy.Project_management(fc,outfc,outCS)
    except:
        print "---------------------------------------"

    

originPath=r"E:\20130622�ӵ���mdb�������ͶӰ\������\����\new"#Դ��ַ
targetPath=r"E:\20130924mdb����ȥ������\������\����"#Ŀ���ַ
modelMdbPath=r"E:\20130924mdb����ȥ������\code\model.mdb"#�հ����ݿ��ַ

for r,ds,fs in os.walk(originPath):
    for f in fs:
        if f[-4:]=='.mdb':
            originMdbPath=os.path.join(r,f)
            targetMdbPath=os.path.join(targetPath,f)
            shutil.copy(modelMdbPath,targetMdbPath)
            print targetMdbPath
            mdbReProject(originMdbPath,targetMdbPath)
            print "done"
            
