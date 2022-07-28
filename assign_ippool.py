#!/usr/bin/env python
###################################################################################
#                           Written by Wei, Hang                                  #
#                          weihanghank@gmail.com                                  #
###################################################################################
"""
Set all pods in a deployment to IP addresses in a specific IP pool
"""

from my_py.configbyssh import *
import json

HOST_INFO = {"host": "10.75.53.43", "port": "22", "user": "root", "pass": "cisco123"}

NAMESPACE = "default"
DEPLOYMENT = "myweb"
IPPOOL = "ip250"
CMD = '''
kubectl patch deployment {} -n {} -p '{{"spec": {{"template":{{"metadata":{{"annotations":{{"cni.projectcalico.org/ipv4pools":"[\\"{}\\"]"}}}}}}}} }}'
'''.format(DEPLOYMENT, NAMESPACE, IPPOOL)
print(CMD)


def main():
    """
    Push the commands and get the response
    """
    # result_dict = {}
    # result_dict = json.loads(configbyssh(HOST_INFO, CMD))
    print(bytes.decode(configbyssh(HOST_INFO, CMD)))


if __name__ == '__main__':
    main()
