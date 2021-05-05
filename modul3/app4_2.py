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
    result=[]
    my_iter= data.splitlines().__iter__()
    for line in my_iter:
        if line == "":
            continue
        if "-----" == line:
            #section = next(my_iter)
            result.append([next(my_iter)])
            next(my_iter)
            #print("Sections is: ", section)
           # result.append([section])
            continue
        result[-1].append(line)
        print(line)

    return result
var = parse_data(data)
print(var)