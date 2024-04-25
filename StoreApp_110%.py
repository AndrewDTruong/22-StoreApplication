from appJar import gui
import pandas

storeitemsdf = pandas.read_csv("storeitems.csv")
accessorieslist = list(storeitemsdf.Accessories)
outerwearlist = list(storeitemsdf.Outerwear)
sockslist = list(storeitemsdf.Socks)


def user_greeting(store_greeting, sentinel, input_one, input_two):
    userinput = ' '
    user = sentinel
    print(store_greeting)
    while user == sentinel:
        userinput = input(input_one)
        user = input(input_two)
    if userinput == "Accessories":
        print()
        accessories("Welcome to the Accessories section of our store! We currently have these items in stock:"
                    , accessorieslist
                    , "Please select which accessories to buy or exit. ")
    elif userinput == "Outerwear":
        print()
        outerwear("Welcome to the Outerwear section of our store! We currently have these items in stock:"
                  , outerwearlist
                  , "Please select which outerwear to buy or exit. ")
    elif userinput == "Socks":
        print()
        socks("Welcome to the Socks section of our store! We currently have these items in stock:"
              , sockslist
              , "Please select which socks to buy or exit. ")
    else:
        print()
        print('Unfortunately, we do not have those items in our store. We hope to see you again soon!')


def accessories(intro, item_selection, chosen_item):
    print(intro)
    for item in item_selection:
        print(item)
    accessories_pick = input(chosen_item)
    if accessories_pick == "exit":
        print("Goodbye, have a nice day!")
    elif accessories_pick == "Hats":
        c_statement("Hats", 25, "Thank you for purchasing our Hats!")
    elif accessories_pick == "Handbags":
        c_statement("Handbags", 15, "Thank you for purchasing our Handbags!")
    else:
        c_statement("Watches", 17, "Thank you for purchasing our Watches!")


def outerwear(intro, item_selection, chosen_item):
    print(intro)
    for item in item_selection:
        print(item)
    outerwear_pick = input(chosen_item)
    if outerwear_pick == "exit":
        print("Goodbye, have a nice day!")
    elif outerwear_pick == "Jacket":
        c_statement("Jacket", 25, "Thank you for purchasing our Jacket!")
    elif outerwear_pick == "Hoodie":
        c_statement("Hoodie", 15, "Thank you for purchasing our Hoodie!")
    else:
        c_statement("Cardigans", 17, "Thank you for purchasing our Cardigans!")


def socks(intro, item_selection, chosen_item):
    print(intro)
    for item in item_selection:
        print(item)
    socks_pick = input(chosen_item)
    if socks_pick == "exit":
        print("Goodbye, have a nice day!")
    elif socks_pick == "Short":
        c_statement("Short", 25, "Thank you for purchasing our Short Socks!")
    elif socks_pick == "Long":
        c_statement("Long", 15, "Thank you for purchasing our Long Socks!")
    else:
        c_statement("Dress", 17, "Thank you for purchasing our Dress Socks!")


def c_statement(selected_item, price, closing):
    print()
    print("The price of the item you chose", selected_item + ", is $" + str(price))
    extra = input("Would you like to pick another item (y/n)? ")
    if extra == "y":
        user_greeting("Fantastic!", "n",
                      "Which section of our store would you like to browse (Accessories, Outerwear, Socks)? "
                      , "Ready to browse (y/n)? ")
    else:
        for l in closing:
            print(l, end="")


def notice():
    print("Our next selection of items will be coming to the store soon.")
    print()


def press(btn):
    if btn == "Exit":
        app.stop()
    elif btn == "Greeting":
        user_greeting("Welcome to the Fashionable Store", "n"
                      , "Which section of our store would you like to browse (Accessories, Outerwear, Socks)? "
                      , "Are you ready to browse our selections (y/n)? ")
    elif btn == "Accessories":
        accessories("Welcome to the Accessories section of our store! We currently have these items in stock:"
                    , accessorieslist
                    , "Please select which accessories to buy or exit. ")
    elif btn == "Outerwear":
        outerwear("Welcome to the Outerwear section of our store! We currently have these items in stock:"
                  , outerwearlist
                  , "Please select which outerwear to buy or exit. ")
    elif btn == "Socks":
        socks("Welcome to the Socks section of our store! We currently have these items in stock:"
              , sockslist
              , "Please select which socks to buy or exit. ")
    elif btn == "Notice":
        notice()
    else:
        print('Please choose an available option')


app = gui("Main Menu", "500x500")

app.addLabel("title", "Welcome to the Fashionable Store Team's Main Menu")
app.setLabelBg("title", "orange")

app.addImage("decor", "k.gif")
app.setFont(18)

app.addButton("Greeting", press)
app.addButton("Accessories", press)
app.addButton("Outerwear", press)
app.addButton("Socks", press)
app.addButton("Notice", press)
app.addButton("Exit", press)
app.go()
