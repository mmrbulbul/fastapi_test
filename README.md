# Basic overview 
- `main.py` entrypoint of the app. 

    Contains all the endpoints. All were written into main.py as it was a fairly small api.

- `app/config.py`. Configaration for the app.
- `app/crud.py`. All CRUD operation for database.
- `app/db.py`. DB initialization and helper functions
- `apps/deps.py` Contains dependency needed by the endpoints.
- `app/model.py` Database model.




# Running the app
Try this: 
```bash
./scripts/run.sh
```

# Notes:
- Code was tested on **Python 3.10.15**
- All the python requirements has been added to `requirements.txt`