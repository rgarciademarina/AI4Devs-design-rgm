# LTI-JACA

## Conclusions

- **Compiling a great manifest of the project (PRD, Roadmap, Architecture, Design, etc.) is essential to allow us to explore and take advantage of any chatbot.** Due to the limitations of my free Claude account (number of messages and size of conversation), I faced some issues getting results for my last prompts. I had to edit the previous prompt until I reached the maximum number of messages. Then, I decided to test in a different chatbot, ChatGPT, to avoid providing all the prompts I did in the previous exercise to have a similar context. I just provided the link to the PRD created in the last session, and ChatGPT did an excellent job making the Product Backlog; however, I think it could be even better with a better-provided manifest.
  - Reading the Claude documentation, I learned that Claude reads all the conversations every time we provide a new prompt. It's good to know since that guarantees our new prompt will work over the previous context.
  - When I changed to ChatGPT, I got a notification that ChatPGT cannot have context between different windows and is fully customizable. I didn't test it but that will be helpful to have different chats for specific tasks/experts (Design, Architecture, Product, Development, Sells, etc.)
- On the other hand, if we want to take advantage of all the capabilities of a chatbot and we have the opportunity, it is worth spending some bucks to acquire a license for our favorite chatbot after a full test, exploration, and analysis of the capabilities of each available product in the market.

## Claude

The following prompts were used in the previous conversation for the LTI-ATS-JACA as a context (continue the discussion in the same chat).

### Prompt 1

- Highlights:
  - Prompt completely built by myself.
  - Including 2 special texts from the AI response in previous conversation where it suggested the following steps to build the ATS: `Development Planning` and `Core Feature Development`.
- Results:
  - 👍 The AI provided a great result including everything that was asked for (separation - epics, USs, subtasks -, titles, descriptions, estimations, etc.)
  - 👎 The AI didn't take in consideration a "natural" roadmap, even when is not considered business critical, the authentication part was included until Epic 5.

```
Let's start with the Development Planning and Core Feature Development, starting with the MVP features for the LTI-ATS-JACA system.

Create a Product Backlog for the "Must Have" features:
- It should be split into Epics that contain a Business Requirement objective to develop.
- Each Epic must be prioritized based on the Business Impact.
- Epics must be estimated using the T-Shirt Size approach from XS to XXXL based on their complexity.
- Each Epic must contain a big-picture description of the feature to build.
- Add any other information that could be relevant to understand the business requirement.

Then, each Epic must contain a set of related User Stories:
- Each user story must be related to their parent Epic.
- Each user story must split a bit-sized Business Requirement to help build the epic objective.
- Each user story must follow a final user point of view.
- Each user story must follow the following template as a good practice:
 - Title: Summary description of the need
 - Description: As a [persona], I want to [intent], so that I can [benefit].
 - Definition of done: a description that will help determine if the objective of the user story is fulfilled.
 - Notes: Add any helpful information that can help you understand and build the needed solution.
- Each user story must be prioritized based on the final-user impact.
- Each story must be sized using the Fibonacci scale.
- Add tags to each user story that helps to understand the business impact and classify them, for example, Hiring Manager, Recruiter, Interviewer, Candidate, Login, Application Process, Screening, etc.
- Add any vital information to understand the final user's point of view, requirements, etc.

Finally, each User Story must contain a set of Subtasks that will adequately define all the technical tasks:
- Each subtask must have a technical perspective.
- Each subtask must follow the following template:
 - Title: Summary technical description of the requirement.
 - Detailed Description: must include all the technical information needed to complete the task and its purpose.
 - Acceptance Criteria: technical list of all the functional and non-functional requirements to be met.
 - Acceptance Tests: Manual tests must be executed to verify the functionality is correct.
- Each task must prioritized using the Eisenhower matrix to determine which tasks are fully needed and 
- Each task must estimated using two different scales:
 - Fibonacci to size the complexity effort.
 - Time to help understand the Product Team and how many days the work could take.
- Add tags to each user story that help to understand and classify which workstream will work on that and which sections of the system will be impacted, for example, Architecture, Backend, Frontend, Database, Cache, Infrastructure, etc.
```

I understand you want a comprehensive Product Backlog for the LTI-ATS-JACA system, focusing on the "Must Have" features. I'll create this backlog with Epics, User Stories, and Subtasks as requested. Due to the length and complexity of this task, I'll provide a detailed structure for one Epic with its associated User Stories and Subtasks, and then outline the remaining Epics. This approach will give you a clear template to follow for the rest of the backlog.

Epic 1: Job Requisition Management

Priority: High
T-Shirt Size: L
Description: Develop a robust job requisition management system that allows recruiters and hiring managers to create, edit, and manage job postings efficiently.
Business Impact: Critical for initiating the hiring process and attracting suitable candidates.

User Story 1.1:
Title: Create Job Requisition
Description: As a recruiter, I want to create a new job requisition, so that I can start the hiring process for a new position.
Definition of Done: A new job requisition can be created with all necessary details and saved in the system.
Priority: High
Size: 13
Tags: Recruiter, Job Posting
Notes: Consider integration with internal job classification system.

Subtask 1.1.1:
Title: Design database schema for job requisitions
Detailed Description: Create a database schema to store job requisition information including fields for title, description, requirements, salary range, location, and status.
Acceptance Criteria:
- Schema includes all necessary fields
- Proper data types and constraints are applied
- Schema is optimized for performance
Acceptance Tests:
- Verify all fields can be populated and retrieved correctly
- Test data integrity constraints
Priority: Urgent and Important
Complexity: 8
Estimated Time: 2 days
Tags: Backend, Database

Subtask 1.1.2:
Title: Develop API endpoint for creating job requisitions
Detailed Description: Create a RESTful API endpoint that accepts job requisition details and saves them to the database.
Acceptance Criteria:
- Endpoint accepts POST requests with job requisition data
- Input validation is implemented
- Successful creation returns a 201 status code and the created job ID
- Proper error handling and status codes for invalid inputs
Acceptance Tests:
- Test successful job creation with valid data
- Test error handling with invalid or incomplete data
- Verify correct status codes are returned
Priority: Urgent and Important
Complexity: 5
Estimated Time: 3 days
Tags: Backend, API

