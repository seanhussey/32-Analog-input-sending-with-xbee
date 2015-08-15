import serial
import sys 
import time 

def xbee_reading():
        Port=sys.argv[1]
        #Port='COM3'
        buffer_clear=0
        p=0;
        q=0;
        ser = serial.Serial(port=Port,baudrate=115200)
        counter=0
        string=""
        msb=0;
        lsb=0;
        formatter=0
        reading=0

        a=time.time()
        while True and counter<52  :
                s=ser.read()
                n=float(ord(s))
                #print(n)
                if(n==126):
                    counter=0;
                    #print "---------- Timestamp: "+str(time.time())+"-----------------"
                    buffer_clear=0
                    formatter=0
                                   
                counter=counter+1
                
                    
            
                if(counter>=19):
                        #print str(n)+"    "+str(counter)
                        rem=(counter-18)%2
                        square=(counter-18)%8

                        if(rem==1):
                                lsb=n
                        if(rem==0):
                                msb=n
                                reading=(lsb*256)+msb
                                if(reading<1023):
                                        reading=5.0*(reading/1023.0)
                                        string+=str(reading)+" ;"#+str(buffer_clear)+" "
                                        buffer_clear+=1
                        #if(square==0):
                         #       string+=";"
        #print len(string)
                        
                        
        b=time.time()


                
        #file = open("newfile.txt", "w")

        #file.write(string)
        #file.close()

                        
        #output="1 2 ;3 4"

        #print string
        #print b-a
        
        ser.close()

        return string



def __main__():
        s=""
        for i in range(1,18):
                s+=xbee_reading()+"   ";

        sys.stdout.write(s)
__main__()

