def print_sorted_dictionary(a_dictionary):
    list_keys = sorted(a_dictionary.keys())
    for e in list_keys:
        print("{}: {}".format(e, a_dictionary[e]))