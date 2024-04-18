def watch(input_brand):
    return input_brand
print(watch("quartz")) #quartz
def ds(input_brand):
    return input_brand + 5
print(ds(10)) #15

def ds(input_brand):
    return input_brand + 'string'
print(ds('quartz')) #quartzstring


def ds(input_brand):
    return input_brand + 5

try:
    ds("quartz")
except:
     print("string+int are not concadenate") #string+int are not concadenate 

'''output
quartz
15
quartzstring
string+int are not concadenate
'''


class calculation:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num1 + self.num2 #additon 5
    def sub(self):
        return self.num1 -self.num2 #subtraction 3
    def multi(self):
        return self.num1*self.num2 #multiply 24
    def div(self):
        return self.num1/self.num2 #divide 1.5555555555


perform=calculation(15,2)
print("addition",perform.add())
print("subtraction",perform.sub())
print("multiplication",perform.multi())
print("division",perform.div())
'''
output
addition 5
subtraction 3
multiplication 24
division 1.5555555555
'''

def watch(input_brand):
    return input_brand + 5

try:
    watch("quartz")
except (ValueError,TypeError):
    print('not clear')

    """ OUTPUT :
    not clear"""




def Email(name,type,modal,colour,size):
    
    print("Name is", name)
    print("type is ", type)
    print("modal is ",modal)
    print("colour is ",colour)
    print("And size is ",size)
# you will get correct output because argument is given in order
print("case-1:")
Email("stylishone","quartz","new","black",12)
"""
Name is stylishone
type is quartz
modal is new
colour is black
And size is 12
"""

def bodmas(val1,val2):
    return val1-val2
val1,val2=50,20
result=bodmas(val1,val2)
print(result) #output :30

#defining car class
class car():
    #args receives unlimited no. of arguments as an array
    def __init__(self, *args):
        #access args index like array does
        self.type = args[0]
        self.color =args[1]
#creating objects of car class
tesla = car('normal','red') 
mahindra = car('smart','blue')
honda = car('self-driving','black')
#print a type and color of a car
print(tesla.color)
print(mahindra.type)
'''
output:
red
smart'''
#define pencil class
class pencil():
    #args receives unlimited no.of arguments as array
    def __init__(self,**apsara):
        #access args index like array does
        self.type= apsara['y']
        self.color= apsara['c']

#creating objects of pencil class
doms = pencil(y='branded_pencil',c='black')
nataraj = pencil(y='normal_pencil',c='brown')
camlin = pencil(y='color_pencil',c='all')


   #printing a color and type of a pencil
print(doms.color)
print(camlin.type)
'''
output:
black
color_pencil'''
