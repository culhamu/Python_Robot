*** Settings ***
Library    SeleniumLibrary



*** Test Cases ***
Test01
    Open Browser    https://www.google.com    chrome
    Sleep    1
    Click Button    Accept all
    Sleep    1
    Input Text    id=APjFqb    Robot Framework
