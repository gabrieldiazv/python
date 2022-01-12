class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def say_hello(self):
        print('hello, my name is {} and i am {} years old'.format(self.name, self.age))
        

if __name__ == '__main__':
    person = Person('gabriel',22)
    print(person.name) # ? gabriel
    print(person.age) # ? 22 
    person.say_hello() # ? hello, my name is gabriel and i am 22 years old