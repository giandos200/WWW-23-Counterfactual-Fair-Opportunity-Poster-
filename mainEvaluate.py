from sklearn.compose import ColumnTransformer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

from src.utils.CFoppMetrics import CFmetrics
from src.utils.dataloader import dataLoader
from xgboost import XGBClassifier
import os
import yaml

if __name__ == '__main__':
    for dataset in os.listdir('Results'):
        Results = {}
        XGBresults = {}
        basePath = f"config/{dataset}/"
        path = ''.join([basePath,os.listdir(basePath)[0]])
        with open(path, 'r') as stream:
            try:
                file = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
        df, target, sensitiveFeature, outcomeFeature, numvars, categorical = \
            dataLoader(file['data'])
        x_train, x_test, y_train, y_test = train_test_split(df, target, test_size=0.1,
                                                                                random_state=file['seed'],
                                                                                stratify=target)
        modelSF = XGBClassifier(**file['modelSF'])
        numeric_transformer = Pipeline(
            steps=[('scaler', StandardScaler())])

        categorical_transformer = Pipeline(
            steps=[('onehot', OneHotEncoder(handle_unknown='ignore', sparse=False))])

        transformations = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numvars),
                ('cat', categorical_transformer, categorical)])
        pipeSF = Pipeline(steps=[('preprocessor', transformations),
                                      ('classifier', modelSF)])
        pipeSF.fit(x_train,y_train[sensitiveFeature])
        for model in os.listdir(f'Results/{dataset}'):
            Results[model] = ''
            for SF in os.listdir(f'Results/{dataset}/{model}'):
                Results[model] = f'Results/{dataset}/{model}/{SF}/Genetic.pickle'
        CFmetrics(Results, 'genetic', SF, pipeSF)