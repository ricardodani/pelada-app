run:
	uvicorn main:app --host 0.0.0.0 --port 8000

update-requirements:
	pip freeze > requirements.txt

install-requirements:
	pip install requirements.txt

install-heroku:
	curl https://cli-assets.heroku.com/install-ubuntu.sh | sh