name = 'Florin'
age = 26
print ('name ', name, ', age:', age)
#print = 'print'
#print ('name ', name, ', age', age)
#type function
result = type(name)
print(result)
result = type(age)
print(result)

result = id(name) #arata locatia memoriei
print(result)

print(8+8)
print((8).__add__(8))
print(8*'text')
print((8).__mul__('text'))
print(('text').__mul__(8))

print(8-8)
print((8).__sub__(8))
print (8/8)
print((8).__truediv__(8))

print(8**8)
print((8).__pow__(8))
print(pow(8, 8))
#float
result = ((8).__truediv__(8))
print(type(result))

a=3
b=4
c=5
x = (-b + ((b**2) - 4 * a * c)**(1/2))/(2*a)
print(x)
x = (-b - ((b**2) - 4 * a * c)**(1/2))/(2*a)
print(x)


bsqr= b.__pow__(2)
multi= (4).__mul__(a.__mul__(c))
dif= bsqr.__sub__(multi)
dif=float(dif)
var=(1).__truediv__(2)
rad=dif.__pow__(var)
b= complex(b)
dif2=(-b).__sub__(rad)
mul1=(2).__mul__(a)
ec= dif2.__truediv__(mul1)
print(ec)
#comlex
#obligatoriu j la capat
nr1 = 1.0+1.0j
nr2 = 3+ 5J
print(nr1+nr2)
print(type(nr1))

#strings
my_str1='My String \n' # nu poti avea multi line text
print(my_str1)
my_str1 = '''this 
is
a
multy
line
test''' #poti avea multi line

print(my_str1)
my_str2= r"""My String \n""" # no multi line (r)
print(my_str2)
my_str2 = f"""My string {my_str1}""" # (f) folostest obiect in string
print(my_str2)

#dir
info = dir(my_str2) # arata ce metode se pot folosi
print(info)

var1 ='this is {}'
cap = var1.capitalize()
print(cap)
format1 = var1.format('a string')
print(format1)
phone = "0747.655.444"
split1 = phone.split("7")
print(split1)
split1=phone.rsplit(sep=".", maxsplit=1)
print(split1)

#input
var3 = 'this is my text'
#name1 = input('give me your name: ') #introduci din tastatura
#print(var3, name1)

#slice
text= "my text"
first_letter = "My text"[0]
print(first_letter)
slice1 = text[1:4]
print(slice1)
slice2 = text[0:7:2]
print(slice2)

input1 = input('Enter text here')
slice3 = input1[0:5]
slice4 = input1[5:11]
print(slice4 + slice3)
reverse1 = slice3[::-1]
reverse2 = slice4[::-1]
#negative step  -> inverseaza caracterele ex.dreapta la stanga
#reverse= text[::-1]
#print(reverse)
print(reverse2+reverse1)

#boolean true false
my_bool = True
print(type(my_bool))
my_bool = False
print(type(my_bool))
print(id(True))
print(id(False))
print(id(10))

Addboolean = True + False
print(Addboolean)
print(dir(Addboolean))
x=True.__add__(False)
print(x)

#None
my_none = None

x=print('')
print(x)

#Truth

#0   ->False
#'a' ->True
#''  ->False
#None->False

print(bool(0+0j))
print(bool(0.0))
