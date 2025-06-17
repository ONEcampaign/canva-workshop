"""Generate GHED data"""

from bblocks.data_importers import GHED
import pandas as pd

from src.config import Paths, logger

units =  {"_gdp": "percent of GDP",
          "_usd": "current USD millions",
          "_pc_usd": "current USD per capita",
          "_usd2022": "constant (2022) USD, millions",
          "_usd2022_pc": "constant (2022) USD per, capita",
          # "_ppp_pc": "current international $ (PPP), per capita",
          "_che": "percentage of total health expenditure"
          }

INDICATORS = {
    "che": "Total current health expenditure",
    "gghed": "Domestic general government health expenditure",
    "pvtd": "Domestic private health expenditure",
    "ext": "External health expenditure",
    "hf3": "Household out-of-pocket health expenditure",

    "dis1": "Health expenditure on infectious and parasitic diseases",
    "dis11": "Health expenditure on infectious and parasitic diseases - HIV/AIDS and other STDs",
    "dis12": "Health expenditure on infectious and parasitic diseases - Tuberculosis (TB)",
    "dis13": "Health expenditure on infectious and parasitic diseases - Malaria",
    "dis16": "Health expenditure on infectious and parasitic diseases - Neglected tropical diseases (NTDs)",
    "dis192": "Health expenditure on infectious and parasitic diseases - SARS-CoV-2 (COVID-19)",

    "dis2": "Health expenditure on reproductive health",
    "dis3": "Health expenditure on nutritional deficiencies",
    "dis4": "Health expenditure on non-communicable diseases",
    "dis5": "Health expenditure on injuries",
    "disnec": "Health expenditure on other diseases and conditions",

}


def gen_mappers() -> tuple[list[str], dict[str, str], dict[str, str]]:
    """return tuple containing indicator code list, indicator name mapper, and unit mapper"""

    inds = []
    inds_name_mapper = {}
    inds_units_mapper = {}

    for ind_code, ind_name in INDICATORS.items():
        for unit_code, unit_name in units.items():
            code = f"{ind_code}{unit_code}"
            inds.append(code)
            inds_name_mapper[code] = ind_name
            inds_units_mapper[code] = unit_name

    return inds, inds_name_mapper, inds_units_mapper


def fetch_ghed_data() -> pd.DataFrame:
    """Fetch GHED data from the GHED site"""

    ghed = GHED()
    return ghed.get_data()

def format_data(df: pd.DataFrame) -> pd.DataFrame:
    """Format the GHED data"""

    inds, inds_name_mapper, inds_units_mapper = gen_mappers()

    return (df
          .loc[lambda d: d.indicator_code.isin(inds), ["country_name", "iso3_code", "year", "indicator_code", "value"]]
          .assign(unit=lambda d: d.indicator_code.map(inds_units_mapper),
                  indicator_name=lambda d: d.indicator_code.map(inds_name_mapper)
                  )
          )


def split_and_save(df: pd.DataFrame) -> None:
    """Split dataframe into dataframe per indicator and save to CSV files"""



    for code, name in INDICATORS.items():
        (df.loc[lambda d: d.indicator_name == name]
         .reset_index(drop=True)
         .to_csv(Paths.data / f"ghed/{code}.csv", index=False)
         )

if __name__ == "__main__":

    # Fetch GHED data
    data = fetch_ghed_data()

    # Format the data
    formatted_data = format_data(data)

    # Save each indicator to a separate CSV file
    split_and_save(formatted_data)

    logger.info("GHED data extracted and saved to CSV files.")