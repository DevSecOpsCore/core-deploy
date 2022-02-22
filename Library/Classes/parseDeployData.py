import argparse
from ast import arg


class parseDeployData:

    commandParameters = {}

    def __init__(self):
        pass

    @staticmethod
    def splitSysParams():
        parser = argparse.ArgumentParser()
        parser.add_argument("-kc", "--kubeConfig", required=True)

        args = parser.parse_args()
        parseDeployData.commandParameters['kubeConfig'] = args.kubeConfig

