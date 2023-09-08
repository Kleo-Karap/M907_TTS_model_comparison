# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 14:11:51 2023

@author: kleop
"""

import pandas as pd
import string
import matplotlib.pyplot as plt
import numpy as np
#%%
original_sentences = {
    0: "Now, i am become death, the destroyer of worlds",
    1: "with slow advance ukraine aims for better shot at russian targets",
    2: "Please do not remove the battery, while the phone is updating, as it may cause software issues and void the warrant",
    3: "tomorrow the weather forecast predicts clear skies and high temperatures throughout the day ,with no chance of rain",
    4: "why do colorless green ideas sleep furiously?"

}
#%%
def remove_punctuation(text):
    # Helper function to remove punctuation from a string
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

def calculate_intelligibility_score(original_transcript, evaluator_transcripts):
    # Step 1: Determine the total number of words in the original transcript
    original_words = remove_punctuation(original_transcript.lower()).split()
    total_original_words = len(original_words)

    # Step 2: Calculate the percent-intelligible score for each evaluator
    scores = []
    for evaluator_transcript in evaluator_transcripts:
        evaluator_words = evaluator_transcript.split()
        correctly_identified_words = sum(1 for word in evaluator_words if word in original_words)
        percent_intelligible = correctly_identified_words / total_original_words * 100
        scores.append(percent_intelligible)

    # Step 3: Calculate the average percent-intelligible score
    overall_intelligibility_score = sum(scores) / len(scores)

    return overall_intelligibility_score

# Function to plot intelligibility scores for all models
def plot_intelligibility_scores(all_scores):
    sentences = [f"Sentence{i+1}" for i in range(len(original_sentences))]
    num_sentences = len(sentences)
    width = 0.2  # Width of the bars
    x = np.arange(num_sentences)

    fig, ax = plt.subplots(figsize=(10, 6))
    for i, (model_info, scores) in enumerate(all_scores.items()):
        offset = (i - 1) * width / 2
        ax.bar(x + offset, scores, width, label=model_info)

    ax.set_xticks(x)
    ax.set_xticklabels(sentences, rotation=15, ha="right")
    ax.set_ylim(0, 100)
    ax.set_xlabel("Sentences")
    ax.set_ylabel("Intelligibility Score (%)")
    ax.set_title("Intelligibility Scores for All Models")
    ax.legend()
    plt.tight_layout()
    plt.show()

# Function to calculate and write scores (updated to return overall scores)
def calculate_and_get_scores(df, original_sentences):
    overall_scores = []
    for sentence_id in range(len(df.columns)):
        original_sentence = original_sentences[sentence_id]
        evaluator_transcripts = df.iloc[:, sentence_id].tolist()
        intelligibility_score = calculate_intelligibility_score(original_sentence, evaluator_transcripts)
        overall_scores.append(intelligibility_score)
    return overall_scores

def calculate_and_write_scores(df, original_sentences, model_name, output_file):
    # Calculate the overall intelligibility score for each sentence in the DataFrame
    overall_scores = {}
    for sentence_id in range(len(df.columns)):
        original_sentence = original_sentences[sentence_id]
        evaluator_transcripts = df.iloc[:, sentence_id].tolist()
        intelligibility_score = calculate_intelligibility_score(original_sentence, evaluator_transcripts)
        overall_scores[sentence_id] = intelligibility_score
    
    # Write the overall intelligibility scores to the .txt file
    output_file.write(f"Results for {model_name}:\n")
    for sentence_id, score in overall_scores.items():
        output_file.write(f"Sentence {sentence_id + 1}: {score:.2f}%\n")
    output_file.write("\n")

#%% Capacitron

df_capacitron=pd.read_csv('C:/Users/kleop/Desktop/TTS_Assign/Evaluation_results/Capacitron-Evaluation.csv')
#drop 1st row (index 0)
df_capacitron.drop(0, axis=0, inplace=True)
#drop 1st column dy integer index
df_capacitron.drop(df_capacitron.columns[0], axis=1, inplace=True)
#these columns contain the evaluators' transcripts, the rest contain the naturalness scores, so they should be somehow removed from processing
capacitron_selected = df_capacitron.iloc[:, [0, 2, 4, 6, 8]]

#%% GLOW-tts 

df_glow=pd.read_csv('C:/Users/kleop/Desktop/TTS_Assign/Evaluation_results/Glow_TTS-Evaluation.csv')
#drp first 6 rows, because they were experimental
df_glow.drop(df_glow.index[0:6], axis=0, inplace=True)
glow_selected = df_glow.iloc[:, [1, 3, 4, 5, 6]]
#to make sure both dataframes have exactly the same format and indexes
glow_selected.reset_index(drop=True, inplace=True)
glow_selected.index = glow_selected.index + 1

#%% Tacotron2
df_tacotron2=pd.read_csv('C:/Users/kleop/Desktop/TTS_Assign/Evaluation_results/Tacotron2-Evaluation.csv')
df_tacotron2

#%%
#drop 1st column dy integer index
df_tacotron2.drop(df_tacotron2.columns[0], axis=1, inplace=True)
#these columns contain the evaluators' transcripts, the rest contain the naturalness scores, so they should be somehow removed from processing
tacotron2_selected = df_tacotron2.iloc[:, [0, 2, 4, 6, 8]]
#%%
#to make sure all 3 dataframes have exactly the same format and indexes
tacotron2_selected.index = tacotron2_selected.index + 1

#%%
model_data = {
    'capacitron': capacitron_selected,
    'glow-tts': glow_selected,
    'tacotron2': tacotron2_selected
}

# Calculate and get the overall intelligibility scores for each model
overall_scores_dict = {}
with open("intelligibility_scores.txt", "w") as output_file:
    for model_info, df in model_data.items():
        overall_scores = calculate_and_get_scores(df, original_sentences)
        overall_scores_dict[model_info] = overall_scores
        calculate_and_write_scores(df, original_sentences, model_info, output_file)

# Plot the results for all models in a single plot
plot_intelligibility_scores(overall_scores_dict)

print("Results written to intelligibility_scores.txt")
        
