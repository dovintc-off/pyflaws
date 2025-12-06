# PyFlaws v0.1

**PyFlaws** is an experimental library containing *potentially dangerous* or *non-standard* Python functions.  
Use it **only for educational, creative, or testing purposes** — **never in production!**

> ⚠️ Warning: Some functions may disrupt script execution, modify global state, or rely on internal Python APIs. Use with caution!

---

## 📦 Installation

```bash
git clone https://github.com/dovintc-off/PyFlaws.git
```

Then import modules manually (e.g., via sys.path or proper package structure).

---

## 💥 Usage Example
``` python
from pyflaws import *

x = 42
name = "test"
print(x, name)  # → 42 test

wertis()  # wipes all global variables!

print(x, name)  # → None None (or raises NameError, depending on context)
```

---

## 🧪 Disclaimer

Functions rely on sys._getframe() and other CPython-specific internals.
Not compatible with PyPy, Jython, or alternative Python implementations.
Intended solely for experiments, CTF challenges, Python "magic" demos, or playful hacking.

---

## 📝 License
Check the repository for license information. It’s highly recommended to add a LICENSE file before public distribution.

---

**Author: [dovintc-off](https://github.com/dovintc-off)**