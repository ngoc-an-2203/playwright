# PLAYWRIGHT

https://playwright.dev/python/

## 1. Install Python

Download and install the latest version of Python from [python.org](https://www.python.org/downloads/). Ensure that you check the box to **Add Python to PATH** during the installation process.


## 2. Install dependency

Document: https://playwright.dev/python/docs/intro

```bash
pip install -r requirements.txt

playwright install
```	

## 3. Run test

You need to Login first to generate new token, using to signed all test later:

- For hanbai project

```bash
pytest -k  test_hanbai_auth_setup
```

### 3.1. Run test on background

- Run all tests in folder:

```bash
pytest example
```

- Run specific test file:

```bash
pytest example/test_clear_completed_button.py example/test_counter.py
```

- Run specific test case:
```bash
pytest example/test_mark_all_as_completed.py -k test_should_allow_me_to_mark_all_items_as_completed
```

Or use this (might conflict if test names are duplicated)

```bash
pytest -k test_should_allow_me_to_mark_all_items_as_completed
```

### 3.2. Run test with open browser

```bash
pytest --headed
```

You can run trace with specific folder/file/test case (see example at [3.1.](#31-run-test-on-background)). Example: 

```bash
pytest --headed -k test_should_allow_me_to_mark_all_items_as_completed
```

### 3.3. Debug test

```bash
PWDEBUG=1 pytest -s
```

You can run trace with specific folder/file/test case (see example at [3.1.](#31-run-test-on-background)). Example: 

```bash
PWDEBUG=1 pytest -s -k test_should_allow_me_to_mark_all_items_as_completed
```

### 3.4. Tracing viewer

- Create trace file

```bash
pytest --tracing on
```

You can run trace with specific folder/file/test case (see example at [3.1.](#31-run-test-on-background)). Example: 

```bash
pytest --tracing on -k test_should_display_the_correct_text
```

You will see file at: `test-results/example-test-clear-completed-button-py-test-should-display-the-correct-text-chromium/trace.zip`

- Open trace view:

```bash
playwright show-trace test-results/example-test-clear-completed-button-py-test-should-display-the-correct-text-chromium/trace.zip
```

Tips: `Right click the file in Left Panel -> Copy Relative Path` to copy file name, not need to manual copy

## 4. Generate test

Document: https://playwright.dev/python/docs/codegen-intro

```bash
playwright codegen demo.playwright.dev/todomvc
```

## 5. Useful script

### 5.1 Push code to github

- You need to run this first (one time):

```bash
chmod +x ./commit.sh
```

- Commit and push code
```bash
./commit.sh
```

After that, you need to enter commit name -> Enter