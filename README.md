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

immo_data_clean2.csv:

This is a preprocessed version of immo_data.csv following instructions in **data_prepare_visualize.ipynb** without text data 
(description and facilities field )
.This data located at [here](
https://drive.google.com/file/d/1dEWxv9TK6D53t_NK1069FsxMTXubLhO9/view?usp=sharing)

immo_data_clean.csv:
This data is as same as immo_data_clean.csv but with
**facilities** adn **description** columns in order to train the
**BERT** for text.


## Models:
 I have used many models for training on this data such as XgBoost,CatBoost,LightGBM,Neural Nets and for data which
contains text data I have trained a **MultiModal Transformer** which consists of a German
Bert and MLP together.

 
### XgBoost
