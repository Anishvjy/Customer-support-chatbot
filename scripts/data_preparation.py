# -*- coding: utf-8 -*-
"""data_preparation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Fi2BBMa9D7UDEIowYInhSavXwtD5eVqq
"""

import os
import json

def load_taskmaster_data():
    all_conversations = []

    # Load Taskmaster-1 data
    tm1_dir = 'Taskmaster/TM-1-2019'
    if os.path.exists(tm1_dir):
        tm1_files = ['woz-dialogs.json', 'self-dialogs.json']
        for file in tm1_files:
            file_path = os.path.join(tm1_dir, file)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    all_conversations.extend(data)
            else:
                print(f"File {file} does not exist in Taskmaster-1 directory.")
    else:
        print(f"Directory {tm1_dir} does not exist.")

    # Load Taskmaster-2 data
    tm2_dir = 'Taskmaster/TM-2-2020/data'
    if os.path.exists(tm2_dir):
        tm2_files = [f for f in os.listdir(tm2_dir) if f.endswith('.json')]
        for file in tm2_files:
            file_path = os.path.join(tm2_dir, file)
            if os.path.exists(file_path):
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    if isinstance(data, list):
                        all_conversations.extend(data)
                    elif isinstance(data, dict):
                        if 'dialogs' in data:
                            all_conversations.extend(data['dialogs'])
                        else:
                            print(f"Unknown data format in {file}.")
                    else:
                        print(f"Unexpected data type in {file}.")
            else:
                print(f"File {file} does not exist in Taskmaster-2 data directory.")
    else:
        print(f"Directory {tm2_dir} does not exist.")

    return all_conversations

def preprocess_conversations(conversations):
    dialogue_texts = []
    for convo in conversations:
        dialogue = ''
        if 'utterances' in convo:
            for utterance in convo['utterances']:
                speaker = utterance.get('speaker', '').upper()
                text = utterance.get('text', '').strip()
                if speaker == 'USER':
                    dialogue += f'<|user|>{text}<|endofturn|>'
                elif speaker in ['ASSISTANT', 'AGENT', 'SYSTEM']:
                    dialogue += f'<|assistant|>{text}<|endofturn|>'
                else:
                    dialogue += f'<|{speaker.lower()}|>{text}<|endofturn|>'
            dialogue_texts.append(dialogue)
        else:
            print("No 'utterances' key in conversation.")
    return dialogue_texts

if __name__ == '__main__':
    # Load conversations
    conversations = load_taskmaster_data()
    print(f'Total conversations loaded: {len(conversations)}')

    # Preprocess conversations
    dialogue_texts = preprocess_conversations(conversations)
    print(f'Total dialogues processed: {len(dialogue_texts)}')

    # Save preprocessed dialogues
    os.makedirs('data', exist_ok=True)
    with open('data/dialogue_texts.txt', 'w', encoding='utf-8') as f:
        for dialogue in dialogue_texts:
            f.write(dialogue + '\n')