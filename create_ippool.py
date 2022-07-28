#!/usr/bin/env python
###################################################################################
#                           Written by Wei, Hang                                  #
#                          weihanghank@gmail.com                                  #
###################################################################################
"""
Push any command through SSH, and get response
"""

from my_py.configbyssh import *
import json

HOST_INFO = {"host": "10.75.53.43", "port": "22", "user": "root", "pass": "cisco123"}
SUBNET = "10.244.252.0/24"
NAME = "ip252"
CMD = '''
cat <<EOF | calicoctl apply -f -
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
