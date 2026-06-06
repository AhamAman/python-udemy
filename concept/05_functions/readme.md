# 🔧 Python Functions: Mastery Checklist

A complete roadmap from beginner usage to deep internals, closures, decorators, function objects, CPython implementation details, and professional engineering patterns. All are not covered now but a general road map to learn.

---

# 🎯 First Principles

* [ ] What is a function?
* [ ] Why do programming languages need functions?
* [ ] What problem do functions solve?
* [ ] What would programming look like without functions?
* [ ] What is abstraction?
* [ ] What is code reuse?
* [ ] What is modularity?
* [ ] What is decomposition?
* [ ] How do functions improve maintainability?
* [ ] Why are functions considered a fundamental programming construct?

---

# 🌱 Basic Function Creation

* [ ] What is the `def` keyword?
* [ ] Basic function syntax
* [ ] Function naming conventions
* [ ] Calling a function
* [ ] Function execution flow
* [ ] What happens when a function is called?
* [ ] What happens when a function finishes?
* [ ] Difference between defining and calling a function
* [ ] Empty functions using `pass`
* [ ] Function documentation strings

---

# 🌱 Parameters & Arguments

* [ ] What is a parameter?
* [ ] What is an argument?
* [ ] Difference between parameters and arguments
* [ ] Positional arguments
* [ ] Keyword arguments
* [ ] Mixing positional and keyword arguments
* [ ] Default parameters
* [ ] Required parameters
* [ ] Optional parameters
* [ ] Parameter ordering rules

---

# 🌱 Return Values

* [ ] What does `return` do?
* [ ] Why do functions return values?
* [ ] Returning a single value
* [ ] Returning multiple values
* [ ] Tuple packing and unpacking
* [ ] Returning None
* [ ] Early returns
* [ ] Multiple return statements
* [ ] Return vs print
* [ ] Function output design

---

# 🌱 Scope Fundamentals

* [ ] What is scope?
* [ ] Local scope
* [ ] Global scope
* [ ] Variable visibility
* [ ] Name resolution
* [ ] Why local variables disappear
* [ ] Shadowing variables
* [ ] Accessing global variables
* [ ] Modifying global variables
* [ ] Scope-related errors

---

# 🌱 LEGB Rule

* [ ] What is LEGB?
* [ ] Local scope
* [ ] Enclosing scope
* [ ] Global scope
* [ ] Built-in scope
* [ ] Name lookup process
* [ ] Variable resolution order
* [ ] Common LEGB debugging scenarios

---

# 🌱 Function Arguments Deep Dive

* [ ] Positional-only arguments
* [ ] Keyword-only arguments
* [ ] Variable-length positional arguments (`*args`)
* [ ] Variable-length keyword arguments (`**kwargs`)
* [ ] Unpacking arguments
* [ ] Combining *args and **kwargs
* [ ] Forwarding arguments
* [ ] API design considerations

---

# 🌱 Mutable Default Arguments

* [ ] What are mutable default arguments?
* [ ] Why are they dangerous?
* [ ] Function definition time vs execution time
* [ ] Common bugs
* [ ] Safe alternatives
* [ ] Using None as a default value

---

# 🌱 First-Class Functions

* [ ] What does first-class function mean?
* [ ] Assigning functions to variables
* [ ] Passing functions as arguments
* [ ] Returning functions from functions
* [ ] Storing functions in data structures
* [ ] Functions as objects
* [ ] Why Python treats functions as objects

---

# 🌱 Lambda Functions

* [ ] What is a lambda?
* [ ] Lambda syntax
* [ ] Lambda vs def
* [ ] Common lambda use cases
* [ ] Limitations of lambda
* [ ] Readability concerns
* [ ] Functional programming usage

---

# 🌱 Recursion

* [ ] What is recursion?
* [ ] Base case
* [ ] Recursive case
* [ ] Call stack behavior
* [ ] Recursive problem solving
* [ ] Direct recursion
* [ ] Indirect recursion
* [ ] Infinite recursion
* [ ] Recursion limits
* [ ] Recursion vs iteration

---

# 🌱 Nested Functions

* [ ] What are nested functions?
* [ ] Why create functions inside functions?
* [ ] Scope interactions
* [ ] Accessing outer variables
* [ ] Encapsulation benefits
* [ ] Real-world applications

---

# 🌱 Closures

* [ ] What is a closure?
* [ ] Why closures exist
* [ ] Capturing variables
* [ ] Closure memory behavior
* [ ] State retention
* [ ] Closure use cases
* [ ] Closures vs classes
* [ ] Debugging closures

---

# 🌱 nonlocal Keyword

* [ ] What is nonlocal?
* [ ] Why nonlocal exists
* [ ] Difference between global and nonlocal
* [ ] Closure state modification
* [ ] Common use cases

---

# 🌱 Higher-Order Functions

