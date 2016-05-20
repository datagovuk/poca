

# Manual Installation (for now)

```
vagrant up
vagrant ssh 
sudo apt-get update
sudo apt-get install python-virtualenv postgis postgresql-server-dev-9.3 python3-cxx-dev git
virtualenv -p /usr/bin/python3 ~/poca
. ~/poca/bin/activate
cd /vagrant
pip install -r requirements/dev.txt
...

```


# Running the server

```
. ~/poca/bin/activate
cd /vagrant
python project/manage.py runserver
```
