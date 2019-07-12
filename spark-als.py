import pyspark
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pyspark.sql import SparkSession
from pyspark.ml.recommendation import ALS
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.functions import mean,isnan,col
spark = SparkSession.builder.getOrCreate()

class SparkALS():
    
    def train(self,train_df,regParam,maxIter,rank):
        self.train_df = train_df
        model = ALS(userCol='userId',itemCol='movieId',ratingCol='rating',nonnegative=True,regParam=regParam,maxIter=maxIter,rank=rank)
        self.recommender = model.fit(train_df)
    
    def predict(self,test_df):
        self.predictions = self.recommender.transform(test_df)
        
    def evaluate(self):
#         in pandas:
#         train_pandas = self.train_df.toPandas()
#         predictions_df = self.predictions.toPandas().fillna(train_pandas['rating'].mean())
#         predictions_df['squared_error'] = (predictions_df['rating'] - predictions_df['prediction'])**2
#         return np.sqrt(sum(predictions_df['squared_error']) / len(predictions_df))
        
        
        mean_rating = train_df.select([mean('rating')]).collect()
        mean_rating
        results={}
        for i in mean_rating:
            results.update(i.asDict())
        the_mean = results['avg(rating)']
        new_predictions = self.predictions.na.fill({'prediction': the_mean})
        evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",predictionCol="prediction")
        return evaluator.evaluate(new_predictions)
    
if __name__ == '__main__':
    train_pandas_df = pd.read_csv('data/movies/ratings_train.csv',index_col=0)
    train_df = spark.createDataFrame(train_pandas_df)
    
    test_pandas_df = pd.read_csv('data/movies/ratings_test.csv',index_col=0)
    test_df = spark.createDataFrame(test_pandas_df)
    
    test = SparkALS()
    test.train(train_df,0.1,10,10)
    test.predict(test_df)
    rmse = test.evaluate()
    print(rmse)