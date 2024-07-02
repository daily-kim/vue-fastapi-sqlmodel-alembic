reset:
	@docker-compose down -v   
	@docker-compose up -d --build
	
down:
	@docker-compose down -v   

up:
	@docker-compose up -d --build

alembic_reset:
	@docker-compose exec backend alembic downgrade base
	@docker-compose exec backend sh -c 'rm -r ./migrations/versions/*init.py'
	@docker-compose exec backend alembic revision --autogenerate -m  "init" --rev-id=1
	@docker-compose exec backend alembic upgrade head
