# CSSLO

A library for finding logical operators of quantum CSS error correction codes.

## Installation

```bash
pip install -e ".[test]"  # Install with test dependencies
```

## Usage

```python
import csslo

# Example usage
result = csslo.minWeightZ2(matrix)
distance = csslo.distGenetic(matrix)
```

## Development

### Running Tests

```bash
pytest
```

### Code Quality

The project uses several tools to maintain code quality:
- flake8 for linting
- black for code formatting
- isort for import sorting
- mypy for type checking

## License

This project is licensed under the terms of the license included in the repository. 