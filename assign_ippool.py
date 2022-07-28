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

# HOST_INFO import from configbyssh module

NAMESPACE = "default"  # name of k8s namespace
DEPLOYMENT = "myweb"   # name of k8s deployment
IPPOOL = "ip250"       # name of calico ipam IP Pool
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
