
'''You have a list of city names. Check whether "Chicago" exists.'''
city_list = ["Dallas","Denver", "Chicago", "New York", "Los Angeles"]
for city in city_list:
    if city.__contains__("Chicago"):
        print('Chicago is in the list')
