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

This is a preprocessed version of immo_data.csv following instructions in [**data_prepare_visualize.ipynb**](https://github.com/amirhossein-yousefi/HouseOffers/blob/master/data_prepare_visualize.ipynb) without text data 
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
This part is in the [**xgboost_final.ipynb**](https://github.com/amirhossein-yousefi/HouseOffers/blob/master/xgboost_final.ipynb)

Note: this model is trained on data without description and facilities fields

### AutoGloun(AutoML)
This library contains almost all of ensemble models and some deep models such as BERT
and after data preparation we feed the data into this model which all is in [**auto_gloun_with_text.ipynb**](https://github.com/amirhossein-yousefi/HouseOffers/blob/master/auto_gloun_with_text.ipynb)
and [**autogloun_without_text.ipynb**](https://github.com/amirhossein-yousefi/HouseOffers/blob/master/autogloun_without_text.ipynb)

Note:All log of this model and weights(for with_text config) is [here](https://drive.google.com/drive/folders/1--CnHmK5DsPuEroyeYYCpXYWjCF28HW5?usp=sharing)
and for without_text config model located at [here](https://drive.google.com/drive/folders/13-OYRaLfkvD2X4bvR2qxxWOSltc4f3CF?usp=sharing)

As mentioned, we have two type of data(with and without description and facilities) which we train 
**AutoGloun** model for both of these data

For training the [**auto_gloun_with_text.ipynb**](https://github.com/amirhossein-yousefi/HouseOffers/blob/master/auto_gloun_with_text.ipynb) I have rented a colabPRO(as it is a big model) and it took
about 6 hours to train this model on it as it used pretrained German BERT which is raely a big model.
THe results for data without text(without facilities and description fields)(r2_score) is as following:

<img src="/assets/img/results_without_text_r2score.png" alt="MarineGEO circle logo" style="height:500px; width:500px;"/>

THe results for data with text(without facilities and description fields)(r2_score) is as following:

<img src="/assets/img/r2_score_with_text.png" alt="MarineGEO circle logo" style="height:500px; width:500px;"/>

### GermanBert+MLP(MultiModal):
This is a abstract view of my model:

<img src="/assets/img/over_view_of_model.png" alt="MarineGEO circle logo" style="height:300px; width:300px;"/>

This part is the most sophisticated part of my work
where I combined the feature extracted from the BERT and
numerical and boolean feature to train the final MLP the notebook related
to this is [**German_BERT_rent_prediction.ipynb**](https://github.com/amirhossein-yousefi/HouseOffers/blob/master/German_BERT_rent_prediction.ipynb)

All log of this model and weights are [here](https://drive.google.com/drive/folders/1f-j8H5j_Vnuih6qhps6TGYbbGZkpNuKB?usp=sharing)

As you may know that transformers computation is so high so I rent a **colabPRO** to train this model and takes about 6 hours
to train on 2 epoch and reached to RMSE: 516.35.


NOTE:We must partition data into three chunks of train,validation and test because when we want to
tune the hyperparameters we should not use test data in order no to overestimate the performance of model but as I did not have enough computation
power I just use two chunk of train and test. It is so important that my test data has no contribution to select the hyperparameter of the model so as to prevent model from data leakage.