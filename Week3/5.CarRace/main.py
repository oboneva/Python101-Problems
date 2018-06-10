import sys
import json
from championship import Championship


def standings():
    with open('result.json', 'r') as f:
            data = json.load(f)

    championships = data.keys()

    for championship in championships:
        print(championship)
        Championship.total_ranking(data, championship)

        print('')


def main():
    if len(sys.argv) < 2:
        print('Hello PyRacer!')
        print('Please, call command with proper argument:')
        print('python3.6 main.py start <name> <races_count> -> This will start a new championship with the given name, races count and drivers from cars.json')
        print('python3.6 main.py standings -> This will print the standings for each championship that has ever taken place.')
    elif sys.argv[1] == 'start':
        championship = Championship(sys.argv[2], int(sys.argv[3]))
        championship.start(championship.name)
    elif sys.argv[1] == 'standings':
        standings()

if __name__ == '__main__':
    main()
