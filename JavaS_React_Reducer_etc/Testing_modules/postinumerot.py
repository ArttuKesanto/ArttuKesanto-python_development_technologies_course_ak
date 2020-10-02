# Arttu Aleksi Kesanto, 1900649 - Haaga-Helia, Pasila campus
import urllib.request
import json

JSON_URL = 'https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json'


def hae_postinumerot():  # Can be asserted, did refactoring.
    with urllib.request.urlopen(JSON_URL) as response:
        return json.loads(response.read())


# Can be asserted, did refactoring. DIP-principle.
def populate_toimipaikat_ja_numerot(postinumerot):
    toimipaikat_ja_numerot = {}
    for numero, toimipaikka in postinumerot.items():
        if toimipaikka in toimipaikat_ja_numerot:
            toimipaikat_ja_numerot[toimipaikka].append(numero)
        else:
            toimipaikat_ja_numerot[toimipaikka] = [numero]
    return toimipaikat_ja_numerot


def populate_toimipaikat_ja_numerot_FOR_ASSERTION_EXERCISE(): # This is to practice MOCKER. Could have done it with this method as well.
    postinumerot = hae_postinumerot()
    toimipaikat_ja_numerot = {}
    for numero, toimipaikka in postinumerot.items():
        if toimipaikka in toimipaikat_ja_numerot:
            toimipaikat_ja_numerot[toimipaikka].append(numero)
        else:
            toimipaikat_ja_numerot[toimipaikka] = [numero]
    return toimipaikat_ja_numerot


# Can be asserted, did refactoring.
def search_for_inputted_word(inputSearch, toimipaikat_ja_numerot):
    if inputSearch in toimipaikat_ja_numerot:
        loydetyt = toimipaikat_ja_numerot[inputSearch]
        #print('Postinumerot: ' + ', '.join(loydetyt))
        return loydetyt
    else:
        return {}
        #print('Postitoimipaikkaa ei löytynyt :(')


def main():
    postinumerot = hae_postinumerot()
    toimipaikat = populate_toimipaikat_ja_numerot(postinumerot)
    inputSearch = input('Kirjoita postitoimipaikka: ').strip().upper()
    loydetyt = search_for_inputted_word(inputSearch, toimipaikat)
    if (search_for_inputted_word(inputSearch, toimipaikat)):  # If this returns TRUE.
        print('Postinumerot: ' + ', '.join(loydetyt))
    else:
        print('Postitoimipaikkaa ei löytynyt :(')


if __name__ == '__main__':
    main()
