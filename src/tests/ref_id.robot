*** Settings ***
Resource  resource.robot
Test Setup  Input Book Without Bib

*** Test Cases ***
Add Bibref Automatically
    Input Print Command
    Output Should Contain  ka00


*** Keywords ***
Input Book Without Bib
    Input Book Without Bibref  book  kalle  kirja  2000  julkaisija