Subtask 1.1.3:
Title: Create job requisition form UI
Detailed Description: Develop a user interface form for creating job requisitions, including all necessary fields and validation.
Acceptance Criteria:
- Form includes all required fields (title, description, requirements, etc.)
- Client-side validation is implemented
- Form submits data to the API endpoint
- Success and error messages are displayed to the user
Acceptance Tests:
- Test form submission with valid data
- Test form validation with invalid data
- Verify success and error messages are displayed correctly
Priority: Urgent and Important
Complexity: 8
Estimated Time: 4 days
Tags: Frontend, UI/UX

User Story 1.2:
Title: Edit Job Requisition
Description: As a hiring manager, I want to edit an existing job requisition, so that I can update the job details as needed.
Definition of Done: An existing job requisition can be modified and the changes are reflected in the system.
Priority: Medium
Size: 8
Tags: Hiring Manager, Job Posting
Notes: Include version history for auditing purposes.

(Subtasks for User Story 1.2 would follow a similar pattern to 1.1)

User Story 1.3:
Title: View Job Requisitions
Description: As a recruiter, I want to view a list of all job requisitions, so that I can manage open positions effectively.
Definition of Done: A list view of all job requisitions is available with key details and filtering options.
Priority: Medium
Size: 5
Tags: Recruiter, Job Posting
Notes: Consider pagination for large numbers of requisitions.

(Subtasks for User Story 1.3 would follow a similar pattern)

Remaining Epics (outlined):

Epic 2: Candidate Application Process
Priority: High
T-Shirt Size: XL
Description: Develop a user-friendly application process for candidates to submit their applications for open positions.

Epic 3: Application Screening and Management
Priority: High
T-Shirt Size: L
Description: Create a system for recruiters to screen and manage incoming applications efficiently.

Epic 4: Interview Scheduling and Feedback
Priority: Medium
T-Shirt Size: L
Description: Implement a system for scheduling interviews and collecting interviewer feedback.

Epic 5: User Management and Authentication
Priority: High
T-Shirt Size: M
Description: Develop a robust user management system with role-based access control.

Epic 6: Reporting and Analytics
Priority: Medium
T-Shirt Size: M
Description: Create a reporting system to provide insights into the hiring process and candidate pipeline.

This structure provides a detailed template for the Product Backlog, focusing on the "Must Have" features for the LTI-ATS-JACA system. Each Epic, User Story, and Subtask follows the requested format and includes all necessary information for prioritization, estimation, and classification. The remaining Epics can be expanded following the same pattern as Epic 1.

### Prompt 1.1

- Highlights:
  - Based in the AI responses from the next prompts, I decided to get back until this point in the conversation and try to generate a timeline for the Product Backlog generated including the environment set-up activities.
- Results:
  - 👍 The AI provided a good result including considering the previous prompt - even after messed up the history a little bit with the other testing prompts.
  - 👎 The AI didn't take in consideration a "natural" roadmap, even when is not considered business critical, the authentication part was included until Sprint 2.

```
Break down the built Product Backlog above into manageable sprints and estimate timelines and resources required. Include a Sprint 0 to set up the environment and other DevOps-related tasks.
```

Certainly! I'll break down the Product Backlog into manageable sprints, including a Sprint 0 for environment setup and DevOps tasks. Each sprint will be two weeks long, which is a common practice in Agile development. I'll provide estimated timelines and resources required for each sprint.

Sprint 0: Environment Setup and DevOps (2 weeks)

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

Sprint 1: Job Requisition Management - Part 1 (2 weeks)

User Stories:
- Create Job Requisition (User Story 1.1)
- Edit Job Requisition (User Story 1.2)

Resources:
- 2 Backend Developers
- 2 Frontend Developers
- 1 QA Engineer

Sprint 2: Job Requisition Management - Part 2 and User Management (2 weeks)

User Stories:
- View Job Requisitions (User Story 1.3)
- User Registration and Authentication (from Epic 5)

Resources:
- 2 Backend Developers
- 2 Frontend Developers
- 1 QA Engineer

Sprint 3: Candidate Application Process - Part 1 (2 weeks)

User Stories:
- Create Candidate Profile
- Submit Job Application

Resources:
- 2 Backend Developers
- 2 Frontend Developers
- 1 QA Engineer

Sprint 4: Candidate Application Process - Part 2 and Application Screening (2 weeks)

User Stories:
- View Submitted Applications
- Screen Applications

Resources:
- 2 Backend Developers
- 2 Frontend Developers
- 1 QA Engineer

Sprint 5: Interview Scheduling and Feedback - Part 1 (2 weeks)

User Stories:
- Schedule Interviews
- Conduct Video Interviews

Resources:
- 2 Backend Developers
- 2 Frontend Developers
- 1 QA Engineer

Sprint 6: Interview Scheduling and Feedback - Part 2 (2 weeks)

User Stories:
- Provide Interview Feedback
- View Interview Schedule

Resources:
- 2 Backend Developers
- 2 Frontend Developers
- 1 QA Engineer

Sprint 7: Reporting and Analytics (2 weeks)

User Stories:
- Generate Basic Reports
- View Hiring Pipeline Analytics

Resources:
- 1 Backend Developer
- 1 Frontend Developer
- 1 Data Analyst
- 1 QA Engineer

Sprint 8: Final Integration and Testing (2 weeks)

Objectives:
- Ensure all components work together seamlessly
- Perform thorough system testing
- Address any remaining bugs or issues

Resources:
- 2 Backend Developers
- 2 Frontend Developers
- 2 QA Engineers
- 1 DevOps Engineer

Total Timeline: 18 weeks (approximately 4.5 months)

Additional Resources Required Throughout:
- 1 Product Owner
- 1 Scrum Master
- 1 UX Designer (part-time, as needed)
- 1 Database Administrator (part-time, as needed)

Notes:
1. This sprint breakdown assumes that the team can work on multiple user stories concurrently.
2. The resource allocation is based on the complexity of tasks in each sprint. Adjust as necessary based on your team's capacity and skills.
3. Each sprint should include time for sprint planning, daily stand-ups, sprint review, and retrospective.
4. QA activities should be ongoing throughout each sprint, not just at the end.
5. Consider having a buffer sprint or allocating some time in each sprint for addressing technical debt and unforeseen issues.
6. The Product Owner and Scrum Master should be involved throughout the process to ensure the project stays on track and aligns with business objectives.
7. After Sprint 8, plan for a soft launch or beta testing phase before full production deployment.

