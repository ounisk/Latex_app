*** Settings ***
Resource  resource.robot
Test Setup  Input Add Command To Add Article

*** Test Cases ***
Add Article Successfully
    Input Article Reference  article  kalle  otsikko  julkaisu  2023  kalle2002
    Output Should Contain  \nReference type article added

Add Article With Invalid Year
    Input Article Without Bibref  article  kalle  otsikko  julkaisu  2032
    Input  2022
    Input  ka22
    Run Application
    Output Should Contain  Year has to be in the range of 0-2023. Please try again.
    

*** Keywords ***
Input Add Command To Add Article
    Input Add Command  