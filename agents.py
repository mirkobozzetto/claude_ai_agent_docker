# importing necessary libraries
# type: ignore

import csv
import os
import anthropic
# from anthropic import Anthropic

# set up the API key
if not os.getenv("ANTHROPIC_API_KEY"):
  os.environ["ANTHROPIC_API_KEY"] = input("Enter your API key: ")