This sprint plan covers the development of the MVP features for the LTI-ATS-JACA system. It's important to remain flexible and adjust the plan as needed based on progress and any changing requirements or priorities.

### Prompt 2

- Highlights:
  - Little prompt built asking for taking the previous context.
  - Including 1 special text from the AI response in previous conversation where it suggested the following steps to build the ATS: `break down the project into manageable sprints or phases`.
- Results:
  - 👍 The AI created a timeline and took in consideration a "natural" roadmap, first setting up the environment, then building the authentication (users) functionality and finally all the business requirements.
  - 👎 The AI provided a poor result to build a backlog.

```
Considering the created use cases, functional and non-functional requirements, EMR and architecture provided before, break down the project into manageable sprints or phases.
```

Certainly. Based on the previously created use cases, functional and non-functional requirements, ERD, and architecture, I'll break down the project into manageable sprints or phases. We'll focus on delivering incremental value while building towards the complete LTI-ATS-JACA system. Each sprint will be two weeks long, and we'll plan for a total of 6 sprints (3 months) to deliver the MVP.

Sprint 1: Foundation and User Management
Focus: Set up the basic infrastructure and implement core user functionality.
Goals:
1. Set up development environment and CI/CD pipeline
2. Implement User Service microservice
3. Create basic frontend structure
4. Implement authentication and authorization

Key User Stories:
- User registration
- User login
- User profile management
- Role-based access control

Sprint 2: Job Requisition Management
Focus: Implement the core job posting functionality.
Goals:
1. Implement Job Service microservice
2. Create job requisition CRUD operations
3. Develop job listing and detail views in the frontend

Key User Stories:
- Create job requisition
- Edit job requisition
- View job requisitions
- Search and filter job requisitions

Sprint 3: Candidate Application Process
Focus: Enable candidates to apply for jobs and manage their applications.
Goals:
1. Implement Application Service microservice
2. Create candidate profile and application submission functionality
3. Develop application tracking for candidates

Key User Stories:
- Create candidate profile
- Submit job application
- View application status
- Edit/withdraw application

Sprint 4: Application Screening and Management
Focus: Provide tools for recruiters to screen and manage applications.
Goals:
1. Implement application screening functionality
2. Create applicant tracking system for recruiters
3. Develop basic search and filter capabilities for applications

Key User Stories:
- Screen applications
- Change application status
- Search and filter applications
- View applicant details

Sprint 5: Interview Management
Focus: Implement interview scheduling and feedback collection.
Goals:
1. Implement Interview Service microservice
2. Create interview scheduling functionality
3. Develop interview feedback collection system

Key User Stories:
- Schedule interviews
- Send interview invitations
- Collect interview feedback
- View interview schedule

Sprint 6: Reporting and Final Integration
Focus: Implement basic reporting and ensure full integration of all components.
Goals:
1. Implement basic reporting and analytics
2. Ensure seamless integration between all microservices
3. Perform end-to-end testing and bug fixes
4. Prepare for deployment

Key User Stories:
- Generate basic hiring reports
- View hiring pipeline analytics
- End-to-end application process testing

Throughout all sprints:
- Continuously refine and update the product backlog
- Conduct regular sprint planning, review, and retrospective meetings
- Ensure all implemented features meet the defined acceptance criteria
- Maintain and update documentation
- Address any critical bugs or issues that arise

Post-MVP Sprints (Future phases):
1. Advanced search and matching algorithms
2. Integration with external job boards
3. Advanced analytics and reporting
4. Onboarding process management
5. Mobile app development
6. Integration with HRIS and other internal systems
7. Customizable workflows and approval processes

This sprint breakdown ensures that we're building the system incrementally, with each sprint delivering tangible value. The order of the sprints is designed to create a minimum viable product as quickly as possible, starting with the core functionality of user management and job requisitions, then moving on to applications, screening, interviews, and finally reporting.

Each sprint builds upon the previous ones, gradually constructing the full system. This approach allows for early feedback and the ability to adjust plans if needed. The post-MVP sprints provide a roadmap for future enhancements once the core system is in place.

Remember to remain flexible and adjust this plan based on progress, feedback, and any changing priorities throughout the development process.

### Prompt 3

- Highlights:
  - Little prompt built asking for taking the previous context.
  - Including 2 special texts from the AI response in previous conversation where it suggested the following steps to build the ATS: `break down the project into manageable sprints or phases` and `estimate timelines and resources required`.
- Results:
  - 👍 The AI created a timeline, included team composition, allocation and took in consideration a "natural" roadmap, first setting up the environment (Sprint 0), then building the User Management module (Sprint 1) functionality and finally all the business requirements (Sprints 2 - 6).
  - 👎 The AI provided a poor result to build a backlog.

```
Considering the created use cases, functional and non-functional requirements, EMR and architecture provided before, break down the project into manageable sprints or phases and estimate timelines and resources required.
```

Certainly. I'll break down the project into manageable sprints and provide estimates for timelines and resources required, based on the previously created use cases, functional and non-functional requirements, ERD, and architecture. We'll assume a two-week sprint cycle and a cross-functional team structure.

Team Composition:
1. 1 Product Owner
2. 1 Scrum Master
3. 3 Full-stack Developers
4. 1 Frontend Developer
5. 1 UI/UX Designer
6. 1 QA Engineer
7. 1 DevOps Engineer

Total team size: 9 members

Timeline: 6 Sprints (12 weeks / 3 months) for MVP

Sprint Breakdown:

Sprint 1: Foundation and User Management (2 weeks)
Focus: Set up the basic infrastructure and implement core user functionality.
Resources:
- All team members involved
- AWS resources set up
- Development environments established

Key Deliverables:
- CI/CD pipeline setup
- User Service microservice MVP
- Basic frontend structure
- Authentication and authorization implementation

Sprint 2: Job Requisition Management (2 weeks)
Focus: Implement the core job posting functionality.
Resources:
- 2 Full-stack Developers
- 1 Frontend Developer
- 1 UI/UX Designer
- 1 QA Engineer

Key Deliverables:
- Job Service microservice MVP
- Job requisition CRUD operations
- Job listing and detail views in the frontend

Sprint 3: Candidate Application Process (2 weeks)
Focus: Enable candidates to apply for jobs and manage their applications.
Resources:
- 2 Full-stack Developers
- 1 Frontend Developer
- 1 UI/UX Designer
- 1 QA Engineer

