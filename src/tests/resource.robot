*** Settings ***
Library  ../AppLibrary.py

*** Keywords ***
Input Add Command
    Input  add

Input Print Command
    Input  print

Input Create Command
    Input  c

Input Book Reference
    [Arguments]  ${type}  ${author}  ${title}  ${year}  ${publisher}  ${bib_ref}
    Input  ${type}
    Input  ${author}
    Input  ${title}
    Input  ${year}
    Input  ${publisher}
    Input  ${bib_ref}
    Run Application

Input Book Without Bibref
    [Arguments]  ${type}  ${author}  ${title}  ${year}  ${publisher}
    Input  ${type}
    Input  ${author}
    Input  ${title}
    Input  ${year}
    Input  ${publisher}

Input Book Without Publisher
    [Arguments]  ${type}  ${author}  ${title}  ${year}
    Input  ${type}
    Input  ${author}
    Input  ${title}
    Input  ${year}

Input Article Reference
    [Arguments]  ${type}  ${author}  ${title}  ${journal}  ${year}  ${bib_ref}
    Input  ${type}
    Input  ${author}
    Input  ${title}
    Input  ${journal}
    Input  ${year}
    Input  ${bib_ref}
    Run Application

Input Article Without Bibref
    [Arguments]  ${type}  ${author}  ${title}  ${journal}  ${year}
    Input  ${type}
    Input  ${author}
    Input  ${title}
    Input  ${journal}
    Input  ${year}

Input Inproceedings Reference
    [Arguments]  ${type}  ${author}  ${title}  ${book_title}  ${publisher}  ${year}  ${bib_ref}
    Input  ${type}
    Input  ${author}
    Input  ${title}
    Input  ${book_title}
    Input  ${publisher}
    Input  ${year}
    Input  ${bib_ref}
    Run Application

Input Inproceedings Without Bibref
    [Arguments]  ${type}  ${author}  ${title}  ${book_title}  ${publisher}  ${year}
    Input  ${type}
    Input  ${author}
    Input  ${title}
    Input  ${book_title}
    Input  ${publisher}
    Input  ${year}

Input File Name
    [Arguments]  ${filename}
    Input  ${filename}
    Run Application
