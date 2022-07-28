#!/usr/bin/env python
###################################################################################
#                           Written by Wei, Hang                                  #
#                          weihanghank@gmail.com                                  #
###################################################################################
"""
Delete the IP Pool with Calico IPAM
"""

from my_py.configbyssh import *
import json

# HOST_INFO import from configbyssh module
SUBNET = "10.244.252.0/24"    # subnet of the calico ipam IP Pool, currently only support one subnet
NAME = "ip252"                # name of calico ipam IP Pool
CMD = '''
cat <<EOF | calicoctl delete -f -
apiVersion: projectcalico.org/v3
kind: IPPool
metadata:
  name: {}
spec:
  cidr: {}
  ipipMode: Never
  natOutgoing: false
  nodeSelector: all()
  vxlanMode: Never
  disabled: false
EOF
'''.format(NAME, SUBNET)
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
