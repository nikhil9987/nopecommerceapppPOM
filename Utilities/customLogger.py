import logging 

class LogGen:
    @staticmethod
    def logger():  
        print('inside logger method')
        logging.basicConfig(filename= r"Logs\automation.log",
                            format= r'%(asctime)s: %(levelname)s : %(message)s',datefmt= r'%m/%d/%Y %I:%M:%S %p' 
                            ,force=True
                            )
        
        logger = logging.getLogger()    
        logger.setLevel(logging.INFO)
        return logger

