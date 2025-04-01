from configparser import ConfigParser


def read_configuration(category,key):
    config = ConfigParser()
    config.read("/Users/shreya/PycharmProjects/pythonBDD_project/configurations/config.ini")
    return config.get(category,key)