from pyspark.sql.functions import col

# ==============================
# SALES VALIDATION
# ==============================

def validate_sales(df):
    """
    Apply validation rules for sales data
    """

    valid_df = df.filter(
        (col("order_status") != "Failed") &
        (col("feedback_score").between(1, 5)) &
        (col("total_amount").isNotNull()) &
        (col("order_date").isNotNull())
    )

    invalid_df = df.subtract(valid_df)

    return valid_df, invalid_df


# ==============================
# EXCHANGE VALIDATION
# ==============================

def validate_exchange(df):
    """
    Apply validation rules for exchange rate data
    """

    valid_df = df.filter(
        (col("exchange_rate").isNotNull()) &
        (col("exchange_rate") > 0) &
        (col("month").between(1, 12))
    )

    invalid_df = df.subtract(valid_df)

    return valid_df, invalid_df