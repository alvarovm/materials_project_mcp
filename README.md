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

## Development

### Local Setup

```bash
# Clone the repository
git clone https://github.com/justaddcoffee/materials-project-mcp.git
cd materials-project-mcp

# Install development dependencies
uv pip install -e ".[dev]"
```

### Running Tests

```bash
pytest
```

