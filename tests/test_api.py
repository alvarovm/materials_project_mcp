import pytest
from unittest.mock import patch, Mock
from materials_project_mcp.api import get_mp_client, fetch_materials_by_elements


@pytest.fixture
def mock_mprester():
    mock_mpr = Mock()
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
    
    mock_summary = Mock()
    mock_summary.search.return_value = mock_results
    
    mock_mpr.summary = mock_summary
    return mock_mpr


def test_fetch_materials_by_elements(mock_mprester):
    with patch("materials_project_mcp.api.get_mp_client", return_value=mock_mprester):
        with patch("materials_project_mcp.api.MPRester") as mock_mp_rester:
            mock_mp_rester.return_value.__enter__.return_value = mock_mprester
            
            results = fetch_materials_by_elements(
                elements=["Fe", "O"],
                max_records=1
            )
    
    assert len(results) == 1
    assert results[0]["material_id"] == "mp-149"
    assert results[0]["formula_pretty"] == "Fe2O3"