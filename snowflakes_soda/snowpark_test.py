from snowflake.snowpark import Session
from soda.scan import Scan
from soda.data_sources.snowflake_data_source import SnowflakeDataSource
from snowflake.snowpark.functions import udf
import json


connection_parameters = {
    "account": "vrcleuv-ie46785",
    "user": "pravash02",
    "password": "***",
    "role": "ACCOUNTADMIN",  # optional
    "warehouse": "PRAY_TEST",  # optional
    "database": "SODA_TEST",  # optional
    "schema": "SODA_SCHEMA_POC",  # optional
  }  

new_session = Session.builder.configs(connection_parameters).create()
# print(new_session)

# creating custom dataframe
# print("test dataframe - ")
# data = [["1", "2023-01-13", "success", "100"]]
# columns = ["CUSTKEY", "ORDERDATE", "ORDERSTATUS", "PRICE"]
# dataframe = new_session.createDataFrame(data, columns)
# print(type(dataframe))
# dataframe.show()

# getting table data
print("snowflakes table data")
session_df = new_session.table("SODA_POC")
# session_df.createOrReplaceTempView('soda_poc_df')
print(type(session_df))

# test dataframe
temp_df = new_session.createDataFrame(['1']).to_df('col')
temp_df.createOrReplaceTempView('soda_poc_df')

scan = Scan()
scan.set_scan_definition_name("soda_poc_tbl_scan")
scan.set_data_source_name("spark_df")

# scan.add_configuration_yaml_file(file_path="./config/configuration.yml")
scan.add_spark_session(spark_session=new_session, data_source_name='spark_df')

scan.add_sodacl_yaml_file("./checks/snowspark_check.yml")

scan.execute()
res = scan.get_scan_results()
res2 = scan.get_all_checks_text()
res3 = scan.get_logs_text()
print(res)

# with open(f"./snowflakes_soda/json_output/SODA_POC.json", "w") as write_file:
#     json.dump(res, write_file, indent=4)

# df_json = new_session.read.json(f"./snowflakes_soda/json_output/soda_poc.json")
# df_json.show()

