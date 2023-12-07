*** Settings ***
Resource  resource.robot
Test Setup  Input Book Without Bib

*** Test Cases ***
Add Bibref Automatically
    Input  \
    Run Application
    Output Should Contain  \nReference type book added

Add Bibref Manually
    Input  kal20
    Run Application
    Output Should Contain  \nReference type book added


*** Keywords ***
Input Book Without Bib
    Input Add Command
    Input Book Without Bibref  book  kalle  kirja  2000  julkaisija