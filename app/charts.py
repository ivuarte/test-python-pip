import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, vaules):
  fig, ax = plt.subplots()
  ax.bar(labels, vaules)
  plt.savefig(f'./imgs/{name}bar.png')
  plt.close()


def generate_pie_chart(labels, vaules):
  fig, ax = plt.subplots()
  ax.pie(vaules, labels=labels)
  ax.axis('equal')
  plt.savefig('pie.png')
  plt.close()


if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  vaules= [100,200,50]
  #generate_bar_chart(labels, vaules)
  generate_pie_chart(labels, vaules)