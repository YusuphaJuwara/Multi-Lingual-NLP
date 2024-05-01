import os
import csv
import json
import pandas as pd
import copy
import random
# random.seed(49)

def emotivITA(input_file_path: str, 
              output_file_path: str, 
              float_to_cat_list: list[str], 
              shuffle_labels: bool=False, 
              verbose: bool=False
              ) -> None :
    """Reformat the data in the input file to a JSONL format in the output file.

    Args:
        input_file_path (str): a valid path to the input file
        output_file_path (str): a non-valid path to the output file. Need to add one from ['Valence', 'Arousal', 'Dominance']. 
        E.g., output_file_path.format('Dominance') =  HM1_A-1\EmotivITA\EmotivITA_Dominance_dev.jsonl
        float_to_cat_list: list[str]: a list of categorical values.
        shuffle_labels (bool, optional): Shuffle the choices so that the model learns not just the ordering of the labels, 
    but the actual semantic meaning of them. Defaults to False.
        verbose (bool, optional): whether to print or not. Defaults to False. Defaults to False.
        
    Raises:
        ValueError: If the file extension is not .tsv or .csv.
        
    Returns:
        None
        
    Examples:
        emotivITA('HM1_A-1936515\EmotivITA\Development set.csv', 
                'HM1_A-1936515\EmotivITA\EmotivITA_{}_dev.jsonl',
                float_to_cat_list=['Bassa', 'Media', 'Alta', 'Molto Alta'],
                shuffle_labels=True,
                verbose=True)
    """
    
    file_extension = input_file_path.split('.')[-1]
    print(f"File extension: {file_extension}")

    # Read the data from a .tsv or .csv file
    if file_extension == 'tsv':
        data = pd.read_csv(input_file_path, sep='\t')
    elif file_extension == 'csv':
        data = pd.read_csv(input_file_path)
    else:
        raise ValueError(f'Invalid file format for the file: {input_file_path}. Only .tsv and .csv files are supported.')
    
    # Create a list for each item to store the jsonl entries
    jsonl_entry_V = []
    jsonl_entry_A = []
    jsonl_entry_D = []
    
    if args.map_option == 0:
        count_each_label = {'Bassa': 0, 'Media': 0, 'Alta': 0}
    else:
        count_each_label = {'Bassa': 0, 'Media': 0, 'Alta': 0, 'Molto Alta': 0}
        
    # Iterate over each row in the data
    for index, row in data.iterrows():
        text = row['text']
        V = float(row['V'])
        A = float(row['A'])
        D = float(row['D'])
        
        v = map_float_to_cat_idx(V)
        a = map_float_to_cat_idx(A)
        d = map_float_to_cat_idx(D)
        
        if shuffle_labels:
            shuffle_choices_v, shuffle_label_v = shuffle_labels_func(float_to_cat_list, v, verbose)
            count_each_label[shuffle_choices_v[shuffle_label_v]] += 1
            
            shuffle_choices_a, shuffle_label_a = shuffle_labels_func(float_to_cat_list, a, verbose)
            count_each_label[shuffle_choices_a[shuffle_label_a]] += 1
            
            shuffle_choices_d, shuffle_label_d = shuffle_labels_func(float_to_cat_list, d, verbose)
            count_each_label[shuffle_choices_d[shuffle_label_d]] += 1

            if index >= 5: 
                verbose = False
            else:
                print(f"""{shuffle_choices_v[shuffle_label_v]=}, \t{shuffle_choices_a[shuffle_label_a]=}, \t{shuffle_choices_d[shuffle_label_d]=}
                      \n{count_each_label=}
                      """)
                print(f"{float_to_cat_list=}, \t{shuffle_choices_d=}")
        
        # Create a jsonl entry.
        # Add the dimension so that the model can differentiate between the three dimensions.
        # Said by one of the TAs on Google Classroom.
        jsonl_entry_V.append(
            {
                'text': text,
                'choices': shuffle_choices_v,
                'label': shuffle_label_v,
                'dimension': 'Valence'
            }
        )
        jsonl_entry_A.append(
            {
                'text': text,
                'choices': shuffle_choices_a,
                'label': shuffle_label_a,
                'dimension': 'Arousal'
            }
        )
        jsonl_entry_D.append(
            {
                'text': text,
                'choices': shuffle_choices_d,
                'label': shuffle_label_d,
                'dimension': 'Dominance'
            }
        )
    
    print(f"End -- {count_each_label=}")

    # Write the jsonl entries for each item to a file
    open_and_write_jsonl(output_file_path.format('Valence'), jsonl_entry_V)
    open_and_write_jsonl(output_file_path.format('Arousal'), jsonl_entry_A)
    open_and_write_jsonl(output_file_path.format('Dominance'), jsonl_entry_D)
    
def open_and_write_jsonl(output_file_path: str, 
                         jsonl_entries: list[dict]
                         ) -> None:
    """Takes a list of jsonl entries and writes them to a file.

    Args:
        output_file_path (str): a valid path to the output file
        jsonl_entries (list(Dict)): a list of jsonl entries
        
    Returns:
        None
        
    Example:
        open_and_write_jsonl('HM1_A-1\EmotivITA\EmotivITA_{Dominance}_dev.jsonl', jsonl_entries)
    """
    # Write the jsonl entries to a file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for entry in jsonl_entries:
            json_string = json.dumps(entry, ensure_ascii=False)
            f.write(json_string + '\n')
            
    print('Data written successfully to:', output_file_path, '!')
    
