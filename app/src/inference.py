from autogluon.tabular import TabularDataset, TabularPredictor
import pandas as pd


def load_data(address: str = 'test_data.csv'):
    ##Note that this data must follow the preprocess and the put here
    data = pd.read_csv(address)
    return data


def prediction(test_data):
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
    ##test_data is a dataframe wchich contains its labels
    test_data = TabularDataset(test_data)
    label = 'rent'
    predictor = TabularPredictor(label=label, eval_metric='r2').load('final_outs_agModels-predictClass_with_text drive')
    predictions = predictor.predict(test_data)
    perf = predictor.evaluate_predictions(y_true=test_data['rent'], y_pred=predictions, auxiliary_metrics=True)

    return perf, predictor.leaderboard(test_data)


if __name__ == "__main__":
    test_data_address = ''
    test_data = load_data(test_data_address)
    prediction(test_data=test_data)
