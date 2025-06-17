""""Generate UNAIDS data"""

from bblocks.data_importers import UNAIDS
import pandas as pd

from src.config import Paths, logger


INDICATORS: dict = {
    # mortality
    "aids_mortality_per_1000_population": "AIDS mortality per 1000 population",
    "aids_orphans": "AIDS Orphans",
    "aids_related_deaths": "AIDS-related deaths",

    # incidence
    "hiv_incidence_per_1000_population": "HIV Incidence per 1000 population",
    "new_hiv_infections": "New HIV Infections",
    "hiv_prevalence": "HIV Prevalence",
    "people_living_with_hiv": "People living with HIV",

    # treatment and care
    "art_coverage_people_living_with_hiv": "Coverage of people living with HIV receiving ART",
    "people_on_art": "People receiving antiretroviral therapy",
    "hiv_testing_pregnant_women": "HIV testing in pregnant women",
    "new_hiv_infections_averted_pmtct": "New HIV Infections averted due to PMTCT",
    "deaths_averted_due_to_art": "Deaths averted due to ART"
}


def fetch_indicators() -> pd.DataFrame:
    """Fetch UNAIDS indicator data from UNAIDS site"""

    unaids = UNAIDS()
    data = unaids.get_data()

    return data.loc[lambda d: d.indicator_name.isin(INDICATORS.values())].reset_index(drop=True)


def split_and_save(df: pd.DataFrame) -> None:
    """Split dataframe into dataframe per indicator and save to CSV files"""

    for code, name in INDICATORS.items():
        (df.loc[lambda d: d.indicator_name == name]
            .reset_index(drop=True)
            .to_csv(Paths.data / f"hiv/{code}.csv", index=False)
        )


if __name__ == "__main__":

    # Fetch UNAIDS data
    data = fetch_indicators()

    # Save each indicator to a separate CSV file
    split_and_save(data)

    logger.info("HIV data extracted and saved to CSV files.")