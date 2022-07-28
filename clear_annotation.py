#!/usr/bin/env python
###################################################################################
#                           Written by Wei, Hang                                  #
#                          weihanghank@gmail.com                                  #
###################################################################################
"""
Clear the annotations that were previously added because of associating IP Pool
"""

from my_py.configbyssh import *
import json

# HOST_INFO import from configbyssh module

NAMESPACE = "default"  # name of k8s namespace
DEPLOYMENT = "myweb"  # name of k8s deployment
IPPOOL = "ip250"  # name of calico ipam IP Pool

CMD1 = '''
kubectl get deployment {} -n {} -o jsonpath={{.spec.template.metadata.annotations."cni\.projectcalico\.org/ipv4pools"}}
'''.format(DEPLOYMENT, NAMESPACE)
CMD2 = '''
kubectl patch deployment {} -n {} --type=json -p='[{{"op":"remove","path":"/spec/template/metadata/annotations/cni.projectcalico.org~1ipv4pools"}}]'
'''.format(DEPLOYMENT, NAMESPACE)
print(CMD2)


def main():
    """
    Push the commands and get the response
    """
    # result_dict = {}
    # result_dict = json.loads(configbyssh(HOST_INFO, CMD))
    if configbyssh(HOST_INFO, CMD1):
        print(bytes.decode(configbyssh(HOST_INFO, CMD2)))
    else:
        print("No such annotation")


if __name__ == '__main__':
    main()
