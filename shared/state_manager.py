import json
from pathlib import Path
from datetime import datetime, UTC


BASE_DIR = Path("state/projects")


def now_iso() -> str:
    return datetime.now(UTC).replace(microsecond=0).isoformat()


def ensure_project_dirs(project_id: str) -> Path:
    project_dir = BASE_DIR / project_id
    (project_dir / "tasks").mkdir(parents=True, exist_ok=True)
    (project_dir / "reports").mkdir(parents=True, exist_ok=True)
    (project_dir / "decisions").mkdir(parents=True, exist_ok=True)
    return project_dir


def read_json(path: Path, default=None):
    if default is None:
        default = {}
    if not path.exists():
        return default
    text = path.read_text(encoding="utf-8").strip()
    if not text:
        return default
    return json.loads(text)


def write_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")


def get_project_path(project_id: str) -> Path:
    return ensure_project_dirs(project_id) / "project.json"


def load_project(project_id: str) -> dict:
    ensure_project_dirs(project_id)
    path = get_project_path(project_id)
    if not path.exists():
        project = {
            "project_id": project_id,
            "title": project_id,
            "status": "new",
            "current_owner": "ceo-agent",
            "human_approved": False,
            "created_at": now_iso(),
            "last_updated": now_iso(),
        }
        write_json(path, project)
        return project
    return read_json(path, default={})


def save_project(project_id: str, project: dict):
    project["last_updated"] = now_iso()
    write_json(get_project_path(project_id), project)


def create_task(project_id: str, agent: str, task_type: str, payload: dict) -> str:
    project_dir = ensure_project_dirs(project_id)
    tasks_dir = project_dir / "tasks"
    existing = sorted(tasks_dir.glob("task_*.json"))
    task_id = f"task_{len(existing)+1:03d}"
    task = {
        "task_id": task_id,
        "project_id": project_id,
        "agent": agent,
        "task_type": task_type,
        "payload": payload,
        "status": "pending",
        "created_at": now_iso(),
        "updated_at": now_iso(),
    }
    write_json(tasks_dir / f"{task_id}.json", task)
    return task_id


def update_task_status(project_id: str, task_id: str, status: str):
    path = ensure_project_dirs(project_id) / "tasks" / f"{task_id}.json"
    task = read_json(path, default={})
    task["status"] = status
    task["updated_at"] = now_iso()
    write_json(path, task)


def write_report(project_id: str, report_name: str, data: dict):
    path = ensure_project_dirs(project_id) / "reports" / f"{report_name}.json"
    write_json(path, data)


def read_report(project_id: str, report_name: str, default=None):
    path = ensure_project_dirs(project_id) / "reports" / f"{report_name}.json"
    return read_json(path, default=default or {})


def append_decision(project_id: str, decision: dict):
    decisions_dir = ensure_project_dirs(project_id) / "decisions"
    existing = sorted(decisions_dir.glob("decision_*.json"))
    decision_id = f"decision_{len(existing)+1:03d}"
    decision["decision_id"] = decision_id
    decision["created_at"] = now_iso()
    write_json(decisions_dir / f"{decision_id}.json", decision)
    return decision_id