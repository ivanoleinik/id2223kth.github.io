# Whisper Swedish Audio Translation Project

This project demonstrates a ready to use application from a fine-tuned and improved whisper model for the Swedish language

## UI Usage Instructions

The UI allows for audio or video file uploads in mp3, mp4, etc., formats in a file dropbox on the left. When the user clicks on submit button, the UI makes a call to the best-performing model among the checkpoints saved by the training pipeline and outputs the transcribed text in a box to the right. 

## Table of Contents
1. [Introduction](#introduction)
2. [Dataset](#dataset)
3. [Training Notebook](#training-notebook)

## Introduction

This project aims to predict the quality of wines using machine learning. It covers various aspects, including data preparation, model training, model deployment, and user interaction.

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




