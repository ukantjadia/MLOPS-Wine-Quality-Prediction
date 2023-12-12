from mlproject import logger

from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

from mlproject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

from mlproject.pipeline.stage_03_data_transformation import DataTransformationPipeline

from mlproject.pipeline.stage_04_model_training import ModelTrainerTrainingipeline

from mlproject.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline


logger.info("Welcome to our custome logger ")


STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<  \n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<  \n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    data_transfomation = DataTransformationPipeline()
    data_transfomation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<  \n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Traning Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    model_trainer = ModelTrainerTrainingipeline()
    model_trainer.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<  \n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e  


STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>> stage {STAGE_NAME} completed <<<<<  \n\n x=======x")
except Exception as e:
    logger.exception(e)
    raise e  
