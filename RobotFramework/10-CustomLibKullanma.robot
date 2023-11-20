*** Settings ***
# Python dosyalarını import etmek icin Library kullanılır
Library    10-CustomLib.py
# Robot dosyalarını import etmek icin Resource kullanılır
Resource    reusableKeywords.resource
# Python dosyalarını import etmek icin Variables kullanılır
Variables    Locates.py

*** Variables ***
#


*** Test Cases ***
Test 01
    ${sailarinToplami}    Sayilari Topla    40    50
    Log To Console   ${sailarinToplami}
    Mustafa'nin keywordu    15    25
    Ekrana merhaba de


*** Keywords ***
#