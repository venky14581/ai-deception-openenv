from pydantic import BaseModel
from typing import List

class Observation(BaseModel):
    failed_logins: int
    port_scans: int
    suspicious_ips: List[str]

class Action(BaseModel):
    action: str

class Reward(BaseModel):
    reward: float
    done: bool
