from typing import List, Tuple

import numpy as np
import pandas as pd

# read data
data = pd.read_csv("data/immo_data.csv", nrows=10000,lineterminator='\n')
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 2000)
print(data.head(1))
# schema design
## table: address
# - regionLevel1 e.g. (Nordrhein_Westfalen, Rheinland_Pfalz)
# - houseNumber e.g. (244)
# - street e.g. (Schüruferstraße)
# - postcode e.g. (44269.0, 67459.0)
# - floor e.g. (1.0)
# - regionLevel2 e.g. (Dortmund, Rhein_Pfalz_Kreis)
# - regionLevel3 e.g. (Schüren, Böhl_Iggelheim)
## table: charges and rent info
# - serviceCharge e.g. (245.0, 134.0)
# - totalRent e.g. (840.0  )
# - heatingCosts e.g. (87.23)
# - electricityBasePrice (90.76)
# - electricityKwhPrice (0.2265)
## table: unit
# - heatingType e.g. (central_heating, self_contained_central_heating)
# - newlyConst e.g. (False)
# - balcony e.g. (False)
# - yearConstructed e.g. (1965.0, 1871.0)
# - noParkSpaces e.g. (1.0, 2.0)
# - firingTypes e.g. (oil, gas)
# - kitchen e.g. (False)
# - cellar e.g. (True)
# - livingSpace e.g. (86.0)
# - condition e.g. (well_kept, refurbished, first_time_use, fully_renovated)
# - interiorQuality e.g. (normal, sophisticated)
# - petsAllowed e.g. (no, negotiable)
# - lift e.g. (False)
# - typeOfFlat e.g. (ground_floor, apartment, other, roof_storey)
# - noRooms e.g. (4.0, 3.0)
# - numberOfFloors e.g. (3.0)
# - garden e.g. (True)
# - energyEfficiencyClass (B, E)
# - lastRefurbish e.g. (2019.0)
## table: telekom
# - telekomTvOffer e.g. (ONE_YEAR_FREE)
# - telekomHybridUploadSpeed e.g. (10.0)
# - telekomUploadSpeed e.g. (10.0, 2.4, 40.0)
## table: unit_ad
# - description e.g. (Die ebenerdig zu erreichende Erdgeschosswohnun...)
# - facilities e.g. (Die Wohnung ist mit Laminat ausgelegt. Das Bad...)
# - date

#---------------------------
# check possible unique content in columns
number_of_unique_content_per_column: List[Tuple[str, int]] = []
for col in data.columns:
    number_of_unique_content_per_column.append((col, len(data[col].unique())))
number_of_unique_content_per_column.sort(key=lambda x: x[1]) # sort base on number of unique items
print(number_of_unique_content_per_column)

for col, number_of_unique_content_per_col in number_of_unique_content_per_column:
    if number_of_unique_content_per_col < 30:
        print(f"col: {col} has {number_of_unique_content_per_col} items: {data[col].unique()}")

print(data[['telekomTvOffer', 'telekomHybridUploadSpeed', 'telekomUploadSpeed']].nunique())


telekoms = data[['telekomTvOffer', 'telekomHybridUploadSpeed', 'telekomUploadSpeed']]
addresses = data[['regionLevel1', 'regionLevel2', 'regionLevel3', 'street', 'houseNumber', 'floor', 'postcode']]
cost_infos = data[['electricityBasePrice', 'electricityKwhPrice', 'heatingCosts', 'serviceCharge', 'totalRent']]
units = data[['heatingType',
              'newlyConst',
              'balcony',
              'yearConstructed',
              'noParkSpaces',
              'firingTypes',
              'kitchen',
              'cellar',
              'livingSpace',
              'condition',
              'interiorQuality',
              'petsAllowed',
              'lift',
              'typeOfFlat',
              'noRooms',
              'numberOfFloors',
              'garden',
              'energyEfficiencyClass',
              'lastRefurbish'
              ]]

unit_ads = data[['description', 'facilities']]
print(len(telekoms.drop_duplicates()))  # 13
print(len(addresses.drop_duplicates()))  # 197467
print(len(cost_infos.drop_duplicates()))  # 130973
print(len(units.drop_duplicates()))  # 252817
print(len(unit_ads.drop_duplicates()))  # 243980
print(len(data.drop_duplicates()))  # 265897
