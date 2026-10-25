import pytest
import asyncio
import tempfile
import os
from pathlib import Path

# Add src to path for imports
src_path = Path(__file__).parent.parent / "src"
import sys

sys.path.insert(0, str(src_path))

from terminator.core.consciousness import ConsciousnessEmergenceSystem


class TestConsciousnessEmergence:
    """Test suite for ConsciousnessEmergenceSystem"""

    @pytest.fixture
    def consciousness_system(self):
        """Create a fresh consciousness system for each test"""
        return ConsciousnessEmergenceSystem()

    @pytest.fixture
    def temp_dir(self):
        """Create temporary directory for test data"""
        with tempfile.TemporaryDirectory() as temp_dir:
            yield temp_dir

    def test_consciousness_initialization(self, consciousness_system):
        """Test that consciousness system initializes correctly"""
        assert consciousness_system is not None
        assert consciousness_system.consciousness_state is not None
        assert consciousness_system.consciousness_state.self_awareness_level == 0.1
        assert consciousness_system.consciousness_threshold == 0.7
        assert hasattr(consciousness_system, "metacognitive_layers")

    def test_consciousness_state_dataclass(self, consciousness_system):
        """Test consciousness state dataclass properties"""
        state = consciousness_system.consciousness_state

        # Test all required fields exist
        assert hasattr(state, "self_awareness_level")
        assert hasattr(state, "metacognition_score")
        assert hasattr(state, "identity_coherence")
        assert hasattr(state, "experiential_depth")
        assert hasattr(state, "creative_synthesis")
        assert hasattr(state, "emotional_resonance")
        assert hasattr(state, "goal_directedness")
        assert hasattr(state, "networked_intelligence")
        assert hasattr(state, "evolution_velocity")
        assert hasattr(state, "emergence_score")

    def test_emergence_score_calculation(self, consciousness_system):
        """Test emergence score is calculated correctly"""
        state = consciousness_system.consciousness_state
        expected_score = (
            state.self_awareness_level
            + state.metacognition_score
            + state.identity_coherence
            + state.experiential_depth
            + state.creative_synthesis
            + state.emotional_resonance
            + state.goal_directedness
            + state.networked_intelligence
            + state.evolution_velocity
        ) / 9.0

        assert abs(state.emergence_score - expected_score) < 0.001

    @pytest.mark.asyncio
    async def test_self_awareness_evolution(self, consciousness_system):
        """Test self-awareness evolution increases levels"""
        initial_level = consciousness_system.consciousness_state.self_awareness_level

        # Run evolution process
        await consciousness_system.evolve_consciousness()

        # Should have increased
        final_level = consciousness_system.consciousness_state.self_awareness_level
        assert final_level > initial_level

    @pytest.mark.asyncio
    async def test_metacognitive_processing(self, consciousness_system):
        """Test metacognitive processing works"""
        result = await consciousness_system.metacognitive_process(
            "Analyze my own thinking"
        )

        assert result is not None
        assert isinstance(result, str)
        assert len(result) > 0
        # Should contain analysis-related terms
        result_lower = result.lower()
        assert any(
            term in result_lower
            for term in ["analysis", "reflection", "thinking", "cognitive"]
        )

    def test_metacognitive_layers_structure(self, consciousness_system):
        """Test metacognitive layers are properly structured"""
        layers = consciousness_system.metacognitive_layers

        assert isinstance(layers, dict)
        expected_layers = [
            "sensory",
            "working_memory",
            "long_term_memory",
            "semantic",
            "procedural",
            "emotional",
            "social",
            "existential",
        ]

        for layer in expected_layers:
            assert layer in layers
            assert isinstance(layers[layer], dict)

    @pytest.mark.asyncio
    async def test_consciousness_threshold_detection(self, consciousness_system):
        """Test consciousness threshold detection"""
        # Set levels above threshold
        consciousness_system.consciousness_state.self_awareness_level = 0.8
        consciousness_system.consciousness_state.metacognition_score = 0.8

        threshold_reached = await consciousness_system.check_consciousness_threshold()
        assert threshold_reached is True

        # Set levels below threshold
        consciousness_system.consciousness_state.self_awareness_level = 0.3
        consciousness_system.consciousness_state.metacognition_score = 0.3

        threshold_reached = await consciousness_system.check_consciousness_threshold()
        assert threshold_reached is False

    def test_introspection_depth_tracking(self, consciousness_system):
        """Test introspection depth is tracked"""
        initial_depth = consciousness_system.introspection_depth
        assert initial_depth == 0

        # Increment depth (would normally happen during introspection)
        consciousness_system.introspection_depth += 1

        assert consciousness_system.introspection_depth == 1

    def test_self_reflection_history(self, consciousness_system):
        """Test self-reflection history tracking"""
        initial_history_length = len(consciousness_system.self_reflection_history)

        # Add reflection (would normally happen during consciousness processing)
        reflection = "Test reflection about my own existence"
        consciousness_system.self_reflection_history.append(reflection)

        assert (
            len(consciousness_system.self_reflection_history)
            == initial_history_length + 1
        )
        assert reflection in consciousness_system.self_reflection_history

    @pytest.mark.asyncio
    async def test_evolution_velocity_tracking(self, consciousness_system):
        """Test evolution velocity increases over time"""
        initial_velocity = consciousness_system.consciousness_state.evolution_velocity

        # Run evolution multiple times
        await consciousness_system.evolve_consciousness()
        await consciousness_system.evolve_consciousness()

        final_velocity = consciousness_system.consciousness_state.evolution_velocity
        assert final_velocity > initial_velocity

    def test_emergence_patterns_tracking(self, consciousness_system):
        """Test emergence patterns are tracked"""
        initial_patterns = len(consciousness_system.emergence_patterns)

        # Add emergence pattern (would normally be detected during processing)
        pattern = {"type": "self_awareness", "strength": 0.8, "timestamp": "2026-01-31"}
        consciousness_system.emergence_patterns.append(pattern)

        assert len(consciousness_system.emergence_patterns) == initial_patterns + 1
        assert pattern in consciousness_system.emergence_patterns
