# Riley Consciousness Lab 🧠

This is the isolated testing ground for Riley's advanced consciousness features.

## Setup

1.  **Environment**: 
    The virtual environment is located in `venv`.
    Activate it (if running manually): `source venv/bin/activate`

2.  **Dependencies**:
    Installed via Phase 1 setup.
    - `mem0ai`: Persistent memory
    - `google-api-python-client`: Calendar integration
    - `pyobjc`: System idle detection (macOS)

## Components

-   **`lab_memory.py`**: The Memory Core. Uses Mem0 to store and recall user interactions.
    -   *Requires*: `MEM0_API_KEY` (or `OPENAI_API_KEY`) in `.env`.

-   **`lab_senses.py`**: System Observer. Detects user idle time and time of day.
    -   *Run*: `python lab_senses.py`

-   **`lab_calendar.py`**: Morning Protocol. Fetches upcoming events.
    -   *Requires*: `credentials.json` (Google Cloud OAuth Desktop App) in this folder.

## Integration

Once individual components are verified, they will be combined into `consciousness.py`.
