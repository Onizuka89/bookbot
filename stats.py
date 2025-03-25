def get_num_words(path:str):
    counter = 0
    with open(path) as file:
        for line in file.readlines():
            counter += len(line.split())
    print("Found {} total words".format(counter))

def count_characters(path:str):
    counter = dict()
    with open(path) as file:
        for line in file.readlines():
            for char in line.lower():
                counter[char] = counter.get(char, 0) + 1

    return counter

def count_characters_sorted_by_frequency(path:str):
    count_dict = list(count_characters(path).items())
    count_dict.sort(key=lambda a: a[1], reverse=True)
    for entry in count_dict:
        if not entry[0].isalpha():
            continue
        print("{}: {}".format(entry[0],entry[1]))
