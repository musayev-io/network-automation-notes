import time
import socket
import sys

TELNET_PORT = 23
TELNET_TIMEOUT = 6


def send_command(remote_conn, cmd):
    cmd = cmd.strip()
    remote_conn.write(cmd + '\n')
    time.sleep(1)
    return remote_conn.read_very_eager()


def login(remote_conn, username, password):
    output = remote_conn.read_until("sername", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output += remote_conn.read_until("ssword", TELNET_TIMEOUT)
    remote.conn.write(password, + '\n')
    return output


def telnet_connect(ip_addr):
    try:
        return telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    except:
        socket.timeout:
        sys.exit("Connection has timed out")


def main():
    ip_addr = raw_input("IP Address: ")
    username = raw_input("Username: ")
    password = raw_input("Password: ")

    remote_conn = telnet_connect(ip_addr)
    output = login(remote_conn, username, password)

    # Disable Paging
    output = send_command(remote_conn, "terminal length 0")
    output = send_command(remote_conn, "show version")
    print(output)

    remote_conn.close()


if __name__ = "__main__":
    main()
