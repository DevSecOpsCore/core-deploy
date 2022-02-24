
from Library.Classes.deploy import deployImageCluster
from Library.Classes.parseDeployData import parseDeployData


import yaml

from Library.Classes.deploy import deployImageCluster

with open('deployment.yaml') as f:
    dataMap = yaml.safe_load(f)

    print(dataMap)



#parseDeployData.splitSysParams()
#deployImageCluster.setKubeConfigFile()
#deployImageCluster.readDeployYamlFile()
#deployImageCluster.deployClusterYamlFile()