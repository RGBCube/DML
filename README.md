# 🈷️ Dotted Markup Language

Translate text to and from DML with ease.

## 📥 Installation

Execute `pip install dotted-ml`.

Add `import dml` to the top of your project.

## ♿ Usage

### 🚮 Encoding

```python
import dml

mycode = """
myvar = "Hello, world!"
print(myvar)
"""

dml.encode(mycode, out="mycode.dml")
```

`mycode.dml`:

```
܁٠܁٠۰܁܁٠܁܁٠܁۰܁܁܁܁٠٠܁۰܁܁܁٠܁܁٠۰܁܁٠٠٠٠܁۰܁܁܁٠٠܁٠۰܁٠٠٠٠٠۰܁܁܁܁٠܁۰܁٠٠٠٠٠۰܁٠٠٠܁٠۰܁٠٠܁٠٠٠۰܁܁٠٠܁٠܁۰܁܁٠܁܁٠٠۰܁܁٠܁܁٠٠۰܁܁٠܁܁܁܁۰܁٠܁܁٠٠۰܁٠٠٠٠٠۰܁܁܁٠܁܁܁۰܁܁٠܁܁܁܁۰܁܁܁٠٠܁٠۰܁܁٠܁܁٠٠۰܁܁٠٠܁٠٠۰܁٠٠٠٠܁۰܁٠٠٠܁٠۰܁٠܁٠۰܁܁܁٠٠٠٠۰܁܁܁٠٠܁٠۰܁܁٠܁٠٠܁۰܁܁٠܁܁܁٠۰܁܁܁٠܁٠٠۰܁٠܁٠٠٠۰܁܁٠܁܁٠܁۰܁܁܁܁٠٠܁۰܁܁܁٠܁܁٠۰܁܁٠٠٠٠܁۰܁܁܁٠٠܁٠۰܁٠܁٠٠܁۰܁٠܁٠۰
```

### ♻️ Decoding

```python
import dml

dml.decode_file("mycode.dml", out="mycode.py")
```

`mycode.py`:

```python

myvar = "Hello, world!"
print(myvar)

```