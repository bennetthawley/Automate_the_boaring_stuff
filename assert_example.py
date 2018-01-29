market_2nd = {'ns': 'green', 'ew': 'red'}


def switch_lights(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    # The assert statement is a 'sanity check' for the programmer
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

switch_lights(market_2nd)

