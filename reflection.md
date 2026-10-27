# Module 3 Phase 2 Reflection

## 1. How does a request travel from React to the backend?

When I open my React application, it sends a GET request to my FastAPI backend to retrieve the campus ideas. The backend processes the request and returns the ideas as JSON. React then displays the ideas on the page.

When I submit a new idea, React sends a POST request containing the title and category. The backend validates the information, stores the new idea, and sends a response back to React. The frontend then updates the list to display the new idea.

## 2. What is the difference between props and state in React?

Props are used to pass information from one component to another. State is used to store information that can change while the application is running.

In my project, state helps manage the list of ideas, form inputs, and messages displayed to the user.

## 3. What is the difference between frontend and backend validation?

Frontend validation checks the information before it is sent to the backend. For example, my React form displays an error when I try to submit an empty title.

Backend validation checks the request again to make sure the data is valid. I tested this using Postman and confirmed that an invalid request returned HTTP 400 Bad Request.

Both are important because frontend validation improves the user experience, while backend validation protects the API from invalid requests.

## 4. Describe one bug you encountered and how you fixed it.

One issue I encountered was an ECONNREFUSED error when I tried to send requests through Postman. I discovered that my backend server was not running.

I fixed the issue by installing the required Python dependencies and starting the FastAPI server again. After that, I was able to connect to the API and test my requests successfully.

## 5. What happens when you refresh the browser compared to restarting the backend?

When I refresh the browser, React loads again and retrieves the current list of ideas from the backend. Any ideas stored in the running backend are still available.

When I restart the backend, the ideas added during the previous session disappear because the application uses temporary in-memory storage. The original seed ideas are loaded again.

## Conclusion

This assignment helped me understand how a React frontend communicates with a REST API. I learned how to retrieve data using GET requests, create new data using POST requests, handle invalid input, and troubleshoot connection errors. I also practiced testing my application using Postman and Chrome Developer Tools.