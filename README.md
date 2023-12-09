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