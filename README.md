# NLP-EXAM-23
The current repository holds the code for our exam project for the Natural Language Processing (NLP) exam at the Cognitive Science MSc 2023, Aarhus University. 

The project was developed by `Laura Paaby` and `Emma Olsen`. 

## Pipeline

### Step 1: Activate environment
```
source setup.sh
```

### Step 2: Fetch URLS & clean them
```
```

### Step 3: Scrape URLS
```
```

### Step 4: Extract Information from URLS using Mistral
```
```

### Step 5: Replace artist name and pronouns with the gender-neutral: "artist/artist's"
```
python analysis/mask_name_gender.py
```



### Step n: Applying Distil Multilingual BERT
##### Step n.0 
Preprocess data:
```
python BERT/prep_df_for_distmBERT.py
```

##### Step n.1
Finetune the Distil Multilingual BERT on articles 
```
python BERT/dist_m_BERT_finetune.py
```
##### Step n.2: employ models for classification
Use the pretrained but not finetuned Distil Multilingual BERT and the finetuned Distil Multilingual BERT.
```
python BERT/dist_m_BERT_raw.py
python BERT/ ??!??!?!?!?!?
```
##### Step n.3:
get the attention weigths somehow :D 



