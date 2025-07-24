from datetime import date, timedelta
from typing import Dict, List
from models import Card

MAX_REVIEW_INTERVAL = 60
def get_due_cards(cards: Dict[str, Card]) -> List[Card]:
    today = date.today()
    return [card for card in cards.values() if card.next_review <= today]

def mark_review(card: Card, success: bool) -> None:
    today = date.today()
    card.last_reviewed = today

    if success:
        card.success_streak += 1
        card.interval = min(card.interval * 2, MAX_REVIEW_INTERVAL) if card.interval > 0 else 1
    else:
        card.success_streak = 0
        card.interval = 1

    card.next_review = today + timedelta(days=card.interval)
