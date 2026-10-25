from pathlib import Path


def test_archived_safety_module_is_valid_python():
    module = Path(__file__).parents[1] / "src" / "terminator" / "systems" / "safety_old.py"
    compile(module.read_text(), str(module), "exec")
