#Abbreviate a Two Word Name

def abbrev_name(name):
    words = name.split(' ')
    name_initial = words[0][0].upper()
    last_initial = words[1][0].upper()

    return name_initial + '.' + last_initial



#Sum Arrays

def sum_array(a):
    if a == []:
        return 0
    else:
        return sum(a)
    


#Convert a Boolean to a String

def boolean_to_string(b):
    if b:
        return str(True)
    else:
        return str(False)

#Remove String Spaces

def no_space(x):
    return x.replace(" ", "")
    