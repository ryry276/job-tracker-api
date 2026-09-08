# Job Tracker API

This is a small backend project I’m building with FastAPI to track job applications.

Right now the API lets me create, view, update, delete, and filter applications. The current version still uses in-memory storage, so the data resets whenever the server restarts. I’ll replace that with a real database later.

## What it can do

- Create a new application
- Get all applications
- Get one application by ID
- Update an application
- Delete an application
- Filter by status
- Filter by company
- Use both filters together
- Reject duplicate IDs
- Validate invalid input

## Tech used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Git
- GitHub

## Project structure

```text
job-tracker-api/
|-- main.py
|-- routers/
│   |-- __init__.py
│   |-- applications.py
|-- .gitignore
|-- README.md
```

`main.py` starts the FastAPI app.

The application routes are inside `routers/applications.py`.

## Setup

Clone the repo:

```bash
git clone https://github.com/ryry276/job-tracker-api.git
cd job-tracker-api
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.venv\Scripts\Activate
```

Or on Linux / WSL:

```bash
source .venv/bin/activate
```

Install the packages:

```bash
pip install fastapi uvicorn
```

Run the server:

```bash
uvicorn main:app --reload
```

Swagger docs:

```text
http://127.0.0.1:8000/docs
```

## Application format

Example:

```json
{
  "id": 1,
  "company": "Apple",
  "role": "Software Engineer Intern",
  "status": "applied"
}
```

Allowed status values:

- `applied`
- `interview`
- `rejected`

## Endpoints

### Create application

```http
POST /applications
```

### Get all applications

```http
GET /applications
```

### Get one application

```http
GET /applications/{application_id}
```

Example:

```http
GET /applications/1
```

### Update application

```http
PATCH /applications/{application_id}
```

Example body:

```json
{
  "status": "interview"
}
```

Only the fields sent in the PATCH request are changed.

### Delete application

```http
DELETE /applications/{application_id}
```

## Filtering

Filter by status:

```http
GET /applications?status=interview
```

Filter by company:

```http
GET /applications?company=Apple
```

Company filtering is case-insensitive, so `Apple`, `apple`, and `APPLE` all match.

Use both filters:

```http
GET /applications?status=interview&company=Apple
```

## Validation

The API currently checks for things like:

- invalid IDs
- empty company or role
- invalid status values
- duplicate application IDs
- missing applications

Some of the main response codes are:

- `201` - created
- `204` - deleted
- `404` - application not found
- `409` - duplicate ID
- `422` - invalid request data

## Current limitations

This is still an early version.

Right now:

- data is only stored in memory
- data disappears when the server restarts
- there is no PostgreSQL database yet
- there is no authentication yet
- there are no automated tests yet
- the API is not deployed yet

I’ll keep adding these as the project develops.
