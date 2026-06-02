# Copilot Instructions

## Project status
This repository currently contains only an empty folder structure and a `.gitignore` file. There are no discoverable source files in `dashboard/`, `data/`, `notebooks/`, `reports/`, `scripts/`, or `sql/` in the current workspace snapshot.

## What to do first
- Confirm whether the full project contents are available in the workspace.
- If files are missing, ask the user to reload the repo or provide the source files.
- Do not make large implementation changes until the repository contents are complete.

## When files are present
If the repository is populated, use these conventions:
- `dashboard/` appears to be the main application UI or analysis dashboard layer.
- `data/` contains raw, processed, and database resources; treat `data/db/` as the primary persistent data location.
- `notebooks/` is for exploratory analysis and should not be used as the main production code path.
- `scripts/` and `sql/` are likely to contain utility workflows and database queries.

## Agent behavior
- Prefer asking clarifying questions when the codebase is incomplete.
- Avoid guessing architectural boundaries without source files.
- Once code is available, identify the main data flow from `data/` into `dashboard/` or `notebooks/`, and use the existing folder names as guidance.
