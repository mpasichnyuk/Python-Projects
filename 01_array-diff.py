// codewars

def array_diff(OriginalArray, ItemsToRemove):
    for i in ItemsToRemove:
        print('looking for', i)
        while i in OriginalArray:
            print (i, "found, removing")
            OriginalArray.remove(i)
            
    return OriginalArray
