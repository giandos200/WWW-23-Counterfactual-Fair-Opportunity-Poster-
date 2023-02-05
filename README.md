# WWW-23-	Counterfactual Reasoning for Decision Model Fairness Assessment - Poster -

## Official repository of Counterfactual Reasoning for Decision Model Fairness Assessment (Poster) - The Web Conference 2023 (WWW '23)

Authors: Giandomenico Cornacchia*, Vito Walter Anelli, Fedelucio Narducci, and Azzurra Ragone; 

<p float="left">
  <img src="figure/3D TSNE XGB male f(x)=0(1).svg" width="200" />
  <img src="figure/3D TSNE XGB female f(x)=0(1).svg" width="200" />
  <img src="figure/3D TSNE DEBIASED male f(x)=0(1).svg" width="200" /> 
  <img src="figure/3D TSNE DEBIASED female f(x)=0(1).svg" width="200" />
  </p>

## Setup Instructions

Following, the instruction to install the correct packages for running the experiments. run:
```bash
#(Python version used during experiments 3.8.10)
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Training, test models and generate CF samples
To train, evaluate models, and generate counterfactual samples for each dataset and Classifier, run:

```bash
#sudo chmod +x run_all_generation.sh + User_password if Permission Denied 
./run_all_generation.sh
```
or chose one of the config file for a specific dataset, and run:
```bash
python3 -u mainGenerate.py {config/{dataset}/...}.yml
```

Result can be found in the folder Results/{dataset}/{model}/{SF}/Genetic.pickle

N.B.: Experiments can take several days for each dataset and model. To speed up inference in the Model_Y and Counterfactual Generator loop for some scikit-learn models (e.g. SVM), the ["skearnex"](https://github.com/intel/scikit-learn-intelex) library from intel was used. The metrics' results may vary slightly from the scikit-learn models.

### Counterfactual metrics evaluation
To evaluate the proposed metric for each dataset, simply run the following command:

```bash
python3 -u mainEvaluate.py
```

The script will display Counterfactual Fairness metrics in Table 3.

|        Dataset                    | Target Classifier    | AUC          | ACC          | DSP          | DEO          | DAO          | CFlips@10 Privileged | CFlips@50 Privileged | CFlips@100 Privileged | CFlips@10 Unprivileged | CFlips@50 Unprivileged | CFlips@100 Unprivileged | $\Delta$ CFlips@10                   | $\Delta$ CFlips@50          | $\Delta$ CFlips@100          | nDCCF@10 Privileged | nDCCF@50 Privileged | nDCCF@100 Privileged  | nDCCF@10 Unprivileged | nDCCF@50 Unprivileged | nDCCF@100 Unprivileged | $\Delta$ nDCCF@10     | $\Delta$ nDCCF@50          | $\Delta$ nDCCF@100          |
|----------------------------|--------|-----------------|-----------------|-----------------|-----------------|-----------------|--------|--------|--------|--------|--------|--------|--------------------------|-----------------|-----------------|--------|--------|--------|--------|--------|--------|-----------------|-----------------|-----------------|
|        ADULT                    | LR     | 0.9078          | 0.8099          | 0.2947          | 0.0546          | 0.1241          | 12.332 | 10.886 | 10.212 | 66.353 | 72.932 | 77.165 | 54.021                   | 62.046          | 66.953          | 0.8678 | 0.8849 | 0.886  | 0.3522 | 0.2913 | 0.2497 | 0.5156          | 0.5936          | 0.6363          |
|          ADULT                  | SVM    | 0.9073          | 0.8541          | 0.1769          | 0.0644          | 0.0692          | 6.752  | 7.533  | 7.742  | 77.095 | 80.973 | 81.372 | 70.343                   | 73.44           | 73.63           | 0.9306 | 0.9258 | 0.9171 | 0.2474 | 0.2042 | 0.1948 | 0.6832          | 0.7216          | 0.7223          |
|         ADULT                   | LGB    | 0.9304          | 0.8658          | 0.1850          | 0.0379          | 0.0569          | 9.195  | 8.541  | 8.781  | 65.918 | 76.605 | 79.697 | 56.723                   | 68.064          | 70.916          | 0.9049 | 0.9124 | 0.9049 | 0.3611 | 0.2633 | 0.2272 | 0.5438          | 0.6491          | 0.6777          |
|         ADULT                   | XGB    | **0.9314**   | **0.8698** | 0.1884          | 0.0635          | 0.0680          | 10.011 | 8.788  | 9.07   | 64.796 | 76.243 | 79.512 | 54.785                   | 67.455          | 70.442          | 0.8968 | 0.9088 | 0.9014 | 0.3708 | 0.2677 | 0.2298 | 0.526           | 0.6411          | 0.6716          |
|         ADULT                   | AdvDeb | 0.9123          | 0.8512          | **0.1151** | 0.1399          | 0.0879          | 30.046 | 34.488 | 34.968 | 36.11  | 38.694 | 43.041 | 6.064                    | **4.206**  | **8.073**  | 0.7016 | 0.6668 | 0.6537 | 0.6427 | 0.6199 | 0.5812 | 0.0589          | **0.0469** | **0.0725** |
| ADULT    | lferm  | 0.9031          | 0.8428          | 0.1448          | **0.0194** | **0.0386** | 31.459 | 28.632 | 24.965 | 31.764 | 47.464 | 57.47  | **0.305**           | 18.832          | 32.505          | 0.6857 | 0.7062 | 0.7314 | 0.6864 | 0.5632 | 0.4701 | **0.0007** | 0.143           | 0.2613          |
|        ADULT-DEB                    | LR     | 0.8233          | 0.7367          | 0.1567          | 0.0695          | 0.0693          | 8.438  | 10.838 | 13.192 | 54.816 | 57.521 | 57.047 | 46.378                   | 46.683          | 43.855          | 0.9239 | 0.9012 | 0.8736 | 0.464  | 0.4332 | 0.4303 | 0.4599          | 0.468           | 0.4433          |
|         ADULT-DEB                   | SVM    | 0.8189          | 0.7395          | 0.1062          | **0.0140** | **0.0152** | 11.937 | 16.377 | 17.379 | 31.305 | 33.869 | 35.385 | **19.368**          | **17.492** | **18.006** | 0.8871 | 0.8468 | 0.8295 | 0.6661 | 0.6616 | 0.6449 | **0.221**  | **0.1852** | **0.1846** |
|        ADULT-DEB                    | LGB    | **0.8596** | 0.8371          | 0.1093          | 0.0470          | 0.0356          | 4.624  | 9.419  | 12.848 | 66.966 | 74.223 | 73.445 | 62.342                   | 64.804          | 60.597          | 0.9578 | 0.9182 | 0.8815 | 0.3720 | 0.2863 | 0.2794 | 0.5858          | 0.6319          | 0.6021          |
|        ADULT-DEB                    | XGB    | 0.8578          | **0.8375** | 0.1056          | 0.0400          | 0.0304          | 1.803  | 3.152  | 6.523  | 81.289 | 88.9   | 84.48  | 79.486                   | 85.748          | 77.957          | 0.9804 | 0.9711 | 0.9386 | 0.2183 | 0.1378 | 0.1599 | 0.7621          | 0.8333          | 0.7787          |
|        ADULT-DEB                    | AdvDeb | 0.8309          | 0.8195          | 0.0957          | 0.0326          | 0.0282          | 17.041 | 20.686 | 23.588 | 44.315 | 52.371 | 56.786 | 27.274                   | 31.685          | 33.198          | 0.8425 | 0.8055 | 0.7735 | 0.5852 | 0.5031 | 0.4566 | 0.2573          | 0.3024          | 0.3169          |
| ADULT-DEB | lferm  | 0.8017          | 0.7953          | **0.0639** | 0.0179          | 0.0186          | 8.943  | 13.316 | 16.561 | 47.036 | 54.87  | 55.83  | 38.093                   | 41.554          | 39.269          | 0.9248 | 0.8809 | 0.8452 | 0.5618 | 0.4791 | 0.4584 | 0.363           | 0.4018          | 0.3868          |
|     CRIME                       | LR     | 0.9248          | **0.8700** | 0.6535          | 0.3294          | 0.3438          | 2.857  | 3.429  | 3.714  | 75.286 | 81.914 | 85.043 | 72.429                   | 78.485          | 81.329          | 0.9688 | 0.9656 | 0.9564 | 0.2659 | 0.2015 | 0.1688 | 0.7029          | 0.7641          | 0.7876          |
|       CRIME                     | SVM    | **0.9288** | **0.8700** | 0.6395          | 0.3843          | 0.3390          | 6.667  | 5.917  | 5.671  | 73.38  | 80.676 | 84.437 | 66.713                   | 74.759          | 78.766          | 0.9334 | 0.939  | 0.9349 | 0.2858 | 0.2157 | 0.1781 | 0.6476          | 0.7233          | 0.7568          |
|        CRIME                    | LGB    | 0.9168          | 0.8400          | 0.6363          | 0.2824          | 0.3525          | 5.455  | 5.818  | 5.636  | 74.571 | 80.229 | 83.693 | 69.116                   | 74.411          | 78.057          | 0.9432 | 0.9417 | 0.9364 | 0.2875 | 0.2207 | 0.1842 | 0.6557          | 0.721           | 0.7522          |
|        CRIME                    | XGB    | 0.9099          | 0.8500          | 0.6568          | 0.2941          | 0.3656          | 4.762  | 5.429  | 5      | 73.38  | 80.113 | 83.712 | 68.618                   | 74.684          | 78.712          | 0.9505 | 0.9469 | 0.943  | 0.2938 | 0.2216 | 0.1844 | 0.6567          | 0.7253          | 0.7586          |
|        CRIME                    | AdvDeb | 0.9008          | 0.8100          | **0.5501** | **0.1882** | **0.2732** | 7.5    | 6.875  | 6.969  | 69     | 77.743 | 80.857 | 61.5                     | 70.868          | 73.888          | 0.9302 | 0.931  | 0.9237 | 0.3396 | 0.2506 | 0.2146 | 0.5906          | 0.6804          | 0.7091          |
| CRIME    | lferm  | 0.9100          | 0.8400          | 0.6125          | 0.2941          | 0.3278          | 3.182  | 6      | 6.636  | 64.412 | 71.647 | 75.147 | **61.23**           | **65.647** | **68.511** | 0.9679 | 0.9439 | 0.9306 | 0.3695 | 0.3045 | 0.2681 | **0.5984** | **0.6394** | **0.6625** |
|         GERMAN                   | LR     | **0.8186** | 0.7600          | 0.1187          | 0.1400          | 0.1657          | 4.4    | 6.56   | 7.402  | 30.000 | 28.000 | 34.000 | 25.6                     | 21.44           | 26.598          | 0.9656 | 0.9417 | 0.9267 | 0.7289 | 0.7197 | 0.6728 | 0.2367          | 0.2220          | 0.2539          |
|         GERMAN                   | SVM    | 0.8109          | 0.7600          | 0.0449          | 0.0300          | 0.0892          | 6.667  | 9.167  | 10     | $0^*$  | $0^*$  | $0^*$  | $\mathbf{6.667^\dagger}$ | 9.167           | 10              | 0.9276 | 0.9124 | 0.8985 | $0^*$  | $0^*$  | $0^*$  | 0.9276          | 0.9124          | 0.8985          |
|         GERMAN                   | LGB    | 0.7614          | 0.7500          | 0.1632          | 0.1900          | 0.1117          | 5.385  | 7.231  | 9.538  | 30.000 | 44.000 | 50.50  | 24.615                   | 36.769          | 40.962          | 0.9460 | 0.9329 | 0.9071 | 0.7193 | 0.5990 | 0.5313 | 0.2267          | 0.3339          | 0.3758          |
|         GERMAN                   | XGB    | 0.7871          | **0.7900** | 0.0518          | 0.0400          | 0.0296          | 4.545  | 6.545  | 8      | 23.333 | 24.000 | 26.333 | **18.788**          | **17.455** | **18.33**  | 0.9616 | 0.9414 | 0.9206 | 0.7448 | 0.7569 | 0.7365 | **0.2168** | **0.1845** | **0.1841** |
|        GERMAN                    | AdvDeb | 0.7371          | 0.7300          | 0.1809          | 0.2200          | 0.1267          | 4.167  | 4.333  | 7.167  | 53.333 | 59.333 | 59.000 | 49.166                   | 55              | 51.833          | 0.9661 | 0.9608 | 0.9309 | 0.4389 | 0.4103 | 0.4102 | 0.5272          | 0.5505          | 0.5207          |
| GERMAN   | lferm  | 0.7605          | 0.7200          | **0.0355** | **0.0200** | **0.0746** | 10     | 3      | 7.5    | $0^*$  | $0^*$  | $0^*$  | 10                       | 3               | 7.5             | 0.8552 | 0.9402 | 0.91   | $0^*$  | $0^*$  | $0^*$  | 0.8552          | 0.9402          | 0.91            |

### Generate toy figures

To generate Figure 1, run the following command:

```bash
python3 -u T-SNE.py
```

Image are saved in folder ./figures/3D TSNE {model} {unpriv/priv} f(x)=0.svg

N.B.: Images can be slightly different, based on seed, python and libraries versions. Neverthless, they are only toys image that will return the same conceptual findings.
## License
This repo uses [APACHE2 License](./LICENSE).
