"""Helper functions to load and save CSV data.

This contains a helper function for loading and saving CSV files.

"""
import csv


def load_csv(csvpath):
    """Reads the CSV file from path provided.

    Args:
        csvpath (Path): The csv file path.

    Returns:
        A list of lists that contains the rows of data from the CSV file.

    """
    with open(csvpath, "r") as csvfile:
        data = []
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the CSV Header
        next(csvreader)

        # Read the CSV data
        for row in csvreader:
            data.append(row)
    return data

def save_csv(csvpath, data, header=None):
    """Saves CSV file from path provided.

    Args:
        csvpath is CSV file path
        data is data provided
        header=None means there is no header for CSV file
        
    """
    with open(csvpath, "w", newline="") as csvfile:
       csvwriter = csv.writer(csvfile, delimiter=",")
       header = ["Lender", "Max_Loan_Amount", "Max_LTV", "Max_DTI"," Min_Credit_Score", "Interest_Rate"]
       csvwriter.writerow(header)
       csvwriter.writerows(data)

