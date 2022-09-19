"""stack implementation using array."""

def push(data, stack_pointer):
    my_stack.append(data)
    stack_pointer += 1 
    return stack_pointer
    
def pop(stack_pointer):
    my_stack.pop()
    stack_pointer -= 1
    return stack_pointer
    
def display(stack_pointer):
    print(my_stack)
    if len(my_stack) == 0:
        print("no. of elements:", 0)
    else:
        print("no. of elements:", stack_pointer)

my_stack = []
stack_pointer = 0
display(stack_pointer)
stack_pointer = push(0, stack_pointer)
stack_pointer = push(1, stack_pointer)
stack_pointer = push(2, stack_pointer)
display(stack_pointer)
stack_pointer = pop(stack_pointer)
display(stack_pointer)