import pandas as pd
import argparse

# Load the dataset
def load_dataset(file_path):
    return pd.read_csv(file_path)

# Calculate average price by manufacturer
def calculate_avg_price_by_manufacturer(df):
    return df.groupby("manufacturer")["price"].mean().reset_index()

# Count spare parts by compatible car models
def count_parts_by_car_model(df):
    return df["compatible_car_model"].value_counts().reset_index()

# Remove duplicate records
def remove_duplicates(df):
    return df.drop_duplicates()



def save_report(data, output_file, format="csv"):
    if format == "csv":
        data.to_csv(output_file)
    elif format == "json":
        data.to_json(output_file, orient="records")


def main():
    parser = argparse.ArgumentParser(description="Spare Parts Data Processing")
    parser.add_argument("--file", required=True, help="Input CSV file")
    parser.add_argument("--analyze", action="store_true", help="Analyze data")
    parser.add_argument("--remove-duplicates", action="store_true", help="Remove duplicates")
    parser.add_argument("--generate-report", help="Output report file (CSV/JSON)")

    args = parser.parse_args()

    df = load_dataset(args.file)

    if args.remove_duplicates:
        df = remove_duplicates(df)
        print("Duplicate records removed.")

    if args.analyze:
        avg_price = calculate_avg_price_by_manufacturer(df)
        parts_count = count_parts_by_car_model(df)
        print("Average price by manufacturer:\n", avg_price)
        print("\nCount of spare parts by car model:\n", parts_count)

    if args.generate_report:
        save_report(df, args.generate_report, "csv" if args.generate_report.endswith(".csv") else "json")
        print(f"Report generated in {args.generate_report.upper()} format.")
    
if __name__ == "__main__":
    main()