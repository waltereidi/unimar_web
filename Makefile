build:
	docker compose build
run:
	docker compose up -d --remove-orphans 
stop:
	docker compose stop
bash:
	docker compose exec -it flask bash
runserver:
	docker compose run -p 5000:5000 flask  gunicorn -w 4 -b 0.0.0.0:5000 src.main:app