Key Deliverables:
- Application Service microservice MVP
- Candidate profile and application submission functionality
- Application tracking for candidates

Sprint 4: Application Screening and Management (2 weeks)
Focus: Provide tools for recruiters to screen and manage applications.
Resources:
- 2 Full-stack Developers
- 1 Frontend Developer
- 1 UI/UX Designer
- 1 QA Engineer

Key Deliverables:
- Application screening functionality
- Applicant tracking system for recruiters
- Basic search and filter capabilities for applications

Sprint 5: Interview Management (2 weeks)
Focus: Implement interview scheduling and feedback collection.
Resources:
- 2 Full-stack Developers
- 1 Frontend Developer
- 1 UI/UX Designer
- 1 QA Engineer

Key Deliverables:
- Interview Service microservice MVP
- Interview scheduling functionality
- Interview feedback collection system

Sprint 6: Reporting and Final Integration (2 weeks)
Focus: Implement basic reporting and ensure full integration of all components.
Resources:
- All team members involved

Key Deliverables:
- Basic reporting and analytics
- Full integration of all microservices
- End-to-end testing completed
- System ready for deployment

Resource Allocation Throughout:
- Product Owner: 100% throughout all sprints
- Scrum Master: 100% throughout all sprints
- Full-stack Developers: 100% throughout all sprints
- Frontend Developer: 100% throughout all sprints
- UI/UX Designer: 100% in Sprint 1, then as needed in subsequent sprints
- QA Engineer: 50% in Sprint 1, 100% in subsequent sprints
- DevOps Engineer: 100% in Sprint 1, then 50% in subsequent sprints for maintenance and support

Additional Resources Required:
1. Development and Testing Environment:
   - AWS EC2 instances for each microservice
   - AWS RDS for PostgreSQL databases
   - AWS ElastiCache for Redis
   - AWS Elasticsearch Service
   - AWS EKS for Kubernetes

2. Monitoring and Logging:
   - AWS CloudWatch
   - ELK Stack (Elasticsearch, Logstash, Kibana)

3. CI/CD:
   - GitHub repository
   - GitHub Actions for CI/CD pipeline

4. Communication and Collaboration Tools:
   - Slack for team communication
   - Jira for project management and issue tracking
   - Confluence for documentation

5. Design Tools:
   - Figma for UI/UX design

6. Testing Tools:
   - Jest for unit testing
   - Cypress for end-to-end testing

Timeline Estimates:
- Project Kickoff and Sprint 0 (Initial planning and setup): 1 week
- MVP Development (Sprints 1-6): 12 weeks
- Post-MVP Review and Planning: 1 week

Total Estimated Timeline: 14 weeks

Post-MVP Phases (High-level estimates):
1. Advanced search and matching algorithms: 3-4 weeks
2. Integration with external job boards: 2-3 weeks
3. Advanced analytics and reporting: 3-4 weeks
4. Onboarding process management: 3-4 weeks
5. Mobile app development: 6-8 weeks
6. Integration with HRIS and other internal systems: 4-6 weeks
7. Customizable workflows and approval processes: 3-4 weeks

These post-MVP phases would be prioritized based on business needs and could be tackled in subsequent sprints after the MVP launch.

Notes:
1. The resource allocation and timeline are estimates and may need adjustment based on actual progress and any unforeseen challenges.
2. Regular sprint planning, review, and retrospective meetings should be held to ensure the project stays on track and to address any issues promptly.
3. The Product Owner should continuously refine and prioritize the product backlog to ensure the team is always working on the most valuable features.
4. As this is a microservices architecture, there might be some parallel development possible, which could potentially speed up certain aspects of the development process.
5. Adequate time should be allocated for testing, bug fixing, and performance optimization in each sprint.
6. Consider having a buffer of 1-2 weeks in the overall timeline for any unexpected delays or additional refinement needed.

This breakdown provides a structured approach to developing the LTI-ATS-JACA system, with clear allocation of resources and timeline estimates. It allows for incremental development and delivery of value, with the flexibility to adjust based on feedback and changing priorities.

### Prompt 4

- Highlights:
  - Little prompt asking to follow the best industry standards instead of providing all the list of requirements of the output.
  - Including 2 special texts from the AI response in previous conversation where it suggested the following steps to build the ATS: `break down the project into manageable sprints or phases` and `estimate timelines and resources required`.
- Results:
  - 👍 The AI created a timeline, included team composition, allocation and took in consideration a "natural" roadmap and split the work in epics, USs and subtasks providing estimation.
  - 👎 The details for USs and subtasks is poor.

```
Let's build a Product Backlog split in epics, user stories and subtasks following the best industry standards, break down the project into manageable sprints and estimate timelines and resources required.
```

Certainly! I'll create a comprehensive Product Backlog for the LTI-ATS-JACA system, split into epics, user stories, and subtasks. Then, I'll break it down into manageable sprints and estimate timelines and resources. Let's start with the Product Backlog:

Product Backlog:

Epic 1: User Management and Authentication
Priority: High
T-Shirt Size: M
Description: Implement a secure user management system with role-based access control.

User Story 1.1: User Registration
As a new user, I want to create an account so that I can access the ATS.
Priority: High
Story Points: 5
Tags: Authentication, User Management

Subtasks:
1.1.1: Design and implement user registration API (Backend, 3 points, 1 day)
1.1.2: Create user registration form (Frontend, 2 points, 1 day)
1.1.3: Implement email verification (Backend, 3 points, 1 day)

User Story 1.2: User Login
As a registered user, I want to log in to the system so that I can access my account.
Priority: High
Story Points: 3
Tags: Authentication, User Management

Subtasks:
1.2.1: Implement login API with JWT (Backend, 2 points, 1 day)
1.2.2: Create login form and handle authentication (Frontend, 2 points, 1 day)

User Story 1.3: Role-Based Access Control
As an admin, I want to assign roles to users so that I can control access to different parts of the system.
Priority: Medium
Story Points: 8
Tags: Authorization, User Management

Subtasks:
1.3.1: Design and implement role management API (Backend, 5 points, 2 days)
1.3.2: Create role assignment interface (Frontend, 3 points, 1 day)
1.3.3: Implement route protection based on roles (Frontend, 2 points, 1 day)

Epic 2: Job Requisition Management
Priority: High
T-Shirt Size: L
Description: Develop a system for creating, editing, and managing job requisitions.

