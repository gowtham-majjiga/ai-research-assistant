from dataclasses import dataclass
from typing import Literal

SourceType = Literal["Wikipedia", "arXiv"]

@dataclass(frozen=True)
class SourceDocument:
    title: str
    snippet: str
    url: str
    source: SourceType
    score: float = 0.0
