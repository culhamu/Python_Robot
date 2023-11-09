*** Settings ***
Library    String
*** Variables ***
${isim}     Mustafa
${yas}      35


*** Test Cases ***
Bu benim ilk testim
    Log To Console    ${isim} merhaba!
    ${yeniDegisken}    Set Variable    Helsinki

    ${sayi1}    Set Variable    10
    ${sayi2}    Set Variable    20
    ${toplam}    Evaluate   ${sayi1}+${sayi2}
    Log To Console    ${toplam}

    ${cumle}    Set Variable    BUNLAR BUYUK HARF
    ${kucukHarf}    Convert To Lower Case    ${cumle}
    Log To Console    ${kucukHarf}