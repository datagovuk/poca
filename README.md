

# Manual Installation (for now)

```
vagrant up
vagrant ssh 
sudo apt-get update
sudo apt-get install python-virtualenv postgresql-server-dev-9.3 postgresql python3-cxx-dev git postgresql-client  postgresql-9.3-postgis-2.1
virtualenv -p /usr/bin/python3 ~/poca
. ~/poca/bin/activate
cd /vagrant
pip install -r requirements/dev.txt
...

```

## Creating the database 

```
sudo -u postgres createuser poca 
sudo -u postgres createdb poca_dev -E utf8 -O poca
sudo -u postgres psql poca_dev -c 'CREATE EXTENSION postgis;'
```

## Migrations

Define your model in poca/models/ and make sure to import the class into 
/poca/models/__init__.py

```` 
python project/manage.py db migrate -m 'A message' 
````

To run migrations (if they have changed or another dev has added a model)

```
python project/manage.py db upgrade
```

The command to downgrade is, erm, downgrade

# Loading data

Use the manage.py command, for example

```bash
# Get list of known commands
python project/manage.py

# Import carpark data
python project/manage.py carparks -i data/carparks.csv
```

# Running the server

```
. ~/poca/bin/activate
cd /vagrant
python project/manage.py runserver
```
