from pyspark.sql import SparkSession
from performance_profiler import profile_execution

@profile_execution
def run_pipeline():
    spark = SparkSession.builder.appName("HeartFailurePipeline").getOrCreate()

    df = spark.read.csv("heart_failure_clinical_records_dataset.csv", header=True, inferSchema=True)

    print("Row Count:", df.count())
    print("Columns:", df.columns)

    df.groupBy("DEATH_EVENT").count().show()

    spark.stop()

if __name__ == "__main__":
    run_pipeline()
