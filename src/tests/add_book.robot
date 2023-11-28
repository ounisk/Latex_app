*** Settings ***
Resource  resource.robot
Test Setup  Input Add Command To Add Book

*** Test Cases ***
Add Book Successfully
    Input Book Reference  book  kalle  otsikko  2000  otava  kalle2000
    Output Should Contain  Reference type book added

*** Keywords ***
Input Add Command To Add Book
    Input Add Command  
