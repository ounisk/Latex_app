*** Settings ***
Resource  resource.robot
Test Setup  Input Add Command To Add Inproceedings

*** Test Cases ***
Add Inproceedings Successfully
    Input Inproceedings Reference  inproceedings  kalle  otsikko  kirjax  otava  2001  kalle2001
    Output Should Contain  Reference type inproceedings added

*** Keywords ***
Input Add Command To Add Inproceedings
    Input Add Command  