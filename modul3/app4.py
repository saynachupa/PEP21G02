#result:[['Section1', value1, value2], ['Section2', value1, value2],

data = """
-----
Section1
-----

value1
value2

-----
Section2
-----
value1
value2
-----
Section3
-----
value1
value2

"""

def parse_data(data:str):
    my_section = False
    linii = data.splitlines()
    result = []

    print(linii)
    for line in linii :
        if line =="":
            continue
        if "-----" == line and my_section is False :
            my_section = True
            print("new section")
        elif "-----" == line and my_section is True :
            my_section = False
            print("end section")
        elif my_section is True:
            print("Section name is", line)
            result.append([line])
        elif not my_section:
            result[-1].append(line)
        print(line)

    return result
var = parse_data(data)
print(var)

#     result=[]
#
# gen = data.()
# entity1 = next(gen)
# #print(entity1)
# for i in gen.__iter__():
#     print(i)

