"""
Integration Project
Last updated 2021-04-17
Written with I-F-M format

This program is intended to be an assistant to the Savant-Class of space
shuttles in Kerbal Space Program.
It contains information about the shuttles and in future versions, will
contain a launch checklist for each.

Completed with assistance of the information on
https://www.w3schools.com/python/default.asp and from built-in PyCharm
quick fix tools.
"""
__author__ = "Bradley Walby"

# INITIALIZATIONS--------------------------------------------------------------

loop_counter = 0

# Commented shuttle/rocket line means construction isn't complete yet

shuttle_information_order = ["Weight", "Attachment Style", "Delta-V Empty",
                             "ISP", "Max. Pay. Cap.«!»",
                             "Rec. Pay. Cap.",
                             "Range", "Rendezvous Attempts", "Landing Delta-V"]
shuttle_database = ["Abundant", "Allegiant", "Vigilant"]

shuttle_Abundant_information = [39725, "Docking Port Sr.", 2673, 300,
                                "Awaiting Calculation", 100000,
                                "Low Kerbin Orbit", 0, 0]
shuttle_Allegiant_information = [5535, "Docking Port", 606, 300,
                                 "Awaiting Calculation", 0, "Low Kerbin Orbit",
                                 0, 0]
# shuttle_Reliant_information = []
# shuttle_Triumphant_information = []
# shuttle_Valiant_information = []
shuttle_Vigilant_information = [14052, "Vertical Sepatrons", 1875, 300,
                                "Awaiting Calculation", 16000,
                                "Med Kerbin Orbit", 0, 0]

# Rocket information array order- {Weight, Attachment Style, Delta-V, Designed
#                                  Staging Style}
# Rocket compatibility lists shuttles that the rocket can be attached to
rocket_information_order = ["Weight", "Attachment Style", "Delta-V",
                            "Designed Staging Style"]
rocket_database = []
rocket_Commander_information = [53744, "Docking Port Sr.", 3573, "Onion"]
rocket_Commander_compatibility = ["Abundant"]
# rocket_Explorer_information = []
# rocket_Explorer_compatibility = []
# rocket_Frontier_information = []
# rocket_Frontier_compatibility = []
# rocket_Messenger_information = []
# rocket_Messenger_compatibility = []
# rocket_Trident_information = []
# rocket_Trident_compatibility = []

shuttle_variables = [shuttle_Abundant_information,
                     shuttle_Allegiant_information,
                     shuttle_Vigilant_information]
rocket_variables = [rocket_Commander_information,
                    rocket_Commander_compatibility]


# FUNCTIONS--------------------------------------------------------------------

def floor_divide(int_in):
    """
    Takes a float input and floor-divides that input into the next integer down
    Effectively rounds down the input.
    :param int_in: The float input
    :return: The floor-divided (rounded down) result
    """
    return int(int_in // 1)


def calculate_max_payload(weight_empty, delta_v_empty, isp):
    """
    Calculates the maximum payload that a shuttle can carry. This is different
    from the recommended payload.
    :param weight_empty: Weight of the shuttle w/ fuel, w/o cargo
    :param delta_v_empty: ΔV of the shuttle w/o cargo. This information is
                          provided by the game.
    :param isp: Specific impulse of the engines
    :return: A floor-divided integer of the maximum payload (in kg) of the
             shuttle
    """
    # equation
    max_payload = (((delta_v_empty - 600) * 2.718 * weight_empty) / (
                9.8 * isp)) + weight_empty
    # return the result
    return floor_divide(max_payload)


def longest_string_format(array, sep_factor):
    """
    For printing the information of shuttles/rockets, this function determines
    the longest string in a list to make
    sure all punctuation/other formatting is in-line
    :param array: A list containing strings (example shuttle_information_order)
    :param sep_factor: How many spaces should be at the end of the longest
                       string before the punctuation
    :return: Returns the integer of the length of the longest string + the
             separation factor
    """
    # defining empty string that will be used as storage
    longest_string = ""
    # for-loop to find the longest string in the provided array
    for j in range(len(array)):
        item = str(array[j])
        if len(item) > len(longest_string):
            longest_string = item
    # return the longest string in the array
    return str(len(longest_string) + sep_factor)


def maneuvering(array):  # Calculates maneuverability
    """
    Calculates how many average maneuvers can be performed by a shuttle before
    it runs out of fuel
    :param array: List containing the information of the shuttle being
    referenced
    """
    array[7] = (array[2] // 300) - 1
    # How many average maneuvers can be performed (assuming ΔV of 300 m/s)

    array[8] = (array[2] % 300) + 300
    # How much delta-v is left over when max. rendezvous are achieved


def main():
    """
    The main code of the program
    """
    # iterate shuttles to calculate remaining values
    global loop_counter
    for x in range(len(shuttle_database)):
        # Calculates all unlisted/zeroed values for shuttles for shuttles
        (shuttle_variables[x])[4] = calculate_max_payload(
            (shuttle_variables[x])[0], (shuttle_variables[x])[2],
            (shuttle_variables[x])[3])
        maneuvering(shuttle_variables[x])

    # begin main program
    print("KSP Shuttle Checklist for Savant-Class Shuttles")

    run_condition = True
    while run_condition:
        info_selection = input("shuttle, rocket, or exit- ")
        loop_counter += 1

        if info_selection == "shuttle":
            print("Shuttle information-")

            # print information about Abundant
            print("\nAbundant information-")
            for j in range(len(shuttle_information_order)):
                print(format(shuttle_information_order[j],
                             longest_string_format(shuttle_information_order,
                                                   3)),
                      format(str(shuttle_Abundant_information[j]),
                             longest_string_format(
                                 shuttle_Abundant_information, 1)) + "||",
                      sep='|', end='|\n')

            # print information about Allegiant
            print("\nAllegiant information-")
            for j in range(len(shuttle_information_order)):
                print(format(shuttle_information_order[j],
                             longest_string_format(shuttle_information_order,
                                                   3)),
                      format(str(shuttle_Allegiant_information[j]),
                             longest_string_format(
                                 shuttle_Allegiant_information, 1)) + "||",
                      sep='|', end='|\n')

            # print information about Vigilant
            print("\nVigilant information-")
            for j in range(len(shuttle_information_order)):
                print(format(shuttle_information_order[j],
                             longest_string_format(shuttle_information_order,
                                                   3)),
                      format(str(shuttle_Vigilant_information[j]),
                             longest_string_format(
                                 shuttle_Vigilant_information, 1)) + "||",
                      sep='|', end='|\n')

            print(
                "\n«!» Max payload goes against protocol L-27. Confirm with "
                "Mission Control before launching with "
                "anything heavier than recommended payload\n")

        elif info_selection == "rocket":
            print("\nRocket information-")

            # print information about Commander
            print("\nCommander information-")
            for j in range(len(rocket_information_order)):
                print(format(rocket_information_order[j],
                             longest_string_format(rocket_information_order,
                                                   3)),
                      format(str(rocket_Commander_information[j]),
                             longest_string_format(
                                 rocket_Commander_information, 1)) + "||",
                      sep='|', end="|\n")
            print("\n")

        elif info_selection == "exit":
            run_condition = False
            print("Fun fact- You looped through this program", loop_counter,
                  "times. Goodbye.")

        else:
            print("Selection not recognized, please try again")
    # Note to self- I made the variable names of the shuttles/rockets
    # iterate-able, but I don't know how to iterate this
    # information printing yet


# MAIN CODE--------------------------------------------------------------------
main()
