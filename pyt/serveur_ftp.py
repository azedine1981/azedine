from ftplib import FTP
ftp=FTP()
ftp.connect('ftp.example.com', 21) # Se connecter au serveur FTP
ftp.login('username', 'password') # Se connecter avec vos identifiants
print(ftp.getwelcome()) # Imprimer le message de bienvenue du serveur
