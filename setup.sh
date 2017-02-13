virtualenv -p python2.7 .venv
source .venv/bin/activate
pip install -r requirements.txt
python contrib/secret_gen.py
python manage.py migrate
make createuser
make createcompanies
make createpersons
make createstatus
make createproducts
python manage.py test
echo "Done. User created:"
echo "user: admin"
echo "email: admin@admin.com"
echo "password: demodemo"
echo "Type: python manage.py test"