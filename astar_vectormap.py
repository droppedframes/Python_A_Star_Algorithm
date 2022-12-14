import random
from matplotlib import pyplot as plt

nodes = []
map_width = 500
map_height = 500
node_count = 20

for i in range(node_count):
    x = random.randint(0,map_width)
    y = random.randint(0,map_height)
    nodes.append({'x': x, 'y': y, 'f':0, 'g':0, 'h':0,'previous':None, 'neighbors':list()})
    plt.plot(x,y,'bo')
    plt.plot(x,y,)

node_list = []

for x in range(0,map_width):
    for i in range(len(nodes)):
        if nodes[i]['x']==x:
            node_list.append(i)

for i in range(len(node_list)-1):
    pathx = random.randint(2,4)
    print (pathx)
    for x in range(pathx):
        if i+x < len(node_list):
            rand_node = node_list[i+x]
            nodes[rand_node]['neighbors'].append(node_list[i])
            nodes[node_list[i]]['neighbors'].append(node_list[i])
            x_values = [nodes[rand_node]['x'], nodes[node_list[i]]['x'],]
            y_values = [nodes[rand_node]['y'], nodes[node_list[i]]['y'],]
            plt.plot(x_values, y_values, 'bo', linestyle="-", marker = 'o', ms = 10)

print(node_list)

'''
for i in range(len(nodes)):
    connections = random.randint(1,1)
    for path in range(connections):
        rand_node = random.randint(0,len(nodes)-1)
        nodes[rand_node]['neighbors'].append(i)
        nodes[i]['neighbors'].append(rand_node)
        x_values = [nodes[rand_node]['x'], nodes[i]['x'],]
        y_values = [nodes[rand_node]['y'], nodes[i]['y'],]
        plt.plot(x_values, y_values, 'bo', linestyle="-")
'''

# Displaying grid
plt.grid()

# Controlling axis
plt.axis([0, map_width, 0, map_width ])

# Adding title
plt.title('')

# Displaying plot
plt.show()
