# Star Wars Fact Generator

# Import Modules
import requests
import random
import time

print('Lets explore the planets of the Star Wars Universe!')

time.sleep(3)

print('3...')
time.sleep(0.5)
print('2...')
time.sleep(0.5)
print('1...')
time.sleep(0.5)

print('BLAST OFF!')
time.sleep(0.5)

planet_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def planet():
    url = 'https://swapi.dev/api/planets/{}/'.format(num)
    response = requests.get(url)
    starwarsdata = response.json()
    return {
        'name': starwarsdata['name'],
        'diameter': starwarsdata['diameter'],
        'climate': starwarsdata['climate'],
        'gravity': starwarsdata['gravity'],
        'terrain': starwarsdata['terrain'],
        'population': starwarsdata['population'],
        'number': num
    }


while len(planet_list) > 0:
    num = random.choice(planet_list)

    time.sleep(2.5)

    print('Flying through space...')

    time.sleep(2)

    random_planet = planet()

    user_choice = input('We have found a planet, do you want to land? Yes: Y or No: N : ')

    if user_choice == 'Y' or user_choice == 'y':
        print('Landing...')
        time.sleep(1)
        print('You found the planet {}!'.format(random_planet['name']))
        time.sleep(1.5)
        print('Here are some facts about {}:'.format(random_planet['name']))
        time.sleep(1.3)
        print('{}\'s terrain is {}'.format(random_planet['name'], random_planet['terrain']))
        time.sleep(1.3)
        print('It\'s climate is {}'.format(random_planet['climate']))
        time.sleep(1.3)

        if random_planet['population'] == 'unknown':
            print('It\'s population size is unknown')
        else:
            print('It\'s population is {}'.format(random_planet['population']))

        diameter = random_planet['diameter']

        time.sleep(1.3)

        if int(diameter) > 9000:
            print('{} is a large planet with a diameter of {}'.format(random_planet['name'], random_planet['diameter']))
        else:
            print('It is a small planet that has a diameter of {}'.format(random_planet['diameter']))

    else:
        home = input('Do you want to return home? YES: Y or NO: N : ')
        if home == 'Y' or home == 'y':
            time.sleep(0.5)
            print('Returning Home...')
            time.sleep(0.5)
            print('We have landed back home')
            break

    planet_list.remove(num)


print('------------------------------------------------')




