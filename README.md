# NLP-EXAM-23
The current repository holds the code for our exam project for the Natural Language Processing (NLP) exam at the Cognitive Science MSc 2023, Aarhus University. 
Be aware, that this repository do not hold any data as we do not own it. However, the exact data we used can be extracted following the steps provided in the scraping pipeline, and in this way the entire analysis can be replicated. 

The project was developed by `Laura Paaby` and `Emma Olsen`. 

## Pipeline

## 1. Data Extraction 
### Step 1: Activate environment
To run the scripts below, a virtual environment must be initiated containing the installments required. 
```
source setup.sh
```

### Step 2: Fetch URLS 
URLs to all concert reviews from Ekstra Bladet were collected using webscraper.io. The scraped articles themselves are not shared on this repository, but all code used to fetch the articles are shared for transparency. The fetched URLs can be seen in the csv file `scrape/webscraper_eb_urls.csv`. 


### Step 3: Scrape URLS

To scrape the EB articles, run the following script:

```
python scrape/scraping_eb.py
```

### Step 4: Replace Artist Name and Pronouns 
To replace out names and pronouns of the artist in each article with the gender-neutral: "artist/artist's", run the following script:
```
python analysis/mask_name_gender.py
```



## 2. nb-BERT-large 🤖🤖🤖🤖🤖
 
### Step 2.0 Data preprocessing
To execute this step, run:
```
python BERT/prep_df_for_distmBERT.py
```
<br>

_Now we are leaving scripts behind, and enter the realm of notebooks, as the remaining parts have been executed in Google Colab_

### Step 2.1 Hyperparameter Tuning
We hyperparameter tune the nb-BERT-large model on the validation data prior to fine-tuning using `Optuna`. This step results in finding the optimal hyperparameters.  
To execute this step, run the [`nb_BERT_large/nbl_OPTUNA_param_tune.ipynb`](https://github.com/laurawpaaby/NLP23_exam_BERT/blob/main/nb_BERT_large/nbL_OPTUNA_param_tune.ipynb) 

### Step 2.2: Fine-tuning and Classification
We fine-tune the nb-BERT-large model with the hyperparameters found above on the validation data. The fine-tuned model yielding the lowest loss is found at step 174, epoch 3. We employ this model to the classification task on the test data. 
To execute this step, run the [`nb_BERT_large/nbL_Finetune_opt_param.ipynb`](https://github.com/laurawpaaby/NLP23_exam_BERT/blob/main/nb_BERT_large/nbL_Finetune_opt_param.ipynb)

### Step 2.3: Classification with the Pre-fine-tuned Model.
We employ the model prior fine-tuning to the classification task on the test data. This model have never seen any of the data before. 
To execute this step, run the [`nb_BERT_large/nbL_pretrained_class.ipynb`](https://github.com/laurawpaaby/NLP23_exam_BERT/blob/main/nb_BERT_large/nbL_Pretrained_class.ipynb) 

Now the classification performance of the model prior to and post fine-tuning can be compared. 

## 3. Integrated Gradients (IG) and Differentials 🔦🔦🔦🔦

### Step 3.0: IG from nb-BERT-large Prior to Fine-tuning
We extract the _Integrated Gradients_ from the nb-BERT-large model prior to fine-tuning. 
To execute this step, run the [`IG/IG_pretrained.ipynb`](https://github.com/laurawpaaby/NLP23_exam_BERT/blob/main/IG/IG_pretrained.ipynb). 

### Step 3.1: IG from nb-BERT-large Post Fine-tuning
We extract the _Integrated Gradients_ from the nb-BERT-large model post fine-tuning. Thus, the at checkpoint-174 is loaded and used for the extraction.  
To execute this step, run the [`IG/IG_nbl_FT.ipynb`](https://github.com/laurawpaaby/NLP23_exam_BERT/blob/main/IG/IG_nbl_FT.ipynb).

### Step 3.2: IG Differentials 
We find the _Integrated Gradients Differentials_ by substracting the absolute values found by the model prior to fine-tuning from the ones found post fine-tuning. This is done for male and female predictions respectively and visualised. 
To execute this step, run the [`IG/IG_DIFFERENTIALS.ipynb`](https://github.com/laurawpaaby/NLP23_exam_BERT/blob/main/IG/IG_DIFFERENTIALS.ipynb).



### *Enjoy!*
