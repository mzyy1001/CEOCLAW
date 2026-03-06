import argparse
from shared.state_manager import append_decision, load_project, save_project


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-id", required=True)
    parser.add_argument("--decision-type", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--recommendation", required=True)
    args = parser.parse_args()

    project = load_project(args.project_id)

    decision = {
        "project_id": args.project_id,
        "decision_type": args.decision_type,
        "summary": args.summary,
        "recommendation": args.recommendation,
        "requires_human_approval": True,
        "approved": None,
    }

    decision_id = append_decision(args.project_id, decision)

    project["status"] = f"awaiting_human_approval:{args.decision_type}"
    project["current_owner"] = "ceo-agent"
    save_project(args.project_id, project)

    print(f"Created approval request: {decision_id}")
    print(f"Project status: {project['status']}")
    print("Human approval is required.")


if __name__ == "__main__":
    main()