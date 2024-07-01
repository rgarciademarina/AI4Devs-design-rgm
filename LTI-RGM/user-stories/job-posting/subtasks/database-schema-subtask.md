# Subtask: Set up database schema for job postings

## Description
Create the necessary database schema to store all information related to job postings. This schema should accommodate all fields specified in the user story and allow for efficient querying and indexing.

## Steps
1. Design the database schema
   - Create a `job_postings` table with the following fields:
     * id (Primary Key, UUID)
     * title (VARCHAR(100), NOT NULL)
     * department (VARCHAR(50), NOT NULL)
     * location (VARCHAR(100), NOT NULL)
     * job_type (ENUM('Full-time', 'Part-time', 'Contract', 'Internship'), NOT NULL)
     * experience_level (ENUM('Entry', 'Mid-Level', 'Senior', 'Executive'), NOT NULL)
     * salary_min (DECIMAL(10,2), NULL)
     * salary_max (DECIMAL(10,2), NULL)
     * description (TEXT, NOT NULL)
     * requirements (TEXT, NOT NULL)
     * responsibilities (TEXT, NOT NULL)
     * benefits (TEXT, NULL)
     * application_deadline (DATE, NULL)
     * status (ENUM('Draft', 'Published', 'Closed'), NOT NULL, DEFAULT 'Draft')
     * created_at (TIMESTAMP, NOT NULL, DEFAULT CURRENT_TIMESTAMP)
     * updated_at (TIMESTAMP, NOT NULL, DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP)
     * created_by (UUID, NOT NULL, FOREIGN KEY referencing users table)
     * last_updated_by (UUID, NOT NULL, FOREIGN KEY referencing users table)

2. Create indexes
   - Add indexes on frequently queried fields:
     * CREATE INDEX idx_job_status ON job_postings(status);
     * CREATE INDEX idx_job_department ON job_postings(department);
     * CREATE INDEX idx_job_location ON job_postings(location);
     * CREATE INDEX idx_job_type ON job_postings(job_type);
     * CREATE INDEX idx_job_experience ON job_postings(experience_level);

3. Set up constraints
   - Add a check constraint to ensure salary_min is less than or equal to salary_max
   - Add a check constraint to ensure application_deadline is in the future

4. Create a separate table for job posting revisions
   - Create a `job_posting_revisions` table to store historical changes:
     * id (Primary Key, UUID)
     * job_posting_id (UUID, NOT NULL, FOREIGN KEY referencing job_postings table)
     * revision_data (JSON, NOT NULL) // Stores the entire job posting data at the time of revision
     * created_at (TIMESTAMP, NOT NULL, DEFAULT CURRENT_TIMESTAMP)
     * created_by (UUID, NOT NULL, FOREIGN KEY referencing users table)

5. Set up triggers
   - Create a trigger to add a new record to `job_posting_revisions` whenever a job posting is updated

6. Implement the schema
   - Write and test the SQL scripts to create the tables, indexes, constraints, and triggers
   - Set up a migration script to apply these changes to the database

7. Update ORM models
   - Update the ORM (e.g., Prisma) models to reflect the new schema

## Acceptance Criteria
- The database schema is implemented and can store all required job posting information
- Indexes are in place for efficient querying
- Constraints are implemented to ensure data integrity
- The revision history system is in place and functioning correctly
- ORM models are updated and working correctly with the new schema
- Migration scripts are created and tested

## Notes
- Ensure the schema is optimized for read operations, as job listings will be frequently queried
- Consider partitioning the `job_postings` table by status or date if expecting a very large number of postings
- Discuss with the team if any additional fields or tables (e.g., for tagging or categorization) are needed
