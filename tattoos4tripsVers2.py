from random import randint

hobbiesDict = {1: "hiking", 2: "art", 3: "cooking", 4: "swimming", 5: "gardening", 6: "boating", 7: "photography",
               8: "people-watching", 9: "reading", 10: "cultural exploration"}

destinationMods = {"Paris": 0, "Bahamas": 0, "Alaska": 0, "Switzerland": 0}

# the dictionary that contains information of which hobbies are related to which destinations
destinationHobbies = {'Paris': ["art", "cooking", "people-watching", "cultural exploration"],
                      'Bahamas': ["swimming", "boating", "people-watching", "reading"],
                      'Alaska': ['boating', "hiking", "photography"],
                      'Switzerland': ["hiking", "gardening", "photography", "cultural exploration"]}

destinationTags = {'Paris': ['exploring', 'love', 'urban', 'ground'], 'Bahamas': ['lazy', 'urban', 'h2o', 'ground'],
                   'Alaska': ['exploring', 'rural', 'h2o', 'sky'],
                   'Switzerland': ['adventurous', 'rural', 'love', 'sky']}


tattoo1 = [1, "mountains or a cliff side "]
tattoo2 = [2, "ski goggles reflecting a natural landscape"]
tattoo3 = [3, "a compass based design (north, east, south, west)"]
tattoo4 = [4, "a singular or cluster of small trees"]
tattoo5 = [5, "any quote from a fictional character"]
tattoo6 = [6, "a tattoo of a gummy bear or similar shaped figure"]
tattoo7 = [7, "any sort of snowflake (entricate or minimalistic)"]
tattoo8 = [8, "a heart with an expression, ex - :)"]
tattoo9 = [9, "an ocean wave tattoo"]
tattoo10 = [10, "a sleigh (like the ones santa uses!)"]
tattoo11 = [11, "a dreamcatcher"]
tattoo12 = [12, "a trail or bubble of hearts"]
tattoo13 = [13, "a city skyline"]
tattoo14 = [14, "a record player or tape"]
tattoo15 = [15, "the spotify barcode for a meaningful song or playlist"]
tattoo16 = [16, "any design of leaf"]
tattoo17 = [17, "a line of code..."]
tattoo18 = [18, "mountain skyline"]
tattoo19 = [19, "seeing the reflection of the sky through your eye"]
tattoo20 = [20, "a singular or cluster of flowers"]
tattoo21 = [21, "a telescope and a couple stars"]
tattoo22 = [22, "hands, in any arrangement"]
tattoo23 = [23, "a vine, any length, going down your arm (or anywhere else!)"]
tattoo24 = [24, "solar system or arangement of planets"]

# determines the adventurous scale of the vacation. would you like to go somewhere extreme? 'chillax'?
adventureTattoo = {"lazy": [tattoo5, tattoo6], "exploring": [tattoo3, tattoo4], "adventurous": [tattoo1, tattoo2]}
adventureTattooCountOg = {"lazy": 0, "exploring": 0, "adventurous": 0}
adventureTattooWin = ""

# helps the program decide between something with water (people who are fond of beaches and "California vibes" are
# more likely to get tattoos of that style) and something more heartfelt and dreamy (similar to vibes that a more
# lovey person/tattoo would give off)

lovingLTattoo = {'h20': [tattoo7, tattoo9, tattoo10], 'love': [tattoo8, tattoo11, tattoo12]}
lovingLTattooCountOg = {'h20': 0, 'love': 0}
lovingLTattooWin = ""
# do get it? because ice (tattoo designs) are cold and theres wholesome hearts (tattoo designs) so an icy heart vs a
# warm heart; they're at different loving levels! :0


# determines whether the destination should be more out in the countryside or more social, in the heart of the area
areaTattoo = {"rural": [tattoo14, tattoo16, tattoo18], "urban": [tattoo13, tattoo15, tattoo17]}
areaTattooCountOg = {"rural": 0, "urban": 0}
areaTattooWin = ""

# determines whether skies and astrology are more meaningful or Earth and flowers are (earthy, ground vibes)
spaceTattoo = {"sky": [tattoo19, tattoo20, tattoo21], "ground": [tattoo22, tattoo23, tattoo24]}
spaceTattooCountOg = {"sky": 0, "ground": 0}
spaceTattooWin = ""  # whichever one has the most points at the end is assigned to this variable

tattoosOrg = {"adventure": "", "lovingL": "", 'area': "", "space": ""}


def intro():
    print("Hello! Welcome to Tattoos4Trips. This is a demo of a tattoo based vacation planner.")
    print(
        "Use this to find your next vacation destination by choosing the tattoos you feel resonates with you or who "
        "you want to be!")

    input("\n(press any key to continue)")
    input("\n \n \nare you ready to begin? \n \n(press any key to continue)")


