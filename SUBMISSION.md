# Phase 1 submission
Name: Zainab Kelani
Course or section: INEW-2434 - Advanced Web Programming
Chosen track: Python FastAPI

## My campus idea
My Campus Idea Board is a web-based application that allows students to submit and view ideas for improving campus life, such as creating student clubs, study groups, and environmental projects.

## Evidence log

1. Personalized GET /api/hello:
   Method: GET
   URL: http://127.0.0.1:8000/api/hello
   Status: 200 OK
   Response: {"message": "Hello Zainab! Welcome to the Campus Idea Board!"}

2. GET /api/ideas before creating:
   Method: GET
   URL: http://127.0.0.1:8000/api/ideas
   Status: 200 OK
   Response: Two existing campus ideas were returned.

3. Valid POST /api/ideas:
   Method: POST
   URL: http://127.0.0.1:8000/api/ideas
   Status: 201 Created
   Response: {"id": 3, "title": "Start a robotics club", "category": "clubs"}

4. GET /api/ideas after creating:
   Method: GET
   Status: 200 OK
   Response: Three ideas were returned, including the new robotics club idea.

5. Blank title POST:
   Method: POST
   Status: 400 Bad Request
   Response: {"message": "Invalid request"}
   The invalid idea was not added.

6. Malformed JSON POST:
   Method: POST
   Status: 400 Bad Request
   Response: {"message": "Invalid request"}
   The invalid idea was not added.

7. Restart the server and GET /api/ideas:

   Method: GET

   URL: http://127.0.0.1:8000/api/ideas

   Status: 200 OK

   Response: After restarting the FastAPI server, the API returned only the two original ideas: "Start a coding club" and "Create a campus garden." The previously created robotics club idea was no longer present. This confirmed that the application stores data temporarily in memory and resets when the server restarts.

## Reflection

1. What does a controller do?
   A controller handles incoming API requests, processes the request by calling the appropriate application logic, and returns a response to the client. In my FastAPI project, the route functions in main.py perform this role.

2. How is GET different from POST?
   GET retrieves information from the server without creating new data, while POST sends data to the server to create a new resource. I used GET to retrieve campus ideas and POST to create a new idea.

3. How do JSON title and category become Java data?
   In Java Spring Boot, JSON fields are converted into Java object properties through deserialization. Since I chose Python FastAPI, Pydantic validates the incoming JSON and converts the title and category fields into attributes of an IdeaRequest model.

4. Why does our added idea disappear after restarting?
   The application stores ideas temporarily in memory instead of using a database. When the server process restarts, the temporary data is lost and the original sample ideas are loaded again.

5. What would the React frontend need to know to use this API?
   The React frontend needs to know the API base URL, the available endpoints, the GET and POST methods, the expected JSON fields such as title and category, and how to handle success and error responses.


## Debugging story

Symptom: While testing my API in Postman, I initially had trouble loading the response from my local server.

Hypothesis: I suspected that the FastAPI server was not running correctly or that Postman was using an incorrect request URL.

Change: I checked the server in the VS Code terminal and verified that Postman was using the correct URL and HTTP method.

Observed result: I successfully received a 200 OK response for GET /api/hello and GET /api/ideas, and a 201 Created response when I submitted a valid POST request. I also confirmed that invalid POST requests returned 400 Bad Request.

## Assistance disclosure

I used ChatGPT as a learning assistant while completing this assignment. It helped me understand how to set up my Python FastAPI environment, implement GET and POST endpoints, troubleshoot indentation errors, write automated tests, and test API requests using Postman.

I followed the instructions in VS Code, ran the application, tested the endpoints, reviewed the results, and corrected errors as they occurred.

## Automated test evidence

**Command used:**
`python -m pytest -v`

**Test results:**
- Total tests: 5
- Passed: 5
- Failed: 0
- Skipped: 0
- Warnings: 1

All five automated tests passed successfully. The tests verified that the greeting endpoint worked, the API returned the original campus ideas, valid POST requests created new ideas, the store saved the correct title and category, and newly created ideas received unique IDs.

The warning was related to a deprecated dependency feature and did not prevent the tests from passing.
**Two completed unit tests:**

1. `test_adding_idea_stores_title_and_category` — Verifies that a new idea is stored with the correct title and category. It also checks that the idea appears in the stored list.

2. `test_two_new_ideas_receive_different_ids` — Verifies that two newly created ideas receive different IDs, ensuring each idea can be uniquely identified.

**Completed POST API test:**

The POST API test verifies that submitting a valid idea to `/api/ideas` creates a new idea and returns the expected response. In Postman, I confirmed that the API returned `201 Created` with the new idea's ID, title, and category.

**Difference between unit tests and Postman requests:**

Unit tests automatically check individual functions or components to verify that they behave correctly. Postman requests test how the API responds to HTTP requests, including status codes and JSON responses. Both help identify errors, but unit tests are especially useful for repeatedly checking application logic.

**Required test confirmation:**

I ran `python -m pytest -v` in the VS Code terminal. All five tests passed, with zero failures and one dependency warning. No tests were reported as skipped or disabled.