User Story 2.1: Create Job Requisition
As a recruiter, I want to create a new job requisition so that I can start the hiring process.
Priority: High
Story Points: 8
Tags: Job Posting, Recruiter

Subtasks:
2.1.1: Design and implement job creation API (Backend, 5 points, 2 days)
2.1.2: Create job requisition form (Frontend, 5 points, 2 days)
2.1.3: Implement form validation (Frontend, 2 points, 1 day)

User Story 2.2: Edit Job Requisition
As a recruiter, I want to edit an existing job requisition so that I can update job details.
Priority: Medium
Story Points: 5
Tags: Job Posting, Recruiter

Subtasks:
2.2.1: Implement job update API (Backend, 3 points, 1 day)
2.2.2: Create edit job form (Frontend, 3 points, 1 day)

User Story 2.3: List Job Requisitions
As a recruiter, I want to view a list of all job requisitions so that I can manage open positions.
Priority: Medium
Story Points: 5
Tags: Job Posting, Recruiter

Subtasks:
2.3.1: Implement job listing API with pagination (Backend, 3 points, 1 day)
2.3.2: Create job listing page with filters (Frontend, 5 points, 2 days)

Epic 3: Candidate Application Process
Priority: High
T-Shirt Size: XL
Description: Develop a user-friendly application process for candidates.

User Story 3.1: Submit Job Application
As a candidate, I want to submit an application for a job so that I can be considered for the position.
Priority: High
Story Points: 13
Tags: Application Process, Candidate

Subtasks:
3.1.1: Design and implement application submission API (Backend, 8 points, 3 days)
3.1.2: Create multi-step application form (Frontend, 8 points, 3 days)
3.1.3: Implement resume parsing functionality (Backend, 5 points, 2 days)

User Story 3.2: View Application Status
As a candidate, I want to view the status of my applications so that I can track my progress.
Priority: Medium
Story Points: 5
Tags: Application Process, Candidate

Subtasks:
3.2.1: Implement application status API (Backend, 3 points, 1 day)
3.2.2: Create application status dashboard (Frontend, 3 points, 1 day)

Epic 4: Application Screening and Management
Priority: High
T-Shirt Size: L
Description: Create tools for recruiters to screen and manage applications efficiently.

User Story 4.1: Screen Applications
As a recruiter, I want to review and screen incoming applications so that I can identify suitable candidates.
Priority: High
Story Points: 8
Tags: Screening, Recruiter

Subtasks:
4.1.1: Implement application review API (Backend, 5 points, 2 days)
4.1.2: Create application screening interface (Frontend, 5 points, 2 days)
4.1.3: Implement basic candidate ranking algorithm (Backend, 5 points, 2 days)

User Story 4.2: Manage Applicant Pipeline
As a recruiter, I want to move candidates through different stages so that I can manage the hiring pipeline.
Priority: Medium
Story Points: 8
Tags: Screening, Recruiter

Subtasks:
4.2.1: Design and implement pipeline management API (Backend, 5 points, 2 days)
4.2.2: Create drag-and-drop pipeline management interface (Frontend, 8 points, 3 days)

Epic 5: Interview Management
Priority: Medium
T-Shirt Size: L
Description: Implement interview scheduling and feedback collection system.

User Story 5.1: Schedule Interviews
As a recruiter, I want to schedule interviews with candidates so that I can assess their suitability for the role.
Priority: High
Story Points: 8
Tags: Interview, Recruiter

Subtasks:
5.1.1: Implement interview scheduling API (Backend, 5 points, 2 days)
5.1.2: Create interview scheduling interface (Frontend, 5 points, 2 days)
5.1.3: Implement email notifications for interviews (Backend, 3 points, 1 day)

User Story 5.2: Collect Interview Feedback
As an interviewer, I want to submit feedback after an interview so that I can share my assessment of the candidate.
Priority: Medium
Story Points: 5
Tags: Interview, Interviewer

Subtasks:
5.2.1: Design and implement feedback submission API (Backend, 3 points, 1 day)
5.2.2: Create feedback form and summary view (Frontend, 5 points, 2 days)

Epic 6: Reporting and Analytics
Priority: Medium
T-Shirt Size: M
Description: Develop basic reporting and analytics features for hiring insights.

User Story 6.1: Generate Hiring Reports
As a hiring manager, I want to generate reports on the hiring process so that I can analyze our recruitment efforts.
Priority: Medium
Story Points: 8
Tags: Reporting, Hiring Manager

Subtasks:
6.1.1: Implement report generation API (Backend, 5 points, 2 days)
6.1.2: Create report configuration and display interface (Frontend, 5 points, 2 days)

User Story 6.2: View Hiring Analytics Dashboard
As a recruiter, I want to view key hiring metrics on a dashboard so that I can monitor our recruitment performance.
Priority: Low
Story Points: 5
Tags: Analytics, Recruiter

Subtasks:
6.2.1: Implement analytics data API (Backend, 3 points, 1 day)
6.2.2: Create analytics dashboard with charts (Frontend, 5 points, 2 days)

Now, let's break down the project into manageable sprints and estimate timelines and resources:

Sprint 1 (2 weeks): User Management and Authentication
- User Story 1.1: User Registration
- User Story 1.2: User Login
- User Story 1.3: Role-Based Access Control

Sprint 2 (2 weeks): Job Requisition Management
- User Story 2.1: Create Job Requisition
- User Story 2.2: Edit Job Requisition
- User Story 2.3: List Job Requisitions

Sprint 3 (2 weeks): Candidate Application Process
- User Story 3.1: Submit Job Application
- User Story 3.2: View Application Status

Sprint 4 (2 weeks): Application Screening and Management
- User Story 4.1: Screen Applications
- User Story 4.2: Manage Applicant Pipeline

Sprint 5 (2 weeks): Interview Management
- User Story 5.1: Schedule Interviews
- User Story 5.2: Collect Interview Feedback

Sprint 6 (2 weeks): Reporting and Analytics, Final Integration
- User Story 6.1: Generate Hiring Reports
- User Story 6.2: View Hiring Analytics Dashboard
- Final integration, testing, and bug fixes

Total timeline: 12 weeks (3 months) for MVP

Resources required:
1. Frontend Developer (2)
2. Backend Developer (2)
3. Full-stack Developer (1)
4. UI/UX Designer (1)
5. Quality Assurance Engineer (1)
6. Product Owner (1)
7. Scrum Master (1)
8. DevOps Engineer (1, part-time)

