# Embedded Documentation for Python

## Explanation

`docstrings` is Python's built-in method. They are string literals `"""Like
this"""` placed as the very first statement inside a module, class, method, or
function definition.

Typical function documentation:

* What does this function do?
* What does it expect?
* What does it give back?
* What might go wrong?"

The Google Style Docstring Format is a clear way to answer these questions. Here
is the basic structure:

```python
"""One-line summary: What the function does.

(Optional) More detailed explanation paragraph(s).

Args:
    param_name (param_type): Description of the parameter.
    param_name2 (param_type): Description of the parameter.

Returns:
    return_type: Description of the return value. Can include conditions.

Raises:
    ErrorType: Explanation of when this error is raised.
"""
```

There are a number of tools pick up the *docstrings* and automatically create documentation:

* sphinx — [http://www.sphinx-doc.org/en/master/index.html](http://www.sphinx-doc.org/en/master/index.html)
* pdoc — [https://github.com/BurntSushi/pdoc](https://github.com/BurntSushi/pdoc)
* pydoctor — [https://github.com/twisted/pydoctor](https://github.com/twisted/pydoctor)
* Doxygen — [http://www.stack.nl/~dimitri/doxygen/index.html](http://www.stack.nl/~dimitri/doxygen/index.html)

IDE will also pick up the documentation strings and show them as you use a function.

