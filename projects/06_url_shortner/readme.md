# 📦 Framework & Dependency Deep Dive (Flask URL Shortener)

Understanding every dependency used in the project and the architecture behind it.

---

# 🌱 Flask Fundamentals

- [ ] What is Flask?
- [ ] Why was Flask created?
- [ ] What problem does Flask solve?
- [ ] Flask vs Django
- [ ] Flask vs FastAPI
- [ ] What makes Flask a micro-framework?
- [ ] What responsibilities does Flask handle?
- [ ] What responsibilities are left to the developer?
- [ ] Flask architecture overview
- [ ] Flask ecosystem overview

---

# 🌱 Flask Application Internals

- [ ] What does `Flask(__name__)` do?
- [ ] What is `__name__`?
- [ ] Why does Flask need it?
- [ ] How Flask locates templates
- [ ] How Flask locates static files
- [ ] Application startup lifecycle
- [ ] Development server startup
- [ ] Production server startup
- [ ] Request lifecycle
- [ ] Response lifecycle

---

# 🌱 Routing

- [ ] What is a route?
- [ ] Why routing exists
- [ ] Route decorators
- [ ] URL mapping
- [ ] Dynamic routes
- [ ] Route parameters
- [ ] Route matching
- [ ] Route resolution order
- [ ] Redirect routes
- [ ] Route best practices

---

# 🌱 Request Handling

- [ ] Request object
- [ ] Form data
- [ ] Query parameters
- [ ] Request headers
- [ ] Cookies
- [ ] Sessions
- [ ] Request validation
- [ ] Request parsing
- [ ] Request context
- [ ] Application context

---

# 🌱 Response Handling

- [ ] Response object
- [ ] Returning strings
- [ ] Returning HTML
- [ ] Returning JSON
- [ ] Returning redirects
- [ ] Custom status codes
- [ ] Response headers
- [ ] Response lifecycle
- [ ] Redirect responses
- [ ] Error responses

---

# 🌱 Jinja2

## Fundamentals

- [ ] What is Jinja2?
- [ ] Why template engines exist
- [ ] Template rendering
- [ ] Dynamic HTML generation
- [ ] Separation of frontend and backend

## Templates

- [ ] Variables
- [ ] Loops
- [ ] Conditionals
- [ ] Template inheritance
- [ ] Includes
- [ ] Filters
- [ ] Macros
- [ ] Template organization

## Flask Integration

- [ ] render_template()
- [ ] Passing variables
- [ ] Rendering dynamic content
- [ ] Escaping output
- [ ] Security implications

---

# 🌱 Werkzeug

## Fundamentals

- [ ] What is Werkzeug?
- [ ] Why Werkzeug exists
- [ ] Relationship between Flask and Werkzeug
- [ ] WSGI fundamentals
- [ ] Request processing
- [ ] Response generation

## Routing

- [ ] URL routing internals
- [ ] URL matching
- [ ] URL building
- [ ] Route resolution

## URL Shortener Context

- [ ] Redirect implementation
- [ ] HTTP status handling
- [ ] Request parsing
- [ ] URL utilities

---

# 🌱 MarkupSafe

## Fundamentals

- [ ] What is MarkupSafe?
- [ ] Why HTML escaping matters
- [ ] What is XSS?
- [ ] User input dangers
- [ ] HTML injection

## Flask Context

- [ ] Jinja2 escaping
- [ ] Safe rendering
- [ ] Preventing XSS
- [ ] Security best practices

---

# 🌱 Click

## Fundamentals

- [ ] What is Click?
- [ ] Why Click exists
- [ ] Command-line applications
- [ ] CLI architecture

## Flask Context

- [ ] flask run
- [ ] flask shell
- [ ] Flask CLI commands
- [ ] Custom CLI commands
- [ ] Environment management

---

# 🌱 ItsDangerous

## Fundamentals

- [ ] What is ItsDangerous?
- [ ] Why signed data exists
- [ ] What is tamper detection?
- [ ] Cryptographic signatures
- [ ] Secure token generation

## Flask Context

- [ ] Session cookies
- [ ] Secure tokens
- [ ] Password reset links
- [ ] Verification links
- [ ] Session protection

---

# 🌱 Blinker

## Fundamentals

- [ ] What is Blinker?
- [ ] What are signals?
- [ ] Event-driven programming
- [ ] Publisher-subscriber pattern
- [ ] Loose coupling

## Flask Context

- [ ] Flask signals
- [ ] Request signals
- [ ] Application signals
- [ ] Custom events
- [ ] Event-driven architecture

---

# 🌱 Dependency Relationships

- [ ] Why Flask depends on Werkzeug
- [ ] Why Flask depends on Jinja2
- [ ] Why Flask depends on Click
- [ ] Why Flask depends on ItsDangerous
- [ ] Why Jinja2 depends on MarkupSafe
- [ ] Why Flask can use Blinker
- [ ] Dependency graph understanding
- [ ] Framework architecture understanding

---

# 🌱 WSGI Fundamentals

- [ ] What is WSGI?
- [ ] Why WSGI exists
- [ ] Request flow through WSGI
- [ ] Flask as WSGI application
- [ ] Gunicorn and WSGI
- [ ] Development server vs production server

---

# 🌱 Security Concepts

- [ ] XSS attacks
- [ ] CSRF attacks
- [ ] Open redirects
- [ ] Session security
- [ ] Secure cookies
- [ ] Input validation
- [ ] URL validation
- [ ] Security headers

---

# 🧠 Internal Architecture

```text
Browser
    ↓
Flask Router
    ↓
Werkzeug Request
    ↓
View Function
    ↓
Database
    ↓
Jinja2 Template
    ↓
Werkzeug Response
    ↓
Browser
```

- [ ] Trace request flow
- [ ] Trace redirect flow
- [ ] Trace template rendering flow
- [ ] Trace error handling flow
- [ ] Trace database interactions
- [ ] Trace session handling

---

# 🧠 Python Internals

- [ ] Decorators used in routing
- [ ] Function registration
- [ ] Closures in Flask
- [ ] Context locals
- [ ] Thread-local storage
- [ ] Import system interactions
- [ ] Request object lifecycle

---

# 🏛 Architecture & Design

- [ ] MVC pattern
- [ ] Service layer pattern
- [ ] Repository pattern
- [ ] Dependency injection concepts
- [ ] Separation of concerns
- [ ] Clean architecture principles
- [ ] Scalability considerations

---

# 🏆 Veteran Questions

- [ ] Why is Flask called a micro-framework?
- [ ] Why doesn't Flask include ORM by default?
- [ ] Why does Flask rely on Werkzeug?
- [ ] Why does Flask use Jinja2?
- [ ] Why are signed cookies important?
- [ ] Why are route decorators powerful?
- [ ] Could you build a mini Flask framework?
- [ ] Could you build your own router?
- [ ] Could you build your own template engine?
- [ ] Could you explain every dependency in requirements.txt?
- [ ] Could you trace a request from browser to database and back?
- [ ] Could you explain Flask architecture from first principles?

---

# 🚀 Ultimate Mastery

- [ ] Explain every dependency in requirements.txt
- [ ] Explain Flask architecture confidently
- [ ] Understand request lifecycle
- [ ] Understand response lifecycle
- [ ] Understand template rendering
- [ ] Understand routing internals
- [ ] Understand session management
- [ ] Understand WSGI
- [ ] Build a mini Flask clone
- [ ] Teach Flask from beginner to veteran level