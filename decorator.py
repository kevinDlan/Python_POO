from decorators import addition,multiplication

def operation(opt_type):
    
    def add(n1,n2):
        return n1+n2
    
    def sub(n1,n2):
        return n1-n2
    
    if opt_type == 'add':
        return add
    else:
        return sub



add = operation('add')
sub = operation('sub')
# print(add(10,5),'|',sub(25,10))

# Décorator


@addition
def add(opt,result):
    return f'{opt} gives result as {result}'

@multiplication
def multi(opt,res):
    return f'{opt} gives result as {res}'


print(add(2,3))
print(multi(12,3))
