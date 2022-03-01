
from Library.Classes.deploy import deployImageCluster
from Library.Classes.parseDeployData import parseDeployData



parseDeployData.splitSysParams()
deployImageCluster.setKubeConfigFile()
deployImageCluster.deployClusterYamlFile()