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
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for cool UI/UX
st.markdown("""
<style>
/* Import cool font */
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

/* Global styles */
.stApp {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    font-family: 'Poppins', sans-serif;
}

/* Header styles */
.main-header {
    text-align: center;
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4, #45B7D1, #96CEB4);
    background-size: 400% 400%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: gradient 3s ease infinite;
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Card container */
.game-container {
    background: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(20px);
    border-radius: 20px;
    padding: 2rem;
    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
    border: 1px solid rgba(255,255,255,0.2);
    margin: 2rem 0;
}

/* Player info section */
.player-section {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 1.5rem;
    border-radius: 15px;
    margin-bottom: 2rem;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

/* Bingo grid styling */
.bingo-grid {
    display: grid;
    grid-template-columns: repeat(5, 1fr);
    gap: 10px;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

/* Stats container */
.stats-container {
    background: linear-gradient(135deg, #FF6B6B, #4ECDC4);
    color: white;
    padding: 1.5rem;
    border-radius: 15px;
    margin: 2rem 0;
    text-align: center;
}

/* Celebration styles */
.celebration {
    background: linear-gradient(45deg, #FFD700, #FFA500, #FF6347);
    background-size: 400% 400%;
    animation: gradient 2s ease infinite;
    color: white;
    padding: 2rem;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 0 50px rgba(255, 215, 0, 0.5);
    margin: 2rem 0;
}

/* Button animations */
.stButton > button {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    border-radius: 10px;
    border: none;
    font-weight: 500;
}

.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.2);
}

/* Input styling */
.stTextInput > div > div > input {
    border-radius: 10px;
    border: 2px solid #e1e5e9;
    transition: all 0.3s ease;
}

.stTextInput > div > div > input:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
}

/* Progress bar */
.progress-container {
    background: rgba(255,255,255,0.2);
    border-radius: 10px;
    padding: 10px;
    margin: 20px 0;
}

/* Floating elements */
.floating {
    animation: float 3s ease-in-out infinite;
}

@keyframes float {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

/* Pulse animation for important elements */
.pulse {
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

/* Hide default streamlit elements */
.stDeployButton {display:none;}
footer {visibility: hidden;}
.stDecoration {display:none;}

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
                row.append("🎉 FREE SPACE! 🎉")
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

# Main app with cool header
st.markdown('<h1 class="main-header">🎯 Friday Fun Remote Work Bingo! 🎉</h1>', unsafe_allow_html=True)

# Game container
st.markdown('<div class="game-container">', unsafe_allow_html=True)

# Player section
st.markdown('<div class="player-section">', unsafe_allow_html=True)
col1, col2 = st.columns([3, 2])

with col1:
    st.markdown("### 🚀 Welcome to the Ultimate Remote Work Comedy!")
    st.markdown("**Check off squares as you experience these hilarious remote work moments!**")

with col2:
    player_name = st.text_input("🎮 Enter your player name:", value=st.session_state.player_name, placeholder="Your awesome name here...")
    if player_name:
        st.session_state.player_name = player_name

st.markdown('</div>', unsafe_allow_html=True)

# Control buttons with cool styling
col_a, col_b, col_c, col_d = st.columns([1, 1, 1, 1])
with col_a:
    if st.button("🎲 Generate New Card", type="primary", help="Get a fresh, random bingo card!"):
        st.session_state.bingo_card = generate_bingo_card()
        st.session_state.marked_cells = {(2, 2)}  # Mark center as free
        st.session_state.game_started = True
        st.rerun()

with col_b:
    if st.button("🔄 Reset Game", help="Clear all your marks and start over"):
        st.session_state.marked_cells = {(2, 2)} if st.session_state.bingo_card else set()
        st.rerun()

with col_c:
    if st.button("🎊 Celebrate", help="Feel good about your progress!"):
        st.balloons()

# Display the bingo card
if st.session_state.bingo_card:
    # Player's card header
    if st.session_state.player_name:
        st.markdown(f'<div style="text-align: center; font-size: 2rem; font-weight: 600; color: #667eea; margin: 2rem 0;">🎮 {st.session_state.player_name}\'s Bingo Card</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div style="text-align: center; font-size: 2rem; font-weight: 600; color: #667eea; margin: 2rem 0;">🎮 Your Bingo Card</div>', unsafe_allow_html=True)
    
    # Create the bingo card grid with custom styling
    card = st.session_state.bingo_card
    
    # Display the card with enhanced UI
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
                        button_type = "secondary"
                    else:
                        button_label = f"✅ {card[i][j]}"
                        button_type = "secondary"
                else:
                    button_label = card[i][j]
                    button_type = "primary"
                
                # Create button with enhanced styling
                if st.button(
                    button_label,
                    key=f"cell_{i}_{j}",
                    help=f"Click to {'unmark' if is_marked and (i,j) != (2,2) else 'mark'} this square",
                    disabled=(i == 2 and j == 2),  # Free space is always marked
                    use_container_width=True,
                    type=button_type
                ):
                    if (i, j) in st.session_state.marked_cells and (i, j) != (2, 2):
                        st.session_state.marked_cells.remove((i, j))
                    else:
                        st.session_state.marked_cells.add((i, j))
                    st.rerun()
    
    # Check for bingo with celebration
    if check_bingo(st.session_state.marked_cells):
        st.markdown('<div class="celebration pulse">', unsafe_allow_html=True)
        st.markdown("# 🏆 BINGO! YOU'RE THE CHAMPION! 🏆")
        if st.session_state.player_name:
            st.markdown(f"## 🎊 Congratulations {st.session_state.player_name}! 🎊")
        st.markdown("### 🌟 Share your epic victory with your team! 🌟")
        st.markdown('</div>', unsafe_allow_html=True)
        st.balloons()
    
    # Game stats with cool styling
    marked_count = len(st.session_state.marked_cells)
    completion_percent = (marked_count / 25) * 100
    
    st.markdown('<div class="stats-container">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🎯 Squares Marked", marked_count, delta=None)
    with col2:
        st.metric("⏳ Remaining", 25 - marked_count, delta=None)
    with col3:
        st.metric("📊 Progress", f"{completion_percent:.1f}%", delta=None)
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Progress bar
    progress_bar = st.progress(completion_percent / 100)

else:
    # Welcome section when no card is generated
    st.markdown("""
    <div style="text-align: center; padding: 3rem; background: linear-gradient(135deg, #FF9A8B 0%, #A8E6CF 100%); border-radius: 20px; margin: 2rem 0;">
        <h2 style="color: white; margin-bottom: 2rem;">🎯 Ready to Play?</h2>
        <p style="color: white; font-size: 1.2rem; margin-bottom: 2rem;">Click "Generate New Card" above to start your hilarious remote work adventure!</p>
    </div>
    """, unsafe_allow_html=True)
    
    # How to play section
    st.markdown("""
    <div style="background: rgba(255,255,255,0.9); padding: 2rem; border-radius: 15px; margin: 2rem 0;">
        <h3 style="color: #667eea; text-align: center; margin-bottom: 2rem;">🎮 How to Play</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem;">
            <div style="background: linear-gradient(135deg, #667eea, #764ba2); color: white; padding: 1rem; border-radius: 10px; text-align: center;">
                <h4>1. 🎲 Generate</h4>
                <p>Get your unique bingo card with funny remote work scenarios</p>
            </div>
            <div style="background: linear-gradient(135deg, #FF6B6B, #4ECDC4); color: white; padding: 1rem; border-radius: 10px; text-align: center;">
                <h4>2. ✅ Mark</h4>
                <p>Click squares when you experience those moments</p>
            </div>
            <div style="background: linear-gradient(135deg, #45B7D1, #96CEB4); color: white; padding: 1rem; border-radius: 10px; text-align: center;">
                <h4>3. 🏆 Win</h4>
                <p>Get 5 in a row and celebrate your victory!</p>
            </div>
            <div style="background: linear-gradient(135deg, #A8E6CF, #DCEDC8); color: #333; padding: 1rem; border-radius: 10px; text-align: center;">
                <h4>4. 🎊 Share</h4>
                <p>Screenshot and share with your team for maximum fun!</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # Close game container

# Team play tips with modern styling
st.markdown("""
<div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; padding: 2rem; border-radius: 20px; margin: 2rem 0;">
    <h3 style="text-align: center; margin-bottom: 2rem;">🎯 Pro Tips for Epic Team Play</h3>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; text-align: center;">
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; backdrop-filter: blur(10px);">
            <h4>📸 Share Screenshots</h4>
            <p>Post your cards in team chat for friendly competition!</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; backdrop-filter: blur(10px);">
            <h4>📢 Call Out Moments</h4>
            <p>Announce when you mark a square during meetings</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; backdrop-filter: blur(10px);">
            <h4>🏆 Bragging Rights</h4>
            <p>First to BINGO gets to be team champion!</p>
        </div>
        <div style="background: rgba(255,255,255,0.1); padding: 1rem; border-radius: 10px; backdrop-filter: blur(10px);">
            <h4>🔄 Multiple Rounds</h4>
            <p>Generate new cards for endless entertainment</p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Footer with floating animation
st.markdown("""
<div class="floating" style="text-align: center; padding: 2rem; margin-top: 3rem; background: rgba(255,255,255,0.1); border-radius: 15px; backdrop-filter: blur(10px);">
    <p style="color: white; font-size: 1.1rem; margin: 0;">
        Made with ❤️ and lots of ☕ for remote teams who know the struggle is real! 
    </p>
    <p style="color: rgba(255,255,255,0.8); margin-top: 0.5rem;">
        🎮 Game on, remote warriors! 🎮
    </p>
</div>
""", unsafe_allow_html=True)