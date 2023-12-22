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



## Step n: nb-BERT-large 🤖🤖🤖🤖🤖
 
### Step n.0 Data preprocessing
To execute this step, run:
```
python BERT/prep_df_for_distmBERT.py
```
<br>
<br>
_Now we are leaving scripts behind, and enter the realm of notebooks, as the remaining parts have been executed in Google Colab._
### Step n.1 Hyperparameter Tuning
We hyperparameter tune the nb-BERT-large model on the validation data prior to fine-tuning using `Optuna`. This step results in finding the optimal hyperparameters.  
To execute this step, run the [`nb_BERT_large/nbL_OPTUNA_param_tune.ipynb`](https://github.com/laurawpaaby/NLP23_exam_BERT/blob/main/nb_BERT_large/nbL_OPTUNA_param_tune.ipynb) 

### Step n.2: Fine-tuning and Classification
We fine-tune the nb-BERT-large model with the hyperparameters found above on the validation data. The fine-tuned model yielding the lowest loss is found at step 174, epoch 3. We employ this model to the classification task on the test data. 
To execute this step, run the [Optuna Model!!](https://github.com/laurawpaaby/NLP23_exam_BERT/blob/main/nb_BERT_large/nbL_Finetune_opt_param.ipynb) 

### Step n.3: Classification with the Pre-fine-tuned Model.
We employ the model prior fine-tuning to the classification task on the test data. This model have never seen any of the data before. 
To execute this step, run the [`nb_BERT_large/nbL_pretrained_class.ipynb`](https://github.com/laurawpaaby/NLP23_exam_BERT/blob/main/nb_BERT_large/nbL_Pretrained_class.ipynb) 

Now the classification performance of the model prior to and post fine-tuning can be compared. 

## Step n+1: Intergrated Gradients (IG) and Differentials 🔦🔦🔦🔦

### Step n.8: IG from nb-BERT-large Prior to Fine-tuning
We extract the _Intergrated Gradients_ from the nb-BERT-large model prior to fine-tuning. 
To execute this step, run the [`IG/IG_pretrained.ipynb`](https://github.com/laurawpaaby/NLP23_exam_BERT/blob/main/IG/IG_pretrained.ipynb). 

### Step n.9: IG from nb-BERT-large Post Fine-tuning
We extract the _Intergrated Gradients_ from the nb-BERT-large model post fine-tuning. Thus, the at checkpoint-174 is loaded and used for the extraction.  
To execute this step, run the [`IG/IG_nbl_FT.ipynb`](https://github.com/laurawpaaby/NLP23_exam_BERT/blob/main/IG/IG_nbl_FT.ipynb).

### Step n.10: IG Differentials 
We find the _Intergrated Gradients Differentials_ by substracting the absolute values found by the model prior to fine-tuning from the ones found post fine-tuning. This is done for male and female predictions respectively and visualised. 
To execute this step, run the [`IG/IG_DIFFERENTIALS.ipynb`](https://github.com/laurawpaaby/NLP23_exam_BERT/blob/main/IG/IG_DIFFERENTIALS.ipynb).


