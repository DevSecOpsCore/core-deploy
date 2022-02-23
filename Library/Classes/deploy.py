from Library.Classes.parseDeployData import parseDeployData
import subprocess


class deployImageCluster:

    def __init__(self):
        pass

    @staticmethod
    def setKubeConfigFile():
        mkdirKubeDirectory = subprocess.check_output("mkdir /home/runner/.kube ", shell=True)
        print(mkdirKubeDirectory)
        lsYap = subprocess.check_output("echo ls yapıyorum   ", shell=True)
        print(lsYap)
        lsA = subprocess.check_output("ls -A /home/runner/ ", shell=True)
        print(lsA)
        catKubeconfig = subprocess.check_output('echo  "' + parseDeployData.commandParameters['kubeConfig']+'"  > /home/runner/.kube/config', shell=True)
        print(catKubeconfig)
        printConfig = subprocess.check_output("echo config yazdiriyorum ", shell=True)
        print(printConfig)
        configControl = subprocess.check_output("cat /home/runner/.kube/config ", shell=True)
        print(configControl)
        kubectlControl = subprocess.check_output("kubectl get nodes ", shell=True)
        print(kubectlControl)

    @staticmethod
    def deployClusterYamlFile():
        echoDeployment = subprocess.check_output("echo 'deployment dosyasi apply ediliyor' ", shell=True)
        print(echoDeployment)
        kubectlApply = subprocess.check_output("kubectl apply -f deployment.yaml ", shell=True)
        print(kubectlApply)
        kubectlGetall=subprocess.check_output("kubectl get all ", shell=True)
        print(kubectlGetall)
