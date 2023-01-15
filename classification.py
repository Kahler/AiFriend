# import json
#
# # Open the JSON file
# with open("data.json", "r") as f:
#     # Parse the JSON
#     data = json.load(f)
#
# # Access the values in the parsed JSON
# print(data["name"])  # Output: John
# print(data["age"])  # Output: 30
# print(data["city"])  # Output: New York
import re
import numpy as np


def classify_all():
    with open("data/all_types", "r") as f:
        # Read each line of the file
        types = []
        for line in f:
            # Print the line (without the newline character at the end)
            # The regular expression pattern to match
            pattern = r"^\d+\.\s+"
            result = re.sub(pattern, "", line)

            # Replace the matched pattern with the empty string
            if not result.startswith("#") and not len(result.strip()) == 0:
                types.append(result.strip())
                # print(result.strip())

        values, counts = np.unique(types, return_counts=True)
        # print(values, counts)

        values_and_counts = zip(values, counts)

        # Iterate over the list of tuples and print each one
        for value, count in values_and_counts:
            # print(count, '\t', value)
            print("'{t}' |".format(t=value))


def classify_real_response():
    with open("data/question_response", "r") as f:
        # Read each line of the file
        types = []
        for line in f:
            # Print the line (without the newline character at the end)
            # The regular expression pattern to match
            pattern = r"^\d+\.\s+"
            result = re.sub(pattern, "", line)

            # Replace the matched pattern with the empty string
            if not result.startswith("#") and not len(result.strip()) == 0:
                types.append(result.strip())
                # print(result.strip())

        values, counts = np.unique(types, return_counts=True)
        # print(values, counts)

        values_and_counts = zip(values, counts)

        # Iterate over the list of tuples and print each one
        for value, count in values_and_counts:
            # print(count, '\t', value)
            print("'{t}' |".format(t=value))
