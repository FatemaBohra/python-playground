# In this kata you need to check the provided array (x) for
# good ideas 'good' and bad ideas 'bad'. If there are one or
# two good ideas, return 'Publish!', if there are more than 2
# return 'I smell a series!'. If there are no good ideas, as
# is often the case, return 'Fail!'.

def well(x):
    count = 0
    for i in x:
        if i == "good":
            count += 1
    if count < 1:
        return "Fail!"
    elif count == 1 or count == 2:
        return "Publish!"
    else:
        return "I smell a series!"


print(well(['bad', 'bad', 'bad']))
