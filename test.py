import json
import os
import sys
import yaml

from Library.Classes.deploy import deployImageCluster

with open('test.yaml') as f:
    dataMap = yaml.safe_load(f)

    print(dataMap)
print(" sa json olarak okuyom")

print(deployImageCluster.readJsonFile)