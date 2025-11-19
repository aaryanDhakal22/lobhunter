# 🦞 LobHunter Makefile Guide

This Makefile provides convenient commands to manage your LobHunter development environment. All commands are designed to make your development workflow as smooth as possible.

## 🚀 Quick Start

```bash
# Complete project setup (first time)
make setup

# Start development environment
make dev

# Quick start (if already built)
make quick

# View all available commands
make help
```

## 📖 Common Workflows

### 🔧 Development Workflow

```bash
# Start your day
make dev                    # Build and start everything
make logs                   # Watch logs in real-time

# During development
make restart                # Restart services after changes
make backend-shell          # Access Django shell
make db-migrate            # Apply database changes

# End your day
make stop                   # Stop all services
```

### 🗄️ Database Workflow

```bash
# Make model changes
make db-makemigrations      # Create migration files
make db-migrate            # Apply migrations

# Database management
make db-backup             # Backup current data
make db-shell              # Open PostgreSQL shell
make db-reset              # ⚠️ Reset database (deletes all data!)
```

### 🐛 Debugging Workflow

```bash
# Check what's running
make status                 # Show container status
make health                 # Health check all services

# View logs
make logs                   # All services
make logs-backend          # Backend only
make logs-frontend         # Frontend only

# Troubleshooting
make doctor                # Run diagnostics
make fix-ports             # Kill processes on used ports
```

## 📊 Command Categories

### 🐳 Docker Commands
- `make build` - Build all containers
- `make start` - Start all services
- `make stop` - Stop all services
- `make restart` - Restart services
- `make clean` - Remove containers and volumes
- `make reset` - Complete reset (clean + build + start)

### 📋 Monitoring & Logs
- `make logs` - View all logs
- `make logs-backend` - Backend logs only
- `make logs-frontend` - Frontend logs only
- `make status` - Container status
- `make health` - Health check

### 🗄️ Database Management
- `make db-migrate` - Run migrations
- `make db-makemigrations` - Create migrations
- `make db-shell` - Database shell
- `make db-backup` - Backup database
- `make db-restore` - Restore from backup
- `make db-reset` - ⚠️ Reset database

### 🖥️ Backend Commands
- `make backend-shell` - Django shell
- `make backend-bash` - Bash shell
- `make backend-test` - Run tests
- `make backend-createsuperuser` - Create admin user

### 🎨 Frontend Commands
- `make frontend-shell` - Frontend shell
- `make frontend-install` - Install dependencies
- `make frontend-build` - Build for production

### 🔧 Development Tools
- `make sync` - Trigger order sync
- `make orders` - View current orders
- `make test` - Run all tests
- `make lint` - Run code linting

### 🆘 Troubleshooting
- `make doctor` - Run diagnostics
- `make fix-permissions` - Fix file permissions
- `make fix-ports` - Clear blocked ports
- `make network` - Show network info

## 🏃 Shortcuts (Aliases)

For frequently used commands:

```bash
make up         # → make start
make down       # → make stop
make shell      # → make backend-shell
make build-up   # → make build + start
make rebuild    # → make build-no-cache + start
```

## 📦 Production Commands

```bash
make prod                   # Start production environment
make prod-build            # Build production containers
make prod-logs             # View production logs
```

## 🔍 Monitoring Commands

```bash
make ps                     # Show running containers
make top                    # Container resource usage
make inspect-backend       # Backend container details
make volumes               # Docker volumes info
```

## 💡 Pro Tips

### 1. **Multiple Terminal Windows**
```bash
# Terminal 1: Start services
make dev

# Terminal 2: Watch logs
make logs

# Terminal 3: Development work
make backend-shell
```

### 2. **Quick Debugging**
```bash
# Something not working?
make doctor                 # Check overall health
make status                 # Check container status
make logs-backend          # Check backend logs
```

### 3. **Database Workflow**
```bash
# After model changes
make db-makemigrations
make db-migrate

# Before major changes
make db-backup
```

### 4. **Clean Start**
```bash
# If things get messy
make reset                  # Nuclear option - clean everything and start fresh
```

## ⚠️ Important Notes

- **Database Reset**: `make db-reset` will delete ALL your data. Always backup first!
- **Port Conflicts**: Use `make fix-ports` if you get port binding errors
- **Permissions**: Use `make fix-permissions` if you get file permission errors
- **First Time**: Always run `make setup` for initial project setup

## 🆘 Getting Help

If something isn't working:

1. Run `make doctor` for diagnostics
2. Check `make status` for container status
3. View logs with `make logs`
4. Try `make reset` for a clean start

For the complete list of commands and their descriptions, run:
```bash
make help
```

## 🎯 Example Development Session

```bash
# Start your development session
cd lobhunter
make dev

# Make some changes to your code...

# Test your changes
make sync                   # Trigger order sync
make orders                 # Check current orders

# Make database changes
vim backend/lobhunter/models.py
make db-makemigrations
make db-migrate

# Debug an issue
make logs-backend          # Check backend logs
make backend-shell         # Open Django shell for testing

# End your session
make stop
```

This Makefile is designed to make your LobHunter development experience as smooth as possible. Happy coding! 🦞