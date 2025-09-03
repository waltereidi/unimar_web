build:
	docker compose build
run:
	docker compose up -d --remove-orphans 
stop:
	docker compose stop
bash:
	docker compose exec -it flask bash
bashvue:
	docker compose exec -it vue bash
bashdb: 
	docker compose exec -it db bash
runserver:
	docker compose run -p 5000:5000 -p 5678:5678 flask \
	python -m debugpy --listen 0.0.0.0:5678 --wait-for-client -m flask run --host=0.0.0.0 --port=5000 --reload

build-dev:
	docker-compose -f docker-compose.dev.yml  build
runvue:
	docker compose run vue npm install && npm run dev -- --host 0.0.0.0
