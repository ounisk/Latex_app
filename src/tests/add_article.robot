*** Settings ***
Resource  resource.robot
Test Setup  Input Add Command To Add Article

*** Test Cases ***
Add Article Successfully
    Input Article Reference  article  kalle  otsikko  2002  julkaisu  kalle2002
    Output Should Contain  \nReference type article added

Add Article With Invalid Year
    Input Article Reference  article  kalle  otsikko  2032  julkaisu  kalle2032
    Output Should Contain  Year has to be in the range of 0-2023. Please try again.
    

*** Keywords ***
Input Add Command To Add Article
    Input Add Command  