def isbalanced(S):
    my_stack = []
    counter = 0
    for symbol in S:
        counter += 1
        if symbol in ['[', '(', '{']:
            my_stack.append(symbol)
            c = counter
        elif symbol in [']', '}', ')']:
            if len(my_stack) == 0:
                #print(my_stack)
                return counter
            curr_symbol = my_stack.pop()
            c -= 1
            if (curr_symbol == '[' and symbol != ']') or (curr_symbol == '(' and symbol != ')') or (curr_symbol == '{' and symbol != '}'):
               
                return counter
    
    if len(my_stack) != 0:
        return (c)
    else:
        return "Success"    

if __name__ == "__main__":
    S = list(input())
    print(isbalanced(S))
