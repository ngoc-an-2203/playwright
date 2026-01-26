hanbai-auth:
	pytest -k test_hanbai_auth_setup

#--- Run test on background ---
# Raw CLI: pytest example
start:
	pytest $(filter-out $@,$(MAKECMDGOALS))

# Raw CLI: pytest -k test_should_allow_me_to_mark_all_items_as_completed
start-k:
	pytest -k $(filter-out $@,$(MAKECMDGOALS))

#--- Run test with open browser ---
# Raw CLI: pytest --headed example
dev:
	pytest --headed $(filter-out $@,$(MAKECMDGOALS))

# Raw CLI: pytest --headed -k test_should_allow_me_to_mark_all_items_as_completed
dev-k:
	pytest --headed -k $(filter-out $@,$(MAKECMDGOALS))

#--- Run test with debug ---
# Raw CLI: PWDEBUG=1 pytest -s example
debug:
	PWDEBUG=1 pytest -s $(filter-out $@,$(MAKECMDGOALS))

# Raw CLI: PWDEBUG=1 pytest -s -k test_should_allow_me_to_mark_all_items_as_completed
debug-k:
	PWDEBUG=1 pytest -s -k $(filter-out $@,$(MAKECMDGOALS))

#--- Run test with trace ---
# Raw CLI: pytest --tracing on example
trace:
	pytest --tracing on $(filter-out $@,$(MAKECMDGOALS))

# Raw CLI: pytest --tracing on -k test_should_display_the_correct_text
trace-k:
	pytest --tracing on -k $(filter-out $@,$(MAKECMDGOALS))

# Raw CLI: playwright show-trace test-results/example-test-clear-completed-button-py-test-should-display-the-correct-text-chromium/trace.zip
view:
	playwright show-trace $(filter-out $@,$(MAKECMDGOALS))

#--- Generate test ---
# Raw CLI: playwright codegen demo.playwright.dev/todomvc
gen:
	playwright codegen $(filter-out $@,$(MAKECMDGOALS))

#--- Commit code ---
commit:
	bash ./commit.sh

# Must be end of file
%:
	@: