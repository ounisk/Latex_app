*** Settings ***
Resource  resource.robot
Test Setup  Input Add Command To Add Inproceedings

*** Test Cases ***
Add Inproceedings Successfully
    Input Inproceedings Reference  inproceedings  kalle  otsikko  kirjax  otava  2001  kalle2001
    Output Should Contain  \nReference type inproceedings added

Add Inproceedings With Invalid Year
    Input Inproceedings Without Bibref  inproceedings  kalle  otsikko  kirjax  otava  2031
    Input  2023
    Input  ka23
    Run Application
    Output Should Contain  Year has to be in the range of 0-2023. Please try again.

    
*** Keywords ***
Input Add Command To Add Inproceedings
    Input Add Command 