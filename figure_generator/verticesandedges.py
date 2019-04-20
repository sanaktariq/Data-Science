#starting parameters:
"""origin = (0,0)
height = 5
width = 10
radius = 5"""

def fig_gen(shape, origin, width, height):
    if shape == "rectangle":
        give = [
                [origin[0], origin[1]], 
                [origin[0] + width, origin[1]], 
                [origin[0], origin[1] + height], 
                [origin[0] + width, origin[1]+ height]
                ]
    else:
        print("Invalid Entry")
    
    return give



if __name__ == "__main__":

    import matplotlib.pyplot as plt
    x = fig_gen("rectangle", [50, 50], 1000, 500) 
    #print(x)
    #print(x, x[2])

    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np
    import matplotlib.path as mpath
    import matplotlib.lines as mlines
    import matplotlib.patches as mpatches
    from matplotlib.collections import PatchCollection

    #create 3x3 grid to plot the artists
    grid = np.mgrid[0.2:0.8:3j, 0.2:0.8:3j].reshape(2, -1).T
    fig, ax = plt.subplots()
    patches = []

    rectangle = mpatches.Rectangle([50,50], 100, 50, angle=0.0)
    patches.append(rectangle)

    collection = PatchCollection(patches, alpha=0.3)
    ax.add_collection(collection)

    plt.axis('equal')

    plt.show()

    ret = fig_gen(("rectangle"), (50,50), (1000), (500)) 
    result = [[50, 50], [1050, 50], [50, 550], [1050, 550]]
    cond = ret == result

    print("func:" , ret, "res:" , result, "condition:", cond)