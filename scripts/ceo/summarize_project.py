import argparse
from pathlib import Path
from shared.state_manager import load_project, read_json, ensure_project_dirs


def load_all_reports(project_id: str) -> dict:
    reports_dir = ensure_project_dirs(project_id) / "reports"
    reports = {}
    for path in sorted(reports_dir.glob("*.json")):
        reports[path.stem] = read_json(path, default={})
    return reports


def summarize(project: dict, reports: dict) -> str:
    lines = []
    lines.append(f"Project ID: {project.get('project_id', '')}")
    lines.append(f"Title: {project.get('title', '')}")
    lines.append(f"Status: {project.get('status', '')}")
    lines.append(f"Current Owner: {project.get('current_owner', '')}")
    lines.append("")

    if not reports:
        lines.append("No reports available yet.")
        return "\n".join(lines)

    lines.append("Available Reports:")
    for name, content in reports.items():
        lines.append(f"- {name}")
        if isinstance(content, dict):
            summary = content.get("summary") or content.get("recommendation") or content.get("idea_name")
            if summary:
                lines.append(f"  Summary: {summary}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-id", required=True)
    args = parser.parse_args()

    project = load_project(args.project_id)
    reports = load_all_reports(args.project_id)

    print(summarize(project, reports))


if __name__ == "__main__":
    main()