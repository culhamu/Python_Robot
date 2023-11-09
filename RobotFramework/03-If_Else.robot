*** Settings ***
#


*** Variables ***
${cumle}=       Bu benim cumlem
${sayi1}=       10
${sayi2}=       20



*** Test Cases ***
Test 01
    IF    ${sayi2} > ${sayi1}
        Log To Console    sayi2 sayi1 den büyük
        
    ELSE
        Log To Console    sayi1 sayi2 den büyük
        
    END



*** Keywords ***
#

