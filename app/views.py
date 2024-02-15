from django.shortcuts import render
from app.models import *
import csv
from django.http import HttpResponse
# Create your views here.



def Update_Bank(self):
    with open('C:\\Users\\madhu\\OneDrive\\Desktop\\Django projects\\madhu\\Scripts\\project40\\app\\bank.csv','r') as FO:
        IOD=csv.reader(FO)

        for i in IOD:
            bn=i[0].strip()
            BO=Bank(bank_name=bn)
            BO.save()
    return HttpResponse('Bank data is inserted successfully')


def Update_Branch(self):
    with open('C:\\Users\\madhu\\OneDrive\\Desktop\\Django projects\\madhu\\Scripts\\project40\\app\\branch1.csv','r') as FO:
        IOD=csv.reader(FO)
        next(IOD)
        for i in IOD:
            bn=i[0]
            BO=Bank.objects.filter(bank_name=bn)
            if BO:
                ifc=i[1]
                br=i[2]
                add=i[3]
                con=i[4]
                ci=i[5]
                dis=i[6]
                st=i[7]
                BRO=Branch(bank_name=BO[0],ifsc=ifc,branch=br,address=add,contact=con,city=ci,district=dis,state=st)
                BRO.save()
