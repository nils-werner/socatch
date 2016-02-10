StackOverflow Exception Catcher
===============================

Automatically open exceptions in StackOverflow. Because it's a running gag on Twitter now.

Installation
------------

```bash
$ pip install socatch
```

Usage
-----

**Manual Catching.** Lets you define a `try...except` clause after which StackOverflow is opened.

```python
import socatch

try:
    ...
except Exception as e:
    socatch.catch(e)
```

**Automatic catching.** Will open all unhandled exceptions.

```python
import socatch.all
```

Done.
