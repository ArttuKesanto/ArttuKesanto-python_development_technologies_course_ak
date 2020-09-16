# Arttu Aleksi Kesanto, Haaga-Helia.
import urllib.request, json

output = urllib.request.urlopen("http://open-api.myhelsinki.fi/v1/events/").read()
data = json.loads(output)

# with urllib.request.urlopen("http://open-api.myhelsinki.fi/v1/events/") as url:
# data = json.loads(url.read().decode())
# print(len(data))
# print(type(data))
# print(len(data))
# print(len(json.dumps(data)))
# print(data)

# json_string = json.dumps([data for ob in data])
# print(json_string)
# data_json = json.dumps(data) NOT IN USE.
# print(type(data_json))
print(type(data))
print(len(data))
# print(len(data_json))

# print(len(data_json))
# print(data['data'][1]['event_dates']['starting_day']) DEBUGGING.

listOfDatesWithNone = []  # Making on empty list for the dates.


# arr1 = [64, 34, 25, 12, 22, 11, 90] DEBUGGING the bubbleSort.


def main():
    # print(data['event_dates'])
    # print(data['data'][0])
    index = -1
    for _ in data['data']:  # _ as in not used.
        index += 1
        # print(data['data'][index]["event_dates"]["starting_day"])  # This works in order to get all the dates.
        # if len(data['data'][index]["event_dates"]["starting_day"]) > 0:
        listOfDatesWithNone.append(data['data'][index]["event_dates"]["starting_day"])

    listOfDates = list(
        filter(None, listOfDatesWithNone))  # Filtering away the NoneTypes. Making a new list for bubbleSORTING.

    # print(type(listOfDates))
    # print(len(listOfDates))

    # arr = listOfDates

    def bubbleSortMethod(
            arr):  # From https://www.geeksforgeeks.org/bubble-sort/; have done multiple of these with Java.
        # Comparing the value of ISO-type dates. - Arttu K.
        # filter(lambda x: x != None, arr)
        n = len(arr)
        print(n, 'this is n.')

        # Traverse through all array elements.
        for i in range(n):
            swapped = False

            # Last i elements are already in place.
            for j in range(0, n - i - 1):

                # traverse the array from 0 to n-i-1. Swap if the element found is greater than the next element.
                # if arr[j] == 'None':
                # break
                # if j is not None:

                # Cannot handle NonTypes. Did retouching before.
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

                # IF no two elements were swapped by inner loop, then break
            if swapped == False:
                break

    bubbleSortMethod(listOfDates)
    # print(arr1)
    print("Sorted array with dates is in length: ")
    # print(listOfDates)
    print(len(listOfDates), '\n')
    # index1 = -1

    # Iterating and matching the dates from the first to the last and then comparing what data-points have that date.
    for i in listOfDates:
        index1 = -1
        print(i[0:10] + ':')
        print('-----------')
        for _ in data['data']:  # '_' meaning that there is no need for the whole section of the data. Just iterating.
            index1 += 1
            if data['data'][index1]["event_dates"]["starting_day"] == i:
                startTime = data['data'][index1]["event_dates"]["starting_day"][11:16]  # Variable used in print().
                # print('--------')
                if data['data'][index1]["name"]["fi"] is None:
                    data['data'][index1]["name"]["fi"] = '[No name given in Finnish.]'
                name = data['data'][index1]["name"]["fi"]  # Variable used in print().

                # if len(data['data'][index1]["name"]["fi"]) > 0: TRIED to make this work, but NoneType has no len().
                # print(data['data'][index1]["name"]["fi"])
                # elif len(data['data'][index1]["name"]["en"]) > 0:
                # data['data'][index1]["name"]["en"]
                # elif len(data['data'][index1]["name"]["sv"]) > 0:
                # data['data'][index1]["name"]["sv"]
                # elif len(data['data'][index1]["name"]["zh"]) > 0:
                # data['data'][index1]["name"]["zh"]
                # else:
                # continue
                print('     ' + startTime + ': ' + name)
            else:
                continue

    # for i in range(len(listOfDates)):
    # print ("%d" % listOfDates[i])


if __name__ == '__main__':
    main()
