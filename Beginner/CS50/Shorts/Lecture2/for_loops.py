## Initial Version

#def main():
#    print(write_letter("Mario", "Princess Peach"))
#    print(write_letter("Luigi", "Princess Peach"))
#    print(write_letter("Daisy", "Princess Peach"))
#    print(write_letter("Yoshi", "Princess Peach"))

#def write_letter(reciever, sender):
#    return f"""
#    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#        Dear {reciever},

#        You are cordially invited to a ball at
#        Peach's Castle this evening, 7:00 PM.set

#        Sincerely,
#        {sender}
#    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#    """

#main()

## Updates Version

#def main():
#    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
#    for i in range(len(names)):
#        print(write_letter(names[i], "Princess Peach"))

#def write_letter(reciever, sender):
#    return f"""
#    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#        Dear {reciever},

#        You are cordially invited to a ball at
#        Peach's Castle this evening, 7:00 PM.set

#        Sincerely,
#        {sender}
#    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#    """

#main()

## More readible Version

def main():
    names = ["Mario", "Luigi", "Daisy", "Yoshi"]
    for name in names:
        print(write_letter(name, "Princess Peach"))

def write_letter(reciever, sender):
    return f"""
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        Dear {reciever},

        You are cordially invited to a ball at
        Peach's Castle this evening, 7:00 PM.set

        Sincerely,
        {sender}
    +~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    """

main()