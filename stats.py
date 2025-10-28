def get_num_words(string):
    '''
        Reads a string,
        give word count
    '''
    # converts string to list. seperating at words
    string_lst = string.split()
    # gets the amount of words in list
    cnt = len(string_lst)
    return cnt

def get_char_cnt(string):
    '''
        produces a dictionary,
        where the key is the character,
        and the value is the frequency
    '''
    # create dictionary
    frequency = {}

    for c in string.lower():
        # if character in dictionary increase by one
        # else initialise it with a value of 1
        frequency[c] = frequency.get(c, 0) + 1

    return frequency

def sorted_dict_lst(dic):
    def sort_on(items):
        return items["num"]
    lst = []

    for char, frq in dic.items():
        tmp = {"name":char, "num":frq}
        if char.isalpha():
            lst.append(tmp)
    lst.sort(reverse=True, key=sort_on)
    return lst
