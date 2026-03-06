import argparse
from shared.state_manager import load_project, save_project, create_task


def choose_agent(task_type: str) -> str:
    task_type = task_type.strip().lower()

    research_keywords = [
        "research", "market_research", "competitor_scan", "social_listening",
        "validation", "idea_validation"
    ]
    marketing_keywords = [
        "marketing", "campaign", "seo", "messaging", "ab_test", "strategy_test"
    ]
    product_keywords = [
        "product_strategy", "feature_spec", "iteration", "pricing", "onboarding", "ux"
    ]
    sales_keywords = [
        "customer_discovery", "outreach", "lead_qualification", "sales"
    ]
    monitoring_keywords = [
        "metrics", "monitoring", "analysis", "roi", "funnel"
    ]
    web_keywords = [
        "landing_page", "webapp", "deploy", "web_asset"
    ]

    if any(k in task_type for k in research_keywords):
        return "research-agent"
    if any(k in task_type for k in marketing_keywords):
        return "marketing-agent"
    if any(k in task_type for k in product_keywords):
        return "product-agent"
    if any(k in task_type for k in sales_keywords):
        return "sales-agent"
    if any(k in task_type for k in monitoring_keywords):
        return "monitoring-agent"
    if any(k in task_type for k in web_keywords):
        return "web-agent"

    return "research-agent"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--project-id", required=True)
    parser.add_argument("--task-type", required=True)
    parser.add_argument("--summary", required=True)
    args = parser.parse_args()

    project = load_project(args.project_id)
    agent = choose_agent(args.task_type)

    task_id = create_task(
        project_id=args.project_id,
        agent=agent,
        task_type=args.task_type,
        payload={"summary": args.summary},
    )

    project["current_owner"] = agent
    project["status"] = f"assigned:{args.task_type}"
    save_project(args.project_id, project)

    print(f"Created task: {task_id}")
    print(f"Assigned agent: {agent}")
    print(f"Project status: {project['status']}")


if __name__ == "__main__":
    main()