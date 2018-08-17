import paramiko
from getpass import getpass


ip_addr = '10.1.255.20'
username = 'musa'
password = getpass()
MAX_BUFFER = 65535  # Max buffer Parmiko can receive

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.load_system_host_keys()
# remote_conn_pre.load_host_keys("/path/to/.ssh/known_hosts")
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
remote_conn_pre.connect(ip_addr, username=username,
                        password=password, look_for_keys=False,
                        allow_agent=False, port=2222)
# Read once from a Cisco router using exec_command. You can execute multiple commands this way in Linux
# stdin, stdout, stderr = remote_conn.exec_command('show ip int brief \n')
remote_conn = remote_conn_pre.invoke_shell()

# Set timeout to prevent a hanging session
remote_conn.settimeout(6.0)
# remote_conn.gettimeout()

# Check if buffer has been modified since last read
remote_conn.recv_ready()

output = remote_conn.recv(0)

# Capture output if it's bigger than 65535 bytes
if remote_conn.recv_ready():
    output += remote_conn.recv(MAX_BUFFER)
