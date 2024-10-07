import pandas as pd
import os


def process_file(file_path):
    # Read the data from the file
    df = pd.read_csv(file_path)

    # Compute the mean difference
    mean_difference = round(df['difference'].mean())

    # Compute the jitter
    jitter = round(df['difference'].std())

    return mean_difference, jitter


def main(input_directory, output_file):
    # Create a DataFrame to hold the results
    results = []

    # Loop through each file in the directory
    for file_name in os.listdir(input_directory):
        if file_name.endswith(".csv"):  # Assuming you're dealing with CSV files
            file_path = os.path.join(input_directory, file_name)
            mean_diff, jitter = process_file(file_path)
            results.append([file_name, mean_diff, jitter])

    # Convert results to a DataFrame and write to the output file
    df_results = pd.DataFrame(results, columns=['file_name', 'mean_difference', 'jitter'])
    df_results = df_results.sort_values(by=['mean_difference'])
    df_results.to_csv(output_file, index=False)


if __name__ == "__main__":
    input_directory = './result'  # Change this to the path of your input directory
    output_file = './output_results.csv'  # Change this if you want a different output file name or path
    main(input_directory, output_file)
