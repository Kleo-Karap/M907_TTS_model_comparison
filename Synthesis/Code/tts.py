import os
from TTS.api import TTS

def synthesize_and_save(sentences, models, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    for model_name, model_dir in models.items():
        model_folder = os.path.join(output_folder, model_name)
        os.makedirs(model_folder, exist_ok=True)
        
        tts_model = TTS(model_name=model_dir, progress_bar=False, gpu=False)

        for i, text in enumerate(sentences):
            output_file = os.path.join(model_folder, f"sentence_{i}.wav")
            tts_model.tts_to_file(text=text, file_path=output_file)

if __name__ == "__main__":
    sentences_to_synthesize = [
        "Now, I am become Death, the destroyer of worlds.",
        "With Slow Advance, Ukraine Aims for Better Shot at Russian Targets",
        "Please do not remove the battery while the phone is updating, as it may cause software issues and void the warranty",
        "Tomorrow the weather forecast predicts clear skies and warm temperatures throughout the day with no chance of rain",
        "Why do colorless green ideas sleep furiously?"
    ]

    models = {
        "glow-tts": "tts_models/en/ljspeech/glow-tts",
        "tacotron2": "tts_models/en/ek1/tacotron2",
        "capacitron-t2-c50": "tts_models/en/blizzard2013/capacitron-t2-c50"
    }

    output_folder = "output"
    synthesize_and_save(sentences_to_synthesize, models, output_folder)
