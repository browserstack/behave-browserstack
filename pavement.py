from paver.easy import *
from paver.setuputils import setup
import threading, os, platform

setup(
    name = "behave-browserstack",
    version = "0.1.0",
    author = "BrowserStack",
    author_email = "support@browserstack.com",
    description = ("Behave Integration with BrowserStack"),
    license = "MIT",
    keywords = "example selenium browserstack",
    url = "https://github.com/browserstack/lettuce-browserstack",
    packages=['features']
)

def run_behave_test(config, feature, task_id=0):
    if platform.system() == 'Windows':
        sh('SET CONFIG_FILE=config/%s.json & SET TASK_ID=%s & behave features/%s.feature' % (config, task_id, feature))
    else:
        sh('export CONFIG_FILE=config/%s.json && export TASK_ID=%s && behave features/%s.feature' % (config, task_id, feature))

@task
@consume_nargs(1)
def run(args):
    """Run single, local and parallel test using different config."""
    if args[0] in ('single', 'local'):
        run_behave_test(args[0], args[0])
    else:
        jobs = []
        for i in range(4):
            p = threading.Thread(target=run_behave_test,args=(args[0], "single",i))
            jobs.append(p)
            p.start()

        for th in jobs:
         th.join()

@task
def test():
    """Run all tests"""
    sh("paver run single")
    sh("paver run local")
    sh("paver run parallel")
