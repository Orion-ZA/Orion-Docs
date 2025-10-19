# Agile Methodology Documentation

---

## Table of Contents

1. [Overview](#overview)
2. [Agile Principles](#agile-principles)
3. [Team Roles](#team-roles)
4. [Workflow](#workflow)
5. [Sprints](#sprints)
6. [Ceremonies](#ceremonies)
7. [Tools and Technologies](#tools-and-technologies)
8. [Collaboration & Communication](#collaboration--communication)
9. [Version Control Strategy](#version-control-strategy)
10. [Definition of Done](#definition-of-done)
11. [Retrospectives](#retrospectives)

---

## Overview

We follow the Agile methodology to ensure that our software development process is iterative, flexible, and centered around continuous feedback. Agile empowers our team to adapt to changes quickly while maintaining high standards of quality and user satisfaction.

---

## Agile Principles

We align our workflow with the **12 Principles of Agile**:
- Customer satisfaction through early and continuous delivery.
- Welcome changing requirements.
- Deliver working software frequently.
- Close collaboration between business and developers.
- Build projects around motivated individuals.
- Face-to-face (or real-time) communication is best.
- Working software is the primary measure of progress.
- Sustainable development pace.
- Continuous attention to technical excellence.
- Simplicity—the art of maximizing work not done.
- Self-organizing teams.
- Regular reflection and adjustment.

---

## Team Roles

| Role              | Name                | Responsibilities                                           |
|-------------------|---------------------|------------------------------------------------------------|
| Product Owner     | Zayd              | Defines features, prioritizes backlog, and stakeholder communication. |
| Scrum Master      | Zayd, Jaairdan and Ashly            | Facilitates meetings, removes blockers, and ensures process adherence. |
| Development Team  | Zayd, Ashly, Jaairdan, Ndumiso, Leethee and Terence     | Implements features, tests, and deploys the product.        |
| QA / Tester       | Ashly and Terence              | Writes and runs tests, ensures product quality.             |
| UI/UX Designer    | Ndumiso and Leethee            | Designs user interfaces and ensures usability.              |

---

## Workflow

We follow a simplified Agile Scrum workflow:

1. **Backlog Grooming** – Product owner prepares a list of features/tasks.
2. **Sprint Planning** – Team selects items from backlog for the sprint.
3. **Daily Stand-ups** – Short updates on progress, blockers, and next steps.
4. **Development & Testing** – Build features, write tests, review code.
5. **Sprint Review** – Demo completed work to stakeholders.
6. **Sprint Retrospective** – Reflect and improve.

---

## Sprints

- **Sprint Length**: 2 Weeks
- **Sprint Goals**: Clearly defined and measurable objectives.
- **Sprint Backlog**: User stories/tasks selected for the sprint.
- **Velocity Tracking**: Measured using story points.

---

## Ceremonies

| Ceremony            | Frequency      | Description |
|---------------------|----------------|-------------|
| Sprint Planning      | Start of Sprint | Plan work and assign tasks. |
| Daily Standup        | Daily           | Share progress, issues, and plans. |
| Sprint Review        | End of Sprint   | Demo and feedback session. |
| Sprint Retrospective | End of Sprint   | Reflect on process and make improvements. |

---

## Tools and Technologies

- **Project Management**: GitHub Projects
- **Version Control**: Git + GitHub
- **Code Review**: Pull Requests with approvals
- **CI/CD**: GitHub Actions / Firebase Hosting
- **Communication**: Discord
- **Documentation**: Markdown deployed via Pages

### Project Tracking

- **Burn-up Chart**: [GitHub Projects Insights](https://github.com/orgs/Orion-ZA/projects/3/insights?period=max) - Track sprint progress and velocity over time

---

## Collaboration & Communication

- Daily check-ins on Discord or via standups.
- Use GitHub issues to track bugs and tasks.
- Tag teammates in comments for assistance.
- Weekly sync meetings (voice/video) to ensure alignment.

---

## Version Control Strategy

- **Branching Model**: Git Flow (or simplified)
  - `main`: Production-ready code
  - `dev`: Staging and feature merges
  - `feature/xyz`: Individual features
  - `bugfix/xyz`: Fixes and patches
  - `hotfix/xyz`: Needed fix to `main` branch

- **Pull Request Rules**:
  - Code must be reviewed by at least one teammate.
  - All tests must pass before merge.
  - Descriptive commit messages.

---

## Definition of Done

A task is considered "Done" when:
- Code is written, tested, and reviewed.
- It meets the acceptance criteria.
- UI/UX is verified.
- It is pushed to the dev branch without bugs.
- Documentation is updated (if applicable).

---

## Retrospectives

After every sprint, the team meets to reflect on:
- **What went well**
- **What didn’t go well**
- **What can be improved**
- **Action items for next sprint**

We record retrospective notes and revisit them to track team improvements.

---

## Authors

- [Zayd](https://github.com/2653934) – Product Owner and Dev
- [Ashly](https://github.com/AshlyMasipa) – Backend Dev and Scrum Master
- [Jaairdan](https://github.com/jaairdan) – DB Dev and Security Engineer
- [Leethee](https://github.com/Leethee-Kgalaletso) - UI / UX Designer and Frontend Engineer
- [Ndumiso](https://github.com/theegentlemaniac) - UI / UX Designer and Frontend Engineer
- [Terence](https://github.com/Terence-wits) - Backend Troll (Dev)

---
