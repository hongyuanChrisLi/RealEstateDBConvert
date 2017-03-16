DROP TABLE IF EXISTS county;
DROP TABLE IF EXISTS prop_addr_price_month_rpt;
DROP TABLE IF EXISTS mls_price_rpt;

CREATE TABLE county
(
    COUNTY_ID int,
    NAME varchar(20)
);

CREATE TABLE prop_addr_price_month_rpt
(
    AREA_ID int ,
    PROP_TYPE_ID int,
    RPT_DATE date,
    CITY varchar(20),
    ZIPCODE varchar(5),
    AVG_PRICE numeric(10,2),
    AVG_PRICE_STRUCT_SQFT numeric(10,2),
    AVG_PRICE_TOT_SQFT numeric(10,2)
);

CREATE TABLE mls_price_rpt(
    AREA_ID int ,
    PROP_TYPE_ID int,
    RPT_DATE date,
    CITY varchar(20),
    ZIPCODE varchar(5),
    AVG_PRICE numeric(10,2),
    AVG_PRICE_STRUCT_SQFT numeric(10,2),
    AVG_PRICE_TOT_SQFT numeric(10,2),
    TOT_NUM int
);