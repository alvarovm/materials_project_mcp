# Materials Project MCP

A fastmcp-based tool for writing prompts against data in the Materials Project database.

## Installation

You can install the package from source:

```bash
pip install -e .
```

Or using uv:

```bash
uv pip install -e .
```

### Installation with `uv`

```bash
git clone https://github.com/alvarovm/materials_project_mcp.git
cd materials_project_mcp
uv tools install .
```

## Usage

You can use the CLI:

```bash
mp-mcp
```

Or import in your Python code:

```python
from materials_project_mcp.main import create_mcp

mcp = create_mcp()
mcp.run()
```

## API Key Setup

The Materials Project API requires an API key. You can set up your API key in several ways:

1. Pass it directly to the MPRester:
   ```python
   from mp_api.client import MPRester
   with MPRester("your_api_key_here") as mpr:
       # do stuff with mpr
   ```

2. Set it as an environment variable:
   ```bash
   export MP_API_KEY="your_api_key_here"
   ```

## Example

Here's a simple example that demonstrates how to use the MCP tools directly:

```python
import os
import json
from materials_project_mcp.tools import (
    get_materials_with_elements,
    get_material_details,
    find_materials_by_formula
)

# Set your API key
os.environ["MP_API_KEY"] = "your_api_key_here"
# Or load it from a file
# with open("~/materials_project_api.key", "r") as f:
#     os.environ["MP_API_KEY"] = f.read().strip()

# Function to print JSON data in a readable format
def print_json(data):
    print(json.dumps(data, indent=2))

# Find materials containing Fe and O
print("\n=== Finding materials containing Fe and O ===")
materials = get_materials_with_elements(
    elements=["Fe", "O"],
    max_records=3
)
print_json(materials)

# Get details for a specific material
if materials:
    material_id = materials[0]["material_id"]
    print(f"\n=== Getting details for material {material_id} ===")
    details = get_material_details(material_id)
    print_json(details)

# Find materials with a specific formula
print("\n=== Finding materials with formula Fe2O3 ===")
formula_materials = find_materials_by_formula(
    formula="Fe2O3",
    max_records=3
)
print_json(formula_materials)
```

## Development

### Local Setup

```bash
# Clone the repository
git clone https://github.com/justaddcoffee/materials-project-mcp.git
cd materials-project-mcp

# Install development dependencies
uv pip install -e ".[dev]"
```

### Adding MCP to OpenCode

Locate a the full path for the `mp-mcp` binary, and get an MP API key from [materialsproject.org/api](https://next-gen.materialsproject.org/api).
With this information you can create an `opencode.json` file and add:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "servers": {
       "mp-mcp": {
         "type": "local",
         "command": ["/path/bin/mp-mcp"],
         "environment": {
           "MP_API_KEY": "xxxxHERE_your_MP_APIKEYxxxx"
         },
         "enabled": true
       }
    }
  }
}
```

Test with 
`Using the material project MCP, mp-mcp, Finding materials with formula Fe2O3`

### Running Tests

```bash
pytest
```

