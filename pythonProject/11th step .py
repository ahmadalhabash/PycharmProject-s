# Collections tuple - practice

# 1 - Creat a tuple of tech terms
technological_tems = ('python', 'pycharm IDE', 'tuple', 'collections', 'string')
print('(1) - This is the tuple collections : ' + str(technological_tems))

# 2 - Print a sentece using cell extraction : Regular & negative
# we are ninja developers. We write python code in pycharm IDE, and now practincing tuple collections topic, that contains string variables

print("(2) - we are ninja developers. We write " + technological_tems[0] + " code in " + technological_tems[1]
+ ", and now practicing " + technological_tems[2] + " collections topic , that contains" + technological_tems[-1] + " variables ")


# 3 - Insert 'float' and 'list' variables into the tuple
technological_tems_list = list(technological_tems)

technological_tems_list.append('float')
technological_tems_list.append('list')

technological_tems = tuple(technological_tems_list)
print("(3) - This is our new tuple with the added cells : " + str(technological_tems))


# 4 - Creat a single cell tuple
single_cell_tuple = (1,)
print("(4) - Print the single cell tuple : " + str(single_cell_tuple))
print(type(single_cell_tuple))