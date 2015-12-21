"""
This modular class is to initialize serial control and basic functionalites of serialcontrol module.

@author: Sunil
@date: 2015/07/12
"""
import serial
import time
import logger as logger

class Serialcontrol:

    def __init__( self, port ):
        errorCounter = 0
        self.initialized = False
        self.logger = logger.Logger("serialcontrol")
        while errorCounter < 10:
            try:
                self.ser = serial.Serial( port )
                self.initialized = True
                print (errorCounter)
                break
            except:
                errorCounter += 1
                time.sleep( 2 )


    def is_serialport_open( self ) :
        if self.initialized:
            return self.ser.isOpen()
        else:
            return False

    def close_serialport( self ):
        if self.initialized:
            self.ser.close()

    def sendcmd( self, cmd ):
        if self.initialized:
            cmd = cmd + '\r'
            self.ser.write(cmd.encode())
            #self.ser.write( cmd + '\r' )

    def readall( self ):
        if self.initialized:
            out = ''
            response = b""
        # let's wait one second before reading output (let's give device time to answer)
            time.sleep(1)
            while self.ser.inWaiting() > 0:
                out = self.ser.read(1)
                response += out


            if response != '':
                self.logger.log_string(">>" + response.decode()) 
            return response

    def __del__( self ):
        if self.initialized:
            self.close_serialport()


