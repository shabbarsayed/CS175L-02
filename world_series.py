#Shabbar Sayed
#CS 175L 02
#world_series

def main():
    infile = open('WorldSeriesWinners.txt', 'r')

    for line in open('WorldSeriesWinners.txt'):
        line = line.rstrip('\n')

    winners = infile.read().splitlines()

    infile.close()
    search(winners)

    
def search(winners):

    team = " "
    while team != 'Quit':
        team = input('Enter the name of a team or Quit: ')
        if team == 'Quit':
            break

        counter = 0

        for winner in winners:
            if team.lower()== winner.lower():
                counter = counter + 1


        if counter == 1:
            print('The', team, 'won the world series', counter, 'time between 1903 and 2009.')

        elif counter > 1:
            print('The', team, 'won the world series', counter, 'time between 1903 and 2009.')
        else:
            print('The', team, 'never won the world series.')

main()
