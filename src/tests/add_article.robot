*** Settings ***
Resource  resource.robot
Test Setup  Input Add Command To Add Article

*** Test Cases ***
Add Article Successfully
    Input Article Reference  article  kalle  otsikko  julkaisu  2002  kalle2002
    Output Should Contain  Reference type article added

*** Keywords ***
Input Add Command To Add Article
    Input Add Command  