This breakdown provides a structured approach to building the LTI-ATS-JACA system, with clear epics, user stories, and subtasks. The sprint plan allows for incremental development and delivery of features, with each sprint building on the previous ones. The resource allocation ensures that all necessary skills are covered for the development process.

Remember that this is an initial plan and may need to be adjusted based on actual progress, feedback, and any changes in priorities during the development process.

### Prompt 5

- Highlights:
  - Include all the details and information required.
  - Takes information provided by the AI.
- Results:
  - 👍 The Product Backlog contains all the required information.
  - 👎 The sprint planning and timelines were omitted, it provided suggestions about how to do it but it didn't include it per se.

```
Let's create a Product Backlog split in epics, user stories and subtasks following the best industry standards, break down the project into manageable sprints and estimate timelines and resources required.

The Product Backlog for the "Must Have" features:
- It should be split into Epics that contain a Business Requirement objective to develop.
- Each Epic must be prioritized based on the Business Impact.
- Epics must be estimated using the T-Shirt Size approach from XS to XXXL based on their complexity.
- Each Epic must contain a big-picture description of the feature to build.
- Add any other information that could be relevant to understand the business requirement.

Then, each Epic must contain a set of related User Stories:
- Each user story must be related to their parent Epic.
- Each user story must split a bit-sized Business Requirement to help build the epic objective.
- Each user story must follow a final user point of view.
- Each user story must follow the following template as a good practice:
 - Title: Summary description of the need
 - Description: As a [persona], I want to [intent], so that I can [benefit].
 - Definition of done: a description that will help determine if the objective of the user story is fulfilled.
 - Notes: Add any helpful information that can help you understand and build the needed solution.
- Each user story must be prioritized based on the final-user impact.
- Each story must be sized using the Fibonacci scale.
- Add tags to each user story that helps to understand the business impact and classify them, for example, Hiring Manager, Recruiter, Interviewer, Candidate, Login, Application Process, Screening, etc.
- Add any vital information to understand the final user's point of view, requirements, etc.

Finally, each User Story must contain a set of Subtasks that will adequately define all the technical tasks:
- Each subtask must have a technical perspective.
- Each subtask must follow the following template:
 - Title: Summary technical description of the requirement.
 - Detailed Description: must include all the technical information needed to complete the task and its purpose.
 - Acceptance Criteria: technical list of all the functional and non-functional requirements to be met.
 - Acceptance Tests: Manual tests must be executed to verify the functionality is correct.
- Each task must prioritized using the Eisenhower matrix to determine which tasks are fully needed and 
- Each task must estimated using two different scales:
 - Fibonacci to size the complexity effort.
 - Time to help understand the Product Team and how many days the work could take.
- Add tags to each user story that help to understand and classify which workstream will work on that and which sections of the system will be impacted, for example, Architecture, Backend, Frontend, Database, Cache, Infrastructure, etc.
```

I understand you want a comprehensive Product Backlog for the "Must Have" features of the LTI-ATS-JACA project. I'll create this backlog following the structure and best practices you've outlined. Given the complexity and depth of this task, I'll provide a sample of the backlog, focusing on one Epic with its related User Stories and Subtasks. This sample will serve as a template for how the entire backlog should be structured.

Epic 1: Job Posting Management

Priority: High
T-Shirt Size: L
Description: Develop a comprehensive job posting management system that allows recruiters and hiring managers to create, edit, publish, and manage job listings efficiently. This system should streamline the job creation process, ensure compliance with company standards, and improve the visibility of open positions.

User Stories:

1. Title: Create New Job Posting
   - Description: As a recruiter, I want to create a new job posting, so that I can advertise open positions in our company.
   - Definition of Done: 
     - A new job posting can be created with all required fields
     - The posting is saved in draft status
     - Validation is in place for all required fields
   - Notes: Consider integrating with company-wide job templates for consistency
   - Priority: High
   - Size: 13
   - Tags: Recruiter, Job Posting, Creation

   Subtasks:

   - 1.1 Title: Design Job Posting Database Schema
       - Detailed Description: Create a database schema for storing job postings, including fields for title, description, requirements, location, salary range, and status.
       - Acceptance Criteria:
         - Schema includes all necessary fields
         - Appropriate data types and constraints are used
         - Schema is optimized for performance
       - Acceptance Tests:
         - Verify all fields can be populated and retrieved correctly
         - Test constraints with valid and invalid data
       - Priority: Urgent and Important
       - Complexity: 8
       - Estimated Time: 2 days
       - Tags: Backend, Database

   - 1.2 Title: Implement Job Posting API Endpoints
       - Detailed Description: Create RESTful API endpoints for creating, reading, updating, and deleting job postings.
       - Acceptance Criteria:
         - Endpoints for CRUD operations are implemented
         - Proper authentication and authorization are in place
         - Input validation is implemented
         - Appropriate HTTP status codes are returned
       - Acceptance Tests:
         - Test each endpoint with valid and invalid data
         - Verify authentication works as expected
       - Priority: Urgent and Important
       - Complexity: 13
       - Estimated Time: 4 days
       - Tags: Backend, API

   - 1.3 Title: Develop Job Posting Creation UI
       - Detailed Description: Create a user-friendly interface for recruiters to input job posting details.
       - Acceptance Criteria:
         - All required fields are present in the form
         - Form validation is implemented
         - User can save as draft or submit for publication
         - Responsive design works on desktop and mobile
       - Acceptance Tests:
         - Test form submission with valid and invalid data
         - Verify draft saving functionality
         - Check responsiveness on various devices
       - Priority: Important but Not Urgent
       - Complexity: 8
       - Estimated Time: 3 days
       - Tags: Frontend, UI/UX

