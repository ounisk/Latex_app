*** Settings ***
Resource  resource.robot
Test Setup  Input Add Command To Add Article

*** Test Cases ***
Add Article Successfully
    Input Article Reference  article  kalle  otsikko  julkaisu  2002  kalle2002
    Output Should Contain  \nReference type article added

Add Article Wiht Invalid Year
    Input Article Reference  article  kalle  otsikko  julkaisu  2032  kalle2032
    Output Should Contain  Year has to be in the range of 0-2023. Please try again.
    

*** Keywords ***
Input Add Command To Add Article
    Input Add Command  