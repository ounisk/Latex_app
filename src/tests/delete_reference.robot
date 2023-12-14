*** Settings ***
Resource  resource.robot
Test Setup  Input Add Command To Add Book And Delete Bib-reference

*** Test Cases ***
Delete Bib-reference
    Input Book Reference  book  kalle  joulukuuset  2021  otava  kalle21
    Output Should Contain  \nReference type book added
    Input Delete Command
    Input Bibref  kalle21
    Output Should Contain  The reference has been deleted. Select (C)reate bib to update your bib-file.\n


*** Keywords ***
Input Add Command To Add Book And Delete Bib-reference
    Input Add Command 