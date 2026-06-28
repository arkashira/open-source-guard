# Tech Spec: Open-Source-Guard
=====================================

## Stack
---------------

*   **Language:** Node.js (14.x)
*   **Framework:** Express.js (4.x)
*   **Runtime:** Docker (20.x)
*   **Database:** PostgreSQL (13.x) with Sequelize ORM
*   **Storage:** Local file system for storing project data

## Hosting
------------

*   **Free-tier-first:** Deploy on Heroku Free (1 dyno, 512 MB RAM)
*   **Specific platforms:**
    *   Heroku (paid plans for scalability)
    *   DigitalOcean (droplets for custom configurations)
    *   AWS (EC2 instances for enterprise deployments)

## Data Model
-------------

### Tables/Collections

*   **projects**: stores project metadata
    *   `id` (primary key, UUID): unique project identifier
    *   `name`: project name
    *   `description`: project description
    *   `owner_id`: project owner ID (foreign key referencing users)
*   **tasks**: stores task metadata
    *   `id` (primary key, UUID): unique task identifier
    *   `project_id` (foreign key referencing projects): task project ID
    *   `title`: task title
    *   `description`: task description
    *   `priority`: task priority (low, medium, high)
    *   `status`: task status (open, in_progress, completed)
*   **users**: stores user metadata
    *   `id` (primary key, UUID): unique user identifier
    *   `email`: user email
    *   `password`: user password (hashed)

### Key Fields

*   **project_id**: foreign key referencing projects in tasks table
*   **owner_id**: foreign key referencing users in projects table

## API Surface
----------------

### Endpoints

1.  **GET /projects**: retrieve a list of all projects
2.  **GET /projects/{id}**: retrieve a single project by ID
3.  **POST /projects**: create a new project
4.  **PUT /projects/{id}**: update an existing project
5.  **DELETE /projects/{id}**: delete a project
6.  **GET /tasks**: retrieve a list of all tasks
7.  **GET /tasks/{id}**: retrieve a single task by ID
8.  **POST /tasks**: create a new task
9.  **PUT /tasks/{id}**: update an existing task
10. **DELETE /tasks/{id}**: delete a task
11. **GET /users**: retrieve a list of all users
12. **GET /users/{id}**: retrieve a single user by ID
13. **POST /users**: create a new user
14. **PUT /users/{id}**: update an existing user
15. **DELETE /users/{id}**: delete a user

## Security Model
-----------------

*   **Authentication:** JSON Web Tokens (JWT) for user authentication
*   **Authorization:** Role-Based Access Control (RBAC) for project and task access
*   **Secrets:** environment variables for storing sensitive data (e.g., database credentials)
*   **IAM:** Identity and Access Management (IAM) for user and role management

## Observability
----------------

*   **Logs:** Winston logger for logging API requests and errors
*   **Metrics:** Prometheus for monitoring API performance and latency
*   **Traces:** Jaeger for tracing API requests and errors

## Build/CI
------------

*   **Build:** Node.js and npm for building and packaging the application
*   **CI:** GitHub Actions for automating testing, building, and deployment
*   **Deployment:** Heroku or DigitalOcean for deploying the application