from dataclasses import dataclass
from datetime import date
from typing import Dict

@dataclass
class Card:
    title: str
    last_reviewed: date
    next_review: date
    interval: int
    success_streak: int

def dict_to_card(card_id: str, data: Dict) -> Card:
    return Card(
        title=data.get("title", card_id),
        last_reviewed=date.fromisoformat(data["last_reviewed"]),
        next_review=date.fromisoformat(data["next_review"]),
        interval=int(data["interval"]),
        success_streak=int(data["success_streak"])
    )

def card_to_dict(card: Card) -> Dict:
    return {
        "title": card.title,
        "last_reviewed": card.last_reviewed.isoformat(),
        "next_review": card.next_review.isoformat(),
        "interval": card.interval,
        "success_streak": card.success_streak
    }
