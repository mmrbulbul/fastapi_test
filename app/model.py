from datetime import datetime, timezone
from typing import Optional

from sqlmodel import Field, SQLModel


class RecipeBase(SQLModel):
    title: str = Field(max_length=100, nullable=False)
    making_time: str = Field(max_length=100, nullable=False)
    serves: str = Field(max_length=100, nullable=False)
    ingredients: str = Field(max_length=300, nullable=False)
    cost: int = Field(nullable=False)
    

class Recipe(RecipeBase, table=True):
    __tablename__ = "recipes"
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: Optional[datetime] = Field(default_factory= lambda: datetime.now(timezone.utc))
    updated_at: Optional[datetime] = Field(default_factory= lambda: datetime.now(timezone.utc), sa_column_kwargs={"onupdate": datetime.now(timezone.utc)})

class Recipies(SQLModel):
    recipes: list[Recipe]

class RecipeUpdateOut(SQLModel):
    message: str = Field(default="Recipe successfully updated!")
    recipe: Recipe