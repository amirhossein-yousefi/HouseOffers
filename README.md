# Rental offers

```angular2html
docker-compose up -d
```

# Model versioning
This part is done using following steps:

Installation:
```
pip install --upgrade pip
pip install dvc
then:
dvc add #the name of your data or model(deep model or ML one)#
git add #the .dvc file #
dvc push
git push
```
As I did not have such cloud storage so dvc push won't work.
I just give the link of google drive for each data bellow:
## Data
immo_data.csv:
 
This original data located at [here](
https://drive.google.com/file/d/1Y6SIw4bsiULgjMMb6ePp7vjFi-SrVOpi/view?usp=sharing)

immo_data_clean.csv:

This is a preprocessed version of immo_data.csv following instructions in **data_prepare_visualize.ipynb** without text data 
(description and facilities field )
.This data located at [here](https://drive.google.com/file/d/1Imn04Y4tECUzDHU-0CjYhSXrv0VehGHb/view?usp=sharing)

immo_data_clean2.csv:
This data is as same as immo_data_clean.csv but with
**facilities** adn **description** columns in order to train the
**BERT** for text.
This data located at
[here](
https://drive.google.com/file/d/1dEWxv9TK6D53t_NK1069FsxMTXubLhO9/view?usp=sharing)


## Models:
 I have used many models for training on this data such as XgBoost,CatBoost,LightGBM and Neural Nets and for data which
contains text data(description and facilities fields included) I have trained a **MultiModal Transformer** which consists of a German
Bert and MLP together.

Note:Ensemble models perform better than Deep models
for tabular data as our data is tabular, I follow almost all 
ensemble models(catboost,xgboost,LightGBM,CatBoost)
 
### XgBoost
This model is based on gradient boosting and is one of the ensemble methods which is
so powerful for tabular data.
This part is in the **xgboost_final.ipynb**

Note: this model is trained on data without description and facilities fields

### AutoGloun(AutoML)
This library contains almost all of ensemble models and some deep models such as BERT
and after data preparation we feed the data into this model which all is in **auto_gloun_with_text.ipynb**
and **autogloun_without_text.ipynb**
Note:All log of this model and weights(for with_text config) is [here](https://drive.google.com/drive/folders/1--CnHmK5DsPuEroyeYYCpXYWjCF28HW5?usp=sharing)
and for without_text config model located at [here](https://drive.google.com/drive/folders/13-OYRaLfkvD2X4bvR2qxxWOSltc4f3CF?usp=sharing)

THe results is as following:
<img src="/assets/img/results_without_text_r2score.png" alt="MarineGEO circle logo" style="height:500px; width:500px;"/>

### GermanBert+MLP(MultiModal):
This part is the most sophisticated part of my work
where I combined the feature extracted from the BERT and
numerical and boolean feature to train the final MLP the notebook related
to this is **German_BERT_rent_prediction.ipynb**
All log of this model and weights are [here](https://drive.google.com/drive/folders/1f-j8H5j_Vnuih6qhps6TGYbbGZkpNuKB?usp=sharing)

