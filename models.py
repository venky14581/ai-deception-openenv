from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any


class Observation(BaseModel):
    failed_logins: int
    port_scans: int
    suspicious_ips: List[str] = Field(default_factory=list)
    total_requests: Optional[int] = 0
    attack_types: List[str] = Field(default_factory=list)


class Action(BaseModel):
    action: str


class Reward(BaseModel):
    reward: float
    done: bool
    info: Dict[str, Any] = Field(default_factory=dict)