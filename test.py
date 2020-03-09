a = [[1,2,-1,-4],
    [2,3,4,5],
    [3,4,5,6]]
b = [1,2,3,4]

dict = {"A":3,"B":3}
print(max(dict))

def get_key (dict, value):
    return [k for k, v in dict.items() if v == value]
print(get_key(dict,3))