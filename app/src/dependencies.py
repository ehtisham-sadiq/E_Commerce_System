
from typing import Annotated
from fastapi import Depends
from ..src.database import get_session, AsyncSession

SessionDep = Annotated[AsyncSession, Depends(get_session)]