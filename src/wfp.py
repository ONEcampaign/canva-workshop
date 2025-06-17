"""Generate WFP food security data"""

from bblocks.data_importers import WFPFoodSecurity
import pandas as pd

from src.config import Paths, logger


def fetch_wfp_data(level) -> pd.DataFrame:
    """Fetch WFP food security data for national and subnational levels."""

    wfp = WFPFoodSecurity()

    return wfp.get_data(level=level)


def save(df: pd.DataFrame, level: str) -> None:
    """Split dataframe into dataframe per country and save to CSV files"""

    df.to_csv(Paths.data / f"wfp/food_security_{level}.csv", index=False)


if __name__ == "__main__":

    # Fetch WFP food security data for national level
    wfp_national = fetch_wfp_data("national").pipe(save, level="national")
    logger.info("Extracted WFP food security data for national level.")

    # Fetch WFP food security data for subnational level
    wfp_subnational = fetch_wfp_data("subnational").pipe(save, level="subnational")
    logger.info("Extracted WFP food security data for subnational level.")