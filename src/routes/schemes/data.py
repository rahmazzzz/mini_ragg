from pydantic import BaseModel
from typing import Optional

class ProcessRequest(BaseModel):
    file_id: str 
    chunk_size: Optional[int] = 512000  # Default chunk size of 512KB
    overlap_size: Optional[int] = 100  # Default overlap size of 100
    do_reset : Optional[int] = 0  # Default to not reset