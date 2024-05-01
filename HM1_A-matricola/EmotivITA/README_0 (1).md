**
    EmotivITA – Dimensional and Multi-dimensional emotion analysis**
EmotivITA is a task of emotion regression based on EmoITA, the Italian version of the EmoBank dataset .
EmotivITA follows the VAE model, for which emotional states can be described relative to three fundamental emotional dimensions: Valence, Arousal, and Dominance.
Search online to obtain more details about this model.

Your task:

1. Download the dataset from : https://github.com/GiovanniGafa/EmoITA

### Reformat data:

In the original data, for a given sentence, you will a list of three float values, one for each dimension, Valence, Arousal, and Dominance, respectively.
First you have to map the numerical values into a label, an EXAMPLE should be this (try to motivate your choices):

[0.0,2.5) -> "bassa"
[2.5, 4.0) -> "media"
[4.0, 5.0] -> "alta"

Then, for each sample in the data, create three json entries (in different files), one per dimension, with the following format, so you will create three different dataset for each given split.

```JSON
{
    "text": str, # the input sentence,
    "choices": List[str], # the list of possible answers (from the aforementioned mapping for each dimension)
    "label": int, # the correct answer
}
```

write the resulting jsons in the following files:

- ``EmotivITA_Valence_dev.jsonl``, ``EmotivITA_Valence_test.jsonl``
- ``EmotivITA_Arousal_dev.jsonl``, ``EmotivITA_Arousal_test.jsonl``
- ``EmotivITA_Dominance_dev.jsonl``, ``EmotivITA_Dominance_test.jsonl``

### Prompts

Create ``prompt.jsonl``.
In this file you have to report the prompts you designed for the task.
Each line in your output file (1 line per prompt) must be a JSON object like the one below:

```JSON
{
    "prompt": "..."
}
```

## Deliver format

You have to format your data using JSON Lines standard.
