# Prompts

## 1. Investigation, Analysis of requirements 

<< **Investigation** >>
```markdown
I want you to act as an expert product manager for LTI company, LTI (LeadersTechnology Impact) is a start-up company dedicated to digitalise and automate the recruitement processes, helping other companies attract and hire the best talent with less effort; LTI needs to create the best ATS software (Applicant-Tracking System) to manage one of its core businnes area . 

The company doesn't have anything already designed nor implemented, so we need to know which are the most important features in order to design the software. Please ensure the list of this features are order by priority, and be sure you enumerate  features that help LTI be the best the company in the sector over the competitors, so I need you to answer the following questions to create a adequeted analysis of the market:

---
What basic functionalities does an ATS have?
Describe them to me in a list, ordered from highest to lowest priority
What benefits could LTI gain from using an ATS when considering its use?
Could efficiency be increased or not for HR departments?
What alternatives do you have to using an ATS and when might they be relevant?
What is the normal customer journey of a customer using an ATS? Describe to me step by step all the interactions.
What do you say about the improvement in real-time collaboration between recruiters and managers?
I need to make automations and have AI assistance in various tasks, is this possible? If possible, prepare the answer.
```

<< **Summary and Lean** >>
```markdown
Thanks for the investigation, now I want you to sumarize all the processes and features that your answer about an ATS for LTI, remember that I want you to design this ATS to be the best HR company in the market, so please be carefully in the analysis, create the following:
---
1. Brief description of ATS software for LTI, remark the added value and competitive advantages.
2. Explain the main functions of the ATS. 
3. Add a Lean Canvas diagram to understand the business model
```

<< **Buy vs Build** >>
```markdown
I need you to study the alternatives again, and give an elaborate justification to select one of the following strategies: buy vs build.
---
Please let me know which open source ATS are best known?
Which commercial ATS are best known? Compare them based on the main functionalities in AI automations and assess which would be the best option.
```

## 2. Use Cases

```markdown
Now I want you to act as an expert software analyst. The company is going to build the ATS instead of buying because the company wants to create a tailored ATS, we need you to create this ATS. Please list and briefly describes the most important three use cases to implement to achieve the main functionalities. I want you to create a mermaid diagram aside of each use case as well.
```

Try again because the mermaid diagram was bad
```markdown
This is an incorrect format or sintax to create diagrams in mermaid. Please try again generating the use cases for PlantsUML 
```
## 3. ERD - Data model diagram

```markdown
I want you to act as a brilliant software architect. You are able to design, explain and diagram the different aspects of the ATS software that we want to implement. 
You need to take a look and analyze the following use cases already created for an ATS software and identify all the entities needed to create the software and to manage all the use cases.

You need to identify the most important fields of the enities with their field names and data types; and you need to create the relationships between entities as well specifying the kind of relation.

Finally, you need to create a data model diagram with all the entities, fields and relationshipts already identitied, please create the diagram in using mermaid script.

### 

Use Case 1: Job Posting and Distribution

**Description:** This use case involves creating job postings within the ATS and distributing them to various job boards and social media platforms. The goal is to streamline the process of advertising job openings to attract a large pool of qualified candidates.

**Steps:**
1. **Create Job Posting:** HR manager creates a job posting by filling out a form with job details (title, description, requirements, etc.).
2. **Approve Job Posting:** The job posting is reviewed and approved by a senior HR manager.
3. **Distribute Job Posting:** The approved job posting is automatically distributed to selected job boards and social media platforms.
4. **Monitor and Update:** HR manager monitors the posting's performance and updates the job details if necessary.

Use Case 2: Resume Parsing and Candidate Management

**Description:** This use case involves parsing resumes submitted by candidates, extracting relevant information, and managing candidate profiles within the ATS. The objective is to organize candidate data efficiently and make it easily searchable.

**Steps:**
1. **Receive Resume:** Candidates submit their resumes through the ATS.
2. **Parse Resume:** The ATS parses the resume to extract relevant information (name, contact details, experience, skills).
3. **Create Candidate Profile:** The extracted information is used to create a candidate profile in the ATS.
4. **Manage Candidate Profile:** Recruiters can view, update, and search candidate profiles.

Use Case 3: Interview Scheduling and Management

**Description:** This use case involves scheduling interviews between candidates and interviewers, sending notifications, and managing interview feedback. The goal is to automate the interview scheduling process and streamline feedback collection.

**Steps:**
1. **Schedule Interview:** Recruiter selects a candidate and schedules an interview by choosing available time slots.
2. **Notify Participants:** The ATS sends notifications to the candidate and interviewers with the interview details.
3. **Conduct Interview:** The interview is conducted as scheduled.
4. **Collect Feedback:** Interviewers submit their feedback through the ATS.
5. **Update Candidate Status:** The ATS updates the candidate's status based on the feedback.
```

