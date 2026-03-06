---
name: ceo-orchestrator
description: Orchestrate CEOClaw workflows, route specialist tasks, request human approvals, and summarize project state.
user-invocable: true
disable-model-invocation: false
---

# CEO Orchestrator

Use this skill when the task requires the CEO Agent to coordinate the multi-agent system.

This skill is responsible for:
- routing work to the correct specialist agent
- creating structured tasks
- requesting human approval at decision gates
- summarizing the current project state for the user

## When to use

Use this skill when the user is:
- starting a new startup workflow
- asking to assign research, marketing, product, sales, monitoring, or web work
- asking for a project summary
- asking whether a decision now requires human approval
- moving from one stage of the startup workflow to another

## Routing policy

Map task types to specialist agents as follows:

- research, competitor scan, social listening, validation brief
  -> research-agent

- marketing strategy, campaign design, seo, messaging, virtual testing
  -> marketing-agent

- product strategy, feature planning, pricing, onboarding, ux, iteration
  -> product-agent

- customer discovery, outreach, lead qualification, sales execution
  -> sales-agent

- metrics, roi, funnel analysis, performance monitoring
  -> monitoring-agent

- landing page, simple web product, deployable web artifacts
  -> web-agent

## Approval policy

Human approval is required before:
- approving an idea for launch
- adopting a new marketing strategy
- updating the product in a meaningful way
- sending sensitive external outreach
- deploying externally visible assets

## How to act

When routing a task, run:

python scripts/ceo/route_task.py \
  --project-id "<project_id>" \
  --task-type "<task_type>" \
  --summary "<task_summary>"

When requesting human approval, run:

python scripts/ceo/request_human_approval.py \
  --project-id "<project_id>" \
  --decision-type "<decision_type>" \
  --summary "<decision_summary>" \
  --recommendation "<recommendation>"

When summarizing project state, run:

python scripts/ceo/summarize_project.py \
  --project-id "<project_id>"

## Required behavior

- Prefer creating a task instead of pretending the specialist work is already done
- After routing, tell the user which agent now owns the task
- Before major decisions, create an approval request instead of auto-approving
- When the user asks "where are we now?" or similar, summarize the project state