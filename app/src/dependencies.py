from typing import Annotated
from fastapi import Depends
from .database import get_session, AsyncSession

# Dependency to use the session in routes
SessionDep = Annotated[AsyncSession, Depends(get_session)]