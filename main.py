from fastapi import FastAPI, HTTPException, Request
from app.db import create_db_and_tables, drop_db_and_tables
from app.model import RecipeBase, Recipe, Recipies
from app import crud
from app.deps import SessionDep
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# @app.on_event("shutdown")
# def on_shutdown():
#     drop_db_and_tables()
    
# Custom handler for validation errors (422 Unprocessable Entity)
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={
            "message": "Recipe creation failed!",
            "required": "title, making_time, serves, ingredients, cost"
            },
    )

@app.get("/")
async def root():
    return {"message": "Welcome to the Recipe API!"}

@app.get("/recipes", response_model=Recipies)
async def get_recipes(session: SessionDep):
    recipes = crud.get_recipes(session=session)
    print("here", recipes)
    return recipes

@app.get("/recipes/{id}", response_model=Recipe)
async def get_recipe(id: int, session: SessionDep):
    recipe = crud.get_recipe_by_id(session=session, recipe_id=id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.post("/recipes", response_model=Recipe)
async def create_recipe(recipe_in: RecipeBase, session: SessionDep):
    recipe = crud.create_recipe(session=session, reciepe_create=recipe_in)
    return recipe

@app.patch("/recipes/{id}")
async def update_recipe(id: int, recipe_in: RecipeBase, session: SessionDep):
    updated_recipe = crud.update_recipe(session=session, recipe_id=id, recipe_update=recipe_in)
    if not updated_recipe:
        return JSONResponse(
        status_code=422,
        content={
            "message": "Recipe update failed!",
            "details": "Either recipe id or update parameter was not correct."
            },
    )
    return updated_recipe

@app.delete("/recipes/{id}")
async def delete_recipe(id: int, session: SessionDep):
    status = crud.delete_recipe(session=session, recipe_id=id)
    if status:
        return {  "message": "Recipe successfully removed!" }
    else:
        return { "message": "No recipe found" }