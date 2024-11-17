import ftplib

ftp = ftplib.FTP("127.0.0.1")
ftp.login("username", "password")
file = open('index.html','rb')   
ftp.storbinary("STOR " + file, open(file, "rb"))
file.close()                                   
ftp.quit() 
