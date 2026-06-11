from pyspark.sql.types import *

sales_schema = StructType([
    StructField("order_id", StringType(), True),
    StructField("order_date", StringType(), True),
    StructField("customer_info", StringType(), True),
    StructField("customer_age", StringType(), True),
    StructField("location", StringType(), True),
    StructField("device_type", StringType(), True),
    StructField("items", StringType(), True),
    StructField("payment_method", StringType(), True),
    StructField("currency", StringType(), True),
    StructField("discount_code", StringType(), True),
    StructField("shipping_cost", StringType(), True),
    StructField("total_amount", StringType(), True),
    StructField("order_status", StringType(), True),
    StructField("loyalty_points", StringType(), True),
    StructField("feedback_score", StringType(), True)
])

exchange_schema = StructType([
    StructField("year", IntegerType(), True),
    StructField("month", IntegerType(), True),
    StructField("from_currency", StringType(), True),
    StructField("to_currency", StringType(), True),
    StructField("exchange_rate", DoubleType(), True)
])