* [ ] What is a higher-order function?
* [ ] Functions accepting functions
* [ ] Functions returning functions
* [ ] Callback functions
* [ ] Functional composition
* [ ] Real-world examples

---

# 🌱 Built-in Functional Tools

* [ ] map()
* [ ] filter()
* [ ] reduce()
* [ ] any()
* [ ] all()
* [ ] sorted() with key functions
* [ ] Custom key functions
* [ ] Functional pipelines

---

# 🌱 Decorators

* [ ] What is a decorator?
* [ ] Why decorators exist
* [ ] Function wrapping
* [ ] Decorator syntax
* [ ] Writing simple decorators
* [ ] Decorators with arguments
* [ ] Stacked decorators
* [ ] Preserving metadata
* [ ] functools.wraps
* [ ] Real-world decorator patterns

---

# 🌱 Type Hints

* [ ] What are type hints?
* [ ] Why type hints exist
* [ ] Function parameter annotations
* [ ] Return type annotations
* [ ] Optional types
* [ ] Union types
* [ ] Generic types
* [ ] Static type checking
* [ ] Type hint limitations

---

# ⚙️ Practical Function Design

* [ ] Single responsibility principle
* [ ] Pure functions
* [ ] Side effects
* [ ] Function cohesion
* [ ] Function coupling
* [ ] Naming functions effectively
* [ ] Small vs large functions
* [ ] Refactoring functions

---

# ⚙️ Error Handling

* [ ] Exceptions inside functions
* [ ] Raising exceptions
* [ ] Re-raising exceptions
* [ ] Input validation
* [ ] Defensive programming
* [ ] Error propagation
* [ ] Custom exception usage

---

# ⚙️ Testing Functions

* [ ] Unit testing functions
* [ ] Testing pure functions
* [ ] Mocking dependencies
* [ ] Edge case testing
* [ ] Boundary testing
* [ ] Function contract testing
* [ ] Property-based testing

---

# ⚙️ Async Functions

* [ ] What is an async function?
* [ ] async keyword
* [ ] await keyword
* [ ] Coroutines
* [ ] Event loop interactions
* [ ] Async call chains
* [ ] Async vs synchronous functions
* [ ] Common async pitfalls

---

# 🧠 Function Objects Internals

* [ ] How are functions represented internally?
* [ ] Function objects
* [ ] Code objects
* [ ] Function attributes
* [ ] **name**
* [ ] **doc**
* [ ] **annotations**
* [ ] **defaults**
* [ ] **closure**

---

# 🧠 Stack Frames & Execution

* [ ] What is a stack frame?
* [ ] Function call lifecycle
* [ ] Local variable storage
* [ ] Function call stack
* [ ] Stack unwinding
* [ ] Recursion stack growth
* [ ] Frame inspection

---

# 🧠 Python Internals

* [ ] How does Python compile functions?
* [ ] AST representation of functions
* [ ] Bytecode generation
* [ ] Function call bytecode
* [ ] Argument passing internals
* [ ] Return value internals
* [ ] Closure implementation
* [ ] Decorator implementation

---

# 🧠 CPython Deep Dive

* [ ] PyFunctionObject
* [ ] PyCodeObject
* [ ] Frame objects
* [ ] Evaluation loop
* [ ] Local variable storage
* [ ] Cell objects in closures
* [ ] Function call optimization
* [ ] Vectorcall protocol
* [ ] Built-in function implementation

---

# 📈 Performance Engineering

* [ ] Cost of function calls
* [ ] Stack frame overhead
* [ ] Function inlining concepts
* [ ] Memoization
* [ ] functools.lru_cache
* [ ] Recursive performance
* [ ] Generator performance
* [ ] Closure performance
* [ ] Profiling function execution

---

# 🏛 System Design Perspective

* [ ] Functions in large codebases
* [ ] Service-layer functions
* [ ] Utility functions
* [ ] Domain functions
* [ ] API handler functions
* [ ] Event handler functions
* [ ] Plugin architectures
* [ ] Dependency injection

---

# 🔬 Advanced Patterns

* [ ] Factory functions
* [ ] Builder functions
* [ ] Function composition
* [ ] Currying
* [ ] Partial application
* [ ] Dynamic function creation
* [ ] Dispatch tables
* [ ] Strategy pattern with functions

---

# 🏆 Veteran Questions

* [ ] Why are functions first-class objects?
* [ ] Why does Python use stack frames?
* [ ] Why do closures exist?
* [ ] Why are decorators powerful?
* [ ] Why are mutable default arguments dangerous?
* [ ] Why does LEGB exist?
* [ ] When should closures replace classes?
* [ ] When should classes replace functions?
* [ ] How does CPython execute function calls internally?
* [ ] Could you implement Python's function system from scratch?
* [ ] Could you build closures and decorators yourself?
* [ ] Could you design a plugin architecture using only functions?