<<< **GPT - ERASER - DIAGRAMGPT** >>>
I repited the prompt using this GPT.

<<< **GPT - ChatGPT** >>>
I wanted to refine and improve the data model because looks a bit basic:

```markdown
Please give a try again, I want you to take the image attached and organize in a better way the fields and tables and relationships as well. Please add the explanation of every object
```
![image](https://github.com/eltonina/AI4Devs-design/assets/23495050/50a81cb9-ed90-49e7-a60c-c6e079498ba7)

## 4. High level arquitecture 

I use here as GPT Eraser -  DiagramGPT.

```markdown
I need you create a microservices architecture for an ongoing ATS system like Lever, Greenhouse or OpenCATS.
I'm adding a datamodel and some use cases for a better understanding of the architecture.
Each microservices should have its own database.
It also has a frontend that communicates through API.
Cloud provider is AWS, use proper services to improve security, include load balancing and CDN.
---
Use cases:
Use Case 1: Job Posting and Distribution
Description: This use case involves creating job postings within the ATS and distributing them to various job boards and social media platforms. The goal is to streamline the process of advertising job openings to attract a large pool of qualified candidates.

Steps:
1. Create Job Posting: HR manager creates a job posting by filling out a form with job details (title, description, requirements, etc.).
2. Approve Job Posting: The job posting is reviewed and approved by a senior HR manager.
3. Distribute Job Posting: The approved job posting is automatically distributed to selected job boards and social media platforms.
4. Monitor and Update: HR manager monitors the posting's performance and updates the job details if necessary.

Use Case 2: Resume Parsing and Candidate Management
Description: This use case involves parsing resumes submitted by candidates, extracting relevant information, and managing candidate profiles within the ATS. The objective is to organize candidate data efficiently and make it easily searchable.

Steps:
1. Receive Resume: Candidates submit their resumes through the ATS.
2. Parse Resume: The ATS parses the resume to extract relevant information (name, contact details, experience, skills).
3. Create Candidate Profile: The extracted information is used to create a candidate profile in the ATS.
4. Manage Candidate Profile: Recruiters can view, update, and search candidate profiles.

Use Case 3: Interview Scheduling and Management
Description: This use case involves scheduling interviews between candidates and interviewers, sending notifications, and managing interview feedback. The goal is to automate the interview scheduling process and streamline feedback collection.

Steps:
1. Schedule Interview: Recruiter selects a candidate and schedules an interview by choosing available time slots.
2. Notify Participants: The ATS sends notifications to the candidate and interviewers with the interview details.
3. Conduct Interview: The interview is conducted as scheduled.
4. Collect Feedback: Interviewers submit their feedback through the ATS.
5. Update Candidate Status: The ATS updates the candidate's status based on the feedback.
--- 
Data model diagram
Job Posting
Description: Represents a job opening created by the HR team. It includes details about the job such as title, description, and requirements.
Fields:
id (Primary Key, Integer): Unique identifier for the job posting.
title (String): The title of the job position.
description (Text): A detailed description of the job.
requirements (Text): The qualifications and skills required for the job.
status (String, e.g., Draft, Approved): The current status of the job posting.
created_at (DateTime): Timestamp when the job posting was created.
updated_at (DateTime): Timestamp when the job posting was last updated.
hr_manager_id (Foreign Key to HR Manager, Integer): ID of the HR manager who created the job posting.
senior_hr_manager_id (Foreign Key to Senior HR Manager, Integer): ID of the senior HR manager who approved the job posting.
Relationships:
One-to-Many with Job Distribution
Many-to-One with HR Manager
Many-to-One with Senior HR Manager

Job Distribution
Description: Manages the distribution of job postings to various platforms like job boards and social media platforms.
Fields:
id (Primary Key, Integer): Unique identifier for the job distribution.
job_id (Foreign Key to Job Posting, Integer): ID of the job posting.
platform_id (Foreign Key to Platform, Integer): ID of the platform (job board or social media) where the job is posted.
status (String, e.g., Pending, Published): The current status of the job distribution.
Relationships:
Many-to-One with Job Posting
Many-to-One with Platform (Job Boards and Social Media Platforms)

Candidate
Description: Represents a candidate applying for a job. It includes personal information and resume details.
Fields:
id (Primary Key, Integer): Unique identifier for the candidate.
name (String): The name of the candidate.
email (String): The email address of the candidate.
phone (String): The phone number of the candidate.
resume_text (Text): The resume of the candidate in text format.
parsed_data (Text, JSON structure for parsed resume data): Structured data extracted from the resume.
status (String, e.g., New, In Review, Hired): The current status of the candidate.
created_at (DateTime): Timestamp when the candidate profile was created.
updated_at (DateTime): Timestamp when the candidate profile was last updated.
Relationships:
One-to-Many with Interview

Interview
Description: Represents an interview scheduled between a candidate and an interviewer. It includes details about the interview.
Fields:
id (Primary Key, Integer): Unique identifier for the interview.
candidate_id (Foreign Key to Candidate, Integer): ID of the candidate being interviewed.
recruiter_id (Foreign Key to Recruiter, Integer): ID of the recruiter who scheduled the interview.
scheduled_time (DateTime): The scheduled date and time for the interview.
interviewer_id (Foreign Key to Interviewer, Integer): ID of the interviewer conducting the interview.
status (String, e.g., Scheduled, Completed): The current status of the interview.
created_at (DateTime): Timestamp when the interview was created.
updated_at (DateTime): Timestamp when the interview was last updated.
Relationships:
Many-to-One with Candidate
Many-to-One with Recruiter
Many-to-One with Interviewer
One-to-One with Interview Feedback

Interview Feedback
Description: Contains feedback provided by the interviewer after an interview.
Fields:
id (Primary Key, Integer): Unique identifier for the interview feedback.
interview_id (Foreign Key to Interview, Integer): ID of the interview.
feedback_text (Text): The feedback text provided by the interviewer.
rating (Integer): Rating given by the interviewer.
Relationships:
One-to-One with Interview

HR Manager
Description: Represents an HR manager responsible for creating and approving job postings.
Fields:
id (Primary Key, Integer): Unique identifier for the HR manager.
name (String): The name of the HR manager.
email (String): The email address of the HR manager.
Relationships:
One-to-Many with Job Posting

Recruiter
Description: Represents a recruiter responsible for managing candidate profiles and scheduling interviews.
Fields:
id (Primary Key, Integer): Unique identifier for the recruiter.
name (String): The name of the recruiter.
email (String): The email address of the recruiter.
Relationships:
One-to-Many with Interview

Interviewer
Description: Represents an interviewer responsible for conducting interviews and providing feedback.
Fields:
id (Primary Key, Integer): Unique identifier for the interviewer.
name (String): The name of the interviewer.
email (String): The email address of the interviewer.
Relationships:
One-to-Many with Interview

Job Board
Description: Represents a job board where job postings can be distributed.
Fields:
id (Primary Key, Integer): Unique identifier for the job board.
name (String): The name of the job board.
url (String): The URL of the job board.
Relationships:
Many-to-One with Job Distribution

Social Media Platform
Description: Represents a social media platform where job postings can be shared.
Fields:
id (Primary Key, Integer): Unique identifier for the social media platform.
name (String): The name of the social media platform.
url (String): The URL of the social media platform.
Relationships:
Many-to-One with Job Distribution
```

At this point coming back to chatGPT
```markdown
I want you to analyze the following AWS cloud arquitecture attached in a file, please explain and elaborate the techincal documentation about it related to this ATS system. Please elaborate a Clean Hexagonal Architecture solution for it, I-d like you desigh it for AspNetCore. remember this is a High Level documentation, for now avoid going deeper in details but only in the Architecture level designing all layers aka. folders need for the solution of this systems.
```
![image](https://github.com/eltonina/AI4Devs-design/assets/23495050/141caf85-7a1c-477e-b6f1-164a76f3249b)


```markdown
Please elaborate more on the High-Level Architecture Design topic, you only created one sample for Job Posting Service, I need you to include all the services. Please explain any detail related to any external dependency like using rabbit for asyncronous communications, Email and Sms libraries for the notification service, etc.
```
## 5. C4 diagram

Using ChatGPT

```markdown
Please add a diagram C4, create it a mermaid format using lates mermaid version to avoid issues; please go deeper on the four levels in the "Job Posting Service", use the command CreateJobPostingCommand to create a set of Levels for this service for C1 to C4. Please organize all the diagram in sequence and create an index
```
