# snowflakes_soda % streamlit run soda_scan.py


import json
from soda.scan import Scan
import streamlit as st
from soda.sampler.sampler import Sampler
# from snowflakes_soda.main_app import snowflake_db_query

scan = Scan()
scan.set_data_source_name("snowflake_sample_data")

# add configuration from file
scan.add_configuration_yaml_file(file_path="./config/configuration.yml")

# add variable
scan.add_variables({"date": "2022-12-21"})

# set logs to verbose mode, equivalent to CLI -V option
scan.set_verbose(True)

required_fields = ['defaultdataSource', 'table', 'outcome', 'logs.message']


def run_scan(scan):
    # execute the scan
    scan.execute()

    # inspect the scan result
    res = scan.get_scan_results()
    return res


def write_json(file_nm, json_res):
    with open(f"./json_output/{file_nm}.json", "w") as write_file:
        json.dump(json_res, write_file, indent=4)

# getting table list
# tbl_list = snowflake_db_query
# print(tbl_list)


option = st.selectbox('Select a SnowFlakes Dataset',
                      ('', 'CUSTOMER', 'LINEITEM'),
                      )
if option == '':
    st.write('Please select from the dropdown')
else:
    st.write('You have selected: ', option)

    # add check file
    scan.add_sodacl_yaml_file(f"./checks/{option.lower()}_check.yml")

    if scan.has_error_logs() and option == '':
        pass
    elif scan.has_error_logs():
        st.error(f"selected option: {option} check.yml file not found")
    else:
        json_res = run_scan(scan)
        temp1 = scan.get_all_checks_text()
        # out = {item: json_res.get(item) for item in required_fields}
        st.write(f"{temp1}")
        write_json(option, json_res)


