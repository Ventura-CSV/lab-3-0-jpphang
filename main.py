def main():
    ##################################################
    # Comlete your code here
    ##################################################
    """
    Make your code here
    """
    
    x = int(input("Enter an interger:"))
    
    if x % 2 == 1: 
        result = 1
    
    elif x % 2 == 0:
        result = 0

    print(f"The result is {result}")
  

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
