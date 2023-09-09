# TTS_model_comparison
M.Sc. in Language Technology - Speech Synthesis Technologies assignment

In this project we were asked to use and evaluate several TTS models using  coquiTTS, an open-source speech synthesis tool developed by the Coqui AI team using Python text to speech.
This repo contains:
1. Scripts for generating synthetic speech with TTS models and vocoders of your choice (tts.py)
2. Scripts to calculate the Mean Opinion Score (MOS) of a Naturalness task based on a 5-point Lickert scale rating and plot comparative results of all examined TTS models (MOS.py)
3. Scripts to calculate and plot intelligibility scores of synthetic speech utterances based on a reference transcript. (intellibility+plots.py)
4. Scripts to plot the results of a forced choice task concerning the examined TTS models (comparison.py)

## User Instructions 

1. Install Docker Desktop
2. Navigate to Images< coqui-ai-tts-cpu (pull)<Once installed, Run it.

![image](https://github.com/Kleo-Karap/TTS_model_comparison/assets/117507917/a2c7a843-0090-44e4-85f9-4ab1ae77c650)


Optional settings:

![image](https://github.com/Kleo-Karap/TTS_model_comparison/assets/117507917/cd0c2c84-90c2-4803-baeb-ae7d3bd70d6d)


3. Install VSCode, install Docker extension
4. To make sure the coqui-ai works, right-click on coqui-ai Container in VSCode and choose "Attach Shell"
5. In a new .py file pip install ipython and paste the code content of the tts.py file

## References
https://github.com/coqui-ai/TTS
https://www.youtube.com/watch?v=alpI-DnVlO0&t=346s
