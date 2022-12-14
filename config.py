import getpass
import socket
client_username = getpass.getuser()
client_hostname = socket.gethostname()

# Server side settings
server_ip = '192.168.1.145'  # weasel ip (server)
server_hostname = 'XXXXX'  # kali
server_username = 'XXXXX'  # weasel

# server_savecopy_path = '/home/weasel/Desktop/LOOT/'  # for kali linux
server_savecopy_path = '/data/data/com.termux/files/home/'  # for android Termux


# server_port = 443  # for connection (best choice)
# for connection (android Termux does not allow for 443. So just use this. maybe might fail?)
server_port = 4000

# for copy files. need to always turn on ssh in kali. "sudo service ssh start"
server_ssh_port = 22

# Client side settings
client_savecopy_path = (
    "C:\\Users\\{}").format(client_username)