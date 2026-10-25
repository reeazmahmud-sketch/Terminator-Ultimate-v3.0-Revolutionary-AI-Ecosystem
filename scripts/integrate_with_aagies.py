#!/usr/bin/env python3
"""
Integrate Terminator Ultimate with AAGIES-Core
Complete bidirectional bridge and memory sharing
"""

import asyncio
import sys
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from terminator.integrations.aagies_bridge import AAGIESBridge


async def main():
    """Main integration function"""
    print("🔗 Integrating Terminator Ultimate with AAGIES-Core...")

    # Initialize bridge
    bridge = AAGIESBridge()

    # Connect to AAGIES
    success = await bridge.initialize_connection()

    if not success:
        print("❌ Failed to connect to AAGIES-Core")
        return 1

    print("✅ Successfully connected to AAGIES-Core")

    # Start integration loop
    try:
        await bridge.run_integration_loop()
    except KeyboardInterrupt:
        print("\n🛑 Integration stopped by user")
        return 0
    except Exception as e:
        print(f"❌ Integration error: {e}")
        return 1


if __name__ == "__main__":
    exit_code = asyncio.run(main())
    sys.exit(exit_code)
