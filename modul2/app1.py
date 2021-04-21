
"""
get from input 23:30:31
get from input 23:31:31

find difference between the 2 inputs in seconds
"""
input1 = input('Time1')
input2 = input('Time2')
hours = input1[0:2]
minutes = int(input1[3:5])
seconds = int(input1[6:8])
hours2 = int(input1[0:2])
minutes2 = int(input1[3:5])
seconds2 = int(input1[6:8])
print(type(hours))
print(type(minutes))
print(type(seconds))
timp=3600*hours+60*minutes+seconds
timp2=3600*hours2+60*minutes2+seconds2
print(timp+timp2)
