#!/usr/bin/python36

print("content-type: text/html")
print()
import subprocess as sp
import cgi,cgitb

cgitb.enable()


form = cgi.FieldStorage()
name=form.getvalue('docker_name')
print(name)
img='centos'
#print(name,img)
y=sp.getoutput("sudo  date")
z=y.split()
#print(y,z)
g=z[3].split(":")
row=[z[2],g[0],"Docker",name,"Started",img]
#print(row)


x=sp.getoutput("sudo docker start {}".format(name))

file=open("docker.csv","a")
file.write("\n")
#for j in row:
#	file.write("{},".format(j))
#file.close()

for j in row:
        if j!= j[-1]:
                file.write("{},".format(j))
        else:
                file.write("{}".format(j))
file.close()






#with open('docker.csv','a') as csvFile:
#        writer=csv.writer(csvFile)
#        writer.writerow(row)
#csvFile.close()

