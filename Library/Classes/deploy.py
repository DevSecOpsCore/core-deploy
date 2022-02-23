from Library.Classes.parseDeployData import parseDeployData
import subprocess


class deployImageCluster:

    def __init__(self):
        pass

    @staticmethod
    def setKubeConfigFile():
        echoCommand = subprocess.check_output("echo sa ", shell=True)
        print(echoCommand)
        print(parseDeployData.commandParameters)



