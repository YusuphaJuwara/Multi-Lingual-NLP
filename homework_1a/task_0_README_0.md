**EmotivITA – Dimensional and Multi-dimensional emotion analysis**
EmotivITA is a task of emotion regression based on EmoITA, the Italian version of the EmoBank dataset .
EmotivITA follows the VAE model, for which emotional states can be described relative to three fundamental emotional dimensions: Valence, Arousal, and Dominance.
Search online to obtain more details about this model.

Your task:
1. Download the dataset from : https://github.com/GiovanniGafa/EmoITA

### Reformat data:
In the original data, for a given sentence, you will a list of three float values, one for each dimension, Valence, Arousal, and Dominance, respectively.
First you have to map the numerical values into a label:
[0.0,2.5) -> "LOW"
[2.5, 4.0) -> "MEDIUM"
[4.0, 5.0] -> "HIGH"

Then, for each sample in the data, create three json entries, one per dimension, with the following format 

```JSON
{
    "text": str, # the input sentence,
    "dimension": str, # the given dimension, i.e., one among ["Valence", "Arousal", "Dominance"]
    "choices": List[str], # the list of possible answers (from the aforementioned mapping)
    "label": int, # the correct answer
}
```

write the resulting jsons in the following two files: ```EmotivITA_dev.jsonl``` and ```EmotivITA_dev.jsonl```


### Prompts

Create ```prompt.jsonl```.
In this file you have to report the prompts you designed for the task. 
Each line in your output file (1 line per prompt) must be a JSON object like the one below:

```JSON
{
    "prompt": "..."
}
```


## Deliver format

You have to format your data using JSON Lines standard.