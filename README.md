# MLOPS-Wine-Quality-Prediction

---
1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py 
---

## Workflow

1. Update config.yaml
   - add the direct link, source, url, base info here

2. Update schema.yaml

3. Update params.yaml

4. Update the entity
    Create the dataclass with the dataType of ele in config yaml 

5. Update the configuration manager in src config
    access the data of config.yaml file with constructor and do the assigning like (access the base items from config with the help of entity)

6. Update the components
    Utilize the access items and ele like(download the data file extract it )

7. Update the pipeline 
    connect the all 3 in a row with a pipe(configuration, entity, component ) with a pipe, use config and give input of entity

8. Update the main.py
9.  Update the app.py 




# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlops python=3.10.13 -y
```

```bash
conda activate mlops
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```
### STEP 03- set some python env variable for tracking  

**In conda env**

```python 

# to set new variable 
conda env config vars set MY_VARIABLE=my_value 

# to access that variable 
os.environ.get('MY_VARIABLE')

# to see all available variables 
conda env config vars list

```
**In normal python env**

```python 
# to set new variable
set MY_VARIABLE=my_value

# to access that variable 
os.environ.get('MY_VARIABLE')

```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/ukantjadia/MLOPS-Wine-Quality-Prediction.mlflow \
MLFLOW_TRACKING_USERNAME=ukantjadia \
MLFLOW_TRACKING_PASSWORD=******** \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/ukantjadia/MLOPS-Wine-Quality-Prediction.mlflow

export MLFLOW_TRACKING_USERNAME=ukantjadia 

export MLFLOW_TRACKING_PASSWORD=********

```
