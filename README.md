## Introduction:

This is a course project for a Software Engineering course at the University of Helsinki during fall 2023. The software is an application where the user can input references (e.g. for bachelor's thesis) and the application will convert the references into BibTeX-format in a .bib-file.


## Documentation:

[Product ja sprint backlog](https://docs.google.com/spreadsheets/d/1vIzl9-QaEVPuQLQGrVproVWpNlVGVxZaNG2fZBDroAM/edit?usp=sharing)


## Definition of Done:
### Functionality
- User story fully implemented
- "Works as described", including user documentation updated. 
### Code quality
- Peer reviewed
- Clean, commented and maintainable
- Pylint runs with > 9.0 score
### Testing
- Unit tests
- Tests are automated where possible
- Robot framework testing started
### Documentation
- Code commented reasonably well
- User manual up to date
### Integration
- User story integrated into main codebase (Trunk)
- Application works as intended

## CI:
![GHA workflow badge](https://github.com/ounisk/latex_app/workflows/CI/badge.svg)
[![codecov](https://codecov.io/gh/ounisk/Latex_app/graph/badge.svg?token=9W72J2BX0L)](https://codecov.io/gh/ounisk/Latex_app)

## Instructions for use

Install dependencies with command:

```bash
poetry install
```

Enter virtual environment with command:

```bash
poetry shell
```

Now the app will start with command:

```bash
python3 src/index.py
```

Available command options within the app are shown inside the parentheses.
