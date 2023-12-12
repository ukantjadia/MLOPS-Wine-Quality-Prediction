from mlproject import logger
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from mlproject.entity.config_entity import DataTransformationConfig
from sklearn.preprocessing import StandardScaler


class DataTransformation:
    """_summary_"""

    def __init__(self, config: DataTransformationConfig):
        self.config = config
        """
        Adding the components read below:

# here you can do all your preprocessing of the dataset and after create 
# train and test here only and save them in the seprate csv files
        """
    def preprocessing(self):
        df = pd.read_csv(self.config.data_path)
        logger.info(f"Data shape {df.shape}")
        
        # Handling nan values 
        df['chlorides'] = df['chlorides'].fillna(df['chlorides'].mean())
        df['sulphates'] = df['sulphates'].fillna(df['sulphates'].mean())
        df['density'] = df['density'].fillna(df['density'].mean())
        df['free sulfur dioxide'] = df['free sulfur dioxide'].fillna(df['free sulfur dioxide'].mode()[0])
        df['quality'] = df['quality'].fillna(df['quality'].mode()[0])
        
        # Droping the duplicate values
        df=df.drop_duplicates()
        
        # Transformation Handling the skewness of data
        skewed_col = ['volatile acidity', 'citric acid', 'pH', 'density', 'chlorides'] # col with high skewness
        
        for _,col in enumerate(skewed_col[:4]):
            df[col] = np.log1p(df[col])
            # df[col] = df[col].apply(lambda x: np.log1p(x))
        df[skewed_col[-1]] = df[skewed_col[-1]].apply(lambda x: np.cbrt(x))
        # df[skewed_col[-1]] = np.cbrt(skewed_col[-1])
        
        # col Citric acid has some amount(134 out of 5381) of zeros(0.0)  so dropping them also
        df.drop(df[df['citric acid'] == 0].index, inplace= True)
        df.reset_index(drop=True,inplace=True)
        
        # Making quality column more accurate
        low = np.unique(df[df['quality'] <= 5]['quality'].values)
        average = np.unique(df[df['quality'] == 6]['quality'].values)
        high = np.unique(df[df['quality'] >= 7]['quality'].values)
        df['quality'] = df['quality'].replace(low,0)
        df['quality'] = df['quality'].replace(average,1)
        df['quality'] = df['quality'].replace(high,2)
        
        # normalizing the category col 
        df['category'] = np.where(df['category'] == "white",0,1)
        
        # dropping all nan values generated due to above operation
        df=df.dropna(axis=0)
        
        # normalizing with z score method
        scaler = StandardScaler()
        col_num = df.select_dtypes(include=['float64','int64']).columns
        df[col_num] = scaler.fit_transform(df[col_num])
        logger.info(f"Data shape after preprocessing {df.shape}")
        
        # saving the cleaned data
        df.to_csv(os.path.join(self.config.root_dir,"clean-wine-quality.csv"),index=False)

    def train_test_spliting(self):
        """create the training and testing data
        """
        data = pd.read_csv(self.config.clean_data)
        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        logger.info("Splited data into training and testing sets")
        logger.info(train.shape)
        logger.info(test.shape)
        print(train.shape)
        print(test.shape)
