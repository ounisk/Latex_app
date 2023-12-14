*** Settings ***
Resource  resource.robot
Test Setup  Input Book To References

*** Test Cases ***
Print Summary Successfully
    Input Summary Command
    Run Application
    Output Should Contain  \nReference Summary\n

Print All References Successfully
    Input Print Command
    Run Application
    Output Should Contain  \n\n***REFERENCES***\n

*** Keywords ***
Input Book To References
    Input Add Command
    Input Book Reference  book  otsikko  kalle  2000  otava  kalle2000    
