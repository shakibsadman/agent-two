# agent-two

A small FastAPI app with a hello route and a health route.

| Method | Path | Response |
| --- | --- | --- |
| GET | `/hello` | `{"message": "hello"}` |
| GET | `/health` | `{"status": "ok"}` |

The API listens on port **8000**.

## What to install

Install only the tools for the way you want to run the app.

| Tool | Local (`uv`) | Docker |
| --- | --- | --- |
| Git | Yes | Yes |
| Python 3.13 or newer | Yes | No. The image includes it. |
| [uv](https://docs.astral.sh/uv/) | Yes | No. The image includes it. |
| [Docker Desktop](https://docs.docker.com/desktop/) | No | Yes |

### Git

Install Git from [git-scm.com](https://git-scm.com/downloads), then confirm it:

```bash
git --version
```

### Python 3.13

Install Python 3.13 from [python.org](https://www.python.org/downloads/) or with Homebrew:

```bash
brew install python@3.13
python3 --version
```

`uv` can also install that Python for you after `uv` itself is installed:

```bash
uv python install 3.13
```

### uv

On macOS or Linux:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

On Windows, in PowerShell:

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Homebrew also works: `brew install uv`. Confirm the install with `uv --version`.

### Docker Desktop

Install [Docker Desktop](https://docs.docker.com/desktop/), open it, and wait until it reports that the engine is running.

```bash
docker version
```

## Clone the repository

```bash
git clone <repository-url>
cd agent-two
```

## Run locally

From the project directory, install the dependencies and start the dev server. `uv sync` creates a virtual environment and installs FastAPI.

```bash
uv sync
uv run fastapi dev src/agent_two/app.py
```

Open [http://127.0.0.1:8000/hello](http://127.0.0.1:8000/hello) and [http://127.0.0.1:8000/health](http://127.0.0.1:8000/health). Interactive docs are at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). The dev server reloads when you change the code.

## Run with Docker

Docker Desktop must be running. From the project directory:

```bash
docker build -t agent-two .
docker run --rm -p 8000:8000 agent-two
```

Open [http://localhost:8000/hello](http://localhost:8000/hello) and [http://localhost:8000/health](http://localhost:8000/health). This uses the production server and does not reload on file changes. Stop it with `Ctrl+C`.
