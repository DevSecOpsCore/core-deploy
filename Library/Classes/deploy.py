from Library.Classes.parseDeployData import parseDeployData
import subprocess


class deployImageCluster:

    def __init__(self):
        pass

    @staticmethod
    def setKubeConfigFile():
        mkdirKubeDirectory = subprocess.check_output("mkdir /home/runner/.kube ", shell=True)
        print(mkdirKubeDirectory)
        lsyap = subprocess.check_output("echo ls yapıyorum   ", shell=True)
        print(lsyap)
        lsA = subprocess.check_output("ls -A /home/runner/ ", shell=True)
        print(lsA)
        catKubeconfig = subprocess.check_output('cat ' + parseDeployData.commandParameters['kubeConfig'] + ' > /home/runner/.kube/config', shell=True)
        print(catKubeconfig)
        lsAC = subprocess.check_output("ls -A /home/runner/.kube/ ", shell=True)
        print(lsAC)
  # - name: mkdir .kube directory
  #     run : mkdir /home/runner/.kube
  #   - name : echo secret
  #     run :  cat <<< "${{ secrets.KUBECONFIG }}" > /home/runner/.kube/config
  #   - name : echo secret
  #     run : echo   "${{ secrets.KUBECONFIG }}"
  #   - name: kubectl control
  #     run : kubectl get nodes



#         mkdirKubeDirectory = subprocess.check_output("mkdir /home/runner/.kube ", shell=True)
#         print(mkdirKubeDirectory)
#         catKubeconfig = subprocess.check_output("cat "+parseDeployData.commandParameters['kubeConfig'] + ' > /home/runner/.kube/config', shell=True)
#         print(catKubeconfig)
#         lsConfig = subprocess.check_output("ls -A /home/runner/.kube/ ", shell=True)
#         print(lsConfig)
#         printConfig = subprocess.check_output("echo config yazdiriyorum ", shell=True)
#         print(printConfig)
#         configControl = subprocess.check_output("cat /home/runner/.kube/config ", shell=True)
#         print(configControl)
#         kubectlControl = subprocess.check_output("kubectl get nodes ", shell=True)
#         print(kubectlControl)
#         print(parseDeployData.commandParameters)
