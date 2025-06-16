"""
Example usage of the Materials Project MCP.

This example demonstrates how to use the Materials Project MCP to query
materials data from the Materials Project database.

Before running this example, make sure to set your Materials Project API key:
export MP_API_KEY="your_api_key_here"
"""

import os
import json
from materials_project_mcp.tools import (
    get_materials_with_elements,
    get_material_details,
    find_materials_by_formula
)


def print_json(data):
    """Print JSON data in a readable format."""
    print(json.dumps(data, indent=2))


def main():
    """Run example queries against the Materials Project API."""
    # Check if API key is set
    if not os.environ.get("MP_API_KEY"):
        print("Please set your Materials Project API key:")
        print("export MP_API_KEY=\"your_api_key_here\"")
        return
    
    print("\n=== Finding materials containing Fe and O ===")
    materials = get_materials_with_elements(
        elements=["Fe", "O"],
        max_records=3
    )
    print_json(materials)
    
    if materials:
        material_id = materials[0]["material_id"]
        print(f"\n=== Getting details for material {material_id} ===")
        details = get_material_details(material_id)
        print_json(details)
    
    print("\n=== Finding materials with formula Fe2O3 ===")
    formula_materials = find_materials_by_formula(
        formula="Fe2O3",
        max_records=3
    )
    print_json(formula_materials)


if __name__ == "__main__":
    main()