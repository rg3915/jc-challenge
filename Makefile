createuser:
	python manage.py shell < shell/create_user.py

createcompanies:
	python manage.py shell < shell/create_companies.py

createpersons:
	python manage.py shell < shell/create_persons.py
