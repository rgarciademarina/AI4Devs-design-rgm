# User Story: Create and Post Job Openings

## Title
As a recruiter, I can create and post job openings

## Description
As a recruiter using the ATS, I need to be able to create new job openings and post them to our career portal so that we can attract potential candidates for our open positions.

## Acceptance Criteria

1. The system provides a "Create New Job" button on the recruiter's dashboard.
2. Clicking the button opens a form with fields for all necessary job details.
3. The form includes the following fields:
   - Job Title (required, text, max 100 characters)
   - Department (required, dropdown, list populated from company structure)
   - Location (required, text with autocomplete for known company locations)
   - Job Type (required, dropdown: Full-time, Part-time, Contract, Internship)
   - Experience Level (required, dropdown: Entry, Mid-Level, Senior, Executive)
   - Salary Range (optional, two numeric fields for minimum and maximum)
   - Job Description (required, rich text editor, min 100 characters)
   - Requirements (required, rich text editor, min 50 characters)
   - Responsibilities (required, rich text editor, min 50 characters)
   - Benefits (optional, rich text editor)
   - Application Deadline (optional, date picker)
4. The form has a "Preview" button that shows how the job posting will appear to candidates.
5. The form has a "Save as Draft" button that saves the current state without posting.
6. The form has a "Post Job" button that publishes the job opening.
7. Before posting, the system performs validation on all required fields and data formats.
8. If validation fails, the system highlights the problematic fields and provides error messages.
9. Upon successful posting, the system:
   - Displays a success message with the job ID
   - Adds the job to the list of active job openings
   - Makes the job visible on the company's career portal
   - Generates a shareable link for the job posting
10. The recruiter can edit the job posting after it's been published.
11. Editing a published job adds a "Last Updated" timestamp to the posting.
12. The recruiter can deactivate (unpublish) a job posting.
13. The system logs all actions (create, edit, publish, unpublish) with timestamps and user info.

## Additional Details

- The rich text editor should support basic formatting (bold, italic, bullet points, numbered lists).
- The system should automatically generate SEO-friendly URLs for job postings.
- The form should auto-save every 2 minutes to prevent data loss.
- The system should support creation of job posting templates for frequently used job types.

## UI/UX Considerations

- The form should be responsive and work well on both desktop and mobile devices.
- Use clear labels and help text for each field to guide the recruiter.
- Implement a progress indicator to show completion status of the job posting form.
- Use color coding to distinguish between published, draft, and closed job postings in the job list.

## Technical Considerations

- Implement CSRF protection for the job posting form.
- Use server-side validation in addition to client-side validation for security.
- Ensure the rich text editor sanitizes input to prevent XSS attacks.
- Implement rate limiting to prevent abuse of the job posting feature.
- Use database transactions to ensure data integrity when saving job postings.

## Testing Criteria

- Unit tests for all form validation rules
- Integration tests for the job posting workflow
- UI tests for form interactions and responsiveness
- Performance tests to ensure quick load times for the job list with 1000+ postings
- Security tests for XSS vulnerabilities and CSRF protection

## Definition of Done

- All acceptance criteria have been met
- Code has been reviewed and approved by at least one other developer
- All tests are passing
- Documentation for the job posting feature has been updated
- The feature has been demo'd to and approved by the product owner
