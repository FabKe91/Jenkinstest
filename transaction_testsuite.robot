*** Settings ***
Documentation     Example test cases using the keyword-driven testing approach.
...
...               All tests contain a workflow constructed from keywords in
...               ``TRXLibrary.py``. Creating new tests or editing
...               existing is easy even for people without programming skills.
...
...               The _keyword-driven_ appoach works well for normal test
...               automation, but the _gherkin_ style might be even better
...               if also business people need to understand tests. If the
...               same workflow needs to repeated multiple times, it is best
...               to use to the _data-driven_ approach.
Library           TRXLibrary.py

*** Test Cases ***
Send Valid Transaction
    [Tags]     TES-23

    Trigger Transaction    TEST
    Result should be    TEST

#
#Send invalid Transaction
#    [Tags]     TES-11
#
#    # Negativtest:
#    Trigger Transaction    x0815
#    Result should be    x0815
#

