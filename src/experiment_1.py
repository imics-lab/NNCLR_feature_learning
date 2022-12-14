#Author: Gentry Atkinson
#Organization: Texas University
#Data: 01 August, 2022
#Let's analyze NNCLR as a feature extractor for wearable
#  sensor data.

#Experimental Design:
#  Extract features from a HAR dataset using NNCLR, SIMCLR,
#  an auto-encoder, and signal processing. Use KNN to classify
#  each instance of data in the set

#Hypothesis: NNCLR will have the highest accuracy and F1 when
#  classifying the extracted features

from utils.nnclr_feature_learner import NUM_FEATURES


run_trad = True
run_ae = True
run_nnclr = True
run_nnclr_t = True
run_simclr = True
run_simclr_t = True

NUM_FEATURES = 64

#from utils.import_datasets import get_unimib_data
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from load_data_time_series.HAR.UniMiB_SHAR.unimib_shar_adl_load_dataset import unimib_load_dataset
from load_data_time_series.twristar_dataset_demo import e4_load_dataset
from load_data_time_series.HAR.UCI_HAR.uci_har_load_dataset import uci_har_load_dataset
from utils.sh_loader import sh_loco_load_dataset
from datetime import datetime
import numpy as np
import pandas as pd
import torch
import gc

#Dataset are returned in channels-last format
datasets = {
    'unimib' :  unimib_load_dataset,
    'twister' : e4_load_dataset,
    'uci har' : uci_har_load_dataset,
    'sussex huawei' : sh_loco_load_dataset
}

device = "cuda" if torch.cuda.is_available() else "cpu"

#TensorFlow -> channels last
#PyTorch -> channels first

results = {
    'Features'  : [],
    'Data'      : [],
    'Acc'       : [],
    'F1'        : [],
    'Prec'      : [],
    'Rec'       : []
}

