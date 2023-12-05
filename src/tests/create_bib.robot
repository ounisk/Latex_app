*** Settings ***
Resource  resource.robot
Test Setup  Input Add Command And Input Book To Create Bib

*** Test Cases ***
Create Bib File Successfully
    Input Book Reference  book  Taavetti  Jouluihme  2000  otava  Taa00
    Output Should Contain  \nReference type book added
    Input Create Command
    Input File Name  robot_references.bib
    Output Should Contain  Your BibTeX file 'robot_references.bib' has been created\n

*** Keywords ***
Input Add Command And Input Book To Create Bib
    Input Add Command