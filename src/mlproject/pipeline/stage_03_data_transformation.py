from mlproject.entity.config_entity import DataTransformationConfig
from mlproject import logger 
from mlproject.components.data_transformation import DataTransformation
from mlproject.config.configuration import ConfigurationManager

STAGE_NAME = "Data Transformation stage"

class DataTransformationPipeline:
    def __init__(self):
        pass
    
    
    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config=data_transformation_config)
        data_transformation.train_test_spliting()
        
        
if __name__ == "__main__":
    try: 
        logger.info(f">>>> stage {STAGE_NAME} started <<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(f">>>> stage {STAGE_NAME} completed <<<<<  \n\n x=======x")
    except Exception as e:
        logger.exception(e)
        raise e        