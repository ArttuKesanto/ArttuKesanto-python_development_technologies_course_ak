# Arttu Aleksi Kesanto, 1900649 - Haaga-Helia, Pasila campus
from postinumerot import populate_toimipaikat_ja_numerot, search_for_inputted_word, hae_postinumerot, populate_toimipaikat_ja_numerot_FOR_ASSERTION_EXERCISE


def test_fetching_works():
    postinumerot_dict = hae_postinumerot()

    # Checking if there are items after the fetch. Should be well over 200.
    assert len(postinumerot_dict) > 200

    # Checking if there are multiple values; only one code can be located once in a certain slot.
    for i in range(0, len(postinumerot_dict) - 1):
        # Creating a list so that the values can be indexed.
        postal_first = list(postinumerot_dict)[i]
        postal_second = list(postinumerot_dict)[i+1]

        assert postal_first != postal_second


# Mock-up data for the following methods (e.g. def test_populating_toimipaikat_and_numerot()):

postalNumbers = {
    10120: "TÄHTELÄ",
    10140: "PÄIVÖLÄ",
    10160: "DEGERBY",
    10210: "INKOO",
    10211: "INKOO",
    10214: "SMARTPOST",
}


def test_populating_toimipaikat_and_numerot_with_mock_up_data():
    foundDict = populate_toimipaikat_ja_numerot(postalNumbers)

    assert "TÄHTELÄ" in foundDict and "PÄIVÖLÄ" in foundDict and "INKOO" in foundDict and "SMARTPOST" in foundDict and "DEGERBY" in foundDict and "HELSINKI" not in foundDict


def test_searching_by_a_certain_word_with_mock_up_data():
    searchable_first = "HELSINKI"
    searchable_second = "INKOO"
    foundDict = populate_toimipaikat_ja_numerot(postalNumbers)
    foundPostalCodesForHELSINKI = search_for_inputted_word(
        searchable_first, foundDict)
    foundPostalCodesForINKOO = search_for_inputted_word(
        searchable_second, foundDict)

    # Asserting that there are no numbers found for Helsinki in the mockup-data, and that there is a list of two values (more than one) available for INKOO in the mockup-data.
    assert searchable_first not in foundDict and searchable_second in foundDict and foundPostalCodesForHELSINKI == {} and len(
        foundPostalCodesForHELSINKI) == 0 and foundPostalCodesForINKOO == [10210, 10211] and len(foundPostalCodesForINKOO) > 1 and len(
            foundPostalCodesForINKOO) == 2


def test_get_postal_numbers__with_mock(mocker):
    # Initializing the values - 0-5 ergo length is 5, a DICT:
    my_postal_codes = {
        10410: "ÅMINNEFORS",
        10420: "POHJANKURU",
        10421: "POHJANKURU",
        10424: "SMARTPOST",
        10440: "BOLLSTA",
        10470: "FISKARI",
    }
    mocker.patch('postinumerot.hae_postinumerot', return_value=my_postal_codes)

    postalDict = populate_toimipaikat_ja_numerot_FOR_ASSERTION_EXERCISE() # Now, instead of the whole data, we only get the mockup-data. ... 
    # ... Without mocker, this call would fetch the whole list. There is a connection with the described functions in the module postinumerot.py.
    
    # Asserting the data, checking the exact length and what is in the dictionary, also checking if there is only one postal-code available for certain items:

    assert len(postalDict) < 200 and len(postalDict) == 5 and "SMARTPOST" in postalDict and "HELSINKI" not in postalDict and int(10424) in postalDict["SMARTPOST"] and len(
        postalDict["BOLLSTA"]) == 1

