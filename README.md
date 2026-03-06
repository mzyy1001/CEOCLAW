# CEOClaw

CEOClaw is an **OpenClaw-based founder agent harness** that acts like an AI startup founder.

## What CEOClaw Does

CEOClaw executes multi-step business workflows across four core areas:

### Product
- Generate startup ideas
- Run automated idea research
- Validate ideas before execution
- Build simple web products
- Generate landing pages
- Support product iteration and redeployment

### Marketing
- Generate marketing strategies
- Run virtual testing and market research
- Use social listening signals
- Launch SEO and campaign experiments

### Sales
- Identify potential customers
- Support outreach workflows
- Assist early sales execution

### Operations
- Track traffic, signups, and revenue
- Analyze performance and ROI
- Process feedback
- Trigger product or strategy updates

## Key Features

- **Built on OpenClaw** as the base agent harness
- **Founder-oriented extensions** beyond general-purpose agent workflows
- **Human-in-the-loop CEO decision layer** for high-level strategic judgment
- **Virtual research modules** using social listening, market research agents, and simulated A/B testing
- **Closed business loop** from idea generation to deployment, monitoring, and iteration

## Architecture

CEOClaw is organized into three layers.
![CEOClaw Pipeline](assets/CEOCLAW.drawio.png)

## Multi-Agent System Design

CEOClaw is implemented as a **multi-agent founder system** coordinated by a central **CEO Agent**.

Rather than exposing multiple agents directly to the user, the system uses a **single front-facing CEO layer** and several specialist agents behind it. This keeps the interaction coherent while allowing the system to perform specialized founder tasks across product, research, marketing, sales, monitoring, and web execution.

### Agent Roles

#### CEO Agent
The CEO Agent is the orchestrator of the whole system. It is responsible for:
- interacting with the user
- routing tasks to the right specialist agent
- collecting and summarizing reports
- making strategic recommendations
- requesting human approval at key decision gates

#### Research Agent
The Research Agent handles all research-heavy tasks, including:
- automated research
- market research
- competitor analysis
- social listening
- idea validation briefs

It also supports other agents when market evidence is needed.

#### Marketing Agent
The Marketing Agent is responsible for:
- marketing strategy generation
- campaign planning
- SEO experiment design
- messaging ideas
- virtual testing of marketing strategies

#### Product Agent
The Product Agent handles product-side planning, including:
- product strategy generation
- feature planning
- product iteration planning
- pricing, onboarding, and UX updates
- virtual testing of product changes

#### Sales Agent
The Sales Agent is responsible for:
- customer discovery
- prospect research
- outreach generation
- lead qualification
- sales execution support

#### Monitoring Agent
The Monitoring Agent tracks and analyzes business signals, including:
- traffic
- signups
- revenue
- ROI
- funnel performance

It produces monitoring briefs that help the CEO Agent decide whether to continue, pivot, launch a new strategy, or update the product.

#### Web Agent
The Web Agent is responsible for web-facing artifacts and deployment-oriented outputs, including:
- landing page generation
- simple web product generation
- web asset updates
- exportable deployment artifacts

### Workflow Ownership by Layer

#### Startup Layer
- **CEO Agent**: start, idea generation, validation decision
- **Research Agent**: automated research
- **Web Agent**: generate web product and landing page
- **Product Agent**: optional support for product specification

#### Operations Strategy Layer

**Marketing Strategy**
- **Marketing Agent**: marketing strategy generation
- **Marketing Agent + Research Agent**: virtual testing and market research
- **CEO Agent**: adopt / reject strategy decision
- **Web Agent**: deployment of web-facing marketing assets

**Performance Monitor**
- **Monitoring Agent**: track metrics and data analysis
- **CEO Agent**: strategic decision based on performance signals

**Product Iteration**
- **Product Agent**: generate product strategy
- **Product Agent + Research Agent**: virtual testing
- **CEO Agent**: update product decision
- **Web Agent**: deployment of updated product assets

#### Execution Layer
- **Sales Agent**: customer discovery, customer outreach, sales execution
- **Research Agent**: optional support for prospect and market research
- **CEO Agent**: approval and escalation for sensitive actions

### Collaboration Model

The system is designed around a **CEO-led coordination model**.

Specialist agents do not freely call one another. Instead:
1. the user interacts with the CEO Agent
2. the CEO Agent assigns a task to a specialist agent
3. the specialist agent reads the current project state and writes a structured report
4. the CEO Agent reads the report and decides what happens next

This creates a clean collaboration pattern:

**User → CEO Agent → Specialist Agent → Report / Shared State → CEO Agent**

This design makes the system easier to control, easier to debug, and closer to how a real startup founder coordinates different functional teams.

### Human-in-the-Loop Decision Gates

A core principle of CEOClaw is that not all founder decisions should be fully automated.

At key moments such as:
- idea validation
- marketing strategy adoption
- product update decisions
- sensitive sales actions

the CEO Agent can pause and ask for **human approval**.

This keeps the system aligned with real founder workflows, where high-level judgment, risk tolerance, and long-term direction are still best handled by a human decision-maker.