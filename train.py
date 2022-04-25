import pandas as pd
from autogluon.tabular import TabularDataset, TabularPredictor


def load_data(address: str = 'train_data.csv'):
    data = pd.read_csv(address)
    return data


def train(train, save_dir: str):
    ##train is a panda dataframe which contains label
    hyperparameters = {'AG_IMAGE_NN': {},
                       'AG_TEXT_NN': {'model.hf_text.checkpoint_name': 'bert-base-german-cased',
                                      'optimization.max_epochs': 3},
                       'CAT': {},
                       'GBM': [{},
                               {'ag_args': {'name_suffix': 'XT'}, 'extra_trees': True},
                               'GBMLarge'],
                       'NN_TORCH': {},
                       'VW': {},
                       'XGB': {}}
    train_data = TabularDataset(train)
    label = 'rent'
    predictor = TabularPredictor(label=label, eval_metric='r2', path=save_dir).fit(train_data,
                                                                                   hyperparameters=hyperparameters,
                                                                                   ag_args_fit={'num_gpus': 1})


if __name__ == "__main__":
    data = load_data()
    train(data, 'output')
