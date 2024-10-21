#Initials Joseph Rydberg 10/21/2024


def initials_generator(personsName):

    personsInitials = ""
    #    Add your logic here
    nameList = personsName.split()

    for name in nameList:
        personsInitials += name[0].upper() + "."

    return personsInitials.strip()

personsName = input('Enter the users first, middle, and last name')

initials = initials_generator(personsName)

print(initials)