import argparse


class parseDeployData:

    commandParameters = {}

    def __init__(self):
        pass

    @staticmethod
    def splitSysParams():
        parser = argparse.ArgumentParser()
        parser.add_argument("-kc", "--kubeConfig", required=True)
        parser.add_argument("-dp", "--dPath", required=False)
        parser.add_argument("-dn", "--dName", required=False)

        args = parser.parse_args()
        parseDeployData.commandParameters['kubeConfig'] = args.kubeConfig
        parseDeployData.commandParameters['dPath'] = args.dPath
        parseDeployData.commandParameters['dName'] = args.dName


        print(parseDeployData.commandParameters)
