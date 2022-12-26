from soda.scan import Scan
from soda.sampler.sampler import Sampler

scan = Scan()
scan.set_data_source_name("snowflake_sample_data")

# add configuration from file
scan.add_configuration_yaml_file(file_path="./configuration.yml")

# add variable
scan.add_variables({"date": "2022-12-21"})

# add check file
scan.add_sodacl_yaml_file("./checks.yml")

# execute the scan
# scan.execute()
exit_code = scan.execute()

# set logs to verbose mode, equivalent to CLI -V option
scan.set_verbose(True)

print(scan.get_logs_text())
print(scan.assert_no_checks_fail())

# inspect the scan result
res = scan.get_scan_results()
# print(res)

