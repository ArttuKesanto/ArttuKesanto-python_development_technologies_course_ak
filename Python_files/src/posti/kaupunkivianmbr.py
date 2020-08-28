import json

postinro = input("Kerro postinumero: ")
print(postinro)

with open('postcodes.json') as json_file:
    try:
        data = json.load(json_file)
    # print(data)
        for i in data:
            if i['postcode'] == postinro:
                print(i['postcode_fi_name'])
                break
    except:
        print('Something went wrong, please try again.')
