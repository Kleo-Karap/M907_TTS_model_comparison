# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 00:03:31 2023

@author: kleop
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data
data = {
    'Sentence 1': ['Version_2', 'Version_2', 'Version_2', 'Version_2', 'Version_2'],
    'Sentence 2': ['Version_2', 'Version_1', 'Version_2', 'Version_2', 'Version_2'],
    'Sentence 3': ['Version_2', 'Version_2', 'Version_1', 'Version_2', 'Version_2'],
    'Sentence 4': ['Version_2', 'Version_2', 'Version_3', 'Version_2', 'Version_2'],
    'Sentence 5': ['Version_2', 'Version_2', 'Version_1', 'Version_2', 'Version_2']
}

df = pd.DataFrame(data)

version_to_tts_model = {
    'Version_1': 'Glow-TTS',
    'Version_2': 'Tacotron2',
    'Version_3': 'Capacitron'
}

# Count the occurrences of each version across all sentences
version_counts = df.melt(var_name='Sentence', value_name='Chosen_Version')
version_counts = version_counts.groupby(['Chosen_Version']).size().reset_index(name='count')

# Sort the DataFrame by the chosen version count
version_counts = version_counts.sort_values(by='count', ascending=False)

# Map the version names to the corresponding TTS models
version_counts['Chosen_Version'] = version_counts['Chosen_Version'].map(version_to_tts_model)

# Plot the results
plt.figure(figsize=(8, 6))
sns.barplot(x='count', y='Chosen_Version', data=version_counts, palette='pastel')
plt.xlabel('Number of Times Chosen')
plt.ylabel('TTS Model')
plt.title('Results of Forced Choice Task')
plt.show()