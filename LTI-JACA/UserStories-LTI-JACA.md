# LTI-JACA

# Product Backlog

## Epic 1: Job Requisition Management

- Priority: High
- T-Shirt Size: L
- Description: Develop a robust job requisition management system that allows recruiters and hiring managers to create, edit, and manage job postings efficiently.
- Business Impact: Critical for initiating the hiring process and attracting suitable candidates.

### User Story 1.1
- Title: Create Job Requisition
- Description: As a recruiter, I want to create a new job requisition, so that I can start the hiring process for a new position.
- Definition of Done: A new job requisition can be created with all necessary details and saved in the system.
- Priority: High
- Size: 13
- Tags: Recruiter, Job Posting
- Notes: Consider integration with internal job classification system.

#### Subtask 1.1.1
- Title: Design database schema for job requisitions
- Detailed Description: Create a database schema to store job requisition information including fields for title, description, requirements, salary range, location, and status.
- Acceptance Criteria:
  - Schema includes all necessary fields
  - Proper data types and constraints are applied
  - Schema is optimized for performance
- Acceptance Tests:
  - Verify all fields can be populated and retrieved correctly
  - Test data integrity constraints
- Priority: Urgent and Important
- Complexity: 8
- Estimated Time: 2 days
- Tags: Backend, Database

Subtask 1.1.2:
- Title: Develop API endpoint for creating job requisitions
- Detailed Description: Create a RESTful API endpoint that accepts job requisition details and saves them to the database.
- Acceptance Criteria:
  - Endpoint accepts POST requests with job requisition data
  - Input validation is implemented
  - Successful creation returns a 201 status code and the created job ID
  - Proper error handling and status codes for invalid inputs
- Acceptance Tests:
  - Test successful job creation with valid data
  - Test error handling with invalid or incomplete data
  - Verify correct status codes are returned
- Priority: Urgent and Important
- Complexity: 5
- Estimated Time: 3 days
- Tags: Backend, API

#### Subtask 1.1.3
- Title: Create job requisition form UI
- Detailed Description: Develop a user interface form for creating job requisitions, including all necessary fields and validation.
- Acceptance Criteria:
  - Form includes all required fields (title, description, requirements,   etc.)
  - Client-side validation is implemented
  - Form submits data to the API endpoint
  - Success and error messages are displayed to the user
- Acceptance Tests:
  - Test form submission with valid data
  - Test form validation with invalid data
  - Verify success and error messages are displayed correctly
- Priority: Urgent and Important
- Complexity: 8
- Estimated Time: 4 days
- Tags: Frontend, UI/UX

### User Story 1.2
- Title: Edit Job Requisition
- Description: As a hiring manager, I want to edit an existing job requisition, so that I can update the job details as needed.
- Definition of Done: An existing job requisition can be modified and the changes are reflected in the system.
- Priority: Medium
- Size: 8
- Tags: Hiring Manager, Job Posting
- Notes: Include version history for auditing purposes.

### User Story 1.3
- Title: View Job Requisitions
- Description: As a recruiter, I want to view a list of all job requisitions, so that I can manage open positions effectively.
- Definition of Done: A list view of all job requisitions is available with key details and filtering options.
- Priority: Medium
- Size: 5
- Tags: Recruiter, Job Posting
- Notes: Consider pagination for large numbers of requisitions.

## Epic 2: Candidate Application Process
- Priority: High
- T-Shirt Size: XL
- Description: Develop a user-friendly application process for candidates to submit their applications for open positions.

## Epic 3: Application Screening and Management
- Priority: High
- T-Shirt Size: L
- Description: Create a system for recruiters to screen and manage incoming applications efficiently.

## Epic 4: Interview Scheduling and Feedback
- Priority: Medium
- T-Shirt Size: L
- Description: Implement a system for scheduling interviews and collecting interviewer feedback.

## Epic 5: User Management and Authentication
- Priority: High
- T-Shirt Size: M
- Description: Develop a robust user management system with role-based access control.

## Epic 6: Reporting and Analytics
- Priority: Medium
- T-Shirt Size: M
- Description: Create a reporting system to provide insights into the hiring process and candidate pipeline.

# Planning

## Sprint 0: Environment Setup and DevOps (2 weeks)

Objectives:
- Set up development, staging, and production environments
- Configure CI/CD pipeline
- Set up monitoring and logging systems

Tasks:
1. Set up AWS infrastructure using Terraform
2. Configure Kubernetes clusters
3. Set up Docker registries
4. Configure GitHub Actions for CI/CD
5. Set up Prometheus, Grafana, and ELK stack
6. Configure Kong API Gateway
7. Set up development environments for team members

Resources:
- 2 DevOps Engineers
- 1 Backend Developer
- 1 Frontend Developer

## Sprint 1: Job Requisition Management - Part 1 (2 weeks)

User Stories:
- Create Job Requisition (User Story 1.1)
- Edit Job Requisition (User Story 1.2)

Resources:
- 2 Backend Developers
- 2 Frontend Developers
- 1 QA Engineer

## Sprint 2: Job Requisition Management - Part 2 and User Management (2 weeks)

User Stories:
- View Job Requisitions (User Story 1.3)
- User Registration and Authentication (from Epic 5)

Resources:
- 2 Backend Developers
- 2 Frontend Developers
- 1 QA Engineer

## Sprint 3: Candidate Application Process - Part 1 (2 weeks)

User Stories:
- Create Candidate Profile
- Submit Job Application

Resources:
- 2 Backend Developers
- 2 Frontend Developers
- 1 QA Engineer

## Sprint 4: Candidate Application Process - Part 2 and Application Screening (2 weeks)

User Stories:
- View Submitted Applications
- Screen Applications

Resources:
- 2 Backend Developers
- 2 Frontend Developers
- 1 QA Engineer

## Sprint 5: Interview Scheduling and Feedback - Part 1 (2 weeks)

User Stories:
- Schedule Interviews
- Conduct Video Interviews

Resources:
- 2 Backend Developers
- 2 Frontend Developers
- 1 QA Engineer

## Sprint 6: Interview Scheduling and Feedback - Part 2 (2 weeks)

User Stories:
- Provide Interview Feedback
- View Interview Schedule

Resources:
- 2 Backend Developers
- 2 Frontend Developers
- 1 QA Engineer

## Sprint 7: Reporting and Analytics (2 weeks)

User Stories:
- Generate Basic Reports
- View Hiring Pipeline Analytics

Resources:
- 1 Backend Developer
- 1 Frontend Developer
- 1 Data Analyst
- 1 QA Engineer

## Sprint 8: Final Integration and Testing (2 weeks)

Objectives:
- Ensure all components work together seamlessly
- Perform thorough system testing
- Address any remaining bugs or issues

Resources:
- 2 Backend Developers
- 2 Frontend Developers
- 2 QA Engineers
- 1 DevOps Engineer

## Estimation

Total Timeline: 18 weeks (approximately 4.5 months)

Additional Resources Required Throughout:
- 1 Product Owner
- 1 Scrum Master
- 1 UX Designer (part-time, as needed)
- 1 Database Administrator (part-time, as needed)