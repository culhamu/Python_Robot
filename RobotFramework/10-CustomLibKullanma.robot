*** Settings ***
Library    10-CustomLib.py


*** Variables ***
#


*** Test Cases ***
Test 01
    ${sailarinToplami}    Sayilari Topla    40    50
    Log To Console   ${sailarinToplami}
    Mustafa'nin keywordu    15    25



*** Keywords ***
#