import pexpect
import sys
import time
import re
from getpass import getpass


def main():
    username = 'musa'
    ip_addr = '10.1.255.10'
    port = 22
    password = getpass()
    # Get the router hostname
    router_name = ssh_conn.before
    router_name = router_name.strip()
    prompt = router_name + ssh_conn.after
    prompt = prompt.strip()

    # ssh -l musa 10.1.1.1 -p 2222
    ssh_conn = pexpect.spawn(
        'ssh -l {} {} -p {}'.format(username, ip_addr, port))

    # ssh_conn.logfile = sys.stdout
    ssh_conn.timeout = 2
    ssh_conn.expect('assword')
    ssh_conn.sendline(password)
    # ssh_conn.sendline('sh ip int bri')
    ssh_conn.expect(prompt)
    ssh_conn.expect(prompt)
    # print(ssh_conn.after)
    # Prints out what was captured in the middle of the two expect()
    # print(ssh_conn.before)

    # Catch a timeout if expect() is not found
    # try:
    #     ssh_conn.sendline('show version')
    #     ssh_conn.expect('zzz')
    # except:
    #     print("Timeout")

    pattern = re.compile(r'^Lic.*DI:.*$', re.MULTILINE)
    ssh_conn.sendline('show version')
    ssh_conn.expect(pattern)
    print(ssh_conn.after)


if __name__ == "__main__":
    main()
