---
layout: post
title:  "Effective Python"
date:   2020-02-04 02:50:19
author: Kwanghee Choi
categories: software_design
---

# Overview & Disclaimer
This is a summary of the book [Effective Python, 1st ed](https://books.google.co.kr/books/about/Effective_Python.html?id=ocmqBgAAQBAJ&source=kp_book_description&redir_esc=y). Python 3.5+ contents are missing, as it is written at 2015, but still has great insights for Python programmers. 2nd ed are out, so this summary will hopefully be updated soon.

# 1. Pythonic Thinking
- Know which python you’re using
    - Difference between 2 and 3 / Runtimes (CPython, PyPy, … )
    - Prefer Python 3 over Python 2
- Follow PEP8
- Difference between `bytes`, `str` and `unicode`
    - Python 2: `str`(raw), `unicode` (Interchangeable for ASCII)
    - Python 3: `bytes`(raw), `str`(unicode)
    - → (decode), ← (encode)
- Prefer helper functions over complex expressions
    - Prefer blocks than one-liners
- Sequence slicing
    - Avoid being verbose (ex. No `x[0:]` or `x[:len(x)]`)
    - Slicing always returns new object
    - Avoid using start, end and stride, or use islice
- Use list comprehensions instead of map and filter
    - dict, set, list all supports comprehensions
    - Avoid using nested comprehensions
- Consider generators for large comprehensions
    - Fast execution and low memory, good for chaining
- Make for loops have many information as possible
    - Prefer `enumerate()` over `range()`
    - Use `zip()` (Lazy generator in 3, full result in 2)
    - `zip_longest()` can solve truncations
- Avoid using `else` after `for` / `while`
- Use all `try` / `except` / `else` / `finally`
    - `finally`: cleanup
    - `else` / `except`: visually distinguish success / fail case

# 2. Functions
- Prefer Exceptions over `None`
    - Returning `None` is error prone because other values also evaluates to `False`
- Know variable scope of closures
    - Current function →  Any enclosing scopes →  Global scope →  Built-in scope
    - Note that assignment and declaration have the same grammar
        - Use `nonlocal` for Python 3 and mutable variable for Python 2
- Be cautious on iterating generators
    - Be defensive when iterating over arguments
    - Define your own iterable container type with `__iter__`
    - star args(`*args`) makes generator into list
- Variable positional arguments reduce visual noise
- Keyword arguments can provide optional behavior
- Keyword-only arguments can enforce clarity
    - Use keyword arguments’ pop method to simulate in Python 2
- Use `None` and Docstrings to specify dynamic default arguments

# 3. Classes and Inheritance
- Code has to be dependent on the complexity of the structure
    - `dict` / `tuple` →  `namedtuple` →  Helper classes
    - Know the limitations of `namedtuple`
        - Cannot specify default argument values
        - Attribute values are accessible using numerical indexes and iteration
- Functions are more simple than classes to put as a parameter (as an interface)
    - Use functions if it is stateless
    - Use classes with `__call__` (callable class) if it is not stateless
- Consider classes as parameters for generic classes (class method polymorphism)
    - Use `@classmethod` to define alternative constructors than `__init__`
- Initialize parent classes with super
    - Standard method resolution order (mro) fixes initialization order
    - `super()` in Python 3 is same with `super(__class__, self)`
    - `super(__class__)`: Unbound object
    - `super(__class__, type)`: Bound object, Bound classmethod / method of object
    - `super(__class__, object)`: Bound object, Bound all method
- Use multiple inheritance only with mix-in utility classes
    - Mix-in: Classes with no state, only methods
    - Override mix-in methods with super() in child classes for pluggable behavior
- Plan to allow subclasses to do more with your internal APIs (in other words, avoid private)
    - `__private`: Avoid naming conflicts with subclasses that are out of your control
    - `_protected`: Use documentation to guide subclasses instead of forcing with private
- Inherit directly from Python’s container types for custom container types
    - Preserve semantics and functionalities familiar
    - Inherit list or dict for simple cases
    - Inherit collections.abc to ensure that custom classes match various requirements

# 4. Metaclasses and Attributes
- Use `@property`, `@x.setter`, `@x.getter` to give simple public attributes new functionalities
    - Do not use explicit getter and setter methods
    - Modify related object state only in @x.setter methods
    - `@property` methods has to be fast, so if it is too complex, refactor to stop using it
- Use descriptor classes (`__get__`, `__set__`) to reuse the behavior and validation of `@property`
    - You have to keep track of instances’ each attributes using WeakKeyDictionary
        - If it has the last remaining reference, it automatically empties it
- Use `__getattr__`, `__getattribute__`, `__setattr__` for lazy evaluation of attributes
    - `__getattr__` only runs once to load an attribute
    - `__getattribute__` runs every time when an attribute is accessed
    - `__setattr__` runs every time when attributes are assigned on an instance
    - Avoid infinite recursion in `__getattribute__` and `__setattr__` by using `super()`
- Use metaclass to ensure that subclasses are well formed before objects are constructed
    - Python 3: metaclass parameter / Python 2: `__metaclass__` class attribute
    - Make a metaclass by inheriting from type
    - Metaclass receives the contents of associated class in `__new__`
- Use metaclass to register class existence
    - Factory-like methods for modularization needs classes to be registered
- Use metaclass to modify or annotate class attributes
    - After class is defined, before class is actually used

# 5. Concurrency and Parallelism
- Use subprocess to run child processes and manage `stdin` / `stdout` / `stderr`
- Use Thread only for blocking I/O
    - Python threads cannot run bytecode in parallel because of GIL
    - Use Lock to avoid corruption
    - Use Queue for producer-consumer pattern
- Use coroutines to run thousands of functions seemingly at the same time
    - yield expression can send values to the exterior code
    - Python 3+: can receive values, Python 3.3+: `yield from`, Python 3.6+: `async` / `await`
- Access multiprocessing by concurrent.futures and ProcessPoolExecutor for parallelism

# 6. Built-in Modules
- Use `functool.wraps` to copy all the important metadata about the decorated function
- Use `contextlib`, `with` and `yield` for reusable `try` / `finally` behavior
    - Lock, `open(x)`, setting logging security level can be simplified with `with`
- Use `copyreg` to make `pickle` reliable
    - Adds missing attribute values, allows class versioning, provides stable import path
- Use `datetime` and `pytz` instead of `time` for translating different time zones
    - `time` fails for multiple local times
- Use built-in algorithms and data structures
    - Data structures: `deque`, `OrderedDict`, `defaultdict`, `heapq`, `bisect`
    - `itertools` can link iterators together, filter items, return combinations of items
- Precision: `float` < `decimal` < `fractions`
- Be familiar to Python Package Index (PyPI) and pip
    - Python 3.4+ supports pip default installation

# 7. Collaboration
- Write docstrings for every function, class and module
    - Modules: contents and any important classes or functions
    - Classes: behavior, important attributes, subclass behavior
    - Functions and methods: behavior, every argument, returned value, raised exception
- Use packages to organize modules and provide stable APIs
    - Packages provide non-conflicting namespaces
    - Control publicly visible names with `__all__` attribute and leading underscore names
- Define a root exception when defining a module’s API
- Know how to break circular dependencies
    - Refactor mutual dependencies into a separate module
        - Clear division isn’t always possible
    - Reordering imports
        - Goes against PEP8
        - Very unstable when edited, everything can break down very easily
    - Provide a configure function
        - Enables dependency injection pattern
        - Can be difficult to read and write code as heavy restructuring is needed
    - Dynamic import
        - Simplest solution, as it minimizes refactoring and complexity
        - Cost of import is especially bad in tight loops and sets up surprising failures
- Use virtual environments for isolated and reproducible dependencies
    - Python 3.4+ supports pyvenv default installation

# 8. Production
- Consider module-scoped code to configure deployment environments
    - Module-scoped: not inside any function or class
    - Module contents can be the product of any external condition including `sys` and `os`
    - Consider configuration files used with configparser
- Use `repr` for debugging
    - `repr` is an unambiguous representation, so `x == eval(repr(x))`
    - `str` is a human-readable representation
- Test everything with TestCase in unittest
    - Unit tests for isolated functionality (dedicated method for each behavior expectations)
    - Integration tests for modules that interact (`setUp`, `tearDown` methods)
- Use `pdb` and `set_trace()` for interactive debugging
- Profile and read stats before optimizing
    - Prefer `cProfile` (C-extension) over `profile` (Pure Python)
- Use `gc` and `tracemalloc` to track memory usage and leaks
    - Python 3.4+ supports `tracemalloc`
