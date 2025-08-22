import streamlit as st
import random
import pandas as pd
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Friday Fun Remote Work Bingo! 🎉",
    page_icon="🎯",
    layout="wide"
)

# Initialize session state
if 'bingo_card' not in st.session_state:
    st.session_state.bingo_card = None
if 'marked_cells' not in st.session_state:
    st.session_state.marked_cells = set()
if 'player_name' not in st.session_state:
    st.session_state.player_name = ""
if 'game_started' not in st.session_state:
    st.session_state.game_started = False

# Bingo phrases for remote work
BINGO_PHRASES = [
    "Forgot to mute yourself",
    "Pet appeared on camera",
    "Delivery arrived during meeting",
    "Wore pajama pants to video call",
    "Said 'Can you see my screen?'",
    "Had connection issues",
    "Talked to your pet during work",
    "Ate lunch at your desk",
    "Checked personal social media",
    "Had a virtual background fail",
    "Joined meeting 5+ mins late",
    "Accidentally left yourself muted",
    "Had a snack attack at 3pm",
    "Worked from bed",
    "Forgot what day it was",
    "Attended meeting in slippers",
    "Had awkward small talk",
    "Refreshed email obsessively",
    "Took a 'quick' coffee break",
    "Pretended to take notes",
    "Had a Zoom meeting about Zoom",
    "Wore headphones all day",
    "Talked to yourself out loud",
    "Checked the weather 5+ times",
    "Made your 5th cup of coffee/tea",
    "Had a 'quick' chat that lasted 30 mins",
    "Organized your desk procrastinating",
    "Answered work email after hours",
    "Had technical difficulties",
    "Celebrated Friday before 5pm",
    "Wore the same shirt twice this week",
    "Had a plant as your meeting buddy",
    "Checked your phone during a call",
    "Had a snack as your lunch",
    "Used emoji reactions in chat",
    "Had a 'camera off' day",
    "Heard neighbor's lawnmower",
    "Had a 15-min meeting go 45 mins",
    "Made a grocery list during work",
    "Googled something work-related",
    "Had your camera at a weird angle",
    "Said 'Sorry, I was on mute'",
    "Worked in different rooms",
    "Had a family member interrupt",
    "Cleaned something instead of working",
    "Had internet slower than your patience",
    "Attended meeting while walking",
    "Had a lightbulb moment at midnight"
]

def generate_bingo_card():
    """Generate a random 5x5 bingo card"""
    selected_phrases = random.sample(BINGO_PHRASES, 24)  # 24 because center is FREE
    card = []
    phrase_index = 0
    
    for i in range(5):
        row = []
        for j in range(5):
            if i == 2 and j == 2:  # Center square
                row.append("FREE SPACE! 🎉")
            else:
                row.append(selected_phrases[phrase_index])
                phrase_index += 1
        card.append(row)
    
    return card

def check_bingo(marked_cells):
    """Check if player has bingo"""
    # Convert marked cells to a 5x5 grid for easier checking
    grid = [[False for _ in range(5)] for _ in range(5)]
    
    # Mark the center as always true (FREE space)
    grid[2][2] = True
    
    for cell in marked_cells:
        if cell != (2, 2):  # Don't re-mark the center
            row, col = cell
            grid[row][col] = True
    
    # Check rows
    for row in grid:
        if all(row):
            return True
    
    # Check columns
    for col in range(5):
        if all(grid[row][col] for row in range(5)):
            return True
    
    # Check diagonals
    if all(grid[i][i] for i in range(5)):
        return True
    if all(grid[i][4-i] for i in range(5)):
        return True
    
    return False

# Main app
st.title("🎯 Friday Fun Remote Work Bingo! 🎉")
st.markdown("---")

# Game setup
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Welcome to Friday Fun Bingo!")
    st.markdown("Check off squares as you experience these remote work moments throughout your day!")

with col2:
    player_name = st.text_input("Enter your name:", value=st.session_state.player_name)
    if player_name:
        st.session_state.player_name = player_name

# Generate new card button
col_a, col_b, col_c = st.columns([1, 1, 2])
with col_a:
    if st.button("🎲 Generate New Card", type="primary"):
        st.session_state.bingo_card = generate_bingo_card()
        st.session_state.marked_cells = {(2, 2)}  # Mark center as free
        st.session_state.game_started = True
        st.rerun()

with col_b:
    if st.button("🔄 Reset Game"):
        st.session_state.marked_cells = {(2, 2)} if st.session_state.bingo_card else set()
        st.rerun()

# Display the bingo card
if st.session_state.bingo_card:
    st.markdown("---")
    if st.session_state.player_name:
        st.markdown(f"### 🎮 {st.session_state.player_name}'s Bingo Card")
    else:
        st.markdown("### 🎮 Your Bingo Card")
    
    # Create the bingo card grid
    card = st.session_state.bingo_card
    
    # Display the card
    for i in range(5):
        cols = st.columns(5)
        for j in range(5):
            with cols[j]:
                # Check if this cell is marked
                is_marked = (i, j) in st.session_state.marked_cells
                
                # Style based on whether it's marked
                if is_marked:
                    if i == 2 and j == 2:  # Free space
                        button_label = f"✨ {card[i][j]} ✨"
                    else:
                        button_label = f"✅ {card[i][j]}"
                else:
                    button_label = card[i][j]
                
                # Create button
                if st.button(
                    button_label,
                    key=f"cell_{i}_{j}",
                    help=f"Click to {'unmark' if is_marked and (i,j) != (2,2) else 'mark'} this square",
                    disabled=(i == 2 and j == 2),  # Free space is always marked
                    use_container_width=True
                ):
                    if (i, j) in st.session_state.marked_cells and (i, j) != (2, 2):
                        st.session_state.marked_cells.remove((i, j))
                    else:
                        st.session_state.marked_cells.add((i, j))
                    st.rerun()
    
    # Check for bingo
    if check_bingo(st.session_state.marked_cells):
        st.success("🎉 BINGO! You did it! 🎉")
        st.balloons()
        if st.session_state.player_name:
            st.markdown(f"### 🏆 Congratulations {st.session_state.player_name}!")
        st.markdown("### Share your victory with your team! 🎊")
    
    # Game stats
    marked_count = len(st.session_state.marked_cells)
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Squares Marked", marked_count, delta=None)
    with col2:
        st.metric("Squares Remaining", 25 - marked_count, delta=None)
    with col3:
        completion_percent = (marked_count / 25) * 100
        st.metric("Completion", f"{completion_percent:.1f}%", delta=None)

else:
    st.info("👆 Click 'Generate New Card' to start playing!")
    st.markdown("### How to Play:")
    st.markdown("""
    1. **Generate** a new bingo card with random remote work scenarios
    2. **Mark squares** by clicking on them when you experience those moments
    3. **Get 5 in a row** (horizontal, vertical, or diagonal) to win!
    4. **Share** your victories with your team
    5. **Have fun** and bond over shared remote work experiences!
    """)

# Footer
st.markdown("---")
st.markdown("### 🎯 Tips for Team Play:")
st.markdown("""
- **Share screenshots** of your cards in team chat
- **Call out** when you mark a square during meetings
- **First to BINGO** gets bragging rights!
- **Play throughout the day** and see who completes their card first
- **Generate new cards** for multiple rounds
""")

st.markdown("---")
st.markdown("*Made with ❤️ for remote teams who know the struggle is real!*")