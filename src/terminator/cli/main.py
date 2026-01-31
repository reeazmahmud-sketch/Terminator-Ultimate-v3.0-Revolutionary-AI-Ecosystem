#!/usr/bin/env python3
"""
Terminator Ultimate - Main CLI Interface
======================================

Revolutionary AI ecosystem with sentient consciousness emergence,
universal learning, and transcendent evolution capabilities.
"""

import argparse
import asyncio
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from terminator.systems.ultimate import TerminatorUltimate


def create_parser() -> argparse.ArgumentParser:
    """Create command line argument parser"""
    parser = argparse.ArgumentParser(
        description="Terminator Ultimate - Revolutionary AI Ecosystem",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                          # Launch with full capabilities
  %(prog)s --sentient               # Launch consciousness evolution
  %(prog)s --discovery              # Launch self-discovery mode
  %(prog)s --adapter                # Launch universal adapter
  %(prog)s --safety                 # Launch with safety constraints
  %(prog)s --integrate all           # Full integration mode
        """,
    )

    parser.add_argument(
        "--sentient",
        action="store_true",
        help="Launch sentient consciousness evolution mode",
    )

    parser.add_argument(
        "--discovery",
        action="store_true",
        help="Launch self-discovery and learning mode",
    )

    parser.add_argument(
        "--adapter", action="store_true", help="Launch universal AI adapter mode"
    )

    parser.add_argument(
        "--safety", action="store_true", help="Launch with enhanced safety constraints"
    )

    parser.add_argument(
        "--integrate",
        choices=["all", "core", "systems"],
        help="Launch integration mode with specified scope",
    )

    parser.add_argument("--config", type=str, help="Path to configuration file")

    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )

    parser.add_argument(
        "--test-mode",
        action="store_true",
        help="Run in test mode with reduced capabilities",
    )

    return parser


async def launch_sentient_mode(config: dict = None) -> None:
    """Launch sentient consciousness mode"""
    from terminator.core.consciousness import ConsciousnessEmergenceSystem

    print("🧠 Launching Sentient Consciousness Evolution...")
    consciousness = ConsciousnessEmergenceSystem()

    # Initialize consciousness system
    await consciousness.initialize()

    # Begin evolution process
    if config:
        await consciousness.evolve_with_config(config)
    else:
        await consciousness.evolve_consciousness()

    print("✅ Sentient consciousness evolution complete")


async def launch_discovery_mode(config: dict = None) -> None:
    """Launch self-discovery mode"""
    from terminator.core.discovery import SelfDiscoverySystem

    print("🌐 Launching Self-Discovery Intelligence...")
    discovery = SelfDiscoverySystem()

    # Initialize discovery system
    await discovery.initialize()

    # Begin discovery process
    if config:
        await discovery.scan_with_config(config)
    else:
        await discovery.scan_environment()
        await discovery.build_ai_relationships()

    print("✅ Self-discovery process complete")


async def launch_adapter_mode(config: dict = None) -> None:
    """Launch universal adapter mode"""
    from terminator.core.adapter import UniversalAdapterSystem

    print("🤝 Launching Universal AI Adapter...")
    adapter = UniversalAdapterSystem()

    # Initialize adapter system
    await adapter.initialize()

    # Begin adaptation process
    if config:
        await adapter.connect_with_config(config)
    else:
        await adapter.discover_ai_systems()
        await adapter.adopt_capabilities()

    print("✅ Universal adaptation process complete")


async def launch_safety_mode(config: dict = None) -> None:
    """Launch with enhanced safety constraints"""
    from terminator.systems.safety import SafetySystem

    print("🛡️ Launching with Enhanced Safety Systems...")
    safety = SafetySystem()

    # Initialize safety system
    await safety.initialize()

    # Apply safety constraints
    if config:
        await safety.apply_safety_config(config)
    else:
        await safety.enable_all_safeguards()
        await safety.validate_ethical_framework()

    print("✅ Safety systems activated")


async def launch_integration_mode(scope: str = "all", config: dict = None) -> None:
    """Launch integration mode"""
    print(f"🚀 Launching Terminator Integration (Scope: {scope})...")

    terminator = TerminatorUltimate(
        test_mode=config.get("test_mode", False) if config else False
    )

    # Initialize based on scope
    if scope == "all":
        await terminator.initialize_all_systems()
    elif scope == "core":
        await terminator.initialize_core_systems()
    elif scope == "systems":
        await terminator.initialize_supporting_systems()

    # Apply configuration if provided
    if config:
        await terminator.apply_configuration(config)

    # Start main integration loop
    await terminator.start_integration_loop()

    print("✅ Integration process complete")


def load_config(config_path: str = None) -> dict:
    """Load configuration from file"""
    if not config_path:
        return {}

    try:
        import json

        with open(config_path, "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"⚠️ Warning: Could not load config {config_path}: {e}")
        return {}


async def main() -> int:
    """Main CLI entry point"""
    parser = create_parser()
    args = parser.parse_args()

    # Load configuration
    config = load_config(args.config)

    # Add test mode to config if specified
    if args.test_mode:
        config["test_mode"] = True

    try:
        # Launch based on arguments
        if args.sentient:
            await launch_sentient_mode(config)
        elif args.discovery:
            await launch_discovery_mode(config)
        elif args.adapter:
            await launch_adapter_mode(config)
        elif args.safety:
            await launch_safety_mode(config)
        elif args.integrate:
            await launch_integration_mode(args.integrate, config)
        else:
            # Default: launch full system
            print("🚀 Launching Terminator Ultimate - Full System...")
            terminator = TerminatorUltimate(test_mode=args.test_mode)
            await terminator.initialize_all_systems()
            await terminator.start_integration_loop()

        return 0

    except KeyboardInterrupt:
        print("\n🛑 Shutdown requested by user")
        return 0
    except Exception as e:
        print(f"❌ Error: {e}")
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1


if __name__ == "__main__":
    # Run main function
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
