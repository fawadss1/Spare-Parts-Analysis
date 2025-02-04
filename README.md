# **Spare Parts Data Processing Script**

This Python script processes a dataset of spare parts, performing tasks such as analyzing key metrics, removing duplicate records, and generating reports in CSV or JSON format.  

## **Features**
✅ Load a CSV dataset of spare parts  
✅ Analyze data to compute:
  - Average price by manufacturer  
  - Count of spare parts by car model  
✅ Identify and remove duplicate records  
✅ Save the cleaned data as a report (CSV or JSON)  
✅ Command-line interface for easy execution  

---

## **Installation**

### **1. Create a Virtual Environment**
Before running the script, it's recommended to create a virtual environment to manage dependencies. Run the following commands:

```bash
# Create a virtual environment (venv)
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### **2. Install Required Libraries**
Once the virtual environment is activated, install the required dependencies:

```bash
pip install pandas, numpay, faker
```

---

## **Usage**
Run the script with different options using the terminal:  

### **1. Genrate Data**  
To generate the spar parts data use the below commond it it genrate 10000 records name as "spare_parts.csv":  
```bash
python genrate_data.py
```

### **2. Analyze Data**  
To calculate the average price per manufacturer and count of spare parts per car model:  
```bash
python analyze.py --file spare_parts.csv --analyze
```

### **3. Remove Duplicates and Save Clean Data**  
```bash
python analyze.py --file spare_parts.csv --remove-duplicates --generate-report clean_data.csv
```

### **4. Save Processed Data as JSON**  
```bash
python analyze.py --file spare_parts.csv --remove-duplicates --generate-report report.json
```

### **5. To Remove Duplicate Values**  
```bash
python analyze.py --file spare_parts.csv --remove-duplicates
```

---

## **Arguments**
| Argument | Description | Example |
|----------|-------------|----------|
| `--file` | **(Required)** Path to the CSV file containing spare parts data. | `--file spare_parts.csv` |
| `--analyze` | Perform analysis of the dataset. | `--analyze` |
| `--remove-duplicates` | Remove duplicate records from the dataset. | `--remove-duplicates` |
| `--generate-report` | Save processed data to a CSV or JSON file. | `--generate-report clean_data.csv` |

---
Developed by **Fawad Ali** 🚀  
