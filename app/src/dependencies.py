from typing import Annotated
from databases import get_session, Session
from fastapi import Depends

SessionDep = Annotated[Session, Depends(get_session)]