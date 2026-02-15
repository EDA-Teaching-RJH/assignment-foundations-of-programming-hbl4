ValidRank = ["Ensign", "Lieutenant Junior Grade", "Lieutenant", "Lieutenant Commander", "Commander", "Captain", "Rear Admiral", "Vice Admiral", "Admiral", "Fleet Admiral"]
ValidDivision = ["Command", "Operations", "Sciences"]

def main():
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

def init_database():
    names = ["James T. Kirk", "Spock","Leonard McCoy","Hikaru Sulu","Nyota Uhura"]
    ranks = ["Captain", "Commander","Lieutenant Commander","Lieutenant","Lieutenant"]
    divs =  ["Command", "Sciences","Sciences","Operations","Operations"]
    ids = ["SC-937-0176-CEC","S-179-276-SP","MB-228-727","S-334-165","U-238-470"]
    return names, ranks, divs, ids

def display_menu(Name):
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


def add_member(names, ranks, divs, ids):
    print ("Welcome to option, Add Mmeber please enter your name, rank, division and id ")

         
    




    names.append(names)
    ranks.append(ranks)
    divs.append(divs)
    ids.append(ids)

    
def remove_member(names, ranks, divs, ids):
    pass
def update_rank(names, ranks, ids):
    pass
def display_roster(names, ranks, divs, ids):
    pass
def search_crew(names, ranks, divs, ids):
    pass
def filter_by_division(names, divs):
    pass
def calculate_payroll(ranks):
    pass
def count_officers(ranks):
    pass

main()
    