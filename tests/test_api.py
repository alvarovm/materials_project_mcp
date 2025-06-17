import pytest
from unittest.mock import patch, Mock, MagicMock
from materials_project_mcp.api import fetch_materials_by_elements


@pytest.fixture
def mock_mprester():
    # Create a proper context manager mock
    mock_mpr = MagicMock()
    mock_doc = Mock()
    mock_doc.dict.return_value = {
        "material_id": "mp-149",
        "formula_pretty": "Fe2O3",
        "band_gap": 2.0,
        "formation_energy_per_atom": -3.0,
        "symmetry": {"crystal_system": "trigonal", "symbol": "R-3c"},
        "density": 5.3,
        "is_stable": True
    }
    mock_results = [mock_doc]
    
    # Create the nested structure with materials.summary that matches our API
    mock_summary = Mock()
    mock_summary.search = Mock(return_value=mock_results)
    
    mock_materials = Mock()
    mock_materials.summary = mock_summary
    
    mock_mpr.materials = mock_materials
    
    # Configure the mock to be used in a context manager
    mock_cm = MagicMock()
    mock_cm.__enter__.return_value = mock_mpr
    return mock_cm


def test_fetch_materials_by_elements(mock_mprester):
    with patch("materials_project_mcp.api.get_mp_client", return_value=mock_mprester):
        results = fetch_materials_by_elements(
            elements=["Fe", "O"],
            max_records=1
        )
    
    assert len(results) == 1
    assert results[0]["material_id"] == "mp-149"
    assert results[0]["formula_pretty"] == "Fe2O3"