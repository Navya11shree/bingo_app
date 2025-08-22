# import streamlit as st
# import random
# import pandas as pd
# from datetime import datetime

# # Set page config
# st.set_page_config(
#     page_title="Friday Fun Remote Work Bingo! 🎉",
#     page_icon="🎯",
#     layout="wide"
# )

# # Initialize session state
# if 'bingo_card' not in st.session_state:
#     st.session_state.bingo_card = None
# if 'marked_cells' not in st.session_state:
#     st.session_state.marked_cells = set()
# if 'player_name' not in st.session_state:
#     st.session_state.player_name = ""
# if 'game_started' not in st.session_state:
#     st.session_state.game_started = False

# # Bingo phrases for remote work
# BINGO_PHRASES = [
#     "Forgot to mute yourself",
#     "Pet appeared on camera",
#     "Delivery arrived during meeting",
#     "Wore pajama pants to video call",
#     "Said 'Can you see my screen?'",
#     "Had connection issues",
#     "Talked to your pet during work",
#     "Ate lunch at your desk",
#     "Checked personal social media",
#     "Had a virtual background fail",
#     "Joined meeting 5+ mins late",
#     "Accidentally left yourself muted",
#     "Had a snack attack at 3pm",
#     "Worked from bed",
#     "Forgot what day it was",
#     "Attended meeting in slippers",
#     "Had awkward small talk",
#     "Refreshed email obsessively",
#     "Took a 'quick' coffee break",
#     "Pretended to take notes",
#     "Had a Zoom meeting about Zoom",
#     "Wore headphones all day",
#     "Talked to yourself out loud",
#     "Checked the weather 5+ times",
#     "Made your 5th cup of coffee/tea",
#     "Had a 'quick' chat that lasted 30 mins",
#     "Organized your desk procrastinating",
#     "Answered work email after hours",
#     "Had technical difficulties",
#     "Celebrated Friday before 5pm",
#     "Wore the same shirt twice this week",
#     "Had a plant as your meeting buddy",
#     "Checked your phone during a call",
#     "Had a snack as your lunch",
#     "Used emoji reactions in chat",
#     "Had a 'camera off' day",
#     "Heard neighbor's lawnmower",
#     "Had a 15-min meeting go 45 mins",
#     "Made a grocery list during work",
#     "Googled something work-related",
#     "Had your camera at a weird angle",
#     "Said 'Sorry, I was on mute'",
#     "Worked in different rooms",
#     "Had a family member interrupt",
#     "Cleaned something instead of working",
#     "Had internet slower than your patience",
#     "Attended meeting while walking",
#     "Had a lightbulb moment at midnight"
# ]

# def generate_bingo_card():
#     """Generate a random 5x5 bingo card"""
#     selected_phrases = random.sample(BINGO_PHRASES, 24)  # 24 because center is FREE
#     card = []
#     phrase_index = 0
    
#     for i in range(5):
#         row = []
#         for j in range(5):
#             if i == 2 and j == 2:  # Center square
#                 row.append("FREE SPACE! 🎉")
#             else:
#                 row.append(selected_phrases[phrase_index])
#                 phrase_index += 1
#         card.append(row)
    
#     return card

# def check_bingo(marked_cells):
#     """Check if player has bingo"""
#     # Convert marked cells to a 5x5 grid for easier checking
#     grid = [[False for _ in range(5)] for _ in range(5)]
    
#     # Mark the center as always true (FREE space)
#     grid[2][2] = True
    
#     for cell in marked_cells:
#         if cell != (2, 2):  # Don't re-mark the center
#             row, col = cell
#             grid[row][col] = True
    
#     # Check rows
#     for row in grid:
#         if all(row):
#             return True
    
#     # Check columns
#     for col in range(5):
#         if all(grid[row][col] for row in range(5)):
#             return True
    
#     # Check diagonals
#     if all(grid[i][i] for i in range(5)):
#         return True
#     if all(grid[i][4-i] for i in range(5)):
#         return True
    
