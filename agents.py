# importing necessary libraries
# type: ignore

import csv
import os
import anthropic
from prompts import *
# from anthropic import Anthropic

  """_summary_
    Args:
        file_path (_type_): _description_
        output_file (_type_): _description_
        headers (_type_, optional): _description_. Defaults to None.
  Returns:
      _type_: _description_

      file_path:
      'r' for reading the file

      mode:
      'a' for appending to the file
      'w' for overwriting the file
  """

# set up the API key
if not os.getenv("ANTHROPIC_API_KEY"):
  os.environ["ANTHROPIC_API_KEY"] = input("Enter your API key: ")

# create Anthropic client
client = anthropic.Anthropic()
sonnet = "claude-3-5-sonnet-20240620"

# function for reading the CSV file
def read_csv(file_path):
  data[]
  with open(file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
      data.append(row)
  return data

# function to save the generated data to a new CSV file
def save_csv(data, output_file, headers=None):
  mode = 'w' if headers else 'a'
  with open(output_file, mode, newline='') as f:
    writer = csv.writer(f)
    if headers:
      writer.writerow(headers)
    for row in csv.reader(data.splitlines()):
      writer.writerow(row)

def analyzer_agent(sample_data):
  message = client.messages.create(
    model="claude-3-5-sonnet-20240620",
    max_tokens=400,
    temperature=0.1,
    system=ANALYZER_SYSTEM_PROMPT,
    messages=[
      {
        role: "user",
        content: ANALYZER_USER_PROMPT.format(sample_data=sample_data)
      }
    ]
  )
  return message.content[0].text
