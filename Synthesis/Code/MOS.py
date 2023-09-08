# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 07:23:18 2023

@author: kleop
"""

import numpy as np
import matplotlib.pyplot as plt
from mean_opinion_score import get_ci95, get_mos
#%%
_ = np.nan  #in case some sentence had no rating

# columns represent sentences

ratings_capacitron = np.array([
    [1, 1, 2, 2, 1],  # rater 1
    [1, 1, 4, 3, 4],  # rater 2
    [1, 1, 3, 2, 1],  # rater 3
    [2, 2, 4, 1, 1],  # rater 4
    [2, 2, 3, 1, 2],  # rater 5
    
])

mos_capacitron = get_mos(ratings_capacitron)
ci_capacitron = get_ci95(ratings_capacitron)

print(f"MOS: {mos_capacitron:.2f} ± {ci_capacitron:.4f}")

#%%
ratings_tacotron2 = np.array([
    [3, 4, 5, 5, 4],  # rater 1
    [2, 3, 3, 3, 2],  # rater 2
    [2, 2, 3, 4, 1],  # rater 3
    [3, 3, 4, 4, 2],  # rater 4
    [2, 3, 4, 4, 2],  # rater 5
    
])

mos_tacotron2 = get_mos(ratings_tacotron2)
ci_tacotron2 = get_ci95(ratings_tacotron2)

print(f"MOS: {mos_tacotron2:.2f} ± {ci_tacotron2:.4f}")

#%%
ratings_glow = np.array([
    [4, 2, 3, 4, 2],  # rater 1
    [3, 4, 4, 4, 2],  # rater 2
    [4, 2, 3, 2, 1],  # rater 3
    [4, 3, 5, 5, 2],  # rater 4
    [4, 4, 4, 5, 1],  # rater 5
    
])


mos_glow = get_mos(ratings_glow)
ci_glow = get_ci95(ratings_glow)

print(f"MOS: {mos_glow:.2f} ± {ci_glow:.4f}")


#%%
# Save the results to a .txt file
with open("mos_results.txt", "w") as file:
    file.write("MOS Results:\n")
    file.write(f"Capacitron: MOS = {mos_capacitron:.2f} ± {ci_capacitron:.4f}\n")
    file.write(f"Tacotron2: MOS = {mos_tacotron2:.2f} ± {ci_tacotron2:.4f}\n")
    file.write(f"Glow: MOS = {mos_glow:.2f} ± {ci_glow:.4f}\n")

print("MOS results saved to mos_results.txt")

#%%
# Plot the comparative graph
models = ["Capacitron", "Tacotron2", "Glow"]
mos_scores = [mos_capacitron, mos_tacotron2, mos_glow]
ci_scores = [ci_capacitron, ci_tacotron2, ci_glow]

# Define the x-axis values (0, 1, 2) and corresponding model names for labeling
x = np.arange(len(models))

# Create the bar plot
plt.bar(x, mos_scores, yerr=ci_scores, align='center', alpha=0.7, ecolor='black', capsize=10)
plt.xticks(x, models)
plt.ylabel('Mean Opinion Score (MOS)')
plt.title('Comparative MOS Scores for the Three Models')

# Display the MOS scores on top of the bars
for i, mos in enumerate(mos_scores):
    plt.text(i, mos + 0.2, f"{mos:.2f}", ha='center')

plt.tight_layout()

# Save the plot as an image
plt.savefig("mos_comparison.png")

# Show the plot
plt.show()