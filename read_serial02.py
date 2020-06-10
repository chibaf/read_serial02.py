import serial, sys
import re

strPort = sys.argv[2]   # serial port
ser=serial.Serial(strPort, 115200)
print("connected to: " + ser.portstr)

file=sys.argv[1]  # file name
regex = re.compile('\d+')  # for extracting number from strings
f=open(file,"w+")
while True:
  try:
    line = ser.readline()
    match = regex.findall(str(line))   # extracting number from strings
    # "match[4]+"."+match[5]" is the first Tc value, ..., "match[22]+"."+match[23]" is the tenth Tc value.
    f1=match[4]+"."+match[5]+", "+match[6]+"."+match[7]+", "+match[8]+"."+match[9]+", "+match[10]+"."+match[11]+", "+match[12]+"."+match[13]+", "+match[14]+"."+match[15]+", "+match[16]+"."+match[17]+", "+match[18]+"."+match[19]+", "+match[20]+"."+match[21]+", "+match[22]+"."+match[23]
    # match[1] is minutes, match[2] is seconds, match[3] is sub seconds.
    sec=float(match[1])*60.0+float(match[2])+float(match[3])*0.1
    if(match[3]=="0"):
      print(str(sec)+":"+f1)
    f.write(str(sec)+", "+f1+"\n")
  except KeyboardInterrupt:
    print ('exiting')
    break
ser.flush()
ser.close()
f.close()
