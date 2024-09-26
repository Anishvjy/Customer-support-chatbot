# -*- coding: utf-8 -*-
"""chatbot.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1yQz-YcTix2U5lY0Q1NeWZnmDpMD_t6SL
"""

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

def generate_response(user_input, history, tokenizer, model, device):
    # Append the user input to the history with proper special tokens
    history += f"<|user|>{user_input}<|endofturn|>"

    # Encode the input history
    input_ids = tokenizer.encode(history, return_tensors='pt').to(device)

    # Generate the assistant's response
    output_ids = model.generate(
        input_ids,
        max_length=1024,
        pad_token_id=tokenizer.eos_token_id,
        eos_token_id=tokenizer.convert_tokens_to_ids('<|endofturn|>'),
        no_repeat_ngram_size=3,
        do_sample=True,
        top_k=50,
        top_p=0.95,
        temperature=0.75,
    )

    # Decode the generated tokens
    output_text = tokenizer.decode(output_ids[0], skip_special_tokens=False)

    # Extract the assistant's latest response
    assistant_response = ''
    splits = output_text.split('<|assistant|>')
    if len(splits) > 1:
        assistant_response = splits[-1]
        assistant_response = assistant_response.split('<|endofturn|>')[0].strip()
    else:
        assistant_response = "I'm sorry, I didn't catch that. Could you please repeat?"

    # Update the history with the assistant's response
    history += f"<|assistant|>{assistant_response}<|endofturn|>"

    return assistant_response, history

if __name__ == '__main__':
    # Load the tokenizer and model
    model_path = 'models/chatbot_model'
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)

    # Move the model to the appropriate device
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model.to(device)

    history = ''

    print("Chatbot is ready! Type 'exit' or 'quit' to end the conversation.\n")

    while True:
        user_input = input('User: ')
        if user_input.lower() in ['exit', 'quit']:
            print('Ending conversation.')
            break
        bot_response, history = generate_response(user_input, history, tokenizer, model, device)
        print(f'Assistant: {bot_response}\n')