



value = 1

def recursive(v):
    value += 1
    print("from recursive. Value is: ", value)
    if v <= 10:
        recursive(v)
    
recursive(value)