import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def animateSA(history):
    fig = plt.figure()
    
    x = [history[i][0] for i in range(len(history))]
    y = [history[i][1] for i in range(len(history))]

    # draw axes a little bigger
    extra_x = (max(x) - min(x)) * 0.05
    extra_y = (max(y) - min(y)) * 0.05
    plt.xlim(min(x) - extra_x, max(x) + extra_x)
    plt.ylim(min(y) - extra_y, max(y) + extra_y)
    graph, = plt.plot([], [], 'o')
    
    def update(frame):
        x = [history[frame][0]]
        y = [history[frame][1]]
        graph.set_data(x, y)
        return graph

    ani = FuncAnimation(fig, update, interval=3)
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

def animateWeightSA(history):
    plt.plot([i for i in range(len(history))], history)
    plt.xlabel('Iteration')
    plt.ylabel('Weight (approximate potential energy of the system)')
    plt.show()