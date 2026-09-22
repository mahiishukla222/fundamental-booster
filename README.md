# Python `id()` Function Example

## Program

```python
a = 100
b = 100

print(id(a))
print(id(b))

a = 200
b = 100

print(id(a))
print(id(b))
```

## Explanation

The `id()` function in Python returns the **unique identity (memory identity)** of an object during its lifetime.

### Step 1

```python
a = 100
b = 100
```

Both variables have the same value `100`.

```python
print(id(a))
print(id(b))
```

Python may use the same integer object for `100`, so both `id()` values are generally the same.

### Step 2

```python
a = 200
b = 100
```

Now `a` refers to `200`, while `b` still refers to `100`.

```python
print(id(a))
print(id(b))
```

The `id()` values will generally be different because `a` and `b` now refer to different integer objects.

## Expected Output

The exact numbers will be different on different computers/runs, so your output may look like:

```text
140721234567890
140721234567890
140721234571090
140721234567890
```

> **Note:** Do not expect the exact `id()` numbers shown above. They are only examples.

## Key Point

`id(variable)` tells you the identity of the object that the variable refers to.

```python
id(a)
```

means: **"Give me the identity of the object referenced by `a`."**
# fundamental-booster