2. Title: Edit Existing Job Posting
   - Description: As a recruiter, I want to edit an existing job posting, so that I can update the details or correct any errors.
   - Definition of Done:
     - Existing job postings can be retrieved and edited
     - Changes are saved and reflected immediately
     - Edit history is maintained for auditing purposes
   - Notes: Consider implementing a versioning system for job postings
   - Priority: Medium
   - Size: 8
   - Tags: Recruiter, Job Posting, Editing

   Subtasks:

   - 2.1 Title: Implement Job Posting Retrieval
       - Detailed Description: Create an API endpoint to retrieve a specific job posting by ID.
       - Acceptance Criteria:
         - Endpoint returns all job posting details
         - Proper error handling for non-existent postings
       - Acceptance Tests:
         - Test retrieval of existing and non-existing postings
         - Verify all fields are correctly returned
       - Priority: Urgent and Important
       - Complexity: 5
       - Estimated Time: 1 day
       - Tags: Backend, API

   - 2.2 Title: Develop Job Posting Edit UI
       - Detailed Description: Create an interface for editing existing job postings, pre-populated with current data.
       - Acceptance Criteria:
         - All fields are pre-populated with existing data
         - Changes can be saved or discarded
         - Form validation is implemented
       - Acceptance Tests:
         - Test editing and saving changes
         - Verify validation works for all fields
       - Priority: Important but Not Urgent
       - Complexity: 8
       - Estimated Time: 2 days
       - Tags: Frontend, UI/UX

   - 2.3 Title: Implement Edit History Tracking
       - Detailed Description: Create a system to track and store edit history for job postings.
       - Acceptance Criteria:
         - Each edit is recorded with timestamp and user
         - Edit history can be retrieved and displayed
       - Acceptance Tests:
         - Make multiple edits and verify history accuracy
         - Test retrieval and display of edit history
       - Priority: Not Urgent and Not Important
       - Complexity: 13
       - Estimated Time: 3 days
       - Tags: Backend, Database

This sample provides a detailed structure for one Epic in the Product Backlog, including related User Stories and Subtasks. The actual Product Backlog would contain multiple Epics covering all "Must Have" features, each with its own set of User Stories and Subtasks, following this same format and level of detail.

To break down the project into manageable sprints and estimate timelines:

1. Group related User Stories into potential sprints, aiming for a consistent velocity (sum of story points) per sprint.
2. Prioritize sprints based on the priorities of the Epics and User Stories they contain.
3. Estimate sprint duration based on the team's capacity and the total estimated time of the Subtasks in each sprint.
4. Allocate resources (developers, designers, QA) based on the tags and requirements of the Subtasks in each sprint.

Remember that this is an iterative process, and the backlog should be regularly refined and reprioritized based on feedback and changing business needs.

## ChatGPT

The following prompt is taking in consideration the markdown documentation result in the previous session.

### Prompt 1

- Highlights:
  - Prompt completely built by myself.
  - Including 2 special texts from the AI response in previous conversation where it suggested the following steps to build the ATS: `Development Planning` and `Core Feature Development`.
- Results:
  - 👍 The AI provided a great result including everything that was asked for (separation - epics, USs, subtasks -, titles, descriptions, estimations, etc.)
  - 👎 The AI didn't take in consideration a "natural" roadmap, even when is not considered business critical, the authentication part was included until Epic 5.

```
The following PRD file https://raw.githubusercontent.com/sjaca10/AI4Devs-design/main/LTI-JACA/Design-LTI-JACA.md was built as designed for the LTI-ATS-JACA system. Use it as context to execute the following operations.

Create a Product Backlog for the "Must Have" features:
- It should be split into Epics that contain a Business Requirement objective to develop.
- Each Epic must be prioritized based on the Business Impact.
- Epics must be estimated using the T-Shirt Size approach from XS to XXXL based on their complexity.
- Each Epic must contain a big-picture description of the feature to build.
- Add any other information that could be relevant to understand the business requirement.

Then, each Epic must contain a set of related User Stories:
- Each user story must be related to their parent Epic.
- Each user story must split a bit-sized Business Requirement to help build the epic objective.
- Each user story must follow a final user point of view.
- Each user story must follow the following template as a good practice:
 - Title: Summary description of the need
 - Description: As a [persona], I want to [intent], so that I can [benefit].
 - Definition of done: a description that will help determine if the objective of the user story is fulfilled.
 - Notes: Add any helpful information that can help you understand and build the needed solution.
- Each user story must be prioritized based on the final-user impact.
- Each story must be sized using the Fibonacci scale.
- Add tags to each user story that helps to understand the business impact and classify them, for example, Hiring Manager, Recruiter, Interviewer, Candidate, Login, Application Process, Screening, etc.
- Add any vital information to understand the final user's point of view, requirements, etc.

Finally, each User Story must contain a set of Subtasks that will adequately define all the technical tasks:
- Each subtask must have a technical perspective.
- Each subtask must follow the following template:
 - Title: Summary technical description of the requirement.
 - Detailed Description: must include all the technical information needed to complete the task and its purpose.
 - Acceptance Criteria: technical list of all the functional and non-functional requirements to be met.
 - Acceptance Tests: Manual tests must be executed to verify the functionality is correct.
- Each task must prioritized using the Eisenhower matrix to determine which tasks are fully needed and 
- Each task must estimated using two different scales:
 - Fibonacci to size the complexity effort.
 - Time to help understand the Product Team and how many days the work could take.
- Add tags to each user story that help to understand and classify which workstream will work on that and which sections of the system will be impacted, for example, Architecture, Backend, Frontend, Database, Cache, Infrastructure, etc.
```

To create a comprehensive Product Backlog for the "Must Have" features of the LTI-ATS-JACA system, I'll follow the structure and steps you've outlined. Let's start by creating the Epics with their related User Stories and Subtasks. I'll base these on the context provided by the PRD file.

## Epics

### Epic 1: User Authentication and Authorization

**Big-picture description**: Develop a secure and efficient user authentication and authorization system to manage access to the LTI-ATS-JACA platform. This includes user login, registration, password management, and role-based access control.

**Priority**: High

**T-Shirt Size**: XL

**Business Impact**: Ensures secure access to the system, protecting sensitive data and providing a seamless user experience.

#### User Stories:

**User Story 1.1: User Registration**

- **Title**: Implement user registration
- **Description**: As a new user, I want to register an account so that I can access the LTI-ATS-JACA platform.
- **Definition of done**: Registration form is available, functional, and securely stores user information in the database.
- **Notes**: Ensure data validation and security measures are in place.
- **Priority**: High
- **Size**: 8
- **Tags**: Registration, Security

**User Story 1.2: User Login**

- **Title**: Implement user login
- **Description**: As a registered user, I want to log in so that I can access my account and use the platform features.
- **Definition of done**: Login form is available, functional, and securely verifies user credentials.
- **Notes**: Include error handling for incorrect credentials.
- **Priority**: High
- **Size**: 8
- **Tags**: Login, Security

**User Story 1.3: Password Management**

