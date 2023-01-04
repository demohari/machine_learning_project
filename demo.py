import os,sys
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
def main():
    try:
        pipeline = Pipeline()
        pipeline.run_pipeline()

    except Exception as e:
        #raise HousingException(e,sys) from e
        logging.error("Failed to run pipeline: {e}")
        print(e)


if __name__=='__main__':
    main()