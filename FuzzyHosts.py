############################
######## Fuzzy Hosts #######
## Created by Philip Otter #
## Created September 2022 ##
############################

import json
from datetime import datetime


def title():
    print('''
    _______           _______  _______                      _______  _______ _________ ________ 
    (  ____ \|\     /|/ ___   )/ ___   )|\     /|  |\     /|(  ___  )(  ____ \\__   __/(  ____  |
    | (    \/| )   ( |\/   )  |\/   )  |( \   / )  | )   ( || (   ) || (    \/   ) (   | (    \/
    | (__    | |   | |    /   )    /   ) \ (_) /   | (___) || |   | || (_____    | |   | (_____ 
    |  __)   | |   | |   /   /    /   /   \   /    |  ___  || |   | |(_____  )   | |   (_____  )
    | (      | |   | |  /   /    /   /     ) (     | (   ) || |   | |      ) |   | |         ) |
    | )      | (___) | /   (_/\ /   (_/\   | |     | )   ( || (___) |/\____) |   | |   /\____) |
    |/       (_______)(_______/(_______/   \_/     |/     \|(_______)\_______)   )_(   \_______)

                                            by Philip Otter
    ''')


# Handles writing from json data
def jsonFile(date, target, ip, hosts):
    # open our json file and set it to a python dictionary
    with open(target, 'r') as targetFile:
        jData=json.loads(targetFile.read())


    hosts.write("\n# All below entries added courtesy of Fuzzy Hosts on "+date+" <3 \n\n")
    i = int(0)
    while True:
        # Checks for the end of our key values
        try:
            print("\nAdding:  " + jData["results"][i]['host'])
            # Attempts to add the values into /etc/hosts file
            try:
                payload = ip+" "+jData["results"][i]['host']
                print(payload)
                hosts.write(payload + "\n")

            except:
                print("Failed to create payload")
            i = i+1

        except:
            break



def main():
    title()
    date = str(datetime.now().strftime("%m/%d/%y %H:%M:%S"))
    target = input('Please provide the target file containing the vhosts you would like added to your systems hosts file\nPlease note that this MUST be a json file\n: ')
    ip = input('\nPlease provide the ip address that these virtuial hosts are associated with\n: ')
    print("\n")
    # opens up our systems host file. If for whatever reason your systems host file is elsewhere change this line!
    hosts=open("/etc/hosts", 'a')
    jsonFile(date, target, ip, hosts)
    print("\n\nCompleted with love <3\n")
    hosts.close()


main()