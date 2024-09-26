
%%writefile README.md
# Chatbot Model Using DialoGPT and Taskmaster Dataset

This project involves fine-tuning Microsoft's DialoGPT model on the Taskmaster dataset to create a conversational chatbot capable of handling task-oriented dialogues.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Results](#results)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This project demonstrates how to fine-tune a pre-trained language model for task-oriented dialogue systems. The chatbot is trained on the Taskmaster dataset and can handle conversations related to booking, reservations, and general inquiries.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/chatbot-model.git

2. Navigate to the project directory:

   cd chatbot-model

3. Install the required packages:

    pip install -r requirements.txt

##  Usage

To interact with the chatbot:

```bash
python scripts/chatbot.py

## Dataset

The Taskmaster dataset is a collection of goal-oriented dialogues. It's used to train the chatbot to handle real-world conversations. More information can be found [here](https://github.com/google-research-datasets/Taskmaster).

**Note:** Ensure you have the rights to include or reference the dataset in your project.


## Model Training

The model was fine-tuned using the Hugging Face Transformers library. Training scripts and notebooks are provided in the `notebooks/` and `scripts/` folders.

Steps included:

- Loading and preprocessing the data.
- Tokenizing and encoding.
- Fine-tuning the DialoGPT-small model.
- Saving the trained model.

## Results

- **Perplexity:** Achieved a perplexity score of 4.74 on the validation set.
- **Sample Conversations:** User: Hi, I need to book a table for tonight. 
                            Assistant: Sure, for how many people?

## Folder Structure

chatbot-model/
├── data/
│   ├── data_guide.py
│   
├── logs/
│   ├── events.out.tfevents.xxxxxx
│   └── training.log
├── models/
│   └── saved_models/
│       └── chatbot_model/
│           ├── config.json
│           ├── generation_config.json
│           ├── pytorch_model.bin
│           └── special_tokens_map.json
├── notebooks/
│   └── Customer_support_chatbot_code.py
├── scripts/
│   ├── chatbot.py
│   └── data_preparation.py
│   └── train_model.py
├── requirements.txt
├── .gitignore
├── README.md
└── other_project_files

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

**Your Name** - [anishvijayvergiya1010@gmail.com](mailto:anishvijayvergiya1010@gmail.com)

Project Link: [https://github.com/Anishvjy/chatbot-model](https://github.com/Anishvjy/chatbot-model)






