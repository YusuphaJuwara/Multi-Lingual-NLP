# Homework 1 A

## Task 1, Sub Task A

In each of these prompts, the LLM is presented with a clear task: to choose either "True" or "False" based on whether the given text contains homotransphobic hate speech or not. The prompts are designed to encourage the LLM to reason about the language used, consider the potential impact on marginalized communities, and make an informed decision while upholding the principles of inclusivity and respect.

The explanations provided for each prompt highlight the specific context or perspective that the prompt aims to emphasize, such as content moderation, societal responsibility, promoting diversity and inclusivity, or appealing to the LLM's sense of conscientiousness. By framing the task in different ways, these prompts encourage the LLM to approach the problem from various angles, ensuring a more comprehensive and nuanced understanding of the complexities involved in identifying and addressing hate speech.

- "Prompt 1 appeals to the LLM's sense of conscientiousness and responsibility, prompting it to carefully evaluate the language used and consider the potential harmful impact of such language on marginalized communities."
- "Prompt 2 frames the task within the context of promoting diversity and inclusivity, encouraging the LLM to consider the importance of creating a safe and welcoming environment for all individuals, regardless of their identities."
- "Prompt 3 emphasizes the societal responsibility of identifying and addressing hate speech, prompting the LLM to consider the potential consequences of such language and the importance of promoting inclusivity and understanding."
- "Prompt 4 frames the task in the context of content moderation, encouraging the LLM to consider the potential impact of the language on marginalized groups and the importance of fostering a safe and welcoming environment."
- "Prompt 5 is straightforward and direct, asking the LLM to focus solely on identifying the presence or absence of homotransphobic language in the text, without requiring any additional reasoning or explanation."

- To run the script, cd to the Home directory 'HM1_A-1936515' and run:

```bash
python "./HM1_A-1936515/HODI_2023/scripts.py" --shuffle_labels --verbose
```

Remove the `--shuffle_labels` option if you don't want to shuffle the labels. Do similar for the verbose option.

## Task 0

### Prompt motivation

Prompt 1 allows the model to focus on identifying the level of one emotional dimension (Valence, Arousal, or Dominance) expressed in the text. By providing options for each dimension separately, the model can learn to associate the emotional content of the text with the appropriate dimension.

Prompt 2 places the model in the role of a psychologist studying human emotions, prompting it to analyze the emotional content of the text in terms of one dimension. By considering each dimension separately, the model can learn to discern different aspects of emotional expression.

Prompt 3 directs the model to consider the level of one emotional dimension expressed in the text. By providing separate options for each dimension, the model can learn to associate specific emotional states with the corresponding dimension.

Prompt 4 prompts the model to analyze the text and identify the level of one emotional dimension conveyed in the text. By providing separate options for each dimension, the model can learn to associate different emotional expressions with the appropriate dimension.

Prompt 5 encourages the model to approach the text from the perspective of a researcher analyzing human emotions, prompting it to identify the level of one emotional dimension expressed in the text. By considering each dimension separately, the model can learn to recognize and interpret various emotional states.
