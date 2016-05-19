

# Manual Installation (for now)

```
vagrant up
vagrant ssh 
virtualenv poca --no-site-packages
# On each vagrant ssh, need to run . poca/bin/activate
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
