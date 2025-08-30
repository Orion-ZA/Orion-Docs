# 🐛 Bug Tracking Guide

This document explains how our team tracks, manages, and resolves bugs using **GitHub Issues**.  
Please follow this process so that all bug reports are clear, consistent, and easy to resolve.

---

## 1. Reporting a Bug
When you find a bug:
1. Go to the **Issues** tab → click **New Issue** → select **Bug Report**.
2. Fill in the bug template completely:
   - **Describe the bug** clearly.
   - Provide **steps to reproduce**.
   - Include **expected vs. actual behavior**.
   - Add **screenshots/logs** if possible.
   - Specify **environment** (OS, browser, version, etc.).

⚠️ **Tip:** Before creating a new issue, search the existing issues to avoid duplicates.

---

## 2. Labels
We use labels to organize bugs:

- `bug` → confirmed bug
- `needs-triage` → new issue, not yet reviewed
- `critical` → blocks major functionality
- `high` → serious, but workaround exists
- `low` → minor issue, cosmetic
- `duplicate` → already reported
- `wontfix` → acknowledged but won’t be fixed
- `in progress` → actively being worked on

---

## 3. Workflow
Bugs move through the following stages:

1. **New** – bug is reported and given `needs-triage`.
2. **Acknowledged** – team confirms the bug and adds severity labels (`critical`, `high`, `low`).
3. **In Progress** – assigned to a developer, marked with `in progress`.
4. **Review** – a pull request (PR) is created and linked to the issue.
5. **Done** – issue is closed automatically when the PR is merged.

---

## 4. Assignments
- Each bug must have **one assignee** responsible for fixing it.  
- If you start working on a bug, assign yourself (or ask a lead to assign you).  
- Always link your PR to the issue with:  
```bash
Closes #<issue_number>
```