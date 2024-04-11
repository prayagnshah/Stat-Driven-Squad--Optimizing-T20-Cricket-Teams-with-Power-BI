import pandas as pd
import json

with open("t20_json_files/t20_wc_match_results.json", encoding="utf-8-sig") as f_input:
    df = json.load(f_input)
    df_match = pd.DataFrame(df[0]["matchSummary"])
    print(df_match.count())

# df.to_csv("t20_wc_batting_summary.csv", encoding="utf-8", index=False)
