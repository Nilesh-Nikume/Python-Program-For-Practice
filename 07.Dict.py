# WAPeysto put the keys and values of a given dictionary in two different lists.
def sep_keys_values(dict):
    keys_list =list(dict.keys())
    values_list = list(dict.values())
    return keys_list,values_list

country_capital_dict = {
    "Germany": "Berlin",
    "Italy": "Naples",
    "England": "London",
    "Canada": "Ottawa" }
keys, values = sep_keys_values(country_capital_dict)
print("Keys in dict is",keys)
print("values indict is :", values)