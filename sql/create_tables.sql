CREATE TABLE IF NOT EXISTS telekoms
(
    telekom_id
    int
    NOT
    NULL,
    telekomTvOffer
    varchar
(
    255
),
    telekomHybridUploadSpeed float ,
    telekomUploadSpeed float ,
    PRIMARY KEY
(
    telekom_id
)
    );

CREATE TABLE IF NOT EXISTS addresses
(
    address_id int NOT NULL,
    regionLevel1 varchar(255),
    regionLevel2 varchar(255),
    regionLevel3 varchar(255),
    street varchar(255),
    houseNumber int,
    floor int,
    postcode int,
    PRIMARY KEY(address_id)
);

CREATE TABLE IF NOT EXISTS cost_infos
(
    cost_info_id int NOT NULL,
    electricityBasePrice float,
    electricityKwhPrice float,
    heatingCosts float,
    serviceCharge float,
    totalRent float,
    PRIMARY KEY (cost_info_id)
    );



CREATE TABLE IF NOT EXISTS units
(
    unit_id int NOT  NULL,
    heatingType varchar(255),
    firingTypes varchar(255) ,
    condition varchar(255) ,
    typeOfFlat varchar(255) ,
    interiorQuality varchar(63) ,
    petsAllowed varchar(63) ,
    energyEfficiencyClass varchar(63) ,
    lastRefurbish int,
    numberOfFloors int,
    noParkSpaces int,
    yearConstructed int,
    noRooms float ,
    livingSpace float ,
    newlyConst BOOLEAN,
    balcony BOOLEAN,
    kitchen BOOLEAN,
    cellar BOOLEAN,
    lift BOOLEAN,
    garden BOOLEAN,
    address_id int,
    telekom_id int,
    cost_info_id int,
    PRIMARY KEY(unit_id),
    CONSTRAINT fk_address FOREIGN KEY(address_id) REFERENCES addresses(address_id),
    CONSTRAINT fk_telekom FOREIGN KEY(telekom_id) REFERENCES telekoms(telekom_id),
    CONSTRAINT fk_cost_info FOREIGN KEY(cost_info_id) REFERENCES cost_infos(cost_info_id)
    );

CREATE TABLE IF NOT EXISTS unit_ads
(
    unit_ad_id int NOT NULL,
    description TEXT,
    facilities TEXT,
    date varchar(255),
    unit_id int, PRIMARY KEY(unit_ad_id),
    CONSTRAINT fk_unit FOREIGN KEY(unit_id) REFERENCES units(unit_id)
    );


CREATE VIEW unit_offers AS
(
select regionLevel1,
       serviceCharge,
       heatingType,
       telekomTvOffer,
       telekomHybridUploadSpeed,
       newlyConst,
       balcony,
       telekomUploadSpeed,
       totalRent,
       yearConstructed,
       noParkSpaces,
       firingTypes,
       kitchen,
       cellar,
       houseNumber,
       livingSpace,
       condition,
       interiorQuality,
       petsAllowed,
       street,
       lift,
       typeOfFlat,
       postcode,
       noRooms,
       floor,
       numberOfFloors,
       garden,
       regionLevel2,
       regionLevel3,
       description,
       facilities,
       heatingCosts,
       energyEfficiencyClass,
       lastRefurbish,
       electricityBasePrice,
       electricityKwhPrice
from unit_ads
         join (
    (
        (
            units join addresses on units.address_id = addresses.address_id)
            join telekoms on units.telekom_id = telekoms.telekom_id
        )
        join cost_infos on units.cost_info_id = cost_infos.cost_info_id
    )
              on unit_ads.unit_id = units.unit_id
    );
