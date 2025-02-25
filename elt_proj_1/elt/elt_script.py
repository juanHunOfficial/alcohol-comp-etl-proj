import subprocess
import time

def wait_for_postgres(host, max_retries=5, delay_seconds=5):
    retires=0
    while retires < max_retries:
        try:
            subprocess.run(['pg_isready', '-h', host], check=True)
            print("Postgres is ready!")
            return
        except subprocess.CalledProcessError:
            print("Postgres is not ready. Waiting...")
            retires += 1
            time.sleep(delay_seconds)
    print(f"Postgres is not ready after {max_retries} retries")
    return False
if not wait_for_postgres(host='source_postgres'):
    exit(1)

print("Starting ELT process")

source_config = {
    'database': 'source_db',
    'user': 'postgres',
    'password': 'secret',
    'host': 'source_postgres'
}

destination_config = {
    'database': 'destination_db',
    'user': 'postgres',
    'password': 'secret',
    'host': 'destination_postgres'
}

dump_command = [
    'pg_dump',
    '-h', source_config['host'],
    '-U', source_config['user'],
    '-d', source_config['dbname'],
    '-f', 'data_dump.sql',
    '-w'
]

subprocess_env = dict(PGPASSWORD=source_config['password'])

subprocess.run(dump_command, env=subprocess_env, check=True)

load_command = [
    'psql',
    '-h', destination_config['host'],
    '-U', destination_config['user'],
    '-d', destination_config['dbname'],
    '-a','-f','data_dump.sql',
]

subprocess_env = dict(PGPASSWORD=destination_config['password'])

subprocess.run(load_command, env=subprocess_env, check=True)

print("ELT process completed")
    

