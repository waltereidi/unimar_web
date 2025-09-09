build:
	docker compose -f docker-compose.dev.yml up --build
build-prod:
	docker compose -f docker-compose.prod.yml up --build -d
run:
	docker compose -f docker-compose.dev.yml up -d --remove-orphans 
stop:
	docker compose -f docker-compose.dev.yml stop
bash:
	docker compose exec  -it flask bash
bashvue:
	docker compose -f docker-compose.dev.yml exec -it vue bash
bashdb: 
	docker compose exec -it db bash
runserver:
	docker compose run -p 5000:5000 flask gunicorn -w 4 -b 0.0.0.0:5000 main:app
build-dev:
	docker-compose -f docker-compose.dev.yml  build
runvue:
	docker compose run  -p 5173:5173 vue npm install && npm run build  --remove-orphans
install:
	apt update && apt install docker.io && systemctl start docker && systemctl enable docker 
