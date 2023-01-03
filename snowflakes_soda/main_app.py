# run this code: streamlit run ./snowflakes_soda/main_app.py
"""
ocsp_fail_open - Online Certificate Status Protocol
    Snowflake sends a certificate to confirm that the connection is to Snowflake
    rather than to a host that is impersonating Snowflake)
"""

import streamlit as st
import pandas as pd
import json
import os
import snowflake.connector


def snowflake_conn():
    try:
        conn = snowflake.connector.connect(
            user='pravash02',
            password='Prav@041193',
            account='to55035.central-india.azure',
            warehouse='PRAY_TEST'
        )
        conn.autocommit(True)
        cur = conn.cursor()
        st.write('connection is successful')
        st.write(cur)
        return conn, cur
    except Exception as e:
        raise e


def snowflake_db_query():
    conn, cur = snowflake_conn()
    try:
        # cur.execute("select * from SNOWFLAKE_SAMPLE_DATA.TPCH_SF100.CUSTOMER")
        # one_row = cur.fetchone()

        tbl_list = []
        cur.execute("SHOW TABLES IN snowflake_sample_data.tpch_sf100")
        sfqid = cur.__dict__['_sfqid']      # last executed query
        cur.execute(f"select * from table(result_scan('{sfqid}'))")
        tbl_names = cur.fetchall()
        for tup in tbl_names:
            tbl_list.append(tup[1])
        return tbl_list
    except Exception as e:
        print(e)
    finally:
        cur.close()
    conn.close()


def main(file_path, files):
    # read json file
    for file in files:
        with open(file_path + file, 'r') as data:
            file_data = json.load(data)
            if type(file_data['table_nm']) != list:
                final_report = {}
                for key, val in file_data['table_nm'].items():
                    if key not in final_report.keys():
                        final_report[key] = [val]
                    else:
                        final_report[key] = final_report[key].append(val)
                df = pd.DataFrame(final_report)
                df = df.reset_index(drop=True)

        row_data = df.to_dict("records")
        column_data = [{"field": col, "headerName": col} for col in df.columns]
        st.write(df)


if __name__ == '__main__':
    # list json files
    dir_path = os.path.dirname(os.path.realpath(__file__))
    path_to_json = dir_path + '/json_file/'
    json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]
    # print(path_to_json, json_files)
    # main(path_to_json, json_files)
    snowflake_db_query()
