createuser:
	python manage.py shell < shell/create_user.py

createcompanies:
	python manage.py shell < shell/create_companies.py

createpersons:
	python manage.py shell < shell/create_persons.py

createstatus:
	python manage.py shell < shell/create_status.py

createproducts:
	python manage.py shell < shell/create_products.py
