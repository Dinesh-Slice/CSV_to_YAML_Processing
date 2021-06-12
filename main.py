# ----------------------------------------------------------------------------------------------------
# Imports

import sys
import pandas as pd
import yaml as yml
import numpy as np
from termcolor import colored
import re
import os

# ----------------------------------------------------------------------------------------------------
# Regex Magic


def generate_id(question_code):
    temp = re.sub(r"([A-Z])", r" \1", question_code).split()
    _id = "-".join([str(item).lower() for item in temp])
    return _id


# ----------------------------------------------------------------------------------------------------
# Functions to return desired columns / cells


def get_title(question):
    question = question.split("*")
    return question[0]


def get_description_points(question):
    description_dict = {}
    question = question.split("*")
    question = question[1::]
    for i in range(0, len(question)):
        temp = " ".join(question[i].split())
        desc = {i: {"label": '"' + str.format(temp) + '"'}}
        description_dict.update(desc)
    return description_dict


def get_grouping(grouping):
    if grouping == "ClassRelated":
        group = "classSpecific"
    elif grouping == "General":
        group = "generic"
    elif grouping == "ClaimHistory":
        group = "priorClaims"
    return group


# ----------------------------------------------------------------------------------------------------
# Processing the csv

if __name__ == "__main__":
    csv_file = sys.argv[1]
    yml_file = sys.argv[2]

    df = pd.read_csv(csv_file)
    write_file = open(yml_file, "w")

    to_be_dropped = ["Wave", "Notes / Questions / Decision", "Card", "Screen"]

    # Clean the df
    df.drop(to_be_dropped, inplace=True, axis=1)
    df.replace(" ", np.nan, inplace=True)
    df.dropna(axis=0, how="any", inplace=True)
    df = df.replace("\n", "", regex=True)
    df.columns = df.columns.str.replace("\n", "")
    df = df.reset_index(drop=True)

    data_content = {}

    for i in range(0, len(df)):
        record = df.iloc[i]
        item = {
            record["Question code / Key"]: {
                "title": '"' + get_title(record["Question"]).strip() + '"',
                "type": '"' + "radio" + '"',
                "grouping": '"' + get_grouping(record["group"]) + '"',
                "order": int(record["Order"]),
                "options": {
                    0: {
                        "value": True,
                        "label": '"' + "Yes" + '"',
                        "id": '"'
                        + generate_id(record["Question code / Key"])
                        + "-true"
                        + '"',
                    },
                    1: {
                        "value": False,
                        "label": '"' + "No" + '"',
                        "id": '"'
                        + generate_id(record["Question code / Key"])
                        + "-false"
                        + '"',
                    },
                },
                "descriptionPoints": get_description_points(record["Question"]),
            }
        }
        data_content.update(item)

    data_dict = {"content": data_content}

    # ----------------------------------------------------------------------------------------------------
    # Dump the YAML File

    try:
        yml.dump(data_dict, write_file, sort_keys=False, allow_unicode=True, width=1000)
        write_file.close()
        print("YAML File Generated in: " + colored(os.path.abspath(yml_file), "red"))
    except Exception as error:
        print("Error occurred: " + repr(error))
