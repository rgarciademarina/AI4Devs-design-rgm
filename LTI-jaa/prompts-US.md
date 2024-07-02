# Prompts

## 1. User Story
```markdown
I want you to act as an the best Product Owner for LTI company, LTI (Leaders Technology Impact) is a start-up company dedicated to digitalise and automate the recruitement processes, helping other companies attract and hire the best talent with less effort; LTI wants to implement a new ATS software (Applicant-Tracking System) to manage one of its core businnes area; LTI hsd a PRD already created with the main features and the description of the project (I'm going to attach a file with this information). Given the PRD I want you to create a list of ten most important user stories.
---
Template to Create the User Stories:

Title: [Short descriptive title]

***As a [role], I want to [action], so that [benefit].***

Acceptance Criteria:
- [First acceptance criterion]
- [Second acceptance criterion]
- [Third acceptance criterion]

Priority: [High/Medium/Low]

Story Points: [Estimate]

Description:
[Additional details or context]
```

```
I want you to add User Stories related to the AI, please take a look into the PRD, and look for the topic "Automation and AI Assistance in an ATS", and generate the best two user stories about that; recreate the list again, and replace the two worse stories with the new ones.
```

```
What methodology did you use to prioritize the user stories ?
```

```
Create Product backlog and create a markdown table, please use the following Prioritization Criteria this time:  ---
1. Impact on the user and business value
2. Urgency based on market trends and user feedback
3. Complexity and estimated implementation effort
4. Risks and dependencies between tasks
```

```
I want you to act as the an expert project manager ATS project. The team is going to start implementing the ATS system, it has been considered doing two week sprints (10 working days of 8 hours each day), and the kink-off meeting is going to begin the next Monday. 

I want you to consider the Product backlog table already generated with the user stories and their priorities to generate a new table with all the working tickets or tasks necessary to complete the work in the backlog.

Please separate the tickets by sprints and ordered by top priority to less. Since that the team Speeds per sprint is unknown, and we are going to start from scratch, I also want you to add a estimated time using a suitable average estimation method to calculate this estimation, that would take the team to complete the  product backlog in next months, explain step by step like an Schedule with deadlines; 

To maximize the value of each sprint, it is essential to prioritize the user stories that provide the most value, starting with those stories at the top of the list.

We assume that there won't changes to the backlog items and that the team will work only on those tasks in the following months.

I want you to take the following template to create the tickets or tasks:
---
Title: [Job Ticket Title]
Description: [Technical description of the job ticket]
Criteria of acceptance:
- [Acceptance criterion_1],
- [Acceptance criterion_2]
Priority: [High/Medium/Low]
Estimate: [Story Points]
Assigned to: [Backend Team/Frontend Team/DevOps Team/Designer Team]
Tags: [Security/Backend/Sprint_##]
User Stories Links: [Story_N]
```

```
Please add the following adjusments: ### 1- The dates, asume that we are going to begin the next 01-July-2024. 2-Links, the tasks with User Stories asociated. 3- Number of Sprint is only 8. 4- Consider the following resources for this project: 3 backend developers, 3 frontend developers, 2 designers, 1 team leader, 1 devops engineer and 1 project manager.
```

```
Looks like designers, devops, team leader and project manager don't have tasks we need to add tasks for them. Please add a summary with the total of points per recources. I want you to re-estimate the points per sprint consider the following resources Backend Developers: 3
Frontend Developers: 3, Designers: 2, Team Leader: 1, DevOps Engineer: 1, Project Manager: 1
```

```
The summary is better, please re-generate the sprint plan with tasks breakdown, be precise with this list of tasks because it should match with the amount of points per team, and the amount of points per sprint. I want you to take the following template to create the user tasks:
---
Title: [Job Ticket Title]
Description: [Technical description of the job ticket]
Criteria of acceptance:
- [Acceptance criterion_1],
- [Acceptance criterion_2]
Priority: [High/Medium/Low]
Estimate: [Story Points]
Assigned to: [Backend Team/Frontend Team/DevOps Team/Designer Team]
Tags: [Security/Backend/Sprint_##]
User Stories Links: [Story_N]
```