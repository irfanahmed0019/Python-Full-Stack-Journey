# 🚀 Day 10 – From Static Website to API-Driven Website

## Project
ARCHERS – Association of Computer Science & Technology Students

---

## 🎯 Goal

Until now, all content on the website was hardcoded directly inside HTML.

Example:

```html
<div>
    MINI MILITIA TOURNAMENT
</div>

<div>
    DESIGN WITH AI
</div>
```

This works for a few items, but becomes difficult when the number of events, workshops, or team members grows.

The goal today was to separate data from the user interface and make the website generate content dynamically using a backend API.

---

# 🧠 Concepts Learned

## 1. What is Node.js?

Node.js allows JavaScript to run outside the browser.

Before:

```text
JavaScript
↓
Browser Only
```

After:

```text
JavaScript
↓
Node.js Runtime
↓
Server
```

This allows JavaScript to create servers, APIs, automation scripts, and backend applications.

---

## 2. What is npm?

npm (Node Package Manager) is used to install external libraries and packages.

Example:

```bash
npm init -y
npm install express
npm install cors
```

npm creates:

```text
package.json
node_modules/
```

---

## 3. Understanding node_modules

When a package is installed, npm downloads all required files and dependencies into:

```text
node_modules/
```

Example:

```text
express
│
├── dependency 1
├── dependency 2
├── dependency 3
└── ...
```

This folder contains the actual code used by installed packages.

---

## 4. Creating an Express Server

Created first backend server:

```javascript
const express = require("express");
const app = express();

app.listen(5000, () => {
    console.log("Server running on port 5000");
});
```

Learned:

- require()
- express()
- app
- listen()
- ports

---

## 5. Routes

A route defines what happens when a specific URL is requested.

Example:

```javascript
app.get("/", (req, res) => {
    res.send("Archers backend running");
});
```

Request:

```text
http://localhost:5000/
```

Response:

```text
Archers backend running
```

---

## 6. Request and Response

Learned:

```javascript
(req, res)
```

### req

Contains information coming from the client.

Example:

```javascript
req.params
req.query
req.body
```

### res

Used to send data back.

Example:

```javascript
res.send()
res.json()
```

---

## 7. JSON APIs

Created API endpoints:

```javascript
app.get("/api/events")
```

```javascript
app.get("/api/team")
```

```javascript
app.get("/api/workshops")
```

Returning JSON data:

```javascript
res.json([
    {
        id: 1,
        title: "AI Workshop"
    }
]);
```

---

## 8. What is JSON?

JSON stands for:

```text
JavaScript Object Notation
```

Example:

```json
{
    "title": "AI Workshop",
    "date": "Sep 2026"
}
```

Purpose:

- Standard format for data exchange
- Human readable
- Supported by almost every programming language

---

## 9. Understanding CORS

Installed:

```javascript
const cors = require("cors");

app.use(cors());
```

Purpose:

```text
Frontend
↓
localhost:5500

Backend
↓
localhost:5000
```

Browsers block communication between different origins by default.

CORS allows trusted communication.

---

## 10. Fetch API

Frontend requests data from backend:

```javascript
const response = await fetch(
    "http://127.0.0.1:5000/api/events"
);
```

---

## 11. Async / Await

Used:

```javascript
const response = await fetch(...);
```

and

```javascript
const events = await response.json();
```

Purpose:

Wait for data before continuing execution.

---

## 12. Dynamic Rendering

Instead of writing:

```html
<div>Event 1</div>
<div>Event 2</div>
<div>Event 3</div>
```

Used:

```javascript
events.forEach(event => {
    container.innerHTML += `
        <div>
            ${event.title}
        </div>
    `;
});
```

Now the UI is generated automatically.

---

## 13. Arrays and Objects in Real Projects

Array:

```javascript
[
    {},
    {},
    {}
]
```

Object:

```javascript
{
    title: "AI Workshop",
    date: "Sep 2026"
}
```

Used to store structured data.

---

## 14. Understanding forEach()

```javascript
events.forEach(event => {
});
```

Important discovery:

```javascript
events
```

is the full array.

```javascript
event
```

represents one item at a time.

Example:

```javascript
events.forEach(event => {
    console.log(event.title);
});
```

The loop automatically visits each object.

---

## 15. Template Literals

Used:

```javascript
`${event.title}`
```

Allows JavaScript values to be inserted into HTML strings.

Example:

```javascript
`
<h1>${event.title}</h1>
`
```

---

## 16. Dynamic Website Architecture

Old Architecture:

```text
HTML
↓
Hardcoded Content
```

New Architecture:

```text
Backend API
      ↓
JSON Data
      ↓
Fetch API
      ↓
JavaScript
      ↓
DOM
      ↓
UI
```

This is how modern websites display:

- Products
- Users
- Events
- Blog Posts
- Dashboards

without manually writing every card.

---

# 🛠 APIs Built

## Events API

```text
GET /api/events
```

Returns event information.

---

## Team API

```text
GET /api/team
```

Returns team member information.

---

## Workshops API

```text
GET /api/workshops
```

Returns workshop information.

---

# 🐛 Bugs Debugged

### Variable Naming

Incorrect:

```javascript
event.image
```

inside team rendering.

Correct:

```javascript
member.image
```

---

### Duplicate IDs

Incorrect:

```html
id="team-container"
```

used multiple times.

Fixed by keeping IDs unique.

---

### Case Sensitivity

Incorrect:

```javascript
member.name
```

Correct:

```javascript
member.Name
```

JavaScript is case-sensitive.

---

### Server Troubleshooting

Used:

```bash
ps aux | grep node
```

to verify Node.js processes.

Learned that a running process does not always mean the terminal remains occupied.

---

# 💡 Biggest Lesson

Before today, I thought websites were mostly HTML.

Today I learned that professional websites are usually built around:

```text
Data
 ↓
Logic
 ↓
User Interface
```

The UI is generated from data.

Good engineering is not writing more HTML.

Good engineering is making future changes easier.

---

# ✅ Day 10 Outcome

Built my first API-driven website architecture.

Implemented:

- Node.js
- npm
- Express
- Routes
- JSON APIs
- CORS
- Fetch API
- Async/Await
- Dynamic Rendering
- Team API
- Events API
- Workshops API

ARCHERS is no longer a static HTML page.

It is now powered by backend APIs.

---

## Next Goal (Day 11)

- Learn POST requests
- Send data from frontend to backend
- Handle form submissions
- Understand req.body
- Prepare for Django transition

🚀 Day 10 Complete
