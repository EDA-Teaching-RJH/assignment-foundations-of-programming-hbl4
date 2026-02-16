#i compltely forogt to commit every time i made a new feature and show the before and after and the time frame between it i have sent you an email about it as well but suspect i sent it too late and i am very very sorry
# you may ask how i did not see the commit features and in all honest im very sleep deprived and just read through what each of the key features and skipped the features and only saw it at the end of the prompt

ValidRank = ["Ensign", "Lieutenant Junior Grade", "Lieutenant", "Lieutenant Commander", "Commander", "Captain", "Rear Admiral", "Vice Admiral", "Admiral", "Fleet Admiral"]
ValidDivision = ["Command", "Operations", "Sciences"]

def main(): # this should have been my commit one , this is where i added the menu and the main fucntion that runs the program and call on the other functions
    names, ranks, divs, ids = init_database()

    Name = input ("Please enter your full name: ")

    while True:
        option = display_menu(Name)
        if option == 1:
            add_member(names, ranks, divs, ids)
        elif option == 2:
            remove_member(names, ranks, divs, ids)
        elif option == 3:
            update_rank(names, ranks, ids)
        elif option == 4:
            display_roster(names, ranks, divs, ids)
        elif option == 5:
            search_crew(names, ranks, divs, ids)
        elif option == 6:
            filter_by_division(names, divs)
        elif option == 7:
            calculate_payroll(ranks)
        elif option == 8:
            count_officers(ranks)
        elif option == 9:
            print ("Thank you for using the menu have a nice day ")
            break 
        else:
            print("That is an invalid option")

def init_database(): # this is the initial database that sotred the premade crew members the names , ranks, divs and ids
    names = ["James T. Kirk", "Spock","Leonard McCoy","Hikaru Sulu","Nyota Uhura"]
    ranks = ["Captain", "Commander","Lieutenant Commander","Lieutenant","Lieutenant"]
    divs =  ["Command", "Sciences","Sciences","Operations","Operations"]
    ids = ["SC-937-0176-CEC","S-179-276-SP","MB-228-727","S-334-165","U-238-470"]
    return names, ranks, divs, ids

def display_menu(Name): # this is the main interface for the user to choose which option they want to use and dictates the options 
    print(f"Welcome {Name}, to your menu please pick an option below")
    print ("Option 1, Add Member ")
    print ("Option 2, Remove Member ")
    print ("Option 3, Update Rank ")
    print ("Option 4, Display Roster ")
    print ("Option 5, Search Crew ") 
    print ("Option 6, Filter by Division ")
    print ("Option 7, Calculate Payroll ")
    print ("Option 8, Count Officers ")
    print ("Option 9, Exit Menu ")
    
    option = int(input("Enter an option number between 1 and 9: "))
    return option


def add_member(names, ranks, divs, ids): # this function allows the user to add a new memebr to the premade data base and checks if id has already been used to ensure uniqueness 
    print ("Welcome to option 1 , Add Mmeber. Please enter your  full name, rank, division and id ")
    name_new = input ("What is your Name?: ")
    Rank_new = input("What is your Rank?: ")
    div_new = input("What is your Division?: ")
    id_new = input("What is your Id?: ")
    if id_new in (ids):
        print("This Id has already been used please use a different one")
        add_member(names, ranks, divs, ids)
    else:
        names.append(name_new)
        ranks.append(Rank_new)
        divs.append(div_new)
        ids.append(id_new)
        print(" New memeber has been created ")

    
def remove_member(names, ranks, divs, ids): # this functions allows the user to remove data from the database by uisng the id as the main identifier of the personnel to remove
    id_remove = input("Enter the id of member to remove: ")
    if id_remove not in ids:
        print("id not found try again")
        return
    else:
        Windex = ids.index(id_remove)
        names.pop(Windex)
        ranks.pop(Windex)
        divs.pop(Windex)
        ids.pop(Windex)
        print("Member has been removed successfully")
        return 

def update_rank(names, ranks, ids): # this function will allow the user to updayte the rank of a crew member and checking that the rank is actually valid
    update_id = input("Enter the id of the member you wish to update: ")
    if update_id not in ids:
        print("id not found try again")
        return
    else:
        Windex = ids.index(update_id)
        new_rank = input("Enter the new rank for this member: ")
        if new_rank not in ValidRank:
            print("Invalid rank")
            update_rank(names, ranks, ids)
        else:
            ranks[Windex] = new_rank
            print("Rank has been updated successfully")

def display_roster(names, ranks, divs, ids):# this function will display the cre that is held withing hte current databadse
    print("The current crew withing the database is: ")
    for x in range(len(names)):
        print(names[x] + " - " + ranks[x] + " - " + divs[x] + " - " + ids[x])
    return

def search_crew(names, ranks, divs, ids):# this allows the user to search for the member through their name and displays all information on them 
    search_name = input("Enter name of crew to find: ")
    if search_name not in names:
        print("member not found try again?")
        return
    else:
        Windex = names.index(search_name)
        print(names[Windex] + " - " + ranks[Windex] + " - " + divs[Windex] + " -" + ids[Windex])
        
def filter_by_division(names, divs): # this function allows user to only see the members that are in a specific division of the fleet 
    div_search = input(" Which division are you looking for ?")
    if div_search not in ValidDivision:
        print("Invalid division try again")
        filter_by_division(names,divs)
    else:
        print("These are the members in the selected division: ")
        for x in range (len(names)):
            if divs[x] == div_search:
                print(names[x] + " - " + divs[x])

def calculate_payroll(ranks): # this function calculates how much each of the rnaks are worth and how much their total cost is 
    TotalPay = 0
    for x in range(len(ranks)):
        if ranks[x] == "Ensign":
            TotalPay += 200
        elif ranks[x] == "Lieutenant Junior Grade":
            TotalPay += 400
        elif ranks[x] == "Lieutenant":
            TotalPay += 600
        elif ranks[x] == "Lieutenant Commander":
            TotalPay += 800
        elif ranks[x] == "commander":
            TotalPay += 1000
        elif ranks[x] == "Captain":
            TotalPay += 1200
        elif ranks[x] == "Rear Admiral":
            TotalPay += 1400
        elif ranks[x] == "Vice Admiral":
            TotalPay += 1600
        elif ranks [x] == "Admiral":
            TotalPay += 1800
        elif ranks[x] == "Fleet Admiral":
            TotalPay += 2000
            print("The total cost of the crew is " + str(TotalPay))


    
def count_officers(ranks):# counts the number of officers in fleet checking rank and representing the number of officers
    count = 0 
    for x in range(len(ranks)):
        if ranks[x] in ValidRank:
            count += 1
            print(" The number of officers in the fleet is " + str(count))

main()
    