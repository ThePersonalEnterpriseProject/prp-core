# Contributing to PRP-core

First off, thank you for considering contributing to PRP-core! I'm thrilled you're here and appreciate your interest in helping me build this project. Every contribution, no matter how small, is valuable.

This document provides a set of guidelines for contributing to PRP-core. These are mostly guidelines, not strict rules. Use your best judgment, and feel free to propose changes to this document in a pull request.

## Welcome! I'm Just Getting Started

This project is in a very early stage of development (v0.1), and I am actively building the core project structure and processes. I am excited to have you join me on this journey from the ground up.

As the project grows, I plan to introduce more community tools to facilitate collaboration. For example, a public Matrix chat is on my roadmap but has not been set up yet. I appreciate your patience and welcome your input as I establish the community infrastructure.

## How to Get Help

Before opening an issue, please ask your questions in our primary community channel. This helps me keep the issue tracker focused on bugs and feature requests and allows others in the community to benefit from the discussion.

For asynchronous questions, sharing ideas, or finding "how-to" guides, the **[GitHub Discussions tab](https://github.com/ThePersonalEnterpriseProject/prp-core/discussions)** is the main place for now.

## Reporting Bugs

Bugs are tracked as GitHub issues. When you are creating a bug report, please use the **"Bug Report"** issue template. To help me resolve issues quickly, please be as descriptive as possible and include the following:

-   Your operating system, browser, and version.
-   A clear and concise description of the bug.
-   Detailed steps to reproduce the bug.
-   What you expected to happen.
-   What actually happened.
-   Any relevant screenshots or error messages.

## Suggesting Enhancements

I love to hear your ideas for improving PRP-core! To suggest an enhancement, please use the **"Feature Request"** issue template.

Before creating a new feature request, please take a moment to check the **[GitHub Projects Roadmap](https://github.com/ThePersonalEnterpriseProject/prp-core/projects)** to see if your idea is already being planned. This helps me avoid duplicate suggestions and keeps the conversation in one place.

## Your First Pull Request

I welcome all contributions, from fixing a typo in the documentation to implementing a new feature. No contribution is too small!

If you are adding or changing code, please create or update tests to cover your changes. This ensures that I can maintain a high level of quality and prevent regressions.

For context, the core tech stack of PRP-core is:

-   **Backend:** Python with FastAPI
-   **Frontend:** SvelteKit

If you're unsure where to start, look for issues tagged `good first issue` or `help wanted`.

## Developing Modules

PRP-core uses a modular architecture to keep features organized and toggleable. When adding a new major feature (e.g., Health, Productivity), please follow this structure:

1.  **Backend**: Create a new directory `backend/src/prp_core/modules/<module_name>/`.
    *   Include `models.py`, `schemas.py`, and `router.py`.
    *   Implement a `services/seeder.py` with a `seed(scenario)` function for fake data.
    *   Register the module in `main.py` and `models/__init__.py`.
2.  **Frontend**: Create a new route `frontend/src/routes/<module_name>/`.
    *   Add a link to `Sidebar.svelte` with the `module` property set to your module's name.
    *   Add a toggle to the Settings page (this happens automatically if you register it in the backend).

## Code of Conduct

I am committed to fostering a welcoming, inclusive, and harassment-free environment for everyone. All participants in our community are expected to abide by the Code of Conduct. Please read it to understand what actions will and will not be tolerated.

In the interest of fostering an open and welcoming environment, I as the maintainer pledge to making participation in this project and community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

I expect all communication to be professional and respectful.