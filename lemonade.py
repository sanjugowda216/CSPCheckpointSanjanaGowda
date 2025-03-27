# The Purpose of my program is for users to order lemonade from a lemonade stand.
# My program lets a user customize their lemonade order

print("What a beautiful and sunny day! \nWelcome to Sanjana's Lemonade Stand!\n------------------")
name = input("What is your name: ")

#name parameter
def order(name):
    flavors = ['original','strawberry','peach','rasberry'] #list of flavor options
    #printing a visual of the menu options
    for i in flavors:
        print(flavors.index(i)+1,i)

    print("Hello "+name +"! What would you like to order?") 
    myFlavor = input("Please enter a number from 1-4: ")
    
    #order response checking if input is a digit
    if myFlavor.isdigit():
        myFlavor = int(myFlavor)
        if myFlavor == 1:
            print("You ordered a "+flavors[0]+" lemonade!")
        elif myFlavor == 2:
            print("You ordered a "+flavors[1]+" lemonade!")
        elif myFlavor == 3:
            print("You ordered a "+flavors[2]+" lemonade!")
        elif myFlavor == 4:
            print("You ordered a "+flavors[3]+" lemonade!")
        else:
            print("Have a great day "+name+"!!!")           
    else:
        order(name)
 
order(name)