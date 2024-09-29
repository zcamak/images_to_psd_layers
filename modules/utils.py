from PIL import Image

def divide_list(lst):

    width, height = Image.open(lst[0]).size
    
    start     = 0
    length    = len(lst)
    max_int   = 2**31 - 1
    count     = length // (max_int // (width * height * 4))
    step      = length // count
    remainder = length % count
    sublists  = []
    
    for i in range(count):

        size    = step + (1 if i < remainder else 0)
        sublist = lst[start:start+size]

        sublists.append(sublist)

        start += size
    
    return sublists