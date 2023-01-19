# Astro Soda


### Install conda
> Install conda by going to https://docs.conda.io/en/latest/miniconda.html and choose your operating system (Windows, Mac or Linux).
 
> Download and run the installer to install conda.

### Create a new conda environment
> conda create -n stenv python=3.9

### Activate the conda environment
> conda activate stenv

### Install Airflow
#### set below parameters in bash_profile or zshrc
> export AIRFLOW_HOME=~/airflow
> AIRFLOW_VERSION=2.5.0
> PYTHON_VERSION=3.9.0
> export CONSTRAINT_URL= https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt
#### After this run pip install
> pip install "apache-airflow==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"

### Install the Astro CLI in MAC
> brew install astro

### Install the Astro CLI in Linux
> curl -sSL install.astronomer.io | sudo bash -s

### Install the Astro CLI in Windows
> Go to the Releases page of the Astro CLI GitHub repository, 
> scroll to a CLI version, and then download the .exe file that matches 
> the CPU architecture of your machine.

### Configure a new Astro project to run Airflow locally
> mkdir astro-soda-tutorial && cd astro-soda-tutorial
> astro dev init

### Run the following command to start your project in a local environment:
> astro dev start
> or 
> airflow standalone

### To run manually
> airflow db init
> airflow users create \       
    --username admin \
    --firstname Pravash \
    --lastname Panigrahi \
    --role Admin \
    --email pravash.cse@gmail.com
>
>> 'airflow db init' command. and created user by using 'airflow users create' command.
>> after doing this step by step. use localhost:8080 in place 0.0.0.0:8080.
>> In the browser use admin as username and password you can get from 
>> file- standalone_admin_password.txt inside /airflow folder

#### for error - alembic.util.exc.CommandError: Can't locate revision identified by '290244fb8b83'
> airflow db reset

### Error response from daemon: Ports are not available: listen tcp  127.0.0.1:5432: bind: address already in use
> lsof -i :5432
> kill <pid> or kill -9 <pid>
>kill them all at once with sudo lsof -i tcp:8080 | grep 'username' | awk '{print $2}' | xargs kill -9

### set below lines to include your folder as airflow dag otherwise by default it will load dags form site-packages
> dags_folder = /Users/pravashpanigrahi/PycharmProjects/python_streamlit_lib/astro_soda/dags
> load_examples = False

### use conda env in bash_command in DAG
> conda init bash && source /Library/anaconda3/etc/profile.d/conda.sh && conda activate 

### soda cli command
> pip install soda-core && soda scan -d soda_test -c {SODA_PATH}/configuration.yml {SODA_PATH}/checks.yml 