# Uses any hobbies user may have to optimize results
def hobbyChecker():
    hobbyCheck = input("do you have any hobbies you enjoy doing? \n-of which could possibly be factored into choosing "
                       "your next destination \n \n(yes or no)\n")

    if hobbyCheck == "yes":
        hobbies = input(
            "if any of the following are hobbies you enjoy, go ahead and type their number key below:\n(please "
            "separate them with spaces)\n" + str(
                ["{key} - {hobby}".format(key=key, hobby=values) for key, values in hobbiesDict.items()]) + "\n")

        if len(hobbies) != 0:
            hobbiesList = []
            hobbiesList = hobbies.split(" ")[:-1]

            for hobbyKey in hobbiesList:
                for dKey, dValue in destinationHobbies.items():
                    if hobbiesDict[int(hobbyKey)] in dValue:
                        destinationMods[dKey] += 1

    return destinationMods


# collects information about the users' tattoo preferences, first stage of the quiz

def countTattoo(Tattoo, TattooCount):
    three = False
    while not three:
        for Key, Value in Tattoo.items():
            print(str(["{key} - {tattoo}".format(key=Tat[0], tattoo=Tat[1]) for Tat in Value]) + "\n")
              

        topTatsRaw = input("\nwhich three would you want the most?\n(separate using spaces)\n") + " "

        # restores the original value of the variables, those variables represent the users' top 3 choices from Tattoo
        # (input) division of tattoos
        topTats = []
        topTats = topTatsRaw.split(" ")[:3]

        if len(topTats) == 3:
            three = True
        else:
            print("please try again, you did not properly select three designs!")

    # goes through each of the users' choices and gives points to the category the tattoos were assigned to,
    # whichever category (preference) has the most points, is the one that matches the user most
    for i in topTats:
        for key, value in Tattoo.items():
            print(value[0][0])

            if i in str(value[0][0]):
                TattooCount[key] += 1
    
    return TattooCount

    # the function which determines which pair has the most points



def countTag(TattooCount):
    # keeps track of the current highest points and which tag has it
    highest = ["none", 0]
    # is used when theres ties
    tieCount = [[], 0, 0]

    for key, value in TattooCount.items():
        # if the new value has more points than the previous highest, it replaces it
        if value > highest[1]:
            highest[0] = key
            highest[1] = value

            # also updates the tie count in case the next case is a tie (if its lower it will not update at all,
            # if its higher the new values will be replace it)
            tieCount[0] = [key]
            tieCount[2] = 1

        # if there is a tie, update the list
        if value == highest[1]:
            tieCount[0].append(key)
            tieCount[1] = value
            tieCount[2] += 1

    # chooses a random top category if after the entire loop there is a tie (no single highest category)
    if tieCount[1] > 1:
        num = randint(0, tieCount[2] - 1)
        return tieCount[0][num], tieCount[1]

    return highest



def countryQuiz():
    input("Now lets start the cool stuff (actual tattoo quiz), yeah?\n")

    # 1 - adventure level
    adventureTattooCount = {}
    adventureTattooCount = countTattoo(adventureTattoo, adventureTattooCountOg)

    # 2 - loving level

    lovingLTattooCount = {}
    lovingLTattooCount = countTattoo(lovingLTattoo, lovingLTattooCountOg)

    # 3 - area, rural or urban

    areaTattooCount = {}
    areaTattooCount = countTattoo(areaTattoo, areaTattooCountOg)

    # 4 - preference: space or ground

    spaceTattooCount = {}
    spaceTattooCount = countTattoo(spaceTattoo, spaceTattooCountOg)

    print("\n \n")

    # checks which category in each tattoo subdivision is the prominent one (to be used in matching) and saves it
    tattoosOrg["adventure"] = countTag(adventureTattooCount)[0]
    tattoosOrg["lovingL"] = countTag(lovingLTattooCount)[0]
    tattoosOrg['area'] = countTag(areaTattooCount)[0]
    tattoosOrg["space"] = countTag(spaceTattooCount)[0]

    # looping through the dictionary with all the user info (categories they resonate with) and adding points
    # everytime one of their preferences is matched with a tag in one of the destinations. basically checking which
    # destination is the most related to the users' preferences based on the information we got off of the tattoo
    # choices

    for tKey, tValue in tattoosOrg.items():
        for dKey, dValue in destinationTags.items():

            if tValue in dValue:
                # using destinationMods since hobbies are playing in here, their impact will now be implemented
                destinationMods[dKey] += 1

    
    match = countTag(destinationMods)[0]

    print("Based on you quiz results, you should go to " + match + " !")


intro()
hobbyChecker()
countryQuiz()

