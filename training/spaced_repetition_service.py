from datetime import date, timedelta
from typing import Dict, List
from models import Card
from collections import defaultdict
from random import shuffle

MAX_REVIEW_INTERVAL = 60

def shuffle_cards_by_review_schedule(cards: List[Card]) -> List[Card]:
    d = defaultdict(list)
    cards.sort(key=lambda card: card.next_review)

    for card in cards:
        d[card.next_review].append(card)
    
    for key in d:
        shuffle(d[key])
    return [card for date in sorted(d.keys()) for card in d[date]]

def get_due_cards(cards: Dict[str, Card]) -> List[Card]:
    today = date.today()
    due_cards = [card for card in cards.values() if card.next_review <= today]
    due_cards = shuffle_cards_by_review_schedule(due_cards)
    return due_cards

def refresh_due_cards(due_cards: List[Card], reviewed_card: Card) -> List[Card]:    
    if reviewed_card.next_review <= date.today():
        return due_cards  # No change needed
    
    return [card for card in due_cards if card != reviewed_card]

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
