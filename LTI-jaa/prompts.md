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
