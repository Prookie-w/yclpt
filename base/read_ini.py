import configparser
import os
class ReadIni(object):
    def __init__(self, file_name=None, node=None):
        if file_name == None:
           file_name = os.path.join(os.path.dirname(os.getcwd()), "config\LocalElement.ini")
        if node == None:
            print(node)
            self.node = "LoginElement"
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        cf.read(file_name)
        return cf

    def get_value(self, key):
        data = self.cf.get(self.node, key)
        return data

if __name__ == '__main__':
    read_init =ReadIni(node="LoginElement")
    print(read_init.get_value("username"))
