# importing necessary libraries
# type: ignore

import csv
import os
import anthropic
# from anthropic import Anthropic

# set up the API key
if not os.getenv("ANTHROPIC_API_KEY"):
  os.environ["ANTHROPIC_API_KEY"] = input("Enter your API key: ")

# create Anthropic client
client = anthropic.Anthropic())
sonnet = "claude-3-5-sonnet-20240620"

# function for reading the CSV file
def read_csv(file_path):
  data[]
  with open(file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
      data.append(row)
  return data
