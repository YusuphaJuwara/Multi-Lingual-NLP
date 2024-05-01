# Multi Lingual NLP course for the Degree of Master of Science in AI and Robotics, 2023-2024

- `Homework 1A` is about data preprocessing that is used in `Homework 1B` to train NLP models on the Italian Language.

## Homework 1A -- EmotivITA and HODI Dataset

- This report walks through two tasks: task 0 (EmotivITA) and subtask A of task 1 (HODI). 
- It provides a brief explanation of the two tasks, their input and output formats, how the data are formated, the prompts and the motivation for those specific prompt choices. 
- It also explains how to run the scripts succesfully.
- Read the requirements files here for what to expect from this part: [EmotivITA](./HM1_A-matricola/EmotivITA/README_0%20(1).md) and [HODI](./HM1_A-matricola/HODI_2023/README-HODI.md).

## Homework 1B -- Training NLP Models on the Italian Language using the `EmotivITA` dataset

- This part walks through the key details of the implementation of multiple models on the [EmotivITA](https://github.com/GiovanniGafa/EmoITA/tree/main/EmotivITA) dataset for sentence classification task for the Italian language.
- This work aims to establish `baseline models` and then implement more robust models from the `RNN family` that can outperform them. 
- I experimented with 3 `statistics-based` baselines, 2 `Logistics Regressions` (one with embedding layer), and some combinations of `BiLSTM` and `BiGRU` models. 
- I was able to achieve varying but good results as elaborated in the Results section of its [report](./HM1_A-matricola/).
- I also experimented with `triple head` -- like `Siamese networks` -- where, instead of having a single output layer, it has a triple. This is the same as having 3 different networks. Note that 3 different networks require more compute but more stable and faster to converge. Thus, I implemeneted the later for network training stability.
- For further details on this, see the report here



