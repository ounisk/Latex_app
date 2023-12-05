*** Settings ***
Resource  resource.robot
Test Setup  Input Add Command To Add Inproceedings

*** Test Cases ***
Add Inproceedings Successfully
    Input Inproceedings Reference  inproceedings  kalle  otsikko  2001  kirjax  otava  kalle2001
    Output Should Contain  \nReference type inproceedings added

Add Inproceedings With Invalid Year
    Input Inproceedings Reference  inproceedings  kalle  otsikko  2223  kirjax  otava  kalle2223
    Output Should Contain  Year has to be in the range of 0-2023. Please try again.

    
*** Keywords ***
Input Add Command To Add Inproceedings
    Input Add Command 