"""
Data cleaning module for the BrightCart pipeline.
"""

import pandas as pd


# Import the Excel file
df = pd.read_excel("C:/Users/kbnmi5985/Downloads/online_retail_II.xlsx", sheet_name="Year 2010-2011")
df1 = pd.read_excel("C:/Users/kbnmi5985/Downloads/online_retail_II.xlsx", sheet_name="Year 2009-2010")

# Display the first 5 rows
print(df.head())
print(df1.head())

# Combine the two DataFrames
combined_df = pd.concat([df1, df], ignore_index=True)
print("Combined dataset:", combined_df.shape)
print(combined_df.head())

def clean_data(combined_df):
    
    #Count the number of rows
    
    initial_records = len(combined_df)
    print("Initial records:", initial_records)
    
     # ---------------------------------------------------------
    # Standardize column names
     # ---------------------------------------------------------
    
    combined_df.columns = (
            combined_df.columns
            .str.strip()
            .str.replace(" ", "_")
            .str.replace("-", "_")
        )
    # ---------------------------------------------------------
    # Remove duplicate records
    # ---------------------------------------------------------
    
    combined_df = combined_df.drop_duplicates()
    
    # ---------------------------------------------------------
    # Remove records without CustomerID
    # ---------------------------------------------------------
    
    if "CustomerID" in combined_df.columns:
            combined_df = combined_df.dropna(subset=["CustomerID"])
    
    # ---------------------------------------------------------
    # Convert numeric columns
    # ---------------------------------------------------------
    
    if "Quantity" in combined_df.columns:
            combined_df["Quantity"] = pd.to_numeric(
                combined_df["Quantity"],
                errors="coerce"
            )
    
    if "Price" in combined_df.columns:
            combined_df["Price"] = pd.to_numeric(
                combined_df["Price"],
                errors="coerce"
            )
            
    # ---------------------------------------------------------
    # Remove invalid quantities and prices
    # ---------------------------------------------------------
    
    if "Quantity" in combined_df.columns:
            combined_df = combined_df[combined_df["Quantity"] > 0]
    
    if "Price" in combined_df.columns:
            combined_df = combined_df[combined_df["Price"] > 0]
    
        # ---------------------------------------------------------
        # Convert invoice date
        # ---------------------------------------------------------
    
    if "InvoiceDate" in combined_df.columns:
            combined_df["InvoiceDate"] = pd.to_datetime(
                combined_df["InvoiceDate"],
                errors="coerce"
            )
    
            combined_df = combined_df.dropna(
                subset=["InvoiceDate"]
            )
    
        # ---------------------------------------------------------
        # Create transaction value
        # ---------------------------------------------------------
    
    if "Quantity" in combined_df.columns and "Price" in combined_df.columns:
            combined_df["TransactionValue"] = (
                combined_df["Quantity"] * combined_df["Price"]
            )
    
    # ---------------------------------------------------------
    # Save cleaned data
    # ---------------------------------------------------------
    
    OUTPUT_PATH = "C:/Users/kbnmi5985/Downloads/cleaned_online_retail_II.csv"
    
    combined_df.to_csv(
            OUTPUT_PATH,
            index=False
        )
    
    records_removed = initial_records - len(combined_df)
    
    print(
            f"Cleaning completed.\n"
            f"Initial records: {initial_records:,}\n"
            f"Final records: {len(combined_df):,}\n"
            f"Records removed: {records_removed:,}"
        )
    
    return combined_df
    
    
if __name__ == "__main__":
  clean_data(combined_df)

    
    
    
