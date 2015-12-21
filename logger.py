"""
This modular class is for logging purposes.

@author: Sunil
@date: 2015/07/12
"""

import textwrap

class Logger(object):
    def  __init__(self, whoami_name):
        self.whoami_name = whoami_name.ljust(10, '*')
    
    def whoami(self):
        self.log_string(self.whoami_name)

    def log_string(self, msg):
        offset = " " * (len(self.whoami_name) + 4)
        textwrapper = textwrap.TextWrapper(subsequent_indent=offset)
        print("\n".join(textwrapper.wrap("{0}: {1}".format(self.whoami_name, msg))))

    def log_bytes(self, msg):
        buffer = ""
        for char in msg:
            buffer += "{0:02X} ".format(char)
            msg = buffer.strip()
        self.log_string(msg)

def run():
    logger = Logger("Logger")
    logger.whoami()
    logger.log_string("Example string")
    logger.log_bytes(b'C1 CON 0\r')
    logger.log_string(b'C1 CON 0\r')
        
if __name__ == '__main__':
    run()
