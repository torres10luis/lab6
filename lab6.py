import random

def main():
    dict_arr = ["a", "b", "c"]
    dict1 = {
        "a": "Alpha",
        "b": "Bravo",
        "c": "Cat"
    }
    
    infile = "dictionary.txt"
    file1 = None
    print("random: "), random.choice(dict_arr)
    random_choice = random.choice(dict_arr)
    rand_int = random.randint(0,3)
    while True:
        try:
            file1 = open(infile, 'r')
        except FileExistsError as e:
            print("_________FileExistError e: ", e)
            file1 = open(infile, 'w')
        try:
            keys = dict1.keys()
            script = ", ".join(keys)
            first = script[0:-3]
            last = script[-3:-1]
            print(first, "last", last)
            user_input = input('enter either ' + first + " or " + last + " : ")
            print(dict1[user_input])
            break
        except KeyError as e:
            print("Unacceptable there are errors...", e)
            new_val = input("enter a value for:  " + user_input + " ")
            dict1[user_input] = new_val
        finally:
            for i in dict1:
                print(i)
                file1.writelines(i)
            file1.close()
            #pass            
main()



""" 
            user_input = input("enter either " + script + ": ")
            keys = dict1.keys()
            last = keys[-1]
            script = ", ".join(keys)
            script = script + " or ", last """