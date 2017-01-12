def main():
    global varglob
    varglob = 10
    printer()

def printer():
    varglob +=1#NOT ALLOWED
    print(varglob)
if __name__=='__main__':
    main()