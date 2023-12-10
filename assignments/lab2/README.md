# Whisper Swedish Audio Translation Project

This project demonstrates a ready to use application from a fine-tuned and improved whisper model for the Swedish language

## UI Usage Instructions

The UI allows for audio or video file uploads in mp3, mp4, etc., formats in a file dropbox on the left. When the user clicks on submit button, the UI makes a call to the best-performing model among the checkpoints saved by the training pipeline and outputs the transcribed text in a box to the right. 

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Training Notebook](#training-notebook)
4. [Evaluation](#evaluation)

## Introduction

The goal of this project is to fine-tune Whisper to the Swedish language and to provide a useful UI capable of transcribing Swedish audio input to English text output. 

Whisper, introduced in September 2022 by OpenAI's Alec Radford et al., is an advanced automatic speech recognition (ASR) model. Unlike its predecessors, Whisper is unique in being pre-trained on an extensive 680,000 hours of labeled audio-transcription data, with 117,000 hours dedicated to multilingual ASR. This large-scale pre-training allows Whisper to generalize well across datasets and domains, making it a powerful tool for various ASR tasks.

## Dataset

The fine-tuning dataset contains swedish sentences looks like this:

train: Dataset({
        features: ['audio', 'sentence'],
        num_rows: 12360
    })
    test: Dataset({
        features: ['audio', 'sentence'],
        num_rows: 5069
    })

It contains 12360 training sentences and 5069 test set sentences.

## Fine-tuning Notebook

The notebook performs the following pre-processing steps:

- The notebook clips the audio clips and pads with 0's when necessary to 30 seconds

- Loads a pretrained swedish tokenizer/feature-extractor

- Downsamples the audio fromm 48Hz to 16Hz

- Removes the other features and downloads the audio to disk

- Fine-tunes the pretrained general whisper model on this data, saving and loading checkpoints every thousand steps

## Evaluation 

We traced the WER score of the model on the evaluation dataset after every thousand steps:

- checkpoint-1000: 70.09
- checkpoint-2000: 20.45
- checkpoint-3000: 20.13

We can observe that the last thousand steps of training is a plateau. This is why we decided to restart training from the `checkpoint-2000` for another thousand steps but with a lower learning rate of 3e-6. This resulted in an improved WER score of 19.70 for our final model.




