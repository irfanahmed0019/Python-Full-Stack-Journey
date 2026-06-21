# Day 08 - Backend Fundamentals (Express.js)

## Overview

Today I started learning how the backend works and how websites communicate with servers.

Until now, I focused on:

- HTML
- CSS
- JavaScript
- DOM Manipulation

Today I learned what happens behind the scenes when a website requests data.

---

# What is a Backend?

Frontend = What users see.

Backend = Logic running behind the scenes.

Example:

User clicks a button.

↓

Frontend sends a request.

↓

Backend processes the request.

↓

Backend sends a response.

↓

Frontend displays the result.

---

# What is a Server?

A server is a program that waits for requests and sends responses.

Example:

Browser:

"Give me events."

↓

Server receives request.

↓

Server sends event data.

The server keeps running and waits for new requests.

---

# What are Ports?

Ports are communication doors used by applications.

Example:

- Port 80 → HTTP
- Port 443 → HTTPS
- Port 3000 → Express Development Server
- Port 5500 → VS Code Live Server

A computer can run multiple applications at the same time because each application uses a different port.

Example:

Frontend → localhost:5500

Backend → localhost:3000

---

# DNS vs Ports

DNS answers:

"Which computer should I talk to?"

Example:

google.com

↓

142.x.x.x

Port answers:

"Which application on that computer should I talk to?"

Example:

142.x.x.x:443

↓

HTTPS Website

Easy Memory:

DNS = Computer

Port = Application

---

# What is Express?

Express is a Node.js framework used to build backend applications and APIs.

Install:

```bash
npm install express
```

Import:

```javascript
const express = require("express");
```

Create application:

```javascript
const app = express();
```

---

# My First Express Server

```javascript
const express = require("express");

const app = express();

app.get("/", (req, res) => {
    res.send("ARCHERS Backend Running");
});

app.listen(3000, () => {
    console.log("Server running on port 3000");
});
```

---

# Understanding app.get()

```javascript
app.get("/", (req, res) => {
    res.send("ARCHERS Backend Running");
});
```

This creates a route.

When someone visits:

```text
localhost:3000
```

The server executes the code inside the route.

---

# Understanding req and res

```javascript
(req, res)
```

req = Request

Contains information coming from the browser.

res = Response

Used to send data back to the browser.

Flow:

Browser

↓

Request

↓

Backend

↓

Response

↓

Browser

---

# What is JSON?

JSON (JavaScript Object Notation) is a format used to exchange data.

Example:

```json
{
    "name": "Irfan",
    "role": "Student"
}
```

JSON is commonly used between frontend and backend.

---

# Creating My First API

```javascript
app.get("/events", (req, res) => {
    res.json([
        {
            name: "Mini Militia Tournament"
        },
        {
            name: "Web Development Workshop"
        }
    ]);
});
```

Visiting:

```text
localhost:3000/events
```

returns:

```json
[
    {
        "name": "Mini Militia Tournament"
    },
    {
        "name": "Web Development Workshop"
    }
]
```

---

# Why Use an Array?

An array allows multiple items to be returned.

Example:

```javascript
[
    {
        name: "Event 1"
    },
    {
        name: "Event 2"
    }
]
```

This is useful because websites often display many events, members, or workshops.

---

# Why Not Store Everything in HTML?

For small websites, data can be written directly in HTML.

However, larger applications require:

- Dynamic content
- User accounts
- Databases
- Forms
- Authentication

Backend allows data to be managed centrally.

Example:

Frontend

↓

fetch("/events")

↓

Backend

↓

Database

---

# Frontend and Backend Connection

HTML:

```html
<div id="events"></div>
```

This is an empty container.

JavaScript will later insert data into it.

---

# Fetch API

```javascript
fetch("http://localhost:3000/events")
```

This sends a request to the backend.

Flow:

Browser

↓

GET /events

↓

Backend

↓

JSON Response

↓

Browser

---

# Understanding response.json()

```javascript
.then(response => response.json())
```

The backend returns JSON.

response.json() converts it into JavaScript objects and arrays.

Before:

```text
Raw JSON Data
```

After:

```javascript
[
    {
        name: "Mini Militia Tournament"
    }
]
```

Now JavaScript can work with the data.

---

# Understanding forEach()

```javascript
events.forEach(event => {
});
```

Loops through every event one by one.

Example:

Event 1

↓

Event 2

↓

Event 3

This allows dynamic content creation.

---

# DOM Manipulation with Backend Data

```javascript
eventDiv.innerHTML += `
<h2>${event.name}</h2>
`;
```

Creates HTML using backend data.

Example:

Backend sends:

```json
{
    "name": "Mini Militia Tournament"
}
```

JavaScript creates:

```html
<h2>Mini Militia Tournament</h2>
```

and inserts it into the page.

---

# Full Request Flow

User clicks button

↓

JavaScript fetch()

↓

Backend API

↓

JSON Response

↓

JavaScript

↓

DOM Manipulation

↓

HTML Generated

↓

Content Visible

---

# Biggest Lesson

A website is not just HTML, CSS, and JavaScript.

Modern web applications work like this:

Frontend

↓

Request

↓

Backend

↓

Response

↓

Frontend

Understanding this flow is the foundation of Full Stack Development.

---

## Progress

✅ Learned Express

✅ Created First Server

✅ Understood Routes

✅ Learned req and res

✅ Learned JSON

✅ Created First API

✅ Understood Fetch API

✅ Connected Backend Concepts with DOM Manipulation

🔥 Day 09: Forms, POST Requests, and Sending Data to the Backend