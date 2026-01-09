from pyscript import display, document 

def club_one(o):
    document.getElementById("clubs").innerHTML = "" 
    art_club = {
        'Name': 'Art Club',
        'Description': 'A club for students interested in visual arts.',
        'Meeting Time': 'Every Friday at 2 PM',
        'Location': 'Room 101',
        'Advisor': 'Ms. Smith',
        'Number of Members': '25',
        'Category':'Non-academic',
    }  

    display(art_club, target = "clubs")

def club_two(t):
    document.getElementById("clubs").innerHTML = "" 
    photography_club = {
        'Name': 'Photography Club',
        'Description': 'A club for students who are interested to see thing in the lense of a camera.',
        'Meeting Time': 'Every Monday at 2 PM',
        'Location': 'Room 207',
        'Advisor': 'Mr. Jones',
        'Number of Members': '17',
        'Category':'Non-academic',
    }  

    display(photography_club, target = "clubs")

def club_three(h):
    document.getElementById("clubs").innerHTML = "" 
    drama_club = {
        'Name': 'Drama Club',
        'Description': 'A club for students interested in visual arts.',
        'Meeting Time': 'Every Thursday at 2 PM',
        'Location': 'Room 303',
        'Advisor': 'Ms. Harper',
        'Number of Members': '30',
        'Category':'Non-academic',
    }  

    display(drama_club, target = "clubs")
