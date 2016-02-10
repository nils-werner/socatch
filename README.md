StackOverflow Exception Catcher
===============================

Automatically open exceptions in StackOverflow. Because it's a [running](https://twitter.com/DivineOmega/status/695744177557106688) [gag](https://twitter.com/DivineOmega/status/696806187526983680) on Twitter now.

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
