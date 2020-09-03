import json

postitmp = input("Kerro postitoimipaikkasi: ")
postitmpUpperCase = postitmp.upper()
# No matter if the input is in lower case.
# print(postitmpUpperCase) DEBUGGING
postnrList = []

with open('postcode_map_light.json') as json_file:
    try:
        data = json.load(json_file)
        # print(data['25840'])
        for i in data:
            if data[i] == postitmpUpperCase:
                #postnrList[i] = data[i]
                print(i, end=', ')  # Getting everything to the same page.
    except:
        print('Input a legit place. Thanks!')
