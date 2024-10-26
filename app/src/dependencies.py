from fastapi import Depends
from app.src.database import get_session, AsyncSession
from typing import Annotated
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Dependency to use the session in routes
SessionDep = Annotated[AsyncSession, Depends(get_session)]

async def get_session_with_logging() -> AsyncSession:
    """Get a database session with logging."""
    session = await get_session()
    logger.info("Database session obtained.")
    return session
