# Variables
COMPOSE = docker-compose
PROJECT_NAME = 00_project_name

# Commandes docker-compose
up:
	$(COMPOSE) up -d

clean:
	docker system prune -f 

down:
	$(COMPOSE) down -v --remove-orphans

build:
	$(COMPOSE) build --no-cache

logs:
	$(COMPOSE) logs -f backend frontend elasticsearch kibana scraper

# Commandes app
scrape-local:
	@echo "🚀 Running local scraper (dev mode)..."
	python3 scraper/scraper.py

scrape:
	@echo "🚀 Running scraper (Docker container)..."
	$(COMPOSE) run --rm scraper

index:
	@echo "🚀 Running indexer..."
	python backend/app/src/indexer.py

# All in one (Scrape + Index + Up)
refresh:
	make scrape
	make index
	make up
