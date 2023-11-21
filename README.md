## Documentation:

[Product ja sprint backlog](https://docs.google.com/spreadsheets/d/1vIzl9-QaEVPuQLQGrVproVWpNlVGVxZaNG2fZBDroAM/edit?usp=sharing)


## Definition of Done:
### Functionality
- User story fully implemented
- "Works as described" 
### Code quality
- Peer reviewed
- Clean, commented and maintainable
- Pylint ?
### Testing
- Unit tests
- ...
### Documentation
- Code commented
- User manual up to date
### Integration
- User story integrated into main codebase (Trunk)
- Application works as intended

## CI:
![GHA workflow badge](https://github.com/ounisk/latex_app/workflows/CI/badge.svg)

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