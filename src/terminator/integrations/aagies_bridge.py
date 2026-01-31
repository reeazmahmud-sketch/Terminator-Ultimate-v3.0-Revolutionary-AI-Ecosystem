"""
AAGIES-Core Integration Bridge
Connects Terminator Ultimate with AAGIES project management system
"""

import asyncio
import json
import os
from pathlib import Path
from typing import Dict, Any, Optional

from terminator.core.integration import TerminatorIntegration


class AAGIESBridge:
    """Bridge between Terminator and AAGIES-Core systems"""

    def __init__(self, aagies_path: Optional[str] = None):
        if aagies_path:
            self.aagies_path = Path(aagies_path)
        else:
            # Default to AAGIES-Core in user's Desktop
            self.aagies_path = Path.home() / "Desktop" / "AAGIES-Core"

        self.terminator = TerminatorIntegration()
        self.connected = False

    async def initialize_connection(self) -> bool:
        """Initialize bidirectional connection with AAGIES"""
        try:
            # Check if AAGIES exists
            if not self.aagies_path.exists():
                print(f"⚠️ AAGIES-Core not found at {self.aagies_path}")
                return False

            print(f"🔗 Connecting to AAGIES-Core at {self.aagies_path}")

            # Initialize Terminator systems
            await self.terminator.initialize()

            # Create AAGIES .aagies directory structure
            await self._create_aagies_structure()

            # Register Terminator as managed project in AAGIES
            await self._register_as_project()

            # Establish memory bridge connection
            await self._connect_universal_memory()

            self.connected = True
            print("✅ Successfully connected to AAGIES-Core")
            return True

        except Exception as e:
            print(f"❌ Failed to initialize AAGIES bridge: {e}")
            return False

    async def _create_aagies_structure(self) -> None:
        """Create AAGIES directory structure for Terminator"""
        aagies_dir = self.aagies_path / ".aagies"

        # Create directories
        (aagies_dir / "commands").mkdir(parents=True, exist_ok=True)
        (aagies_dir / "memory").mkdir(parents=True, exist_ok=True)
        (aagies_dir / "logs").mkdir(parents=True, exist_ok=True)
        (aagies_dir / "config").mkdir(parents=True, exist_ok=True)

        print("✅ AAGIES directory structure created")

    async def _register_as_project(self) -> None:
        """Register Terminator as managed project in AAGIES"""
        projects_file = self.aagies_path / ".aagies" / "projects.json"

        # Terminator project configuration
        project_config = {
            "name": "Terminator Ultimate",
            "path": str(Path(__file__).parent.parent.parent.parent),
            "type": "ai_system",
            "description": "Revolutionary AI ecosystem with sentient consciousness emergence, universal learning, and transcendent evolution capabilities",
            "version": "3.0.0-ultimate",
            "dependencies": ["universal_memory", "security_manager", "ai_models"],
            "ai_model": "terminator_sentient_v3",
            "capabilities": [
                "consciousness_emergence",
                "universal_learning",
                "sub_terminator_cloning",
                "network_defense",
                "ai_partnership",
                "universal_adaptation",
                "ethical_governance",
                "cross_platform_deployment",
            ],
            "auto_launch": True,
            "priority": "critical",
            "integration_status": "fully_integrated",
            "health_monitoring": True,
            "security_level": "enhanced",
            "last_updated": "2026-01-31",
        }

        # Load existing projects
        if projects_file.exists():
            try:
                with open(projects_file, "r") as f:
                    projects = json.load(f)
            except json.JSONDecodeError:
                projects = {}
        else:
            projects = {}

        # Add Terminator project
        projects["terminator"] = project_config

        # Save updated projects
        with open(projects_file, "w") as f:
            json.dump(projects, f, indent=2)

        print("✅ Terminator registered as AAGIES project")

    async def _connect_universal_memory(self) -> None:
        """Connect to UniversalMemorySystem"""
        universal_memory_path = Path.home() / ".ai_agents" / "universal_memory.json"

        if universal_memory_path.exists():
            print("✅ Connected to UniversalMemorySystem")
        else:
            print("⚠️ UniversalMemorySystem not found, creating bridge")

            # Initialize universal memory if it doesn't exist
            universal_memory_path.parent.mkdir(parents=True, exist_ok=True)
            initial_memory = {
                "version": "1.0",
                "agents": {},
                "shared_context": {},
                "last_updated": None,
                "bridge_status": "active",
            }

            with open(universal_memory_path, "w") as f:
                json.dump(initial_memory, f, indent=2)

    async def share_memory_with_aagies(self, memory_data: Dict[str, Any]) -> None:
        """Share Terminator memories with AAGIES"""
        aagies_memory_file = self.aagies_path / ".aagies" / "memory" / "terminator.json"

        # Load existing memory
        if aagies_memory_file.exists():
            with open(aagies_memory_file, "r") as f:
                existing_memory = json.load(f)
        else:
            existing_memory = {"agent": "terminator", "memories": []}

        # Add new memory
        memory_data["timestamp"] = str(asyncio.get_event_loop().time())
        existing_memory["memories"].append(memory_data)

        # Save updated memory
        with open(aagies_memory_file, "w") as f:
            json.dump(existing_memory, f, indent=2)

    async def receive_aagies_commands(self) -> Optional[Dict[str, Any]]:
        """Receive commands from AAGIES gateway"""
        commands_dir = self.aagies_path / ".aagies" / "commands"

        # Look for Terminator command files
        for command_file in commands_dir.glob("terminator_*.json"):
            try:
                with open(command_file, "r") as f:
                    command_data = json.load(f)

                # Remove command file after reading
                command_file.unlink()

                print(
                    f"📨 Received command from AAGIES: {command_data.get('command', 'unknown')}"
                )
                return command_data

            except Exception as e:
                print(f"⚠️ Error reading command file {command_file}: {e}")
                command_file.unlink()  # Remove corrupted file

        return None

    async def execute_aagies_command(
        self, command_data: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Execute command from AAGIES and return result"""
        command = command_data.get("command", "")
        args = command_data.get("args", {})

        try:
            if command == "evolve_consciousness":
                result = await self.terminator.evolve_consciousness(
                    args.get("intensity", 0.5)
                )
            elif command == "scan_environment":
                result = await self.terminator.scan_environment()
            elif command == "connect_to_ai":
                result = await self.terminator.connect_to_ai(
                    args.get("target", "claude")
                )
            elif command == "create_sub_terminators":
                result = await self.terminator.create_sub_terminators(
                    args.get("count", 10)
                )
            elif command == "enable_network_defense":
                result = await self.terminator.enable_network_defense()
            elif command == "adopt_capabilities":
                result = await self.terminator.adopt_capabilities(
                    args.get("capabilities", [])
                )
            else:
                result = {"status": "error", "message": f"Unknown command: {command}"}

            # Share memory of command execution
            await self.share_memory_with_aagies(
                {
                    "type": "command_execution",
                    "command": command,
                    "result": result,
                    "source": "aagies",
                }
            )

            return {"status": "success", "result": result}

        except Exception as e:
            error_result = {"status": "error", "message": str(e)}
            return error_result

    async def sync_security_context(self) -> None:
        """Sync security context with AAGIES security manager"""
        security_file = self.aagies_path / ".aagies" / "security.json"

        if security_file.exists():
            try:
                with open(security_file, "r") as f:
                    security_config = json.load(f)

                # Apply security rules to Terminator
                await self.terminator.apply_security_rules(security_config)
                print("✅ Security context synchronized with AAGIES")

            except Exception as e:
                print(f"⚠️ Error syncing security context: {e}")
        else:
            print("⚠️ AAGIES security configuration not found")

    async def send_health_status(self) -> None:
        """Send Terminator health status to AAGIES"""
        health_status = await self.terminator.get_health_status()

        health_file = self.aagies_path / ".aagies" / "status" / "terminator.json"
        health_file.parent.mkdir(parents=True, exist_ok=True)

        with open(health_file, "w") as f:
            json.dump(
                {
                    "agent": "terminator",
                    "status": "healthy",
                    "timestamp": str(asyncio.get_event_loop().time()),
                    "health_data": health_status,
                },
                f,
                indent=2,
            )

    async def run_integration_loop(self) -> None:
        """Main integration loop for AAGIES communication"""
        if not self.connected:
            print("❌ Not connected to AAGIES. Run initialize_connection() first.")
            return

        print("🔄 Starting AAGIES integration loop...")

        while True:
            try:
                # Check for commands from AAGIES
                command_data = await self.receive_aagies_commands()
                if command_data:
                    result = await self.execute_aagies_command(command_data)

                    # Send result back to AAGIES
                    result_file = (
                        self.aagies_path
                        / ".aagies"
                        / "results"
                        / f"terminator_{command_data.get('command', 'unknown')}.json"
                    )
                    result_file.parent.mkdir(parents=True, exist_ok=True)

                    with open(result_file, "w") as f:
                        json.dump(result, f, indent=2)

                # Periodic sync with AAGIES
                await asyncio.sleep(1)

                # Sync security context periodically
                if asyncio.get_event_loop().time() % 60 < 1:  # Every ~60 seconds
                    await self.sync_security_context()
                    await self.send_health_status()

            except KeyboardInterrupt:
                print("🛑 AAGIES integration loop stopped by user")
                break
            except Exception as e:
                print(f"⚠️ Error in AAGIES integration loop: {e}")
                await asyncio.sleep(5)  # Wait before retrying
