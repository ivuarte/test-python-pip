import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 34, 120]

    fig, ax = plt.subplots() #necesario para crear el grafico 
    ax.pie(values, labels=labels) #genera el grafico tip pie
    plt.savefig('pie.png')
    plt.close()