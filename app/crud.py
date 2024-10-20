from sqlmodel import Session, select

from app.model import Recipe, RecipeUpdateOut, Recipies


def create_recipe(*, session: Session, reciepe_create: Recipe) -> Recipe | None:
    db_obj = Recipe.validate(reciepe_create)
    session.add(db_obj)
    session.commit()
    session.refresh(db_obj)
    return db_obj


def get_recipe_by_id(*, session: Session, recipe_id: int) -> Recipe | None:
    statement = select(Recipe).where(Recipe.id == recipe_id)
    db_obj = session.exec(statement).first()
    return db_obj

def get_recipes(*, session: Session) -> list[Recipe]:
    statement = select(Recipe)
    db_obj = session.exec(statement).all()
    return Recipies(recipes=db_obj)

def delete_recipe(*, session: Session, recipe_id: int) -> bool:
    db_obj = get_recipe_by_id(session=session, recipe_id=recipe_id)
    if db_obj:
        session.delete(db_obj)
        session.commit()
        return True
    return False

def update_recipe(*, session: Session, recipe_id: int, recipe_update: Recipe) -> RecipeUpdateOut | None:
    db_obj = get_recipe_by_id(session=session, recipe_id=recipe_id)
    if db_obj:
        db_obj.title = recipe_update.title
        db_obj.making_time = recipe_update.making_time
        db_obj.serves = recipe_update.serves
        db_obj.ingredients = recipe_update.ingredients
        db_obj.cost = recipe_update.cost
        session.add(db_obj)
        session.commit()
        session.refresh(db_obj)
        return RecipeUpdateOut(recipe=db_obj)
    return None