from pydantic import BaseModel
from typing import List, Optional, Dict, Any


class Observation(BaseModel):
    failed_logins: int
    port_scans: int
    suspicious_ips: List[str]
    total_requests: Optional[int] = 0
    attack_types: Optional[List[str]] = []


class Action(BaseModel):
    action: str


class Reward(BaseModel):
    reward: float
    done: bool
    info: Optional[Dict[str, Any]] = {}
