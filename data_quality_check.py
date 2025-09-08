def run_data_quality_checks(df: pd.DataFrame) -> dict:
    """Runs a series of data quality checks and returns a report."""
    
    report = {
        'missing_values': df.isnull().sum().to_dict(),
        'duplicate_rows': df.duplicated().sum(),
        'data_types': df.dtypes.apply(lambda x: x.name).to_dict(),
        'invalid_prices': len(df[df['price'] < 0])
    }
    return report

# Run the checks on our DataFrame
quality_report = run_data_quality_checks(df)

# Print the report
import pprint
pprint.pprint(quality_report)
