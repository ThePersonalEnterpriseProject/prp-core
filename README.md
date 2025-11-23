# PRP-core

## The Grand Vision

PRP-core is envisioned as the foundational data store for your personal information, designed to empower you in planning for a prosperous future. Taking privacy with the utmost seriousness, our goal is to create an intuitive and user-friendly platform that enables individuals to make intelligent financial decisions grounded in factual data, rather than fleeting emotions. Think of it as "Personal Resource Planning" (PRP) or an "ERP for Your Life," providing a comprehensive overview and control over your personal financial landscape.

## Current Status: v0.1 (Minimum Viable Core)

We are thrilled to introduce PRP-core in its nascent stage, version 0.1. This is an early-stage project, representing the absolute minimum viable core functionality.

### Key Features
*   **Dashboard**: A high-level overview of your Net Worth and account summaries.
*   **Accounts Management**: Create, view, and delete Asset and Liability accounts.
*   **Transaction Tracking**: Log income and expenses, linked directly to your accounts.
*   **Developer Tools**: Includes a Fake Data Generator to seed the database with realistic scenarios (Young Professional, Family, Small Business) for testing and demos.

This first version provides a simple `docker-compose` setup with a modern web UI. You can manually create 'Asset' and 'Liability' accounts and manually add transactions to track your Net Worth in real-time.

It is important to note that features such as automatic bank syncing, file uploads, and advanced analytics are all part of the future roadmap, not included in this initial version.

## A Call to Arms: Your Help is Needed

The grand vision for PRP-core is ambitious, and its realization will greatly benefit from the collective passion and expertise of a vibrant community. While currently a solo endeavor, I am actively seeking enthusiastic contributors to help build this future.

All contributions are welcome, regardless of your experience level or area of expertise. Whether you're keen to improve our documentation, squash bugs, or develop exciting new features, your input is invaluable.

*   **Questions and Ideas:** Join the conversation and share your thoughts on our [GitHub Discussions](https://github.com/ThePersonalEnterpriseProject/prp-core/discussions) tab.
*   **Project Roadmap:** Discover what's next and find opportunities to contribute by exploring our [Project Roadmap](https://github.com/ThePersonalEnterpriseProject/prp-core/projects) (in the 'Projects' tab). Look for issues tagged "good first issue" to get started!
*   **How to Contribute:** For detailed guidelines on how to submit pull requests and contribute code, please refer to our [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Getting Started (v0.1)

To get PRP-core v0.1 up and running on your local machine, follow these simple steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/ThePersonalEnterpriseProject/prp-core.git
    cd prp-core
    ```

2.  **Start the application with Docker Compose:**
    ```bash
    docker-compose up --build -d
    ```

This command will build the necessary Docker images, set up the database, backend, and frontend services, and run them in detached mode. Once the services are up, you can access the frontend web UI in your browser, typically at `http://localhost:5173`.