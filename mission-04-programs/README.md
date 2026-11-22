# Mission 4 — How Programs Run

## 1. Task / Objective

Create and run a simple Python program, and compare how compilers and interpreters translate and execute programs.

## 2. Work Completed

- Created `hello.py` inside this mission folder with a one-line print statement.
- Ran the program from Terminal using `python3 hello.py` and confirmed the output.
- Completed the compiler vs interpreter comparison table.
- Wrote an explanation of the difference in my own words.

## 3. Commands / Tools Used

| Command / Tool | Purpose |
|---------------|---------|
| `python3 hello.py` | Run the Python program from Terminal |
| VS Code | Write the hello.py file |
| `cat hello.py` | View the contents of the file to confirm it was saved correctly |

## 4. My Understanding

### Task 4.1 — Create and Run a Python Program

I created a file called `hello.py` with this content:

```python
print("Hello from Python")
```

I ran it from Terminal:

```
$ python3 hello.py
Hello from Python
```

The message appeared immediately. Python read my source code line by line and executed it right away.

### Task 4.2 — Compare Compiler and Interpreter

| Point | Compiler | Interpreter |
|-------|----------|-------------|
| When translation / execution happens | The compiler translates the entire source code into machine code before the program runs. The translated file can then be executed on its own. | The interpreter reads and executes the source code line by line at runtime. There is no separate translation step that produces a standalone file. |
| Typical output | A compiled executable file (like a `.exe` or binary) that can run independently | No separate output file — the program runs directly from the source code |
| One example | C (uses `gcc` compiler to produce a binary) | Python (the `python3` command interprets and runs `.py` files) |
| One advantage | Compiled programs generally run faster because the translation is already done before execution | Easier to test and debug because I can run code immediately without a separate compile step |

**Explanation in my own words:**

A compiler and an interpreter both take source code written by a human and make the computer understand it, but they do it in different ways. A compiler reads through the entire program first, translates everything into machine code, and produces a separate file that the computer can run on its own. This means there is a waiting step before I can see my program work, but once it is compiled, it runs quickly.

An interpreter, on the other hand, reads the code one line at a time and executes each line immediately. There is no separate compiled file — the interpreter does the translation and execution together. This is why when I ran `python3 hello.py`, the output showed up instantly without any compile step. The trade-off is that interpreted programs can be slower for heavy tasks because the translation happens every time the program runs.

In practice, many languages mix both approaches. Python, for example, actually compiles source code to bytecode internally, and then an interpreter runs that bytecode. But from my perspective as a user, it feels like an interpreter because I just run my `.py` file and see results immediately.

## 5. Difficulties Faced

No major difficulties. The Python program was simple and ran on the first attempt.

## 6. How I Resolved Them

Not applicable.

## 7. Evidence / Files

- `mission-04-programs/hello.py` — the working Python program
- `mission-04-programs/README.md` — this file with the comparison table and explanation

## 8. Commit Details

**Commit message:** "Compare compilers and interpreters"
Work has been pushed to GitHub and verified.
