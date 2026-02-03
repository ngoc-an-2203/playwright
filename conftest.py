import os
import shutil

def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing test collection and execution.
    """
    # This hook ensures that the code only runs on the master node,
    # not on any of the worker nodes.
    if not hasattr(session.config, "workerinput"):
        traces_dir = "traces"
        if os.path.exists(traces_dir):
            shutil.rmtree(traces_dir)
        os.makedirs(traces_dir)
