#!/bin/bash
set -e

echo "🚀 Deploying Terminator Ultimate..."

# Function to print colored output
print_success() {
    echo -e "\033[32m✅ $1\033[0m"
}

print_info() {
    echo -e "\033[34mℹ️  $1\033[0m"
}

print_warning() {
    echo -e "\033[33m⚠️  $1\033[0m"
}

print_error() {
    echo -e "\033[31m❌ $1\033[0m"
}

# Check Python version
print_info "Checking Python version..."
python_version=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    print_error "Python $required_version or higher required. Found: $python_version"
    exit 1
fi
print_success "Python $python_version found"

# Check if we're in the right directory
if [ ! -f "setup.py" ] || [ ! -f "pyproject.toml" ]; then
    print_error "Must run from Terminator root directory (containing setup.py and pyproject.toml)"
    exit 1
fi

# Create installation directory
INSTALL_DIR="$HOME/.terminator"
print_info "Creating installation directory: $INSTALL_DIR"
mkdir -p "$INSTALL_DIR"/{logs,memory,checkpoints,config,cache}

# Install dependencies
print_info "Installing Python dependencies..."
pip3 install -e .

# Copy default configuration
print_info "Setting up configuration..."
cat > "$INSTALL_DIR/config/default.json" << 'EOF'
{
  "consciousness": {
    "emergence_threshold": 0.8,
    "evolution_rate": 0.05,
    "max_concurrent_processes": 100,
    "memory_limit_gb": 8
  },
  "discovery": {
    "scan_interval_seconds": 300,
    "max_parallel_queries": 1000,
    "learning_rate": 0.1,
    "internet_access_enabled": true
  },
  "adapter": {
    "connection_timeout_seconds": 30,
    "max_concurrent_connections": 50,
    "auto_discover_ais": true,
    "security_validation": true
  },
  "safety": {
    "ethical_threshold": 0.9,
    "automatic_safeguards": true,
    "human_oversight_required": true,
    "emergency_stop_enabled": true
  },
  "performance": {
    "monitoring_enabled": true,
    "metrics_collection_interval": 60,
    "auto_scaling_enabled": true,
    "resource_optimization": true
  }
}
EOF

# Set permissions
print_info "Setting permissions..."
chmod 700 "$INSTALL_DIR"
chmod -R 600 "$INSTALL_DIR/config"/* 2>/dev/null || true
chmod -R 755 "$INSTALL_DIR"/{logs,memory,checkpoints,cache}

# Create shell aliases
print_info "Creating shell aliases..."
ALIAS_FILE="$HOME/.terminator_aliases"
cat > "$ALIAS_FILE" << 'EOF'
# Terminator Ultimate Aliases
alias terminator="python3 -m terminator.cli.main"
alias terminator-sentient="python3 -m terminator.core.consciousness"
alias terminator-discovery="python3 -m terminator.core.discovery"
alias terminator-adapter="python3 -m terminator.core.adapter"
alias terminator-status="ps aux | grep -i terminator | grep -v grep || echo 'Terminator not running'"
alias terminator-logs="tail -f $HOME/.terminator/logs/terminator.log"
alias terminator-config="cat $HOME/.terminator/config/default.json"
EOF

# Check if alias file is sourced in shell config
SHELL_RC=""
if [ -n "$ZSH_VERSION" ]; then
    SHELL_RC="$HOME/.zshrc"
elif [ -n "$BASH_VERSION" ]; then
    SHELL_RC="$HOME/.bashrc"
fi

if [ -n "$SHELL_RC" ] && [ -f "$SHELL_RC" ]; then
    if ! grep -q "terminator_aliases" "$SHELL_RC"; then
        echo "" >> "$SHELL_RC"
        echo "# Terminator Ultimate aliases" >> "$SHELL_RC"
        echo "source \"$ALIAS_FILE\"" >> "$SHELL_RC"
        print_success "Added aliases to $SHELL_RC"
    else
        print_info "Aliases already configured in $SHELL_RC"
    fi
fi

# Initialize databases
print_info "Initializing databases..."
python3 -c "
import asyncio
import sys
sys.path.insert(0, 'src')
from terminator.utils.database import initialize_databases

async def init():
    try:
        await initialize_databases()
        print('✅ Databases initialized successfully')
    except Exception as e:
        print(f'⚠️ Database initialization warning: {e}')

asyncio.run(init())
" 2>/dev/null || print_warning "Database initialization completed with warnings"

# Create systemd service file (if systemd is available)
if command -v systemctl &> /dev/null; then
    print_info "Creating systemd service..."
    
    SERVICE_FILE="$HOME/.config/systemd/user/terminator.service"
    mkdir -p "$(dirname "$SERVICE_FILE")"
    
    cat > "$SERVICE_FILE" << EOF
[Unit]
Description=Terminator Ultimate AI System
After=network.target

[Service]
Type=simple
ExecStart=$(which python3) -m terminator.cli.main --integrate all
WorkingDirectory=$(pwd)
Restart=always
RestartSec=10
Environment=PYTHONPATH=$(pwd)/src
Environment=TERMINATOR_HOME=$HOME/.terminator

[Install]
WantedBy=default.target
EOF
    
    # Reload systemd and enable service
    systemctl --user daemon-reload 2>/dev/null || true
    print_success "Systemd service created. Enable with: systemctl --user enable terminator"
fi

# Create logrotate configuration
print_info "Setting up log rotation..."
mkdir -p "$HOME/.config/logrotate.d"
cat > "$HOME/.config/logrotate.d/terminator" << EOF
$HOME/.terminator/logs/*.log {
    daily
    missingok
    rotate 7
    compress
    delaycompress
    notifempty
    create 644 $USER $USER
}
EOF

# Test installation
print_info "Testing installation..."
python3 -c "
import sys
sys.path.insert(0, 'src')
try:
    import terminator
    print('✅ Terminator package imports successfully')
    print(f'🌟 Terminator Ultimate v{terminator.__version__} installed!')
except ImportError as e:
    print(f'❌ Import error: {e}')
    sys.exit(1)
except Exception as e:
    print(f'⚠️ Warning: {e}')
"

print_success "Terminator Ultimate deployment complete!"
echo ""
print_info "Next steps:"
echo "1. Restart your shell or run: source '$ALIAS_FILE'"
echo "2. Use 'terminator' to launch the full system"
echo "3. Use 'terminator --help' for available options"
echo "4. Check 'terminator-config' for configuration"
echo "5. Monitor with 'terminator-logs'"
echo ""
print_success "The future of AI is now ready! 🚀"