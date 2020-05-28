import os
with open('/root/mldlcode/cnncode.py') as myfile:
    data = myfile.read()

keyword1 = "sklearn"
keyword2 = "StandardScalar"
keyword3 = "Convolve2D"
keyword4 = "Dense"

file1 = open('/root/pyscript/TypeOfCode.txt','w')

if data.count(keyword1)>0 and data.count("linear_models")>0:
    if data.count(keyword2)>0:
        file1.write("ScaleYes")
        file1.close()
        os.system('sudo docker run -i --name sklearntrain -v /root/mldlcode:/root/sklearncode/  sklearnenv:v1') 
    else:
        file1.write("ScaleNo")
        file1.close()
        os.system('sudo docker run -i --name sklearntrain -v /root/mldlcode:/root/sklearncode/  sklearnenv:v1')

elif data.count(keyword4)>0 and data.count(keyword3)>0:
    file1.write("CNN")
    file1.close()
    os.system('sudo docker run -i --name cnntrain -v /root/mldlcode:/root/cnncode cnnenv:v3')
elif data.count(keyword4)>0 and data.count(keyword3)==0:
    file1.write("ANN")
    file1.close()
    os.system('sudo docker run -i --name cnntrain -v /root/mldlcode:/root/cnncode cnnenv:v3')



