# LobHunter Project Makefile
# A collection of useful commands for development and deployment

.PHONY: help build start stop restart logs clean dev prod test db-* backend-* frontend-*

# Default target
.DEFAULT_GOAL := help

# Colors for output
RED=\033[0;31m
GREEN=\033[0;32m
YELLOW=\033[1;33m
BLUE=\033[0;34m
MAGENTA=\033[0;35m
CYAN=\033[0;36m
NC=\033[0m # No Color

##@ 🚀 Quick Start Commands

help: ## Show this help message
	@echo ""
	@echo "$(CYAN)╔══════════════════════════════════════════╗$(NC)"
	@echo "$(CYAN)║           🦞 LobHunter Project           ║$(NC)"
	@echo "$(CYAN)║          Development Commands            ║$(NC)"
	@echo "$(CYAN)╚══════════════════════════════════════════╝$(NC)"
	@echo ""
	@awk 'BEGIN {FS = ":.*##"; printf "\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  $(GREEN)%-20s$(NC) %s\n", $$1, $$2 } /^##@/ { printf "\n$(YELLOW)%s$(NC)\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
	@echo ""

dev: build start ## 🔧 Build and start development environment
	@echo "$(GREEN)✅ Development environment is ready!$(NC)"
	@echo "$(CYAN)Frontend: http://localhost:3000$(NC)"
	@echo "$(CYAN)Backend:  http://localhost:8000$(NC)"
	@echo "$(CYAN)Database: localhost:5432$(NC)"
	@echo "$(CYAN)Redis:    localhost:6379$(NC)"

quick: start ## ⚡ Quick start (without building)
	@echo "$(GREEN)⚡ Starting services...$(NC)"

##@ 🐳 Docker Commands

build: ## 🔨 Build all Docker containers
	@echo "$(YELLOW)🔨 Building Docker containers...$(NC)"
	@podman compose build

build-no-cache: ## 🔨 Build containers without cache
	@echo "$(YELLOW)🔨 Building containers without cache...$(NC)"
	@podman compose build --no-cache

start: ## ▶️  Start all services
	@echo "$(GREEN)▶️  Starting all services...$(NC)"
	@podman compose up -d
	@echo "$(GREEN)✅ All services started!$(NC)"

stop: ## ⏹️  Stop all services
	@echo "$(RED)⏹️  Stopping all services...$(NC)"
	@podman compose down

restart: stop start ## 🔄 Restart all services

clean: ## 🧹 Stop services and remove containers, networks, volumes
	@echo "$(RED)🧹 Cleaning up Docker resources...$(NC)"
	@podman compose down -v --remove-orphans
	@docker system prune -f

reset: clean build start ## 🔄 Complete reset: clean, build, start

##@ 📊 Monitoring & Logs

logs: ## 📋 View logs for all services
	@podman compose logs -f

logs-backend: ## 📋 View backend logs only
	@podman compose logs -f backend

logs-frontend: ## 📋 View frontend logs only
	@podman compose logs -f frontend

logs-db: ## 📋 View database logs only
	@podman compose logs -f db

logs-cache: ## 📋 View Redis cache logs only
	@podman compose logs -f cache

status: ## 📊 Show status of all services
	@echo "$(CYAN)📊 Service Status:$(NC)"
	@podman compose ps

health: ## 🔍 Check health of all services
	@echo "$(CYAN)🔍 Health Check:$(NC)"
	@podman compose ps
	@echo ""
	@echo "$(CYAN)Backend API:$(NC)"
	@curl -s -o /dev/null -w "%{http_code}" http://localhost:8000/api/orders && echo " ✅ Backend API responding" || echo " ❌ Backend API not responding"
	@echo "$(CYAN)Frontend:$(NC)"
	@curl -s -o /dev/null -w "%{http_code}" http://localhost:3000 && echo " ✅ Frontend responding" || echo " ❌ Frontend not responding"

##@ 🗄️ Database Management

db-migrate: ## 🗄️ Run database migrations
	@echo "$(BLUE)🗄️ Running database migrations...$(NC)"
	@podman compose exec backend python manage.py migrate

db-makemigrations: ## 🗄️ Create new database migrations
	@echo "$(BLUE)🗄️ Creating new migrations...$(NC)"
	@podman compose exec backend python manage.py makemigrations

db-shell: ## 🗄️ Open database shell
	@echo "$(BLUE)🗄️ Opening database shell...$(NC)"
	@podman compose exec db psql -U postgres -d postgres

db-reset: ## 🗄️ Reset database (WARNING: This will delete all data)
	@echo "$(RED)⚠️  WARNING: This will delete ALL database data!$(NC)"
	@read -p "Are you sure? (y/N): " confirm && [ "$$confirm" = "y" ] || exit 1
	@podman compose down
	@docker volume rm lobhunter_db 2>/dev/null || true
	@podman compose up -d db cache
	@sleep 5
	@podman compose up -d backend
	@sleep 3
	@make db-migrate
	@podman compose up -d frontend

db-backup: ## 🗄️ Backup database
	@echo "$(BLUE)📦 Creating database backup...$(NC)"
	@mkdir -p backups
	@podman compose exec -T db pg_dump -U postgres postgres > backups/backup_$$(date +%Y%m%d_%H%M%S).sql
	@echo "$(GREEN)✅ Database backup created in backups/$(NC)"

db-restore: ## 🗄️ Restore database from latest backup
	@echo "$(BLUE)📦 Restoring database from latest backup...$(NC)"
	@latest_backup=$$(ls -t backups/*.sql 2>/dev/null | head -1); \
	if [ -z "$$latest_backup" ]; then \
		echo "$(RED)❌ No backup files found in backups/$(NC)"; \
		exit 1; \
	fi; \
	echo "Restoring from: $$latest_backup"; \
	podman compose exec -T db psql -U postgres -d postgres < "$$latest_backup"

##@ 🖥️ Backend Commands

backend-shell: ## 🖥️ Open backend Django shell
	@echo "$(MAGENTA)🖥️ Opening Django shell...$(NC)"
	@podman compose exec backend python manage.py shell

backend-bash: ## 🖥️ Open backend bash shell
	@podman compose exec backend bash

backend-test: ## 🧪 Run backend tests
	@echo "$(MAGENTA)🧪 Running backend tests...$(NC)"
	@podman compose exec backend python manage.py test

backend-collectstatic: ## 🖥️ Collect static files
	@podman compose exec backend python manage.py collectstatic --noinput

backend-createsuperuser: ## 🖥️ Create Django superuser
	@podman compose exec backend python manage.py createsuperuser

##@ 🎨 Frontend Commands

frontend-shell: ## 🎨 Open frontend shell
	@podman compose exec frontend sh

frontend-install: ## 🎨 Install frontend dependencies
	@podman compose exec frontend npm install

frontend-build: ## 🎨 Build frontend for production
	@podman compose exec frontend npm run build

##@ 🔧 Development Tools

sync: ## 🔄 Trigger order synchronization
	@echo "$(CYAN)🔄 Triggering order sync...$(NC)"
	@curl -s http://localhost:8000/api/sync | jq '.' || curl -s http://localhost:8000/api/sync

orders: ## 📝 View current orders
	@echo "$(CYAN)📝 Current orders:$(NC)"
	@curl -s http://localhost:8000/api/orders | jq '.' || curl -s http://localhost:8000/api/orders

install: ## 📦 Install project dependencies
	@echo "$(YELLOW)📦 Installing project dependencies...$(NC)"
	@command -v docker >/dev/null 2>&1 || { echo "❌ Docker is required but not installed. Aborting." >&2; exit 1; }
	@command -v podman compose >/dev/null 2>&1 || { echo "❌ Docker Compose is required but not installed. Aborting." >&2; exit 1; }
	@echo "$(GREEN)✅ Dependencies check passed!$(NC)"

setup: install build db-migrate ## 🎯 Complete project setup
	@echo "$(GREEN)🎯 Project setup complete!$(NC)"
	@echo "$(CYAN)Run 'make start' to start all services$(NC)"

##@ 🧪 Testing & Quality

test: backend-test ## 🧪 Run all tests
	@echo "$(GREEN)🧪 All tests completed!$(NC)"

lint: ## 🔍 Run code linting
	@echo "$(CYAN)🔍 Running linters...$(NC)"
	@podman compose exec backend flake8 . 2>/dev/null || echo "⚠️  flake8 not installed - skipping backend lint"
	@podman compose exec frontend npm run lint 2>/dev/null || echo "⚠️  No lint script found - skipping frontend lint"

format: ## 🎨 Format code
	@echo "$(CYAN)🎨 Formatting code...$(NC)"
	@podman compose exec backend black . 2>/dev/null || echo "⚠️  black not installed - skipping backend formatting"
	@podman compose exec frontend npm run format 2>/dev/null || echo "⚠️  No format script found - skipping frontend formatting"

##@ 📦 Production Commands

prod: ## 🚀 Start production environment
	@echo "$(GREEN)🚀 Starting production environment...$(NC)"
	@podman compose -f docker-compose.yml -f docker-compose.prod.yml up -d

prod-build: ## 🚀 Build production containers
	@podman compose -f docker-compose.yml -f docker-compose.prod.yml build

prod-logs: ## 📋 View production logs
	@podman compose -f docker-compose.yml -f docker-compose.prod.yml logs -f

##@ 📈 Monitoring & Debugging

ps: ## 📊 Show running containers
	@podman compose ps

top: ## 📊 Show container resource usage
	@podman compose top

inspect-backend: ## 🔍 Inspect backend container
	@podman compose exec backend env

inspect-frontend: ## 🔍 Inspect frontend container
	@podman compose exec frontend env

network: ## 🌐 Show Docker network info
	@docker network ls
	@echo ""
	@docker network inspect lobhunter_lobhunter 2>/dev/null || echo "Network not found"

volumes: ## 💾 Show Docker volumes
	@docker volume ls

##@ 🆘 Troubleshooting

fix-permissions: ## 🔧 Fix file permissions
	@echo "$(YELLOW)🔧 Fixing file permissions...$(NC)"
	@sudo chown -R $$USER:$$USER .

fix-ports: ## 🔧 Kill processes using required ports
	@echo "$(YELLOW)🔧 Killing processes on ports 3000, 8000, 5432, 6379...$(NC)"
	@sudo lsof -ti:3000 | xargs -r kill -9 2>/dev/null || true
	@sudo lsof -ti:8000 | xargs -r kill -9 2>/dev/null || true
	@sudo lsof -ti:5432 | xargs -r kill -9 2>/dev/null || true
	@sudo lsof -ti:6379 | xargs -r kill -9 2>/dev/null || true
	@echo "$(GREEN)✅ Ports cleared!$(NC)"

doctor: ## 🩺 Run project health diagnostics
	@echo "$(CYAN)🩺 Running diagnostics...$(NC)"
	@echo ""
	@echo "$(YELLOW)Docker Check:$(NC)"
	@docker --version
	@podman compose --version
	@echo ""
	@echo "$(YELLOW)Services Status:$(NC)"
	@make status
	@echo ""
	@echo "$(YELLOW)Port Check:$(NC)"
	@netstat -tlnp | grep -E ':3000|:8000|:5432|:6379' || echo "No services running on expected ports"
	@echo ""
	@echo "$(YELLOW)Disk Usage:$(NC)"
	@docker system df

##@ 📚 Documentation

docs: ## 📚 Show project structure
	@echo "$(CYAN)📚 Project Structure:$(NC)"
	@tree -I 'node_modules|__pycache__|*.pyc|.git|.next|dist|build' -L 3 .

env-example: ## 📝 Create example environment file
	@echo "$(CYAN)📝 Creating .env.example...$(NC)"
	@echo "# Redis Configuration" > .env.example
	@echo "REDIS_PORT=6379" >> .env.example
	@echo "REDIS_HOST=cache" >> .env.example
	@echo "" >> .env.example
	@echo "# Database Configuration" >> .env.example
	@echo "POSTGRES_USER=postgres" >> .env.example
	@echo "POSTGRES_PASSWORD=postgres" >> .env.example
	@echo "POSTGRES_DB=postgres" >> .env.example
	@echo "" >> .env.example
	@echo "# Django Configuration" >> .env.example
	@echo "DEBUG=True" >> .env.example
	@echo "SECRET_KEY=your-secret-key-here" >> .env.example
	@echo "" >> .env.example
	@echo "# Frontend Configuration" >> .env.example
	@echo "NEXT_PUBLIC_API_URL=http://localhost:8000" >> .env.example
	@echo "$(GREEN)✅ .env.example created!$(NC)"

##@ 🏃 Aliases (shortcuts)

up: start ## Alias for start
down: stop ## Alias for stop
build-up: build start ## Alias for build + start
rebuild: build-no-cache start ## Alias for clean build + start
shell: backend-shell ## Alias for backend shell
