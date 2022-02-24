
from Library.Classes.deploy import deployImageCluster
from Library.Classes.parseDeployData import parseDeployData


import yaml

with open("deployment.yaml", "r") as stream:
    try:
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)


#parseDeployData.splitSysParams()
#deployImageCluster.setKubeConfigFile()
#deployImageCluster.readDeployYamlFile()
#deployImageCluster.deployClusterYamlFile()