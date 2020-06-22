#!/usr/bin/env python3
import subprocess
import operator
import csv
import re
import collections
import csv

def error_csv():
        errors={}
        with open("syslog.log","r") as file:
                for line in file.readlines():
                        val=re.search(r"ERROR ([\w ']*)", line)
                        if val:
                                val= val.group(1)[:-1]
                        if val == None:
                                continue
                        if val not in errors:
                                errors[val] = 1
                        else:
                                errors[val]= errors.get(val)+1
                sorted_errors = collections.OrderedDict(sorted(errors.items(), key=operator.itemgetter(1), reverse=True))
                with open("error_message.csv","w") as f:
                        writer = csv.DictWriter(f,fieldnames=["Error","Count"])
                        writer.writeheader()
                        [f.write("{0}, {1}\n".format(key,value)) for key,value in sorted_errors.items()]

                return sorted_errors

def user_csv():
        userdata={}
        with open("syslog.log","r") as file:
                for line in file.readlines():
                        val = line[line.find("(")+1:line.find(")")]
                        if val not in userdata:
                                userdata[val]=[0]*2
                        if line.find("ERROR"):
                                errVal=userdata.get(val)[1]+1
                        if line.find("INFO"):
                                infVal=userdata.get(val)[0]+1
                        userdata[val]=[infVal,errVal]
                sorted_userdata=collections.OrderedDict(sorted(userdata.items(),key=operator.itemgetter(0)))
                with open("user_statistics.csv","w") as f:
                        writer=csv.DictWriter(f,fieldnames=["Username","INFO","ERROR"])
                        writer.writeheader()
                        [f.write("{0}, {1}\n".format(key,value)) for key,value in sorted_errors.items()]

                return sorted_errors

def user_csv():
        userdata={}
        with open("syslog.log","r") as file:
                for line in file.readlines():
                        val = line[line.find("(")+1:line.find(")")]
                        if val not in userdata:
                                userdata[val]=[0]*2
                        if line.find("ERROR"):
                                errVal=userdata.get(val)[1]+1
                        if line.find("INFO"):
                                infVal=userdata.get(val)[0]+1
                        userdata[val]=[infVal,errVal]
                sorted_userdata=collections.OrderedDict(sorted(userdata.items(),key=operator.itemgetter(0)))
                with open("user_statistics.csv","w") as f:
                        writer=csv.DictWriter(f,fieldnames=["Username","INFO","ERROR"])
                        writer.writeheader()
                        [f.write("{0}, {1}\n".format(key,value)) for key,value in sorted_userdata.items()]

                return sorted_userdata

error_csv()
user_csv()

