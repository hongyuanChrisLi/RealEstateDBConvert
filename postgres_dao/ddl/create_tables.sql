DROP TABLE IF EXISTS zipcode;
DROP TABLE IF EXISTS city;
DROP TABLE IF EXISTS county;
DROP TABLE IF EXISTS prop_addr_price_rpt;
DROP TABLE IF EXISTS mls_daily_rpt;

CREATE TABLE county
(
    COUNTY_ID int,
    NAME varchar(20),
    CONSTRAINT COUNTY_PK PRIMARY KEY(COUNTY_ID)
);

CREATE TABLE city
(
    CITY_ID int,
    NAME varchar(20),
    COUNTY_ID int REFERENCES county(COUNTY_ID),
    CONSTRAINT CITY_PK PRIMARY KEY(CITY_ID)
);

CREATE TABLE zipcode
(
    AREA_ID int,
    ZIPCODE varchar(5),
    CITY_ID int REFERENCES city(CITY_ID),
    CONSTRAINT ZIPCODE_PK PRIMARY KEY(AREA_ID)
);

CREATE TABLE prop_addr_price_rpt
(
    RPT_ID int,
    COUNTY_ID int,
    CITY_ID int,
    ZIPCODE varchar(5),
    PROP_TYPE_ID int,
    RPT_DATE date,
    AVG_PRICE numeric(10,2),
    AVG_PRICE_STRUCT_SQFT numeric(10,2),
    AVG_PRICE_TOT_SQFT numeric(10,2)
);

CREATE INDEX prop_addr_price_rpt_idx1
ON prop_addr_price_rpt(COUNTY_ID, CITY_ID, ZIPCODE, PROP_TYPE_ID);

CREATE TABLE mls_daily_rpt
(
    COUNTY_ID	int,
    CITY_ID	int,
    AVG_PRICE_STRUCT_SQFT	numeric(10,2),
    AVG_PRICE_TOT_SQFT	numeric(10,2),
    SINGLE_FAMILY_NUM	int,
    TOWNHOUSE_NUM	int,
    CONDO_NUM	int,
    MULTI_UNIT_NUM	int,
    MOBILE_NUM	int,
    CONSTRAINT MLS_DAILY_RPT_PK
    PRIMARY KEY (COUNTY_ID, CITY_ID)
);