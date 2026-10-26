import polars as pl

df = pl.read_csv(
    "file.csv",
    schema_overrides={
        "id": pl.String,          # keeps leading zeros, handles bad values
        "price": pl.Float64,      # allow nulls
        "age": pl.Int32,
        "is_active": pl.Boolean,
        "notes": pl.String,
    },
    null_values=["", "NA", "N/A", "null", "-"],
    try_parse_dates=False,        # important - date parsing causes this error a lot
    infer_schema_length=10000
)
