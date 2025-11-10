# TfL Disruption Proxy

A FastAPI proxy for retrieving Transport for London (TfL) line disruptions by mode.

## Features

- REST API endpoint to fetch disruptions for specified TfL modes (e.g., tube, bus, etc.)
- CORS enabled for all origins
- Docker support for easy deployment

## Requirements

- Python 3.11+
- pip

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ayltai/tfl-disruption-proxy.git
   cd tfl-disruption-proxy
   ```

2. (Optional) Create a virtual environment:
   ```bash
   make venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   make upgrade
   ```

## Development

Run the API server in development mode:
```bash
make
```

## Production

Run the API server in production mode:
```bash
make prod
```

## Docker

Build and run the Docker image:
```bash
make build
make docker
```

Publish the Docker image:
```bash
make deploy
```

## API Usage

### Endpoint

```
GET /api/v1/tfl/disruptions/{modes}
```

- `modes`: Comma-separated list of TfL modes (e.g., `tube,bus`)

#### Example

```bash
curl http://localhost:8000/api/v1/tfl/disruptions/tube
```

#### Response

```json
[
  {
    "category": "RealTime",
    "type": "PlannedWork",
    "description": "Some disruption description",
    "closureText": "Part Closure"
  },
  ...
]
```

## License

MIT
