from Library.Classes.parseDeployData import parseDeployData
import subprocess


class deployImageCluster:

    def __init__(self):
        pass

    @staticmethod
    def setKubeConfigFile():
        mkdirKubeDirectory = subprocess.check_output("mkdir /home/runner/.kube ", shell=True)
        print(mkdirKubeDirectory)
        catKubeconfig = subprocess.check_output("cat "+parseDeployData.commandParameters['kubeConfig'] + ' > /home/runner/.kube/config', shell=True)
        print(catKubeconfig)
        configControl = subprocess.check_output("cat /home/runner/.kube/config ", shell=True)
        print(configControl)
        print(parseDeployData.commandParameters)


  # - name: mkdir .kube directory
  #     run : mkdir /home/runner/.kube
  #   - name : echo secret
  #     run :  cat <<< "${{ secrets.KUBECONFIG }}" > /home/runner/.kube/config
  #   - name : echo secret
  #     run : echo   "${{ secrets.KUBECONFIG }}"
  #   - name: kubectl control
  #     run : kubectl get nodes

