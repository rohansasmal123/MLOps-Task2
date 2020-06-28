import smtplib

f = open("/root/mldlcode/accuracy.txt","r")
accuracy = f.read()
f.close()

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("rohansasmal123@gmail.com", "*********")


message = "Great!!! Your model has achieved final accuracy of "+ accuracy 

# sending the mail 
s.sendmail("rohansasmal123@gmail.com", "softwarehub249@gmail.com", message)
    
s.quit()