if __name__ == '__main__':
    for set in datasets.keys():
        print("------------Set: ", set, "------------")
        X, y, X_test, y_test = datasets[set](incl_xyz_accel=True, incl_rms_accel=False)

        if X.shape[2] == 1:
            flattened_train = X
        else:
            flattened_train = np.array([np.linalg.norm(i, axis=1) for i in X])

        if X_test.shape[2] == 1:
            flattened_test = X_test
        else:
            flattened_test = np.array([np.linalg.norm(i, axis=1) for i in X_test])

        print('Shape of X: ', X.shape)
        print('Shape of y: ', y.shape)
        print('Shape of flattened train X: ', flattened_train.shape)
        print('Shape of flattened test X: ', flattened_test.shape)
        print('Shape of X_test: ', X_test.shape)
        print('Shape of y_test: ', y_test.shape)
        if(run_trad):        
            from utils.ts_feature_toolkit import get_features_for_set as get_trad_features
            train_features = get_trad_features(np.reshape(flattened_train, (flattened_train.shape[0], flattened_train.shape[1])))
            test_features = get_trad_features(np.reshape(flattened_test, (flattened_test.shape[0], flattened_test.shape[1])))
            gc.collect()
            print('Shape of Traditional Features: ', train_features.shape)
            model = KNeighborsClassifier(n_neighbors=3)
            model.fit(train_features, y)
            y_pred = model.predict(test_features)
            print("Trad accuracy: ", accuracy_score(y_test, y_pred))
            results['Features'].append('Traditional')
            results['Data'].append(set)
            results['Acc'].append(accuracy_score(y_test, y_pred))
            results['F1'].append(f1_score(y_test, y_pred, average='weighted'))
            results['Prec'].append(precision_score(y_test, y_pred, average='weighted'))
            results['Rec'].append(recall_score(y_test, y_pred, average='weighted'))
        if(run_ae):        
            from utils.ae_feature_learner import get_features_for_set as get_ae_features
            train_features, ae_feature_learner = get_ae_features(X, with_visual=False, returnModel=True)
            test_features = ae_feature_learner.predict(X_test)
            gc.collect()
            print('Shape of AE Features: ', train_features.shape)
            model = KNeighborsClassifier(n_neighbors=3)
            model.fit(train_features, y)
            y_pred = model.predict(test_features)
            print("AE accuracy: ", accuracy_score(y_test, y_pred))
            results['Features'].append('Autoencoder')
            results['Data'].append(set)
            results['Acc'].append(accuracy_score(y_test, y_pred))
            results['F1'].append(f1_score(y_test, y_pred, average='weighted'))
            results['Prec'].append(precision_score(y_test, y_pred, average='weighted'))
            results['Rec'].append(recall_score(y_test, y_pred, average='weighted'))
        if(run_nnclr):
            from utils.nnclr_feature_learner import get_features_for_set as get_nnclr_features
            train_features, nnclr_feature_learner = get_nnclr_features(X, y=y, returnModel=True, bb='CNN')
            torch_X = torch.tensor(np.reshape(X_test, (X_test.shape[0], X_test.shape[2], X_test.shape[1]))).to(device)
            torch_X = torch_X.float()
            # _, test_features = nnclr_feature_learner(torch_X, return_features=True)
            # test_features = test_features.cpu().detach().numpy()
            # test_features = np.array(test_features)
            test_features = None
            for signal in torch_X:
                signal = signal.to(device).float()
                signal = torch.reshape(signal, (1, torch_X.shape[1], torch_X.shape[2]))
                (_, _), f = nnclr_feature_learner(signal, return_features=True)
                if test_features is None:
                    test_features = f.cpu().detach().numpy()
                else:
                    test_features = np.concatenate((test_features, f.cpu().detach().numpy()), axis=0)
            gc.collect()
            print('Shape of NNCLR Features: ', train_features.shape)
            print('Shape of NNCLR Test Features: ', test_features.shape)
            model = KNeighborsClassifier(n_neighbors=3)
            model.fit(train_features, y)
            y_pred = model.predict(test_features)
            print("NNCLR accuracy: ", accuracy_score(y_test, y_pred))
            results['Features'].append('NNCLR')
            results['Data'].append(set)
            results['Acc'].append(accuracy_score(y_test, y_pred))
            results['F1'].append(f1_score(y_test, y_pred, average='weighted'))
            results['Prec'].append(precision_score(y_test, y_pred, average='weighted'))
            results['Rec'].append(recall_score(y_test, y_pred, average='weighted'))

        if(run_nnclr_t):
            from utils.nnclr_feature_learner import get_features_for_set as get_nnclr_t_features
            train_features, nnclr_feature_learner = get_nnclr_t_features(X, y=y, returnModel=True, bb='Transformer')
            torch_X = torch.tensor(np.reshape(X_test, (X_test.shape[0], X_test.shape[2], X_test.shape[1]))).to(device)
            torch_X = torch_X.float()
            # _, test_features = nnclr_feature_learner(torch_X, return_features=True)
            # test_features = test_features.cpu().detach().numpy()
            # test_features = np.array(test_features)
            test_features = None
            for signal in torch_X:
                signal = signal.to(device).float()
                signal = torch.reshape(signal, (1, torch_X.shape[1], torch_X.shape[2]))
                (_, _), f = nnclr_feature_learner(signal, return_features=True)
                if test_features is None:
                    test_features = f.cpu().detach().numpy()
                else:
                    test_features = np.concatenate((test_features, f.cpu().detach().numpy()), axis=0)
            gc.collect()
            print('Shape of NNCLR Features: ', train_features.shape)
            print('Shape of NNCLR Test Features: ', test_features.shape)
            model = KNeighborsClassifier(n_neighbors=3)
            model.fit(train_features, y)
            y_pred = model.predict(test_features)
            print("NNCLR accuracy: ", accuracy_score(y_test, y_pred))
            results['Features'].append('NNCLR+T')
            results['Data'].append(set)
            results['Acc'].append(accuracy_score(y_test, y_pred))
            results['F1'].append(f1_score(y_test, y_pred, average='weighted'))
            results['Prec'].append(precision_score(y_test, y_pred, average='weighted'))
            results['Rec'].append(recall_score(y_test, y_pred, average='weighted'))

        if(run_simclr):
            from utils.simclr_feature_learner import get_features_for_set as get_simclr_features
            train_features, simclr_feature_learner = get_simclr_features(X, y=y, returnModel=True, bb='CNN')
            torch_X = torch.tensor(np.reshape(X_test, (X_test.shape[0], X_test.shape[2], X_test.shape[1]))).to(device)
            torch_X = torch_X.float()
            test_features = None
            for signal in torch_X:
                signal = signal.to(device).float()
                signal = torch.reshape(signal, (1, torch_X.shape[1], torch_X.shape[2]))
                _, f = simclr_feature_learner(signal, return_features=True)
                if test_features is None:
                    test_features = f.cpu().detach().numpy()
                else:
                    test_features = np.concatenate((test_features, f.cpu().detach().numpy()), axis=0)
            gc.collect()
            print('Shape of SimCLR Features: ', train_features.shape)
            print('Shape of SimCLR Test Features: ', test_features.shape)
            model = KNeighborsClassifier(n_neighbors=3)
            model.fit(train_features, y)
            y_pred = model.predict(test_features)
            print("SimCLR accuracy: ", accuracy_score(y_test, y_pred))
            results['Features'].append('SimClr')
            results['Data'].append(set)
            results['Acc'].append(accuracy_score(y_test, y_pred))
            results['F1'].append(f1_score(y_test, y_pred, average='weighted'))
            results['Prec'].append(precision_score(y_test, y_pred, average='weighted'))
            results['Rec'].append(recall_score(y_test, y_pred, average='weighted'))

        if(run_simclr_t):
            from utils.simclr_feature_learner import get_features_for_set as get_simclr_t_features
            train_features, simclr_feature_learner = get_simclr_t_features(X, y=y, returnModel=True, bb='Transformer')
            torch_X = torch.tensor(np.reshape(X_test, (X_test.shape[0], X_test.shape[2], X_test.shape[1]))).to(device)
            torch_X = torch_X.float()
            test_features = None
            for signal in torch_X:
                signal = signal.to(device).float()
                signal = torch.reshape(signal, (1, torch_X.shape[1], torch_X.shape[2]))
                _, f = simclr_feature_learner(signal, return_features=True)
                if test_features is None:
                    test_features = f.cpu().detach().numpy()
                else:
                    test_features = np.concatenate((test_features, f.cpu().detach().numpy()), axis=0)
            gc.collect()
            print('Shape of SimCLR Features: ', train_features.shape)
            print('Shape of SimCLR Test Features: ', test_features.shape)
            model = KNeighborsClassifier(n_neighbors=3)
            model.fit(train_features, y)
            y_pred = model.predict(test_features)
            print("SimCLR accuracy: ", accuracy_score(y_test, y_pred))
            results['Features'].append('SimClr+T')
            results['Data'].append(set)
            results['Acc'].append(accuracy_score(y_test, y_pred))
            results['F1'].append(f1_score(y_test, y_pred, average='weighted'))
            results['Prec'].append(precision_score(y_test, y_pred, average='weighted'))
            results['Rec'].append(recall_score(y_test, y_pred, average='weighted'))

        result_gram = pd.DataFrame.from_dict(results)
        result_gram.to_csv('src/results/experiment1_dataframe_{}.csv'.format(str(datetime.now())))
        print(result_gram.to_string())
