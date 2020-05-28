import os

file1 = open('/root/pyscript/TypeOfCode.txt','r')
codeType = file1.read()
file1.close()

file2 = open('/root/pyscript/iteration.txt','r')
iteration= int(file2.read())
file2.close()

print(codeType,end="")
if codeType.count("ScaleNo")>0:
    print("d")
    lookup = 'train_test_split'
    with open('/root/mldlcode/code.py') as myfile2:
        for num, line in enumerate(myfile2, 1):
            if lookup in line:
                line_no = num
    print(line_no)

    #tweaking train set
    values1 = """from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)\n"""
    f = open("/root/mldlcode/code.py", "r")
    contents = f.readlines()
    f.close()

    contents.insert(line_no+1, values1)

    f = open("/root/mldlcode/code.py", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()
        
    #tweaking test set
    lookup = 'mind.fit'
    with open('/root/mldlcode/code.py') as myfile2:
        for num, line in enumerate(myfile2, 1):
            if lookup in line:
                line_no = num
    print(line_no)

    values2 = "X_test = sc.transform(X_test)\n"
    f = open("/root/mldlcode/code.py", "r")
    contents = f.readlines()
    f.close()

    contents.insert(line_no+1, values2)

    f = open("/root/mldlcode/code.py", "w")
    contents = "".join(contents)
    f.write(contents)
    f.close()
    os.system("sudo docker run -i --name sklearntrain -v /root/mldlcode:/root/sklearncode/  sklearnenv:v1")
    


if codeType.count("ANN")>0:
    if iteration==1:
        lookup = 'add(Dense'
        contents = "" 
        with open('/root/mldlcode/cnncode.py','r+') as myfile2:
            for num, line in enumerate(myfile2, 1): 
                if lookup in line:
                    if line.count("sigmoid")==0 and line.count("softmax")==0 and line.count("units=1")==0:
                        units = line[line.find("units")+6:line.find(",")]
                        units= int(units)
                        units-=int(0.60*units)
                        new_line = line.replace(line[line.find("units")+6:line.find(",")],str(units))
                        contents+=new_line
                        
                    else:
                        contents+=line
                else:
                    contents+=line

        f = open('/root/mldlcode/cnncode.py','w')
        f.write("{0}".format(contents))
        f.close()
        os.system("sudo docker run -i --name cnntrain -v /root/mldlcode:/root/cnncode/  cnnenv:v3")

    if iteration==2:
        lookup = 'epochs'
        contents= ""
        with open('/root/mldlcode/cnncode.py','r+') as myfile2:            
            for num, line in enumerate(myfile2, 1):
                if lookup in line:
                    units = line[line.find("epochs")+7:line.find(")")]
                    units = int(units)
                    units+=int(0.50*units)
                    new_line = line.replace(line[line.find("epochs")+7:line.find(")")],str(units))
                    contents+=new_line
                else:
                    contents+=line

        f = open('/root/mldlcode/cnncode.py','w')
        f.write("{0}".format(contents))
        f.close()
        os.system("sudo docker run -i --name cnntrain -v /root/mldlcode:/root/cnncode/  cnnenv:v3")
        
            
            
    

                        
                        
 
