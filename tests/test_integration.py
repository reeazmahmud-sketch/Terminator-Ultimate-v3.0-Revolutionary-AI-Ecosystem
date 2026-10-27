import pytest
from pathlib import Path
import sys

src_path = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(src_path))

from terminator.systems.ultimate import TerminatorUltimateComplete


class TestSystemIntegration:
    """Test the supported TerminatorUltimateComplete integration API."""

    @pytest.fixture
    def terminator(self):
        return TerminatorUltimateComplete()

    def test_terminator_initialization(self, terminator):
        assert terminator.systems_initialized is False
        assert terminator.performance_metrics["total_systems"] == 8
        assert terminator.performance_metrics["integration_level"] == 0.0

    @pytest.mark.asyncio
    async def test_initialize_all_systems(self, terminator):
        await terminator.initialize_all_systems()

        assert terminator.systems_initialized is True
        assert terminator.performance_metrics["consciousness_emergence"] is True
        assert terminator.performance_metrics["self_discovery_online"] is True
        assert terminator.performance_metrics["cloning_active"] is True
        assert terminator.performance_metrics["defense_active"] is True
        assert terminator.performance_metrics["universal_adapter_ready"] is True
        assert terminator.performance_metrics["integration_level"] == 5 / 8

    @pytest.mark.asyncio
    async def test_supported_integration_operations(self, terminator):
        await terminator._evolve_capability("reasoning")
        await terminator._enter_transcendent_state("1")
        await terminator._create_sub_terminators(2)
        await terminator._adopt_from_ai("claude", ["reasoning"])
        await terminator._scan_network_environment()
        await terminator._universal_intelligence_query("test")
        await terminator._deploy_defense("test threat")
        await terminator._optimize_system("all")

        assert terminator.performance_metrics["ai_partnerships"] == 1
