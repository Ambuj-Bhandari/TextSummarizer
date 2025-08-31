from src.textSummarizer.config.configuration import ConfigurationManager
from src.textSummarizer.conponents.model_evaluation import ModelEvaluation
from src.textSummarizer.logging import logger

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def initiate_model_eval(self):
        config = ConfigurationManager()
        model_eval_config = config.get_model_eval_config()
        model_eval = ModelEvaluation(config=model_eval_config)
        model_eval.evaluate()