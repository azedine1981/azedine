# Similairement à ftplib, nous pouvons utiliser ftpreety pour nous connecter en toute sécurité à un serveur distant et télécharger des fichiers. Nous pouvons également télécharger des fichiers en utilisant ftpreety. Le programme ci-dessous illustre la même chose.

from ftpretty import ftpretty

# Mention the host
host = "127.0.0.1"

# Supply the credentisals
f = ftpretty(host, user, pass )

# Get a file, save it locally
f.get('someremote/file/on/server.txt', '/tmp/localcopy/server.txt')

# Put a local file to a remote location
# non-existent subdirectories will be created automatically
f.put('/tmp/localcopy/data.txt', 'someremote/file/on/server.txt')