#     return False

# # Main app
# st.title("🎯 Friday Fun Remote Work Bingo! 🎉")
# st.markdown("---")

# # Game setup
# col1, col2 = st.columns([2, 1])

# with col1:
#     st.markdown("### Welcome to Friday Fun Bingo!")
#     st.markdown("Check off squares as you experience these remote work moments throughout your day!")

# with col2:
#     player_name = st.text_input("Enter your name:", value=st.session_state.player_name)
#     if player_name:
#         st.session_state.player_name = player_name

# # Generate new card button
# col_a, col_b, col_c = st.columns([1, 1, 2])
# with col_a:
#     if st.button("🎲 Generate New Card", type="primary"):
#         st.session_state.bingo_card = generate_bingo_card()
#         st.session_state.marked_cells = {(2, 2)}  # Mark center as free
#         st.session_state.game_started = True
#         st.rerun()

# with col_b:
#     if st.button("🔄 Reset Game"):
#         st.session_state.marked_cells = {(2, 2)} if st.session_state.bingo_card else set()
#         st.rerun()

# # Display the bingo card
# if st.session_state.bingo_card:
#     st.markdown("---")
#     if st.session_state.player_name:
#         st.markdown(f"### 🎮 {st.session_state.player_name}'s Bingo Card")
#     else:
#         st.markdown("### 🎮 Your Bingo Card")
    
#     # Create the bingo card grid
#     card = st.session_state.bingo_card
    
#     # Display the card
#     for i in range(5):
#         cols = st.columns(5)
#         for j in range(5):
#             with cols[j]:
#                 # Check if this cell is marked
#                 is_marked = (i, j) in st.session_state.marked_cells
                
#                 # Style based on whether it's marked
#                 if is_marked:
#                     if i == 2 and j == 2:  # Free space
#                         button_label = f"✨ {card[i][j]} ✨"
#                     else:
#                         button_label = f"✅ {card[i][j]}"
#                 else:
#                     button_label = card[i][j]
                
#                 # Create button
#                 if st.button(
#                     button_label,
#                     key=f"cell_{i}_{j}",
#                     help=f"Click to {'unmark' if is_marked and (i,j) != (2,2) else 'mark'} this square",
#                     disabled=(i == 2 and j == 2),  # Free space is always marked
#                     use_container_width=True
#                 ):
#                     if (i, j) in st.session_state.marked_cells and (i, j) != (2, 2):
#                         st.session_state.marked_cells.remove((i, j))
#                     else:
#                         st.session_state.marked_cells.add((i, j))
#                     st.rerun()
    
#     # Check for bingo
#     if check_bingo(st.session_state.marked_cells):
#         st.success("🎉 BINGO! You did it! 🎉")
#         st.balloons()
#         if st.session_state.player_name:
#             st.markdown(f"### 🏆 Congratulations {st.session_state.player_name}!")
#         st.markdown("### Share your victory with your team! 🎊")
    
#     # Game stats
#     marked_count = len(st.session_state.marked_cells)
#     st.markdown("---")
#     col1, col2, col3 = st.columns(3)
#     with col1:
#         st.metric("Squares Marked", marked_count, delta=None)
#     with col2:
#         st.metric("Squares Remaining", 25 - marked_count, delta=None)
#     with col3:
#         completion_percent = (marked_count / 25) * 100
#         st.metric("Completion", f"{completion_percent:.1f}%", delta=None)

# else:
#     st.info("👆 Click 'Generate New Card' to start playing!")
#     st.markdown("### How to Play:")
#     st.markdown("""
#     1. **Generate** a new bingo card with random remote work scenarios
#     2. **Mark squares** by clicking on them when you experience those moments
#     3. **Get 5 in a row** (horizontal, vertical, or diagonal) to win!
#     4. **Share** your victories with your team
#     5. **Have fun** and bond over shared remote work experiences!
#     """)

