# Text-Summerizer-v2.0
## #OVERVIEW 📕
☞ Summary generation is a natural language processing task that involves creating a concise and coherent summary of a longer piece of text. There are various ways to approach this task, ranging from simple rule-based methods to more complex machine learning models. In this blog post, we will look at three different approaches for generating summaries: using a pre-trained language model, using a TfidfVectorizer, and using nltk's cosine distance.

☞ The first approach involves using a TfidfVectorizer to generate a summary. This approach involves creating a vector representation of each sentence in the text and then ranking the sentences based on their relevance. To implement this approach, we first need to import the required libraries and create a summarizer function that takes in a piece of text and returns the summary. The function begins by tokenizing the text using spacy and then creating a TfidfVectorizer object. The TfidfVectorizer is then fit on the list of sentences and used to transform the sentences into vectors. The vectors are then summed and the top N sentences are selected as the summary, where N is the number of sentences we want in the summary.

☞ The second approach involves using nltk's cosine distance to generate a summary. This approach involves measuring the similarity between sentences and selecting the most similar sentences as the summary. To implement this approach, we first need to import the required libraries and create a generate_summary function that takes in a file name and returns the summary. The function begins by reading in the file and tokenizing the sentences using nltk's stopwords. Next, a similarity matrix is created by comparing each sentence to every other sentence in the text. The matrix is then converted into a graph using networkx and the PageRank algorithm is used to rank the sentences based on their importance. The top N sentences are then selected as the summary.

☞ The third approach involves using a pre-trained language model, such as T5, to generate a summary. The T5 model was trained on a large dataset of text and is able to generate human-like summaries by predicting the next word in a sequence. To use this approach, we first need to install the required libraries and load the data. We can then create a NewsSummaryDataset and a NewsSummaryDataModule to handle the data processing and loading. Next, we can define our model by creating a T5ForConditionalGeneration model and specifying the hyperparameters. Finally, we can train the model by defining an AdamW optimizer and a ModelCheckpoint callback to save the model weights at each epoch.


## #MODELS 🏆
☞[`HEADLINE`](https://drive.google.com/file/d/1o6gA5ofRYUL0jCUtjrNcnt2SJN_tAi2n/view?usp=sharing) MODEL

☞[`SUMMARY 3`](https://drive.google.com/file/d/1P87tKfRhVCUtMRDJwh21zs1SSRcTwLY9/view?usp=sharing) MODEL


## #BLUEPRINT 🛰️
🛑 All files must be arrange in given manner (including MODELS) 🛑

``` bash
Text-Summarizer-v2.0
|
│   content.txt
│   headline.py
│   main.py
│   pdf_txt.py
│   README.md
│   requirements.txt
│   summarizer1.py
│   summarizer2.py
│   summarizer3.py   
│   
├───models
│   ├───headline_model
│   │       config.json
│   │       pytorch_model.bin
│   │       special_tokens_map.json
│   │       spiece.model
│   │       tokenizer.json
│   │       tokenizer_config.json
│   │       
│   └───summary_model
│          best-checkpoint.ckpt
│          model.py
│                      
├───screenshots
│       Exception.png
│       File_upload.png
│       Home.png
│       summary_of _uploaded file.png
│       Summery_of_inputText.png
│       Text_input.png
│       
└───uploaded_pdfs
       Independence.pdf
```

## #EXPLAINED IN DETAIL...🌐


## #OUTPUTS 🚀
☞ IN [`screenshots`](https://github.com/shrey-patel-3287/Text-Summerizer-v2.0/tree/main/screenshots) FOLDER


## #ISSUES 💀
☞ Headline only work properly if given input is news article.

☞ We are working on it...........
