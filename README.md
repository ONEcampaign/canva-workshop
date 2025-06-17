# Canva workshop data


Here you can find data from the Canva data visalisation workshop supported by 
the [ONE Campaign](https://data.one.org/) on selected global development topics, sourced from reputable organizations
and data providers.

## Datasets

|   | Dataset                                  | Description                          | Source                                                                                                         |                             
|---|------------------------------------------|--------------------------------------|----------------------------------------------------------------------------------------------------------------|
| 1 | [HIV/AIDS](./data/hiv)                   | HIV/AIDS epidemiological indicators  | [UNAIDS](https://aidsinfo.unaids.org/)                                                                         |
| 2 | [Global Health Expenditure](./data/ghed) | Global health expenditure indicators | [WHO](https://apps.who.int/nha/database)                                                                       |
| 3 | [Food Security](./data/wfp)              | Hunger and Food security indicators  | [WFP HungerMap Live](https://hungermap.wfp.org/)                                                               |
| 4 | [Poverty](./data/pov)                    | Poverty indicators                   | [World Bank](https://datatopics.worldbank.org/world-development-indicators/themes/poverty-and-inequality.html) |


### Replication code

The data is extracted from the original sourced using the `bblocks-importers` package
which provides Pythonic access to a range of development data sources. Replication code
to extract the datasets is found in the `src` directory. 

Learn more about the ONE Campaign's data tools and read the
documentation [here](https://docs.one.org/tools/index.html).