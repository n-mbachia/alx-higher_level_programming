#!/usr/bin/python3
def element_at(my_list, idx):
    if ((idx < 0) or idx >= len(my_list)): # retrives element from list
        return None         # if out of range return none
    else:
        return my_list(idx)
