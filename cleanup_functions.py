import matplotlib.pyplot as plt
import pandas as pd

# Function to format date
def format_date(date_str):
    """
    Formats date string to standard YYYY-MM-DD format.

    Parameters:
    date_str (str): Input date string

    Returns:
    str: Formatted date string
    """
    
    # Check if date string contains '/'
    if '/' in date_str:
        # Convert date string to datetime object using pd.to_datetime
        # Format: MM/DD/YY
        date_obj = pd.to_datetime(date_str, format='%m/%d/%y')
        
        # Convert datetime object to string in YYYY-MM-DD format
        return date_obj.strftime('%Y-%m-%d')
    else:
        # Return original date string if already in desired format
        return date_str   

# Function to drop duplicates
def read_remove_duplicates(file):
    """
    Reads CSV file and removes duplicate rows.

    Parameters:
    file (str): Path to CSV file

    Returns:
    DataFrame: Cleaned DataFrame with duplicates removed
    """
    
    # Read CSV file into DataFrame
    df = pd.read_csv(file)
    
    # Remove duplicate rows based on all columns
    df = df.drop_duplicates()
    
    # Return cleaned DataFrame
    return df

# Calculate Q1 and Q3
def remove_outliers(df, col):
    """
    Removes outliers from a DataFrame column using Interquartile Range (IQR) method.

    Parameters:
    df (DataFrame): Input DataFrame
    col (str): Column name to remove outliers from

    Returns:
    DataFrame: Cleaned DataFrame with outliers removed
    """
    
    # Calculate first quartile (Q1, 25th percentile)
    Q1 = df[col].quantile(0.25)
    
    # Calculate third quartile (Q3, 75th percentile)
    Q3 = df[col].quantile(0.75)

    # Calculate Interquartile Range (IQR)
    IQR = Q3 - Q1

    # Remove outliers outside 1.5*IQR range
    # (below Q1 - 1.5*IQR or above Q3 + 1.5*IQR)
    df = df[~((df[col] < (Q1 - 1.5 * IQR)) | (df[col] > (Q3 + 1.5 * IQR)))]

    # Return cleaned DataFrame
    return df

def remove_nonnumeric(df, col, dtype):
    """
    Removes non-numeric values from specified columns and converts to desired data type.

    Parameters:
    df (DataFrame): Input DataFrame
    col (list): List of column names to clean
    dtype (type): Desired data type (e.g., int, float)

    Returns:
    DataFrame: Cleaned DataFrame
    """
    
    # Iterate over each column to clean
    for c in col:
        # Replace non-numeric characters with 0 using regex and convert to desired type
        df[c] = df[c].replace(r'[a-zA-Z$&%*@#!]', 0, regex=True).astype(dtype)
        
        # Filter out rows with non-positive values if column is numeric
        if df[c].dtype == 'float' or df[c].dtype == 'int':
            # Remove rows where value is less than or equal to 0
            df = df[df[c] > 0]
    
    # Return cleaned DataFrame
    return df

def swap_columns(df, c1, c2):
    """
    Swaps values between two columns if values in c1 are greater than c2.

    Parameters:
    df (DataFrame): Input DataFrame
    c1 (str): First column name
    c2 (str): Second column name

    Returns:
    DataFrame: Modified DataFrame with swapped values
    """
    
    # Iterate over each row in the DataFrame
    for i in range(len(df)):
        # Check if value in c1 is greater than value in c2
        if df.loc[i, c1] > df.loc[i, c2]:
            # Swap values between c1 and c2
            df.loc[i, c1], df.loc[i, c2] = df.loc[i, c2], df.loc[i, c1]
    
    # Return modified DataFrame
    return df

def horizontal_barchart(
                        df,  # Input DataFrame
                        x,  # Column name for x-axis
                        y,  # Column name for y-axis
                        x_label,  # Label for x-axis
                        y_label,  # Label for y-axis
                        title,  # Chart title
                        ascending_type=False,  # Sort order (default: False = descending)
                        bcolor='skyblue',  # Bar color
                        figsize=(25, 12),  # Figure size
                        va='center',  # Vertical alignment for annotations
                        ha='left',  # Horizontal alignment for annotations
                        fontsize=10,  # Font size for annotations
                        fcolor='black'  # Font color for annotations
                        ):
    """
    Create a horizontal bar chart.

    Args:
        df (pd.DataFrame): Input DataFrame.
        x (str): Column name for x-axis.
        y (str): Column name for y-axis.
        x_label (str): Label for x-axis.
        y_label (str): Label for y-axis.
        title (str): Chart title.
        ascending_type (bool, optional): Sort order. Defaults to False.
        bcolor (str, optional): Bar color. Defaults to 'skyblue'.
        figsize (tuple, optional): Figure size. Defaults to (25, 12).
        va (str, optional): Vertical alignment for annotations. Defaults to 'center'.
        ha (str, optional): Horizontal alignment for annotations. Defaults to 'left'.
        fontsize (int, optional): Font size for annotations. Defaults to 10.
        fcolor (str, optional): Font color for annotations. Defaults to 'black'.
    """

    # Sort DataFrame by y-axis values
    df = df.sort_values(by=y, ascending=ascending_type)

    # Create figure with specified size
    plt.figure(figsize=figsize)

    # Create horizontal bar chart
    bars = plt.barh(df[x], df[y], color=bcolor)

    # Set labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Invert y-axis for proper ordering
    plt.gca().invert_yaxis()

    # Add annotations to bars
    for bar in bars:
        # Display value on top of each bar
        plt.text(
            bar.get_width(),
            bar.get_y() + (bar.get_height() / 2),
            f"{bar.get_width():,.2f}",
            va=va,
            ha=ha,
            fontsize=fontsize,
            color=fcolor,
        )

    # Display chart
    plt.show()
