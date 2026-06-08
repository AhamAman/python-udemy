# Python Asyncio Mastery Checklist

---

# Phase 0: Prerequisites

## Python Fundamentals

* [ ] Functions
* [ ] Scope
* [ ] Objects
* [ ] Iterators
* [ ] Generators
* [ ] Decorators

## Concurrency Foundations

* [ ] Process vs Thread
* [ ] Concurrency vs Parallelism
* [ ] Blocking vs Non-blocking
* [ ] CPU-bound vs I/O-bound

---

# Phase 1: Why Async Exists

## The Problem

* [ ] Why synchronous code wastes time
* [ ] Waiting for I/O
* [ ] Network latency
* [ ] Database latency

## First Principles

* [ ] Why threads are expensive
* [ ] Why context switching costs exist
* [ ] Why thousands of threads are problematic

## Understand

* [ ] Async is not parallelism
* [ ] Async is cooperative multitasking

### Exercises

* [ ] Sequential URL fetcher
* [ ] Measure waiting time

---

# Phase 2: Event Loop Fundamentals

## Core Concepts

* [ ] Event Loop
* [ ] Task
* [ ] Coroutine
* [ ] Future

## Understand

* [ ] Event Loop as a scheduler
* [ ] Ready queue
* [ ] Waiting queue

### Visualize

* [ ] How event loop picks tasks
* [ ] How task switching happens

---

# Phase 3: Coroutines

## Syntax

* [ ] async def
* [ ] await

## Understanding

* [ ] What a coroutine object is
* [ ] Coroutine lifecycle
* [ ] Suspended state
* [ ] Resumed state

### Exercises

* [ ] Create simple coroutine
* [ ] Chain multiple coroutines

---

# Phase 4: Await Deep Dive

## Learn

* [ ] await keyword
* [ ] Yielding control
* [ ] Cooperative scheduling

## Understand

* [ ] What happens internally when await executes
* [ ] Why await is a suspension point

### Exercises

* [ ] Trace execution flow
* [ ] Nested awaits

---

# Phase 5: Tasks

## asyncio Tasks

* [ ] asyncio.create_task()
* [ ] Task lifecycle

## Concepts

* [ ] Scheduled tasks
* [ ] Background tasks

### Exercises

* [ ] Run multiple tasks
* [ ] Task monitoring

---

# Phase 6: Futures

## Learn

* [ ] Future Object
* [ ] Future States

### States

* [ ] Pending
* [ ] Running
* [ ] Completed
* [ ] Cancelled

## Understand

* [ ] Relationship between Task and Future

---

# Phase 7: Running Concurrent Work

## APIs

* [ ] asyncio.gather()
* [ ] asyncio.wait()
* [ ] asyncio.as_completed()

## Concepts

* [ ] Fan-out
* [ ] Fan-in

### Exercises

* [ ] Concurrent URL downloader
* [ ] API aggregator

---

# Phase 8: Async Synchronization

## Primitives

* [ ] asyncio.Lock
* [ ] asyncio.Event
* [ ] asyncio.Semaphore
* [ ] asyncio.Condition

## Understand

* [ ] Race conditions still exist

### Exercises

* [ ] Async producer consumer
* [ ] Rate limiter

---

# Phase 9: Cancellation

## Learn

* [ ] task.cancel()
* [ ] CancelledError

## Concepts

* [ ] Graceful shutdown
* [ ] Cancellation propagation

### Exercises

* [ ] Cancel long-running tasks
* [ ] Timeout handling

---

# Phase 10: Timeouts

## APIs

* [ ] asyncio.wait_for()
* [ ] asyncio.timeout()

## Concepts

* [ ] Defensive programming
* [ ] Hung task prevention

---

# Phase 11: Async Queues

## Learn

* [ ] asyncio.Queue
* [ ] PriorityQueue
* [ ] LifoQueue

## Patterns

* [ ] Producer Consumer
* [ ] Work Queue

