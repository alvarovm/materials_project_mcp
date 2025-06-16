################################################################################
# materials_project_mcp/api.py
# This module contains wrapper functions that interact with the Materials Project API
# through the MPRester client
################################################################################
from typing import Any, Dict, List, Optional, Union
import os
from mp_api.client import MPRester


def get_mp_client(api_key: Optional[str] = None) -> MPRester:
    """
    Get a Materials Project API client (MPRester).
    
    Args:
        api_key: Optional API key. If not provided, the function will try to use
                the MP_API_KEY environment variable.
    
    Returns:
        MPRester: Materials Project API client
    """
    if api_key is None:
        api_key = os.environ.get("MP_API_KEY")
        if api_key is None:
            raise ValueError(
                "No API key provided. Please provide an API key or set the MP_API_KEY environment variable."
            )
    
    return MPRester(api_key)


def fetch_materials_by_elements(
    elements: List[str],
    exclude_elements: Optional[List[str]] = None,
    max_records: int = 10,
    properties: Optional[List[str]] = None,
) -> List[Dict[str, Any]]:
    """
    Fetch materials containing specified elements from the Materials Project API.
    
    Args:
        elements: List of elements that must be present in the material.
        exclude_elements: Optional list of elements that must not be present.
        max_records: Maximum number of records to return (default: 10).
        properties: Optional list of properties to include in the results.
    
    Returns:
        List of materials data dictionaries.
    """
    if properties is None:
        properties = [
            "material_id", 
            "formula_pretty",
            "symmetry", 
            "formation_energy_per_atom",
            "band_gap",
            "theoretical",
            "density",
            "is_stable"
        ]
    
    with get_mp_client() as mpr:
        # For materials with specific elements
        query_params = {
            "elements": elements,
            "fields": properties,
        }
        
        # Add exclusion filter if specified
        if exclude_elements:
            excluded_elements_filter = {}
            for elem in exclude_elements:
                excluded_elements_filter[f"elements.{elem}"] = {"$exists": False}
            query_params.update(excluded_elements_filter)
        
        # Get results using the correct API method
        results = mpr.materials.summary.search(**query_params)
        
        # Limit the number of results
        materials = [doc.dict() for doc in results[:max_records]]
        
    return materials


def fetch_material_by_id(
    material_id: str,
    properties: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Fetch a specific material by its Materials Project ID.
    
    Args:
        material_id: The Materials Project ID (e.g., "mp-149").
        properties: Optional list of properties to include in the results.
    
    Returns:
        Dictionary containing the material data.
    """
    if properties is None:
        properties = [
            "material_id", 
            "formula_pretty",
            "symmetry", 
            "formation_energy_per_atom",
            "band_gap",
            "theoretical",
            "density",
            "is_stable",
            "energy_above_hull",
            "elements",
            "nelements",
            "nsites",
            "volume"
        ]
    
    with get_mp_client() as mpr:
        # Search by material_id
        docs = mpr.materials.summary.search(
            material_ids=[material_id],
            fields=properties
        )
        
        if not docs:
            return {"error": f"Material {material_id} not found"}
        
        # Convert to dictionary
        material_dict = docs[0].dict()
        
    return material_dict


def fetch_materials_by_formula(
    formula: str,
    max_records: int = 10,
    properties: Optional[List[str]] = None,
) -> List[Dict[str, Any]]:
    """
    Fetch materials matching a specific formula from the Materials Project API.
    
    Args:
        formula: Chemical formula to search for (e.g., "Fe2O3").
        max_records: Maximum number of records to return (default: 10).
        properties: Optional list of properties to include in the results.
    
    Returns:
        List of materials data dictionaries.
    """
    if properties is None:
        properties = [
            "material_id", 
            "formula_pretty",
            "symmetry", 
            "formation_energy_per_atom",
            "band_gap",
            "theoretical",
            "density",
            "is_stable"
        ]
    
    with get_mp_client() as mpr:
        # Search by formula
        results = mpr.materials.summary.search(
            formula=formula,
            fields=properties
        )
        
        # Limit the number of results and convert to dictionaries
        materials = [doc.dict() for doc in results[:max_records]]
        
    return materials