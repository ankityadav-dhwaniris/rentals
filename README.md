### Rentals

Manage Rentals in Frappe

### Prerequisites

- Bench (Frappe/ERPNext) installed and a running site
- Python and Node toolchain compatible with your bench
- Redis, MariaDB/Postgres as per your bench setup

### Installation

```bash
# From your bench root
bench get-app rentals https://github.com/ankityadav-dhwaniris/rentals.git
bench --site <your-site> install-app rentals
bench --site <your-site> migrate
```

### Development

```bash
# Start bench services (in one terminal)
bench start

# Run JS build (if needed, in another terminal)
bench build
```

### Fixtures

`hooks.py` exports:
- `Vehicle Type` filtered with `is_standard = 1`
- `Rentals Settings` (Single)

Export fixtures:
```bash
bench --site <your-site> export-fixtures
```

Import/sync fixtures (from app/fixtures):
```bash
bench --site <your-site> execute frappe.utils.fixtures.sync_fixtures
```

### Testing

```bash
# All tests
bench --site <your-site> run-tests --app rentals

# Single test module
bench --site <your-site> run-tests --module rentals.rentals.doctype.driver.test_driver
```

### DocTypes

- `Vehicle Type`
- `Vehicle`
- `Driver`
- `Ride Booking`
- `Ride Booking Item`
- `Ride Order`
- `Rentals Settings` (Single)

### Public API

The app exposes a minimal API via whitelisted methods in `rentals/api.py`.

Base URL: `https://<your-site>`

- Ping
  - Endpoint: `/api/method/rentals.api.ping`
  - Method: GET
  - Response: `{ "message": "pong" }`
  - Example:
    ```bash
    curl -s "https://<your-site>/api/method/rentals.api.ping"
    ```

- Send Payment Reminders (scheduled)
  - Path: `rentals.api.send_payment_reminders` (hooked via scheduler)
  - To invoke manually:
    ```bash
    bench --site <your-site> execute rentals.api.send_payment_reminders
    ```

### Authenticated API usage

Authenticate using API key/secret or session cookie.

- Using API key/secret headers:
  ```bash
  curl -s \
    -H "Authorization: token <api_key>:<api_secret>" \
    "https://<your-site>/api/method/rentals.api.ping"
  ```

- Using basic auth (user:password):
  ```bash
  curl -s -u user@example.com:password \
    "https://<your-site>/api/method/rentals.api.ping"
  ```

### Example: CRUD with standard REST endpoints

Frappe provides REST endpoints for DocTypes by default.

- Create Driver
  ```bash
  curl -s -X POST \
    -H "Content-Type: application/json" \
    -H "Authorization: token <api_key>:<api_secret>" \
    -d '{
      "doctype": "Driver",
      "first_name": "John",
      "last_name": "Doe",
      "license_number": "1234567890"
    }' \
    "https://<your-site>/api/resource/Driver"
  ```

- Get Driver
  ```bash
  curl -s -H "Authorization: token <api_key>:<api_secret>" \
    "https://<your-site>/api/resource/Driver/<DRIVER_NAME>"
  ```

- List Drivers (with filters)
  ```bash
  curl -s -G -H "Authorization: token <api_key>:<api_secret>" \
    --data-urlencode 'fields=["name","first_name","last_name","full_name"]' \
    --data-urlencode 'filters=[["Driver","disabled","=",0]]' \
    --data-urlencode 'limit_page_length=20' \
    "https://<your-site>/api/resource/Driver"
  ```

- Update Driver
  ```bash
  curl -s -X PUT \
    -H "Content-Type: application/json" \
    -H "Authorization: token <api_key>:<api_secret>" \
    -d '{ "last_name": "Smith" }' \
    "https://<your-site>/api/resource/Driver/<DRIVER_NAME>"
  ```

- Delete Driver
  ```bash
  curl -s -X DELETE \
    -H "Authorization: token <api_key>:<api_secret>" \
    "https://<your-site>/api/resource/Driver/<DRIVER_NAME>"
  ```

### Coding Standards

- Python: ruff, pyupgrade; Black-style formatting via pre-commit
- JS/TS: eslint + prettier

### Contributing

```bash
cd apps/rentals
pre-commit install
```

### License

mit
