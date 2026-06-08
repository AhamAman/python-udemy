# Python Threading & Concurrency Mastery Checklist

---

# Phase 0: Foundations (Must Know Before Threading)

## How Computers Execute Programs

- [ ] What is a process?
- [ ] What is a thread?
- [ ] CPU vs Core
- [ ] Single-core vs Multi-core CPUs
- [ ] How operating systems schedule work
- [ ] Context Switching
- [ ] Memory layout of a process
- [ ] Stack vs Heap memory

### Build

- [ ] Visualize multiple programs running on your machine
- [ ] Observe processes using Task Manager / htop

---

# Phase 1: Why Concurrency Exists

## Understand the Problem First

- [ ] Why synchronous code can be slow
- [ ] CPU waiting for I/O
- [ ] Blocking operations
- [ ] What is latency?
- [ ] What is throughput?
- [ ] Why CPUs stay idle during network calls

### Exercises

- [ ] Read a large file synchronously
- [ ] Download multiple URLs synchronously
- [ ] Measure execution time

### Questions

- [ ] Why is the CPU mostly idle during I/O?
- [ ] Why doesn't adding a faster CPU solve everything?

---

# Phase 2: Threading Fundamentals

## Python Thread Module

- [ ] What is a thread?
- [ ] Why threads are lighter than processes
- [ ] Main thread
- [ ] Worker thread

### Learn

- [ ] threading.Thread
- [ ] target function
- [ ] args
- [ ] start()
- [ ] run()
- [ ] join()

### Exercises

- [ ] Print from multiple threads
- [ ] Create 10 worker threads
- [ ] Download files concurrently

---

# Phase 3: Thread Lifecycle

## Understand Internals

- [ ] New state
- [ ] Runnable state
- [ ] Running state
- [ ] Waiting state
- [ ] Blocked state
- [ ] Dead state

### Learn

- [ ] Daemon threads
- [ ] Non-daemon threads
- [ ] Thread termination

### Exercises

- [ ] Observe daemon behavior
- [ ] Create background logger thread

---

# Phase 4: Shared Memory

## The Real Challenge

- [ ] Threads share memory
- [ ] Local variables
- [ ] Global variables
- [ ] Shared state

### Learn

- [ ] Race Conditions
- [ ] Data Corruption
- [ ] Lost Updates

### Exercises

- [ ] Build broken counter example
- [ ] Demonstrate race condition

---

# Phase 5: Synchronization

## Protect Shared Data

### Learn

- [ ] Lock
- [ ] RLock
- [ ] Semaphore
- [ ] BoundedSemaphore
- [ ] Event
- [ ] Condition
- [ ] Barrier

### Understand

- [ ] Critical Section
- [ ] Mutual Exclusion

### Exercises

- [ ] Fix race condition using Lock
- [ ] Producer Consumer with Condition
- [ ] Multi-thread downloader using Semaphore

---

# Phase 6: Thread Communication

## Safe Data Exchange

### Learn

- [ ] queue.Queue
- [ ] LifoQueue
- [ ] PriorityQueue

### Concepts

- [ ] Producer Consumer Pattern
- [ ] Work Queue Pattern

### Exercises

- [ ] Job processing system
- [ ] Image processing queue
- [ ] Background email sender

---

# Phase 7: ThreadPoolExecutor

## Modern Threading

### Learn

- [ ] concurrent.futures
- [ ] ThreadPoolExecutor
- [ ] submit()
- [ ] map()
- [ ] Future objects

### Understand

- [ ] Why thread pools exist
- [ ] Cost of thread creation

### Exercises

- [ ] Parallel URL fetcher
- [ ] Bulk API caller
- [ ] Log processor

---

# Phase 8: GIL Mastery

## Python's Biggest Threading Topic

### Learn

- [ ] What is the GIL?
- [ ] Why GIL exists
- [ ] Reference Counting
- [ ] Memory Safety

