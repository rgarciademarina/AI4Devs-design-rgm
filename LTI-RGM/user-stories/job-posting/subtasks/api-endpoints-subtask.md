# Subtask: Create API endpoints for job posting CRUD operations

## Description
Implement RESTful API endpoints to handle Create, Read, Update, and Delete (CRUD) operations for job postings. These endpoints will be used by the frontend to interact with the job posting data.

## Steps
1. Set up the API structure
   - Create a new module or file for job posting related endpoints
   - Set up necessary imports and configurations

2. Implement the following endpoints:

   a. Create Job Posting
   - Method: POST
   - Path: /api/job-postings
   - Request body: JSON containing all job posting fields
   - Response: Created job posting object with 201 status code

   b. Get All Job Postings (with filtering and pagination)
   - Method: GET
   - Path: /api/job-postings
   - Query parameters: status, department, location, job_type, experience_level, page, limit
   - Response: Array of job posting objects and metadata (total count, page info)

   c. Get Single Job Posting
   - Method: GET
   - Path: /api/job-postings/{id}
   - Response: Single job posting object

   d. Update Job Posting
   - Method: PUT
   - Path: /api/job-postings/{id}
   - Request body: JSON containing fields to update
   - Response: Updated job posting object

   e. Delete Job Posting
   - Method: DELETE
   - Path: /api/job-postings/{id}
   - Response: Success message with 200 status code

   f. Publish Job Posting
   - Method: POST
   - Path: /api/job-postings/{id}/publish
   - Response: Updated job posting object with status changed to 'Published'

   g. Unpublish Job Posting
   - Method: POST
   - Path: /api/job-postings/{id}/unpublish
   - Response: Updated job posting object with status changed to 'Closed'

3. Implement input validation
   - Validate all input data before processing
   - Return appropriate error messages for invalid inputs

4. Implement error handling
   - Create custom error handlers for common scenarios (e.g., not found, unauthorized)
   - Ensure all endpoints return appropriate status codes and error messages

5. Implement authentication and authorization
   - Ensure all endpoints (except public reads) require authentication
   - Implement role-based access control (e.g., only recruiters can create/update job postings)

6. Implement logging
   - Log all API calls with relevant details (user, action, timestamp)

7. Optimize query performance
   - Implement efficient database queries, especially for the list endpoint
   - Use pagination to limit the amount of data returned in a single request

8. Implement rate limiting
   - Set up rate limiting to prevent abuse of the API

9. Create API documentation
   - Use a tool like Swagger to create comprehensive API documentation

## Acceptance Criteria
- All CRUD operations are implemented and working correctly
- Endpoints are RESTful and follow API best practices
- Input validation is in place and working correctly
- Error handling is implemented and returns appropriate status codes and messages
- Authentication and authorization are implemented and working correctly
- Logging is in place for all API calls
- Queries are optimized and performant
- Rate limiting is implemented
- API documentation is created and accurate

## Notes
- Ensure all endpoints are thoroughly tested, including edge cases
- Consider implementing a versioning strategy for the API
- Discuss with the frontend team to ensure the API meets their requirements
- Consider implementing GraphQL alongside REST if complex, nested queries are needed
