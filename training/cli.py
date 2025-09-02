import curses
from storage import load_data, save_data
from spaced_repetition_service import get_due_cards, mark_review, refresh_due_cards
from sync_training_data import update_training_data

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()

    cards = load_data()
    due_cards = get_due_cards(cards)

    if not due_cards:
        stdscr.addstr(0, 0, "🎉 No cards due for review today!")
        stdscr.refresh()
        stdscr.getch()
        return

    current_selection = 0
    scroll_offset = 0  # Track the scroll position

    while True:
        stdscr.clear()
        stdscr.addstr(0, 0, "🧠 Cards due today (Use ↑ ↓ to navigate, Enter to select, q to quit):")
        
        max_height, max_width = stdscr.getmaxyx()
        display_limit = max_height - 3  # Reserve space for header and footer

        for idx, card in enumerate(due_cards[scroll_offset:scroll_offset + display_limit]):
            actual_idx = idx + scroll_offset
            if actual_idx == current_selection:
                stdscr.attron(curses.A_REVERSE)
            stdscr.addstr(idx + 2, 2, f"{card.title[:max_width - 2]} | {card.next_review}")
            
            if actual_idx == current_selection:
                stdscr.attroff(curses.A_REVERSE)

        if scroll_offset > 0:
            stdscr.addstr(1, 0, "↑ More cards above")
        if scroll_offset + display_limit < len(due_cards):
            stdscr.addstr(max_height - 1, 0, "↓ More cards below")

        key = stdscr.getch()

        if key == curses.KEY_UP:
            if current_selection > 0:
                current_selection -= 1
            if current_selection < scroll_offset:
                scroll_offset -= 1
        elif key == curses.KEY_DOWN:
            if current_selection < len(due_cards) - 1:
                current_selection += 1
            if current_selection >= scroll_offset + display_limit:
                scroll_offset += 1
        elif key in (10, 13):  # Enter
            selected = due_cards[current_selection]
            review_card(stdscr, selected)
            result = review_card(stdscr, selected)
            
            if result is None:
                continue  # user chose to quit

            mark_review(selected, result)
            save_data(cards)

            due_cards = refresh_due_cards(due_cards, selected)
            
            if not due_cards:
                stdscr.clear()
                stdscr.addstr(0, 0, "✅ All cards reviewed for today.")
                stdscr.refresh()
                stdscr.getch()
                break
            current_selection = min(current_selection, len(due_cards) - 1)
            scroll_offset = max(0, min(scroll_offset, current_selection - display_limit + 1))
        elif key == ord('q'):
            break

def review_card(stdscr, card):
    stdscr.clear()
    stdscr.addstr(0, 0, f"📚 {card.title}")
    stdscr.addstr(2, 0, f"🤔 Did you recall \"{card.title}\" correctly?")
    stdscr.addstr(3, 0, "y = Yes | n = No | q = Abort")
    stdscr.refresh()

    while True:
        key = stdscr.getch()
        if key in (ord('y'), ord('Y')):
            return True
        elif key in (ord('n'), ord('N')):
            return False
        elif key in (ord('q'), ord('Q')):
            return None  # exit gracefully

if __name__ == "__main__":
    update_training_data()
    curses.wrapper(main)
