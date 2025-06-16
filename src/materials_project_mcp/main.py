################################################################################
# materials_project_mcp/main.py
# This module sets up the FastMCP CLI interface
################################################################################

from fastmcp import FastMCP
from materials_project_mcp.tools import (
    get_materials_with_elements,
    get_material_details,
    find_materials_by_formula
)


def create_mcp():
    """Create the FastMCP instance with registered tools."""
    # Create a new FastMCP instance
    mcp = FastMCP("materials_project_mcp")

    # Register all tools
    mcp.tool(get_materials_with_elements)
    mcp.tool(get_material_details)
    mcp.tool(find_materials_by_formula)

    return mcp


# Create the FastMCP instance at module level
mcp = create_mcp()


def main():
    """Main entry point for the application."""
    mcp.run()


if __name__ == "__main__":
    main()
