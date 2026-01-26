# PLAYWRIGHT

https://playwright.dev/python/

## 1. Install tool

### 1.1. Install Python

Download and install the latest version of Python from [python.org](https://www.python.org/downloads/). Ensure that you check the box to **Add Python to PATH** during the installation process.

### 1.2. Install Make
-   **macOS:** `brew install make`
-   **Ubuntu:** `sudo apt install make`
-   **Windows:** [Follow online installation guides](https://gnuwin32.sourceforge.net/packages/make.htm).


## 2. Install dependency

Document: https://playwright.dev/python/docs/intro

```bash
pip install -r requirements.txt

playwright install

nbstripout --install
```

## 3. Run test

You need to log in first to generate a new token, which will be used to sign all tests later.

- For hanbai project

```bash
make hanbai-auth
```

### 3.1. Run test on background

Run all tests in folder/file/keyword:

```bash
make start example
```

```bash
make start hanbai/test_menu.py
```

```bash
make start-k test_menu_visible
```

### 3.2. Run test with open browser

Run all tests in folder/file/keyword:

```bash
make dev example
```

```bash
make dev hanbai/test_menu.py
```

```bash
make dev-k test_menu_visible
```

### 3.3. Run test with debug - step by step

Run all tests in file/keyword:

```bash
make debug hanbai/test_menu.py
```

```bash
make debug-k test_menu_visible
```

### 3.4. Run test with tracing

- Create tracing file for folder/file/keyword


```bash
make trace example
```

```bash
make trace hanbai/test_menu.py
```

```bash
make trace-k test_menu_visible
```

You will see file at: `traces/`

- Open trace view:

```bash
make view traces/test-menu-visible-chromium.zip
```

Tips: `Right click the file in Left Panel -> Copy Relative Path` to copy file name, not need to manual copy

## 4. Generate test

Document: https://playwright.dev/python/docs/codegen-intro

```bash
make gen demo.playwright.dev/todomvc
```

## 5. Useful script

### 5.1 Push code to github

- Commit and push code
```bash
make commit "update"
```

Or

```bash
make commit
```
After that, you need to enter commit name -> Enter