def map_float_to_cat_idx(float_value: float) -> int:
    """This function maps a float value to the index of the corresponding category.
    
    If map_option == 0:
        [0.0,2.5) -> "bassa" -> idx 0 \\
        [2.5, 4.0) -> "media" -> idx 1 \\
        [4.0, 5.0] -> "alta" -> idx 2 \\
        
    If map_option == 1:
        "Bassa" (Low): 0 ≤ value < 1.25 -> idx 0 \\
        "Media" (Medium): 1.25 ≤ value < 2.5 -> idx 1 \\
        "Alta" (High): 2.5 ≤ value < 3.75 -> idx 2 \\
        "Molto Alta" (Very High): 3.75 ≤ value ≤ 5 -> idx 3 \\

    Args:
        float_value (float): A float value from the dataset in range [0.0,5.0]

    Returns:
        int: The index of the category that the float value belongs to.
    """
    
    if args.map_option == 0:
        if float_value < 3.2:
            return 0
        elif float_value < 3.8:
            return 1
        else:
            return 2
    else:
        if float_value < 1.25:
            return 0
        elif float_value < 2.5:
            return 1
        elif float_value < 3.75:
            return 2
        else:
            return 3
    
def shuffle_labels_func(float_to_cat_list: list[str], 
                        label_index: int, 
                        verbose: bool=False
                        ) -> tuple[list[str], int] :
    """Shuffle the choices so that the model learns not just the ordering of the labels, 
    but the actual semantic meaning of them. 
    Note that there is a paper on this that models sometimes memorize the ordering of the labels, 
    and that if the ordering is changed, there may be some (drastic) drop in accuracy.

    Args:
        float_to_cat_list (list(str)): the string of choices to shuffle
        label_index (int): the index of the choice that is true among the choices
        verbose (bool, optional): whether to print or not. Defaults to False.

    Returns:
        choices (list(str)): the shuffled choices (float_to_cat_list)
        label_index (int): the shuffle index of the original choice in the shuffled choices
    """
    
    choices = copy.deepcopy(float_to_cat_list)
    
    # Get the labels from the choices. str
    label_str = choices[label_index]
    if verbose: print(f"Before shuffle {choices=}, {label_str=}, {label_index=}")

    # shuffle labels so that the model doesn't memorize the ordering.
    random.shuffle(choices)
    
    # Get the index of the original label in the shuffled choices
    label_index = choices.index(label_str)
    if verbose: print(f"After shuffle {choices=}, {label_str=}, {label_index=}")
    
    # Return the shuffled choices and the index of the original label.
    return choices, label_index

if __name__ == '__main__':
    
    # Download the EmotivITA dataset files from the URL 
    # and save them to the specified path
    from download_data import download_csv_files
    
    import argparse
    parser = argparse.ArgumentParser(description='Args to be used')
    parser.add_argument(
        "--test",
        action='store_true',
        default=False,
        help="Whether to use the development set or the test set (e.g., --test)"
    )
    parser.add_argument(
        "--shuffle_labels",
        action='store_true',
        default=False,
        help="Whether to shuffle the labels. This way the model will not just memorize the ordering."
    )
    parser.add_argument(
        "--verbose",
        action='store_true',
        default=False,
        help="Whether to print before and after the shuffle."
    )
    parser.add_argument(
        "--map_option",
        type=int,
        default=0,
        help="""0 for   [0.0, 2.5) -> "Bassa"
                        [2.5, 4.0) -> "Media"
                        [4.0, 5.0] -> "Alta" \n
                        AND \n
                1 for   [0.0,1.25) -> "Bassa"
                        [1.25, 2.5) -> "Media"
                        [2.5, 3.75) -> "Alta"
                        [3.75, 5] -> "Molto Alta"
                        """
    )
    parser.add_argument(
        "--download",
        action='store_true',
        default=False,
        help="Whether to download the EmotivITA dataset or not."
    )
    args = parser.parse_args()
    
    # If true, then use the test set instead of the development set.
    if args.test:
        input_file_path = 'EmotivITA\save_folder\Test set - Gold labels.csv'
        output_file_path = 'EmotivITA\EmotivITA_{}_test.jsonl'
    else:
        input_file_path = 'EmotivITA\save_folder\Development set.csv'
        output_file_path = 'EmotivITA\EmotivITA_{}_dev.jsonl'
        
    if args.map_option == 0:
        float_to_cat_list = ['Bassa', 'Media', 'Alta']
    elif args.map_option == 1:
        float_to_cat_list = ['Bassa', 'Media', 'Alta', 'Molto Alta']
    else:
        raise ValueError("args.map_option must be 0 or 1")
    
    repo_url = "https://api.github.com/repos/GiovanniGafa/EmoITA/contents/"
    save_folder = "EmotivITA/save_folder"

    # Create the save folder if it doesn't exist
    os.makedirs(save_folder, exist_ok=True)

    download_csv_files(repo_url, save_folder)
    
    emotivITA(input_file_path, output_file_path, float_to_cat_list, args.shuffle_labels, args.verbose)
    
    
    