### Exercises

* [ ] Async worker pool
* [ ] Task processing system

---

# Phase 12: Async Design Patterns

## Fundamental Patterns

* [ ] Producer Consumer
* [ ] Pipeline
* [ ] Fan-Out
* [ ] Fan-In
* [ ] Scatter Gather

## Advanced Patterns

* [ ] Reactor Pattern
* [ ] Pub/Sub
* [ ] Event Bus

---

# Phase 13: Async Networking

## TCP/IP Basics

* [ ] Sockets
* [ ] TCP
* [ ] UDP

## Asyncio Networking

* [ ] Streams
* [ ] TCP Server
* [ ] TCP Client

### Exercises

* [ ] Echo server
* [ ] Chat server

---

# Phase 14: HTTP Clients

## Libraries

* [ ] aiohttp
* [ ] httpx

## Learn

* [ ] Connection Pooling
* [ ] Retries
* [ ] Timeouts

### Projects

* [ ] Web Scraper
* [ ] API Aggregator

---

# Phase 15: Async Databases

## Libraries

* [ ] asyncpg
* [ ] SQLAlchemy Async

## Concepts

* [ ] Connection Pools
* [ ] Transactions

### Exercises

* [ ] Async CRUD service

---

# Phase 16: Async Web Frameworks

## FastAPI

* [ ] Async routes
* [ ] Dependency Injection

## Alternatives

* [ ] Starlette
* [ ] Sanic
* [ ] Quart

### Projects

* [ ] Async REST API
* [ ] Real-time API

---

# Phase 17: Failure Modes

## Common Bugs

* [ ] Forgotten await
* [ ] Blocking code inside async
* [ ] Event loop starvation

## Concurrency Problems

* [ ] Race conditions
* [ ] Deadlocks
* [ ] Resource leaks

## Production Problems

* [ ] Connection exhaustion
* [ ] Retry storms
* [ ] Thundering herd

---

# Phase 18: Performance Engineering

## Metrics

* [ ] Throughput
* [ ] Latency

## Profiling

* [ ] asyncio debug mode
* [ ] cProfile

## Benchmarks

* [ ] Sync vs Thread vs Async

---

# Phase 19: Event Loop Internals

## Deep Dive

* [ ] Selector
* [ ] Polling
* [ ] epoll
* [ ] kqueue
* [ ] IOCP

## Understand

* [ ] How event loop wakes up
* [ ] How callbacks execute
* [ ] Task scheduling internals

---

# Phase 20: Async Internals

## Under The Hood

* [ ] Coroutine objects
* [ ] await protocol
* [ ] **await**()
* [ ] Generator-based coroutines

## CPython

* [ ] Async bytecode
* [ ] Task implementation
* [ ] Future implementation

---

# Phase 21: Build Internals Yourself

## Build

* [ ] Mini Event Loop
* [ ] Mini Future
* [ ] Mini Task Scheduler
* [ ] Async Queue

---

# Phase 22: Real Projects

## Beginner

* [ ] Concurrent Downloader
* [ ] Async Web Scraper

## Intermediate

* [ ] Chat Server
* [ ] API Gateway

## Advanced

* [ ] Real-time Notification System
* [ ] WebSocket Server
* [ ] Background Job Processor

## Expert

* [ ] Event Loop Clone
* [ ] Async Framework Clone
* [ ] High Throughput Proxy Server

---

# Final Mastery

Can Explain:

* [ ] Event Loop
* [ ] Coroutine
* [ ] Future
* [ ] Task
* [ ] await Internals
* [ ] Reactor Pattern
* [ ] epoll/kqueue/IOCP
* [ ] Async vs Threading
* [ ] Async vs Multiprocessing

Can Build:

* [ ] Async APIs
* [ ] Async Services
* [ ] Worker Pools
* [ ] Chat Servers
* [ ] Event Loops
* [ ] High Throughput Systems
