"""Generate poverty data"""

import pandas as pd
from bblocks.data_importers import WorldBank

from src.config import Paths, logger


INDICATORS = ["SI.POV.NAHC", # headcount ratio at national poverty lines
              "SI.POV.DDAY", # headcount ratio at $2.15 a day (2017 PPP)
              "SI.POV.LMIC", # headcount ratio at $3.65 a day (2017 PPP)
              "SI.POV.UMIC", # headcount ratio at $6.85 a day (2017 PPP)
              "SP.POP.TOTL", # total population
              ]

def fetch_data(wb: WorldBank):
    """fetch data from the World Bank"""

    return wb.get_data( series=INDICATORS)

def add_indicator_names(wb: WorldBank, df: pd.DataFrame) -> pd.DataFrame:
    """Add indicator names to the DataFrame"""

    ind_map = {}

    for indicator in INDICATORS:
        name = wb.get_indicator_metadata(indicator)["IndicatorName"]
        ind_map[indicator] = name

    return df.assign(indicator_name=df["indicator_code"].map(ind_map))


def split_and_save(df: pd.DataFrame):
    """Split the DataFrame by indicator and save each part"""

    for indicator in INDICATORS:
        (df
         .loc[lambda d: d["indicator_code"] == indicator]
         .to_csv(Paths.data / f"pov/{indicator}.csv", index=False)
         )


if __name__ == "__main__":

    wdi = WorldBank()
    wdi.set_database(2)
    data = fetch_data(wdi)
    data = add_indicator_names(wdi, data)
    split_and_save(data)

    logger.info("Extracted poverty data and saved to CSV files.")
