**HODI**

Link: https://hodi-evalita.github.io/

The HODI shared task is focus on the identification of homotransphobia in Italian tweets.

1. Follow the instruction to obtain the data from : https://github.com/HODI-EVALITA/HODI_2023/
2. Unzip HODI_2023_train.zip

**NOTE**: you are asked to perform _only_ sub-task A.

### Reformat data:

Then, for each sample in the data, create a json entry with the following format

```JSON
{
    "text": str, # the input sentence,
    "choices": list[str],
    "label": int, # the correct answer
}
```

write the resulting jsons in ``HODI_2023``

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
