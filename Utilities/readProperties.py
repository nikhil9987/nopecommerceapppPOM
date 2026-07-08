import configparser

config =configparser.RawConfigParser()
config.read('Configuration\config.ini')

class Readconfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info','baseurl')
        return url

    
    @staticmethod
    def getUseremail():
        username = config.get('common info','useremail')
        return username

    
    @staticmethod
    def getPassword():
        password = config.get('common info','password')
        return password