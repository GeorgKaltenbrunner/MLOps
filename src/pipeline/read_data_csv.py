df = (
    spark.read
    .option("header", True)
    .option("inferSchema", True)
    .csv("/Workspace/Users/kaltenbrunnergeorg@googlemail.com/MLOps/Churn Modeling.csv")
)
l


