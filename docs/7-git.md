# 🚀 Git Methodology

## 1. 📁 Organization & Repo Setup

- Create a **GitHub Organization** (e.g., `Orion-ZA`).
- Add a **main project repository** (e.g., `Orion`).
- Enable:
  - Issues ✔️
  - Projects/Boards ✔️

---

## 2. 🌿 Branching Strategy

Keep `main` always production-ready.

| Branch Name          | Description                          |
|----------------------|--------------------------------------|
| `main`               | Stable, production-ready code         |
| `dev`                | Integration branch for features       |
| `feature/<name>`     | New feature development               |
| `bugfix/<name>`      | Non-critical bug fixes                |
| `hotfix/<name>`      | Critical fixes applied to `main`      |

---

## 3. 🔁 Workflow

### A. Start Work
1. Create a **GitHub Issue** → assign yourself
2. Create a branch from `dev`:

```bash
git checkout -b feature/login-page dev
```

### B. Commit Messages (use Conventional Commits)
```bash
feat: add login validation
fix: correct navbar render bug
docs: update installation guide
```

### C. Push & Pull Request

```bash
git push origin feature/login-page
```
- Open a Pull Request into `dev`
- Link it to its Issue
- Assign at least 1 reviewer
- ⚠️ Do not self-merge unless approved

### D. Code Review & Merge

- Teammates review and request changes if needed
- Once approved → squash & merge into `dev`
- Periodically merge `dev` → `main` for releases

---

## 4. ✅ Code Review Checklist

- [ ] Code is clean, readable, and maintainable
- [ ] Meets the requirements of the related Issue
- [ ] Does not break existing functionality
- [ ] Follows naming and style conventions
- [ ] Includes/updates tests if needed
- [ ] Documentation/comments updated where necessary

---

## 5. 🛠 GitHub Collaboration Tools

| Tool         | Purpose                                                |
|--------------|--------------------------------------------------------|
| **Projects** | Kanban board for tracking tasks (To-Do → Doing → Done) |
| **Issues**   | Logging tasks, bugs, feature requests                  |
| **Doc Site** | Project documentation, architecture, guides            |
| **Actions**  | Automation (test runs, CI/CD pipelines)                |

---

## 6. 📦 Release & Tagging

- Follow **Semantic Versioning**:
  v<MAJOR>.<MINOR>.<PATCH> → e.g. v1.0.2
- **MAJOR** = breaking changes
- **MINOR** = new features (backwards-compatible)
- **PATCH** = bug fixes / small improvements
- Use GitHub **Releases** to attach changelog and downloadable assets

---

## 7. 💡 Best Practices Summary

- Regularly pull from `dev` to stay in sync:
```bash
git pull origin dev
```
- Keep Pull Requests small and focused on one thing
- Communicate through Issues and PR comments (not privately)
- Keep README and documentation updated continuously
- Set up branch protection rules on main (e.g., required reviews, no force push)
- Prefer squash merging to keep a clean history
