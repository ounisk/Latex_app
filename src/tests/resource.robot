*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Add Command
    Input  add

Input Print Command
    Input  print

Input Create Command
    Input  create bib

Input References
    [Arguments]  ${type}  ${author}  ${title}  ${year}  ${publisher}  ${bib_ref}
    Input  ${type}
    Input  ${author}
    Input  ${title}
    Input  ${year}
    Input  ${publisher}
    Input  ${bib_ref}
    Run Application