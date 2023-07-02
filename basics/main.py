#decorator function

def decorator_func(original_func):
    def wrapper_func(*args,**kwargs):
        print("Printed before executing original_function " + original_func.__name__)
        return original_func(*args,**kwargs)
    return wrapper_func

#decorator extra argument function
def prefix_decorator(prefix):
    def decorator_func(original_func):
        def wrapper_func(*args,**kwargs):
            print(prefix + " Printed before executing original_function " + original_func.__name__)
            return original_func(*args,**kwargs)
        return wrapper_func
    return decorator_func

@decorator_func
def setName(name,last_name):
    return name + " " + last_name

fullname=setName("John","Doe")
print(fullname)

@prefix_decorator('_CR')
def add_prefix(text):
    print(text)

add_prefix("This is a test")


#Decorator class

class decorator_class(object):
    def __init__(self,original_func):
        self.original_func=original_func

    def __call__(self,*args,**kwargs):
        print("Printed before original funcion is called ")
        return self.original_func(*args,**kwargs)



    
@decorator_class
def display_info(user,action):
    tag='-'
    message = '{2} User {0} has {1} {2}'.format(user,action,tag)
    print(message)


@decorator_func
def display_dic(dict):
    msg= '{name} likes to {action}'.format(**dict)
    print(msg)

display_info("Annon","Logged In")


dict={'name':'Michael Jordan','action':'Slams'}

display_dic(dict)


pi = 3.14159265

affirmation='Pi is equal to {:.2f}'.format(pi)

print(affirmation)


import datetime

my_date= datetime.datetime(2019,5,20,12,21,0)

sentence= '{:%B,%d,%Y}'.format(my_date)
print(sentence)


bad_var_2="1"
try:
    f= open('testfile.csv')
    var = bad_var
except FileNotFoundError:
    print('File doesn\'t exit')
except Exception:
    print('Undefined variable...')
else:
    content=f.read()
    print(content)
finally:
    print("Closing the file")
    try:
        f.close()
    except NameError:
        print("No need to close the file...")


first_name='Corey'
last_name='Schaffer'

#fullname='The user name is {first_name} {last_name}'

print("\r\n--------------------Setters and Getters-----------------------\r\n\r\n")

class Employee:

    def __init__(self,first,last):
        self.first=first
        self.last=last
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    @fullname.setter
    def fullname(self,thename):
        self.first,self.last=thename.split(' ')
    
    @fullname.deleter
    def fullname(self):
        print("User data has been deleted")
        self.first=None
        self.last=None

emp1= Employee('John','Doe')

emp1.first='Jim'

emp1.fullname="Johnny Bravo"

print(emp1.first)
print(emp1.email)
print(emp1.fullname)

del emp1.fullname

print(emp1.last)


class User:

    def __init__(self,username,email,first_name,last_name):
        self.__username=username
        self.__email=email
        self.__first_name=first_name
        self.__last_name=last_name

    def __str__(self):
        return 'User {} <{}> Name: {} {}'.format(self.__username,self.__email,self.__first_name,self.__last_name)
    



print('\r\n\r\n-----------Context managers--------------\r\n\r\n')


class Open_File():
    def __init__(self,filename,mode):
        self.filename=filename
        self.mode=mode

    def __enter__(self):
        self.file=open(self.filename,self.mode)
        return self.file

    def __exit__(self,exc_type,exc_val,traceback):
        self.file.close()
        print("Releasing the file... ")
        if self.file.closed:
            print("ok")


with Open_File('testfile.csv','a') as f:
    newrow="'Manny','Paquiao'"
    f.write(newrow)

from contextlib import contextmanager
@contextmanager
def OpenFile(file,mode):
    f=open(file,mode)
    yield f
    f.close()

with OpenFile('testfile.csv','a') as f:
    f.write("'Tom','Sawyer'")
if f.closed:
    print("The file has been closed!")




import os
@contextmanager
def change_dir(destination):
    try:
        cwd=os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

def test_context_manager(path):
    with change_dir(path):
        print(os.listdir())



test_context_manager('/usr/bin')



def subtract_rec(num):
    num=num-1
    print(num)
    if(num>0):
        subtract_rec(num)

subtract_rec(100)


class animal:
    def __new__(self,*args):
        print("New instance is creating")
    def __init__(self,name):
        print("Init")
        self.__name=name
        print("Init" +  self.__name)
    def __enter__(self):
        print("Object created")
    def __exit__(self):
        print("Terminating the object")
    def showName(self):
        print(self.__name)



#dog = animal("dog")
#dog.showName()




MAPPING_TAGS={
    "Customer Name":"Account",
    "UniqueID":"Support Request Number",
    "RequestType":"Request Type",
    "Region":"Customer Region",
    "Country":"Customer Location Country",
    "Category":"Deal Category",
    "Value":"Total Opportunity Value in USD",
    "Language":"What language applies",
    "PublicSector":"Public Sector",
    "Stage":"Sales Stage",
    "OpportunityID":"Opportunity ID",
    "Industry":"Industry Segment",
    "BusinessUser":"Opportunity Owner Name",
    "Team":"Requestor Name",
    "NewMilestoneDate":"Response By Date",
    "CreationDate":"Request Date",
    "Background":"Request Comments",
    "RequestComments":"Request Title",
    "RequestedLawyers":"Request Comments",
    "UpdateName":"Agreement Name",
    "CreatedBY":"Counterparty Team Leader"
}

mapped_tags=[]

agreement_tags=[
    {'matching_id':'Customer Region','value':'xxxx'},
    {'matching_id':'Turbo','value':'yyyy'}
    ]


for mtag in MAPPING_TAGS:
    #LOOK FOR TAG IN 
    for ctag in agreement_tags:
      if MAPPING_TAGS[mtag]== ctag['matching_id']:
          mapped_tags.append({mtag:ctag['value']})


print(mapped_tags)


text = input("Dime algo!\r\n")
if text == "hola":
    print("Hola humano")
elif text == "adios":
    print("Hasta pronto")
else:
    print("Mis respuestas son limitadas")