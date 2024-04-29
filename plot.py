# import matplotlib.pyplot as plt
# import numpy as np
# import pandas as pd

# bilan = pd.read_csv('bilan.csv')
# species = bilan.iloc[:, 0]  # Les espèces sont dans la première colonne
# perplexity_magnitude = bilan.iloc[:, 2]  # Valeurs de magnitude
# perplexity_wanda = bilan.iloc[:, 3]  # Valeurs de wanda

# x = np.arange(len(species))  # the label locations
# width = 0.35  # the width of the bars

# fig, ax = plt.subplots()

# rects1 = ax.bar(x - width/2, perplexity_magnitude, width, label='Magnitude')
# rects2 = ax.bar(x + width/2, perplexity_wanda, width, label='Wanda')

# # Add some text for labels, title and custom x-axis tick labels, etc.
# ax.set_ylabel('Perplexity')
# ax.set_title('Perplexity by Species and Type')
# ax.legend()

# # Save the graph to a file
# plt.savefig('graphique.png', bbox_inches='tight')
# plt.show()

# data from https://allisonhorst.github.io/palmerpenguins/

import matplotlib.pyplot as plt
import numpy as np

sparity = (0, 0.1, 0.3, 0.5, 0.7, 0.9)
energy = (0.0049, 0.0040, 0.0039, 0.0121, 0.0038, 0.0107, 0.00397, 0.0120, 0.0039, 0.01030, 0.00494, 0.0099)  

# perplexity = {
#     'magnitude': (5.677263259887695, 5.805983066558838, 6.668586730957031, 17.285097122192383, 0, 0),
#     'wanda': (5.677263259887695, 5.696265697479248, 5.998607635498047, 7.257486343383789, 0, 0)
# }
energy_ordonne = {
    'magnitude': (0.004986216659,0.003945943178,0.003832941015,0.00397966,0.003935676640,0.0049406337397),
    'wanda': (0.00401724665898002,0.01214821,0.01071953375,0.01203387,0.01030808847,0.009916691594)
}
x = np.arange(len(sparity))  # the label locations
width = 0.25  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')
for attribute, measurement in energy_ordonne.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1
# for attribute, measurement in perplexity.items():
#     offset = width * multiplier
#     rects = ax.bar(x + offset, measurement, width, label=attribute)
#     #ax.bar_label(rects, padding=3)
#     # Ajout des valeurs associées aux barres
#     for i, rect in enumerate(rects):
#         height = rect.get_height()
#         ax.text(rect.get_x() + rect.get_width() / 2., height, f'{energy[i]}', ha='center', va='bottom')
#     multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('y')
ax.set_title('attributes by species')
ax.set_xticks(x + width, sparity)
ax.legend(loc='upper left', ncols=3)
# ax.set_ylim()

plt.savefig('graphique.png', bbox_inches='tight')
plt.show()
