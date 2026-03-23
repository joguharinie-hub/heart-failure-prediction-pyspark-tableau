from pyspark.sql import SparkSession

def test_pipeline():
    spark = SparkSession.builder.appName("TestPipeline").getOrCreate()

    df = spark.read.csv("heart_failure_clinical_records_dataset.csv",
                        header=True,
                        inferSchema=True)

    assert df.count() > 0, "Dataset is empty!"

    assert "DEATH_EVENT" in df.columns, "Target column missing!"

    print("All tests passed successfully!")

    spark.stop()

if __name__ == "__main__":
    test_pipeline()
