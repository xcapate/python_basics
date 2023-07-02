import uuid

def hello_decorator(func):
    def inner1(*args, **kwargs): 
        transaction_id=uuid.uuid1()
        print("before Execution") 
        print("args: " + str(args)) 
        print("kwargs: " + str(kwargs)) 

        kwargs.update({"transaction_id": transaction_id})
          
        # getting the returned value 
        returned_value = func(*args, **kwargs) 
        print("after Execution") 
          
        # returning the value to the original frame 
        return returned_value 
          
    return inner1 
  
  
# adding decorator to the function 
@hello_decorator
def sum_two_numbers(a, b, **kwargs): 
    print("Inside the function: " + str(kwargs)) 
    return a + b

result = sum_two_numbers(1, 2)
print("Result: " + str(result))