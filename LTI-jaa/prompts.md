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

You need to take a look and analyze the three main use cases already created for our ATS software identify all the important entities needed to create the software and to manage all the use cases.

You need to identify the most important fields of the enities with their field names and data types; and you need to create the relationships between entities as well specifying the kind of relation.

Finally, you need to create a data model diagram with all the entities, fields and relationshipts already identitied, please create the diagram in using mermaid script.
```
The ERD mermaid diagram was with bad sintaxis, and it needed to be re-gneerated using eraser

<< **GPT: ERASER - DIAGRAMGPT** >>
```markdown
Create an ERD with Job Posting (JobID, Title, Description, Requirements, Status, Dates) related to Candidate (CandidateID, Name, Email, Phone, Address, Resume, Skills, Experience, Education) in a Many-to-Many relationship. Also include Interview (InterviewID, CandidateID, JobID, Date, Interviewer, Type, Feedback) with relationships to Candidate and Job Posting.
```
