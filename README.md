# Policy based IP Address Management for MMS with Calico IPAM

## Functions

* create_ippool.py: Create the IP Pool with Calico IPAM
* delete_ippool.py: Delete the IP Pool with Calico IPAM
* assign_ippool.py: Set all pods of a deployment to IP addresses in a specific IP pool
* configbyssh: Any kind of script that pushes commands via SSH will do, such as
```python
#!/usr/bin/env python
###################################################################################
#                           Written by Wei, Hang                                  #
#                          weihanghank@gmail.com                                  #
###################################################################################
"""
Push any command through SSH, and get response
"""
import paramiko
from io import StringIO
import json

HOST_INFO = {"host": "10.1.1.1", "port": "22", "user": "root", "pass": "xxxxx"}


def configbyssh(host, cmd):
    '''
    SSHClient Testing
    '''
    try:
        # create sshClient obj
        ssh = paramiko.SSHClient()
        # trust remote host, allow access
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    except:
        print("There is an error with the SSHClient")
    try:
        # connect to remote host
        ssh.connect(host["host"],
                    host["port"],
                    host["user"],
                    host["pass"])
    except:
        print("Failed to connect to remote server")
    '''
    execute the commands
    '''
    try:
        # note that every time we execute will be in new env
        stdin, stdout, stderr = ssh.exec_command(cmd)

        if stderr.readlines():
            print(stderr.readlines())
        return stdout.read()

    except:
        print('Fail to execute command')

    # close ssh session
    ssh.close()


def main():
    """
    only for testing
    """
    result_dict = {}
    result_dict = json.loads(configbyssh(HOST_INFO, "kubectl get endpointslices myweb-468fl -ojson"))
    print(result_dict['endpoints'])


if __name__ == '__main__':
    main()
```
