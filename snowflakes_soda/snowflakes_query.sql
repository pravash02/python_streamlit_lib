--create schema soda_schema_poc;

--create or replace table soda_poc (
--  custkey number default null,
--  orderdate date default null,
--  orderstatus varchar(100) default null,
--  price varchar(255)
--)

--insert into soda_poc (custkey, orderdate, orderstatus, price)
--   values (1, CURRENT_DATE, 'success', '100');


CREATE OR REPLACE FUNCTION soda_poc_function()
 returns string
 language python
 runtime_version = '3.8'
 imports=('@SODA_STAGE/soda_core-3.0.19-py3-none-any.whl',
          '@SODA_STAGE/test1.csv')
 packages = ('soda', 'pandas', 'streamlit', 'pip')
 handler='compute'
as
 $$
import sys
import os
import json
import streamlit as st

print('Inside snwflakes UDF')
with open(os.path.join(sys._xoptions["snowflake_import_directory"], 'test1.csv'), "r") as f:
    s = f.read()

def compute():
    return s
$$;

select soda_poc_function();


-- snowsql setup in mac

--brew install --cask snowflake-snowsql
-- run the installer from mac's -> Application folder

-- add line - alias <alias snowsql=/Applications/SnowSQL.app/Contents/MacOS/snowsql>
--vi ~/.zshrc
--vi ~/.bash_profile
--source ~/.zshrc
--source ~/.bash_profile

--snowsql -a vrcleuv-ie46785
--use WAREHOUSE PRAY_TEST;
--use DATABASE SODA_TEST;
--use SCHEMA SODA_SCHEMA_POC;

--PUT file:///Users/pravashpanigrahi/Desktop/test1.csv @SODA_STAGE AUTO_COMPRESS=FALSE OVERWRITE=TRUE;
--PUT file:///Users/pravashpanigrahi/Desktop/soda_core-3.0.19-py3-none-any.whl @SODA_STAGE AUTO_COMPRESS=FALSE OVERWRITE=TRUE;