################################################################################
# materials_project_mcp/tools.py
# This module contains tools that consume the generic API wrapper functions in
# materials_project_mcp/api.py and constrain/transform them based on use cases/applications
################################################################################
from typing import Any, Dict, List, Optional, Union
from .api import (
    fetch_materials_by_elements,
    fetch_material_by_id,
    fetch_materials_by_formula
)


def get_materials_with_elements(
    elements: List[str],
    exclude_elements: Optional[List[str]] = None,
    max_records: int = 10
) -> List[Dict[str, Any]]:
    """
    Find materials containing specific elements.
    
    Args:
        elements: List of elements that must be present in the material (e.g., ["Fe", "O"]).
        exclude_elements: Optional list of elements that must not be present.
        max_records: Maximum number of records to return (default: 10).
    
    Returns:
        List of materials containing the specified elements.
    """
    properties = [
        "material_id", 
        "formula_pretty",
        "symmetry", 
        "formation_energy_per_atom",
        "band_gap",
        "density",
        "is_stable"
    ]
    
    materials = fetch_materials_by_elements(
        elements=elements,
        exclude_elements=exclude_elements,
        max_records=max_records,
        properties=properties
    )
    
    # Extract key properties for each material
    simplified_results = []
    for material in materials:
        simplified_material = {
            "material_id": material.get("material_id"),
            "formula": material.get("formula_pretty"),
            "band_gap": material.get("band_gap"),
            "formation_energy": material.get("formation_energy_per_atom"),
            "crystal_system": material.get("symmetry", {}).get("crystal_system"),
            "space_group": material.get("symmetry", {}).get("symbol"),
            "density": material.get("density"),
            "is_stable": material.get("is_stable", False)
        }
        simplified_results.append(simplified_material)
    
    return simplified_results


def get_material_details(material_id: str) -> Dict[str, Any]:
    """
    Get detailed information about a specific material by its Materials Project ID.
    
    Args:
        material_id: The Materials Project ID (e.g., "mp-149").
    
    Returns:
        Dictionary containing detailed information about the material.
    """
    properties = [
        "material_id", 
        "formula_pretty",
        "symmetry", 
        "formation_energy_per_atom",
        "band_gap",
        "density",
        "is_stable",
        "energy_above_hull",
        "theoretical",
        "nelements",
        "elements",
        "nsites",
        "volume",
        "deprecated",
        "deprecation_reasons"
    ]
    
    material = fetch_material_by_id(
        material_id=material_id,
        properties=properties
    )
    
    # Format the output to make it more readable
    result = {
        "material_id": material.get("material_id"),
        "formula": material.get("formula_pretty"),
        "elements": material.get("elements"),
        "number_of_elements": material.get("nelements"),
        "number_of_sites": material.get("nsites"),
        "volume": material.get("volume"),
        "density": material.get("density"),
        "band_gap": material.get("band_gap"),
        "formation_energy": material.get("formation_energy_per_atom"),
        "energy_above_hull": material.get("energy_above_hull"),
        "is_stable": material.get("is_stable", False),
        "is_theoretical": material.get("theoretical", True),
        "crystal_system": material.get("symmetry", {}).get("crystal_system"),
        "space_group": material.get("symmetry", {}).get("symbol"),
        "point_group": material.get("symmetry", {}).get("point_group"),
        "deprecated": material.get("deprecated", False),
        "deprecation_reasons": material.get("deprecation_reasons", [])
    }
    
    return result


def find_materials_by_formula(
    formula: str,
    max_records: int = 10
) -> List[Dict[str, Any]]:
    """
    Find materials with a specific chemical formula.
    
    Args:
        formula: Chemical formula to search for (e.g., "Fe2O3").
        max_records: Maximum number of records to return (default: 10).
    
    Returns:
        List of materials matching the specified formula.
    """
    properties = [
        "material_id", 
        "formula_pretty",
        "symmetry", 
        "formation_energy_per_atom",
        "band_gap",
        "density",
        "is_stable"
    ]
    
    materials = fetch_materials_by_formula(
        formula=formula,
        max_records=max_records,
        properties=properties
    )
    
    # Extract key properties for each material
    simplified_results = []
    for material in materials:
        simplified_material = {
            "material_id": material.get("material_id"),
            "formula": material.get("formula_pretty"),
            "band_gap": material.get("band_gap"),
            "formation_energy": material.get("formation_energy_per_atom"),
            "crystal_system": material.get("symmetry", {}).get("crystal_system"),
            "space_group": material.get("symmetry", {}).get("symbol"),
            "density": material.get("density"),
            "is_stable": material.get("is_stable", False)
        }
        simplified_results.append(simplified_material)
    
    return simplified_results