# # Footer
# st.markdown("---")
# st.markdown("### 🎯 Tips for Team Play:")
# st.markdown("""
# - **Share screenshots** of your cards in team chat
# - **Call out** when you mark a square during meetings
# - **First to BINGO** gets bragging rights!
# - **Play throughout the day** and see who completes their card first
# - **Generate new cards** for multiple rounds
# """)

# st.markdown("---")
# st.markdown("*Made with ❤️ for remote teams who know the struggle is real!*")





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

# Modern CSS styling
st.markdown("""
<style>
    /* Import modern font */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');
    
    /* Main app styling */
    .main > div {
        padding-top: 2rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        min-height: 100vh;
    }
    
    /* Custom font for entire app */
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Header styling */
    .main-header {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
    }
    
    /* Title styling */
    .stTitle {
        color: white !important;
        text-align: center;
        font-weight: 700;
        font-size: 3rem !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 0 !important;
    }
    
    /* Subtitle styling */
    .subtitle {
        color: rgba(255, 255, 255, 0.9);
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-weight: 300;
    }
    
    /* Card container */
    .bingo-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        border: 1px solid rgba(255, 255, 255, 0.3);
    }
    
    /* Button styling */
    .stButton > button {
        background: linear-gradient(45deg, #ff6b6b, #feca57) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        font-weight: 600 !important;
        font-family: 'Poppins', sans-serif !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2) !important;
        height: 3rem !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3) !important;
    }
    
    /* Primary button special styling */
    div[data-testid="stButton"] button[kind="primary"] {
        background: linear-gradient(45deg, #667eea, #764ba2) !important;
    }
    
    /* Bingo cell buttons */
    div[data-testid="column"] .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 500 !important;
        font-size: 0.85rem !important;
        padding: 1rem !important;
        min-height: 100px !important;
        width: 100% !important;
        text-align: center !important;
        line-height: 1.3 !important;
    }
    
    /* Marked cells */
    .marked-cell {
        background: linear-gradient(45deg, #48CAE4, #023E8A) !important;
        box-shadow: 0 0 20px rgba(72, 202, 228, 0.5) !important;
        animation: pulse 2s infinite !important;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 20px rgba(72, 202, 228, 0.5); }
        50% { box-shadow: 0 0 30px rgba(72, 202, 228, 0.8); }
        100% { box-shadow: 0 0 20px rgba(72, 202, 228, 0.5); }
    }
    
    /* Free space special styling */
    .free-space {
        background: linear-gradient(45deg, #ffd700, #ff8c00) !important;
        box-shadow: 0 0 20px rgba(255, 215, 0, 0.6) !important;
    }
    
    /* Input styling */
    .stTextInput > div > div > input {
        background: rgba(255, 255, 255, 0.1) !important;
        color: white !important;
        border: 2px solid rgba(255, 255, 255, 0.3) !important;
        border-radius: 10px !important;
        font-family: 'Poppins', sans-serif !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: rgba(255, 255, 255, 0.7) !important;
    }
    
    /* Metric styling */
    .metric-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1.5rem;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    [data-testid="metric-container"] {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 15px;
        padding: 1rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }
    
    [data-testid="metric-container"] > div {
        color: white !important;
    }
    
    /* Success message styling */
    .stSuccess {
        background: linear-gradient(45deg, #56CCF2, #2F80ED) !important;
        color: white !important;
        border-radius: 15px !important;
        border: none !important;
    }
    
    /* Info message styling */
    .stInfo {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        color: white !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
    }
    
    /* Markdown text in glassmorphism containers */
    .glass-container {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        border: 1px solid rgba(255, 255, 255, 0.2);
        margin: 1rem 0;
        color: white;
    }
    
    /* Hide hamburger menu and footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'bingo_card' not in st.session_state:
    st.session_state.bingo_card = None
if 'marked_cells' not in st.session_state:
    st.session_state.marked_cells = set()
if 'player_name' not in st.session_state:
    st.session_state.player_name = ""
if 'game_started' not in st.session_state:
    st.session_state.game_started = False

# Bingo phrases for remote work - Funny & Family-Friendly Edition
BINGO_PHRASES = [
    "Forgot to mute, everyone heard you sneeze",
    "Pet became the meeting star ⭐",
    "Doorbell rang during important call",
    "Wore business top, pajama bottom combo",
    "Said 'Can you see my screen?' 3 times",
    "WiFi decided to take a coffee break",
    "Had full conversation with your pet",
    "Ate cereal for lunch like a champion",
    "Accidentally shared wrong screen (whoops!)",
    "Virtual background made you look headless",
    "Joined meeting fashionably late (again)",
    "Talked for 2 minutes while muted 🤐",
    "Emergency snack run at 3:17 PM",
    "Turned bed into temporary office",
    "Asked 'What day is it?' seriously",
    "Rocked fuzzy slippers in video call",
    "Weather small talk lasted 10 minutes",
    "Refreshed empty inbox hopefully",
    "5-minute coffee break = 25 minutes",
    "Furiously nodded while zoning out",
    "Attended meeting about scheduling meetings",
    "Headphones became permanent head accessory",
    "Gave yourself a pep talk out loud",
    "Checked weather app like it's news",
    "Coffee cup #6 before noon ☕",
    "15-minute catch-up = 45-minute therapy",
    "Organized desk drawers to avoid work",
    "Replied to work emails at midnight",
    "Blamed 'technical difficulties' for everything",
    "Started weekend celebration at 2 PM",
    "Same shirt 3 days this week (it's clean!)",
    "Plant became your best work buddy 🌱",
    "Phone buzzed, you checked mid-sentence",
    "Granola bar dinner = gourmet meal",
    "Became emoji reaction enthusiast 😂👍",
    "Declared 'No camera Friday'",
    "Neighbor's dog joined your presentation",
    "Meeting stretched like yoga class",
    "Shopping list grew during boring call",
    "Googled 'How to look busy on camera'",
    "Camera angle made you look like giant",
    "Sorry-I-was-on-mute world record attempt",
    "Worked from 4 different rooms today",
    "Kids/family treated you like furniture",
    "Cleaned bathroom instead of spreadsheet",
    "Internet speed = dial-up nostalgia",
    "Walking meeting = treadmill multitasking",
    "3 AM eureka moment about work problem",
    "Forgot pants exist below camera line",
    "Microwave beeping ruined your point",
    "Cat walked across keyboard mid-email",
    "Pretended kitchen background was office",
    "Wore same hoodie entire week",
    "Made grocery list look like meeting notes",
    "Celebration dance for finishing task",
    "Ate lunch at 4 PM (time is a concept)",
    "Talked to screen like person was there",
    "Blamed cat for typing gibberish",
    "Had meeting while doing dishes secretly",
    "Accidentally turned on beauty filter",
    "Searched 'professional working from home'",
    "Made bed your conference room",
    "Wore sunglasses to hide tired eyes",
    "Discovered mute button has superpowers",
    "Treated houseplant like coworker",
    "Friday feeling started on Wednesday"
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
st.markdown('<div class="main-header">', unsafe_allow_html=True)
st.title("🎯 Friday Fun Remote Work Bingo!")
st.markdown('<p class="subtitle">✨ The ultimate remote work experience bingo game ✨</p>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Game setup
st.markdown('<div class="glass-container">', unsafe_allow_html=True)
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 🎮 Welcome to the Ultimate Remote Work Bingo!")
    st.markdown("Check off squares as you experience these hilarious remote work moments throughout your day!")

with col2:
    player_name = st.text_input("🏷️ Enter your name:", value=st.session_state.player_name, placeholder="Your awesome name here...")
    if player_name:
        st.session_state.player_name = player_name

st.markdown('</div>', unsafe_allow_html=True)

# Generate new card button
st.markdown('<br>', unsafe_allow_html=True)
col_a, col_b, col_c = st.columns([1, 1, 2])
with col_a:
    if st.button("🎲 Generate New Card", type="primary", help="Create a brand new bingo card!"):
        st.session_state.bingo_card = generate_bingo_card()
        st.session_state.marked_cells = {(2, 2)}  # Mark center as free
        st.session_state.game_started = True
        st.rerun()

with col_b:
    if st.button("🔄 Reset Game", help="Clear all marked squares and start fresh!"):
        st.session_state.marked_cells = {(2, 2)} if st.session_state.bingo_card else set()
        st.rerun()

# Display the bingo card
if st.session_state.bingo_card:
    st.markdown('<br><div class="bingo-card">', unsafe_allow_html=True)
    if st.session_state.player_name:
        st.markdown(f"### 🎮 {st.session_state.player_name}'s Bingo Card")
    else:
        st.markdown("### 🎮 Your Epic Bingo Card")
    
    st.markdown('<br>', unsafe_allow_html=True)
    
    # Create the bingo card grid
    card = st.session_state.bingo_card
    
    # Display the card with modern styling
    for i in range(5):
        cols = st.columns(5)
        for j in range(5):
            with cols[j]:
                # Check if this cell is marked
                is_marked = (i, j) in st.session_state.marked_cells
                
                # Style based on whether it's marked
                if is_marked:
                    if i == 2 and j == 2:  # Free space
                        button_label = f"✨ FREE SPACE! ✨"
                        button_class = "free-space"
                    else:
                        button_label = f"✅ {card[i][j]}"
                        button_class = "marked-cell"
                else:
                    button_label = card[i][j]
                    button_class = ""
                
                # Create button with enhanced styling
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
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Check for bingo
    if check_bingo(st.session_state.marked_cells):
        st.success("🎉 BINGO! You absolutely crushed it! 🎉")
        st.balloons()
        if st.session_state.player_name:
            st.markdown(f"### 🏆 Congratulations {st.session_state.player_name}! You're the BINGO Champion! 🏆")
        st.markdown("### 🎊 Share your epic victory with your team! 🎊")
    
    # Game stats with modern styling
    st.markdown('<br>', unsafe_allow_html=True)
    marked_count = len(st.session_state.marked_cells)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🎯 Squares Marked", marked_count, delta=None)
    with col2:
        st.metric("⏳ Squares Remaining", 25 - marked_count, delta=None)
    with col3:
        completion_percent = (marked_count / 25) * 100
        st.metric("📊 Completion", f"{completion_percent:.1f}%", delta=None)

else:
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    st.info("👆 Click 'Generate New Card' to start your epic bingo adventure!")
    st.markdown("### 🎯 How to Play:")
    st.markdown("""
    1. **🎲 Generate** a new bingo card with random remote work scenarios
    2. **✅ Mark squares** by clicking on them when you experience those moments
    3. **🏆 Get 5 in a row** (horizontal, vertical, or diagonal) to win!
    4. **📢 Share** your victories with your team
    5. **🎉 Have fun** and bond over shared remote work experiences!
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer with modern styling
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<div class="glass-container">', unsafe_allow_html=True)
st.markdown("### 🚀 Pro Tips for Epic Team Play:")
st.markdown("""
- **📸 Share screenshots** of your cards in team chat
- **📢 Call out** when you mark a square during meetings  
- **🥇 First to BINGO** gets ultimate bragging rights!
- **⏰ Play throughout the day** and see who completes their card first
- **🎲 Generate new cards** for multiple epic rounds
- **🎊 Celebrate victories** with your remote team family!
""")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="glass-container" style="text-align: center; margin-top: 2rem;">', unsafe_allow_html=True)
st.markdown("*✨ Crafted with ❤️ for remote teams who know the struggle is beautifully real! ✨*")
st.markdown('</div>', unsafe_allow_html=True)