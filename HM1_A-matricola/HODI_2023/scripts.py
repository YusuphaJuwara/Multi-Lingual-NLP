import os
import csv
import json
import pandas as pd

def hodi_a(input_file_path, output_file_path, shuffle_labels=False, verbose=False):
    """Reformat the data in the input file to a JSONL format in the output file.

    Args:
        input_file_path (str): a valid path to the input file
        output_file_path (str): a valid path to the output file. 
        shuffle_labels (bool, optional): Shuffle the choices so that the model learns not just the ordering of the labels, 
    but the actual semantic meaning of them. Defaults to False.
        verbose (bool, optional): whether to print or not. Defaults to False. Defaults to False.
        
    Raises:
        ValueError: If the file extension is not .tsv or .csv.
        
    Returns:
        None
        
    Examples:
        hodi_a('HM1_A-1936515\HODI_2023\subtaskA-train.tsv', 
                'HM1_A-1936515\HODI_2023\subtaskA-train.jsonl',
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
    
    # Create a list to store the jsonl entries
    jsonl_entries = []

    # Iterate over each row in the data
    for index, row in data.iterrows():
        text = row['text']
        label = row['homotransphobic']
        
        # Define the choices. 
        # This will be modified inplace by the random.shuffle, so instantiate every time.
        choices = ['Vero', 'Falso']
        
        if shuffle_labels:
            shuffle_choices, shuffle_label = shuffle_labels_func(choices, label, verbose)
            if index >= 12: verbose = False
        
        # Create a jsonl entry
        jsonl_entry = {
            'text': text,
            'choices': shuffle_choices,
            'label': shuffle_label
        }
        
        jsonl_entries.append(jsonl_entry)

    # Write the jsonl entries to a file
    with open(output_file_path, 'w', encoding='utf-8') as f:
        for entry in jsonl_entries:
            json_string = json.dumps(entry, ensure_ascii=False)
            f.write(json_string + '\n')

    print('Data written to: %s' % output_file_path)
    
def shuffle_labels_func(choices, label_index, verbose=False):
    """Shuffle the choices so that the model learns not just the ordering of the labels, 
    but the actual semantic meaning of them. 
    Note that there is a paper on this that models sometimes memorize the ordering of the labels, 
    and that if the ordering is changed, there may be some (drastic) drop in accuracy.

    Args:
        choices (list(str)): the string of choices to shuffle
        label_index (int): the index of the choice that is true among the choices
        verbose (bool, optional): whether to print or not. Defaults to False.

    Returns:
        choices (list(str)): the shuffled choices
        label_index (int): the shuffle index of the original choice in the shuffled choices
    """
    import random
    # random.seed(49)
    
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
    
    # Download the password-protected HODI dataset zip file from the URL 
    # and save it to the specified path
    from download_data import download_and_unzip
    
    import argparse
    parser = argparse.ArgumentParser(description='Args to be used in the HODI task')
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
        help="Whether to before and after the shuffle."
    )
    parser.add_argument(
        "--download",
        action='store_true',
        default=False,
        help="Whether to download the HODI dataset or not."
    )
    args = parser.parse_args()
    
    # URL and file paths
    zip_url = "https://github.com/HODI-EVALITA/HODI_2023_data/raw/main/HODI_2023_train.zip"
    zip_save_path = "HODI_2023/save_folder/HODI_2023_train.zip"
    extract_dir = "HODI_2023/save_folder/HODI_2023_train"
    
    if args.download:
        # Create the save folder if it doesn't exist
        os.makedirs("HODI_2023/save_folder", exist_ok=True)
        download_and_unzip(zip_url, zip_save_path, extract_dir)

    input_file_path = os.path.join(extract_dir, 'HODI_2023_train_subtaskA.tsv')
    output_file_path = 'HODI_2023\HODI_2023_train_subtaskA.jsonl'
    
    hodi_a(input_file_path, output_file_path, shuffle_labels=args.shuffle_labels, verbose=args.verbose)
    

