import pandas as pd
import json

with open("t20_json_files/t20_wc_match_results.json", encoding="utf-8-sig") as f_input:
    df = json.load(f_input)
    df_match = pd.DataFrame(df[0]["matchSummary"])


df_match.rename({"scorecard": "match_id"}, axis=1, inplace=True)

# Creating a dictionary because we want to match the column with the batting summary table and the match id

match_id_dict = {}

for index, row in df_match.iterrows():
    key1 = row["team1"] + " Vs " + row["team2"]
    key2 = row["team2"] + " Vs " + row["team1"]

    match_id_dict[key1] = row["match_id"]
    match_id_dict[key2] = row["match_id"]

# print(match_id_dict)


## Batting summary


with open(
    "t20_json_files/t20_wc_batting_summary.json", encoding="utf-8-sig"
) as f_input:
    df = json.load(f_input)
    # df_batting_summary = pd.DataFrame(df[0]["battingSummary"])
    # print(df_batting_summary.head())

all_records = []
for rec in df:
    all_records.extend(rec["battingSummary"])

df_batting = pd.DataFrame(all_records)

# Adding a column for out and not out

df_batting["out/not out"] = df_batting["dismissal"].apply(
    lambda x: "out" if len(x) > 0 else "not out"
)

# Dropping the dismissal column as it is not required and use inplace so that it applies to the current dataframe

df_batting.drop("dismissal", axis=1, inplace=True)
# print(df_batting.head(11))

# Remove the special characters from the batsmanName column

df_batting["batsmanName"] = df_batting["batsmanName"].str.replace("†", "")


# Applying the created dictionary values to the batting summary table to get the common column match_id

df_batting["match_id"] = df_batting["match"].apply(lambda x: match_id_dict[x])

# Saving the files in CSV format

df_match.to_csv("t20_csv_files/t20_wc_match_results.csv", encoding="utf-8", index=False)
df_batting.to_csv(
    "t20_csv_files/t20_wc_batting_summary.csv", encoding="utf-8", index=False
)