### Understand

- [ ] Why CPU-bound threads don't scale
- [ ] Why I/O-bound threads work well
- [ ] Thread switching under GIL

### Exercises

- [ ] CPU benchmark with threads
- [ ] I/O benchmark with threads

### Internals

- [ ] CPython Interpreter
- [ ] Bytecode Execution
- [ ] Eval Loop

---

# Phase 9: Multiprocessing

## When Threads Are Not Enough

### Learn

- [ ] multiprocessing module
- [ ] Process class
- [ ] Pool
- [ ] ProcessPoolExecutor

### Understand

- [ ] Separate memory spaces
- [ ] IPC
- [ ] Serialization

### Exercises

- [ ] CPU intensive calculations
- [ ] Parallel image processing

---

# Phase 10: Asyncio

## Another Concurrency Model

### Learn

- [ ] Event Loop
- [ ] Coroutine
- [ ] async
- [ ] await

### Understand

- [ ] Threading vs Asyncio
- [ ] Cooperative Scheduling

### Exercises

- [ ] Async web scraper
- [ ] Async API client

---

# Phase 11: Concurrency Design Patterns

### Patterns

- [ ] Producer Consumer
- [ ] Worker Pool
- [ ] Pipeline
- [ ] Fan Out
- [ ] Fan In
- [ ] Publish Subscribe

### Projects

- [ ] Multi-threaded downloader
- [ ] Log processing system
- [ ] Background task queue

---

# Phase 12: Debugging Concurrent Programs

### Learn

- [ ] Deadlock
- [ ] Starvation
- [ ] Livelock

### Tools

- [ ] logging
- [ ] thread identifiers
- [ ] traceback

### Exercises

- [ ] Create deadlock intentionally
- [ ] Fix deadlock

---

# Phase 13: Performance Engineering

### Learn

- [ ] Profiling
- [ ] Throughput
- [ ] Latency
- [ ] Benchmarking

### Tools

- [ ] time
- [ ] timeit
- [ ] cProfile

### Exercises

- [ ] Benchmark sync vs thread vs process vs async

---

# Phase 14: CPython Internals

## Senior Engineer Level

### Learn

- [ ] CPython architecture
- [ ] Bytecode
- [ ] Frame Objects
- [ ] Eval Loop
- [ ] Reference Counting
- [ ] Garbage Collection

### Understand

- [ ] How GIL is implemented
- [ ] Thread scheduling in CPython
- [ ] Why atomic operations appear safe

---

# Phase 15: OS-Level Concurrency

## Systems Understanding

### Learn

- [ ] POSIX Threads
- [ ] Kernel Threads
- [ ] User Threads
- [ ] Scheduler
- [ ] Preemptive Scheduling
- [ ] CPU Affinity

### Understand

- [ ] How Python threads map to OS threads
- [ ] Context Switch Cost

---

# Phase 16: Build Real Projects

### Beginner

- [ ] Multi-file downloader
- [ ] Concurrent web scraper

### Intermediate

- [ ] Chat server
- [ ] Background job system

### Advanced

- [ ] Mini Celery clone
- [ ] Distributed task queue
- [ ] Thread-safe cache

### Expert

- [ ] Build your own ThreadPoolExecutor
- [ ] Build your own Future object
- [ ] Build your own Event Loop
- [ ] Read CPython threading source code

---

# Final Mastery

Can Explain:

- [ ] Process vs Thread
- [ ] Concurrency vs Parallelism
- [ ] Thread vs Asyncio
- [ ] Thread vs Multiprocessing
- [ ] GIL Internals
- [ ] Deadlock
- [ ] Race Condition
- [ ] ThreadPoolExecutor Internals
- [ ] Event Loop Internals
- [ ] CPython Scheduler Behavior

Can Build:

- [ ] Thread-safe applications
- [ ] Concurrent network services
- [ ] High throughput systems
- [ ] Production-grade worker pools