- **Title**: Implement password management
- **Description**: As a user, I want to reset my password if I forget it so that I can regain access to my account.
- **Definition of done**: Password reset functionality is available and secure.
- **Notes**: Ensure secure token generation for password resets.
- **Priority**: Medium
- **Size**: 5
- **Tags**: Password Management, Security

**User Story 1.4: Role-based Access Control**

- **Title**: Implement role-based access control
- **Description**: As an admin, I want to manage user roles and permissions so that users have appropriate access to features.
- **Definition of done**: Roles and permissions are defined and enforced throughout the platform.
- **Notes**: Ensure flexible and scalable role management.
- **Priority**: Medium
- **Size**: 8
- **Tags**: Security, Access Control

#### Subtasks for User Story 1.1: User Registration

**Subtask 1.1.1: Create Registration Form**

- **Title**: Create registration form
- **Detailed Description**: Develop a user registration form with fields for username, email, and password. Ensure client-side validation.
- **Acceptance Criteria**: Form is created with all necessary fields and validations.
- **Acceptance Tests**: Test form for proper validation and error handling.
- **Priority**: Urgent
- **Size**: 5
- **Time Estimate**: 2 days
- **Tags**: Frontend, UI

**Subtask 1.1.2: Backend User Registration Endpoint**

- **Title**: Create backend registration endpoint
- **Detailed Description**: Develop an API endpoint to handle user registration, store user data securely in the database, and send a confirmation email.
- **Acceptance Criteria**: Endpoint is created and properly stores user data.
- **Acceptance Tests**: Test endpoint with various inputs for proper data handling.
- **Priority**: Important
- **Size**: 8
- **Time Estimate**: 3 days
- **Tags**: Backend, API, Database

**Subtask 1.1.3: Email Confirmation Service**

- **Title**: Develop email confirmation service
- **Detailed Description**: Create a service to send confirmation emails to users upon registration. Include secure token generation and email template.
- **Acceptance Criteria**: Email service is functional and sends confirmation emails.
- **Acceptance Tests**: Verify email is sent and confirmation link works.
- **Priority**: Important
- **Size**: 5
- **Time Estimate**: 2 days
- **Tags**: Backend, Email Service

**Subtask 1.1.4: Database Schema for User Data**

- **Title**: Create database schema for user data
- **Detailed Description**: Design and implement the database schema to store user information securely.
- **Acceptance Criteria**: Database schema is created and integrated with the registration endpoint.
- **Acceptance Tests**: Verify data is stored correctly in the database.
- **Priority**: Important
- **Size**: 8
- **Time Estimate**: 3 days
- **Tags**: Database, Backend

---

### Epic 2: Job Application Process

**Big-picture description**: Develop a robust job application process that allows candidates to apply for jobs, upload resumes, and track application status. This includes job listing management, application submission, and status tracking.

**Priority**: High

**T-Shirt Size**: XXL

**Business Impact**: Streamlines the hiring process, making it easier for candidates to apply and for recruiters to manage applications.

#### User Stories:

**User Story 2.1: Job Listing Management**

- **Title**: Implement job listing management
- **Description**: As a recruiter, I want to create and manage job listings so that I can attract and track suitable candidates.
- **Definition of done**: Job listing creation and management functionalities are available and functional.
- **Notes**: Include fields for job description, requirements, and benefits.
- **Priority**: High
- **Size**: 13
- **Tags**: Job Listing, Recruiter

**User Story 2.2: Job Application Submission**

- **Title**: Implement job application submission
- **Description**: As a candidate, I want to apply for jobs and upload my resume so that I can be considered for positions.
- **Definition of done**: Application submission form is available and functional.
- **Notes**: Ensure file upload functionality for resumes.
- **Priority**: High
- **Size**: 8
- **Tags**: Application Process, Candidate

**User Story 2.3: Application Status Tracking**

- **Title**: Implement application status tracking
- **Description**: As a candidate, I want to track the status of my job applications so that I can stay informed about my application progress.
- **Definition of done**: Status tracking feature is available and accurately reflects the application status.
- **Notes**: Include notifications for status updates.
- **Priority**: Medium
- **Size**: 5
- **Tags**: Application Process, Candidate

#### Subtasks for User Story 2.1: Job Listing Management

**Subtask 2.1.1: Create Job Listing Form**

- **Title**: Create job listing form
- **Detailed Description**: Develop a form for recruiters to create job listings with fields for job title, description, requirements, and benefits.
- **Acceptance Criteria**: Form is created and functional with proper validation.
- **Acceptance Tests**: Test form for proper validation and data handling.
- **Priority**: Urgent
- **Size**: 5
- **Time Estimate**: 2 days
- **Tags**: Frontend, UI

**Subtask 2.1.2: Backend Job Listing Endpoint**

- **Title**: Create backend job listing endpoint
- **Detailed Description**: Develop an API endpoint to handle job listing creation, update, and deletion. Store job data in the database.
- **Acceptance Criteria**: Endpoint is created and properly stores job data.
- **Acceptance Tests**: Test endpoint with various inputs for proper data handling.
- **Priority**: Important
- **Size**: 8
- **Time Estimate**: 3 days
- **Tags**: Backend, API, Database

**Subtask 2.1.3: Job Listing Management UI**

- **Title**: Develop job listing management UI
- **Detailed Description**: Create a user interface for recruiters to manage job listings, including viewing, editing, and deleting listings.
- **Acceptance Criteria**: UI is functional and integrates with the backend.
- **Acceptance Tests**: Verify UI functionality and integration with the backend.
- **Priority**: Important
- **Size**: 8
- **Time Estimate**: 3 days
- **Tags**: Frontend, UI

**Subtask 2.1.4: Database Schema for Job Listings**

- **Title**: Create database schema for job listings
- **Detailed Description**: Design and implement the database schema to store job listing information securely.
- **Acceptance Criteria**: Database schema is created and integrated with the job listing endpoint.
- **Acceptance Tests**: Verify data is stored correctly in the database.
- **Priority**: Important
- **Size**: 8
- **Time Estimate**: 3 days
- **Tags**: Database, Backend

---

This structure can be expanded with additional Epics, User Stories, and Subtasks based on the remaining "Must Have" features from the PRD file. Each Epic will follow a similar format, ensuring that all relevant details are captured and prioritized effectively. If you need more specific details or additional Epics, User Stories, and Subtasks, please let me know!
