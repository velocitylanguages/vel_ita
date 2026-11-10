"""VELOCITY ITALIAN - language pack, brand and motion design constants."""

import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

OUTPUT_DIR = BASE_DIR / "output"
LESSONS_DIR = OUTPUT_DIR / "lessons"
HISTORY_DIR = OUTPUT_DIR / "history"
SCENE_DIR = BASE_DIR / "scene"

VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920
FPS = 30

# ---------------------------------------------------------------- brand

BRAND = "VELOCITY ITALIAN"
BRAND_LOCKUP_TOP = "VELOCITY"
BRAND_LOCKUP_BOTTOM = "ITALIAN"
HANDLE = "@velocityitalian"
MASCOT_NAME = "Velo"

# ==== LANGUAGE PACK START ====
LANGUAGE = {
    "code": "it",
    "name": "Italian",
    "native_name": "Italiano",
    "history_key": "italian",
    "english_voice": "en-US-AvaNeural",
    "english_fallback_voice": "en-US-GuyNeural",
    "native_voice": "it-IT-DiegoNeural",
    "native_fallback_voice": "it-IT-ElsaNeural",
    "native_engine": "edge",
    "native_lang_code": "it",
    "english_rate": "-2%",
    "native_rate": "-6%",
    "english_pitch": "+0Hz",
    "native_pitch": "+0Hz",
    "native_label": "ITALIANO",
    "translit_label": "SAY IT LIKE",
    "greeting": "Ciao!",
    "encouragement": "Fantastico!",
    "rtl": False,
    "char_tiles": False,
    "script_font": "",
}
# ==== LANGUAGE PACK END ====

AI_MODEL = os.getenv("AI_MODEL", "gemini-fast")
POLLINATIONS_API_KEY = os.getenv("POLLINATIONS_API_KEY", "")

# ---------------------------------------------------------------- timing (seconds)

INTRO_DURATION = 4.0
OUTRO_DURATION = 5.2
EN_CARD_IN = 0.55
GAP_EN_NATIVE = 0.5
NATIVE_CARD_LEAD = 0.35
GAP_BEFORE_REPEAT = 0.8
TAIL_HOLD = 1.4
MAX_REEL_DURATION = 88.0

# ---------------------------------------------------------------- palette

INK = "#3C3C3C"
MUTED = "#8A8A8A"
CREAM = "#FFF8E7"
GREEN = "#58CC02"
GREEN_DARK = "#46A302"
GREEN_DEEP = "#3D8F00"
BLUE = "#1CB0F6"
PURPLE = "#A560E8"
ORANGE = "#FF7A00"
RED = "#FF4B4B"
YELLOW = "#F5A700"
TEAL = "#00A889"
PINK = "#E056A0"

PALETTE = [GREEN, BLUE, PURPLE, ORANGE, RED, YELLOW, TEAL, PINK]

# ---------------------------------------------------------------- categories
# (english, native, icon, accent)

# ==== CATEGORY TABLE START ====
CATEGORY_TABLE = [
    ("Motivation", "Motivazione", "rocket", "#A560E8"),
    ("Love", "Amore", "heart", "#FF4B4B"),
    ("Success", "Successo", "trophy", "#F5A700"),
    ("Wisdom", "Saggezza", "book", "#A560E8"),
    ("Happiness", "Felicità", "smile", "#F5A700"),
    ("Self Improvement", "Miglioramento Personale", "leaf", "#58CC02"),
    ("Gratitude", "Gratitudine", "heart", "#FF7A00"),
    ("Friendship", "Amicizia", "users", "#00A889"),
    ("Hope", "Speranza", "sun", "#FF7A00"),
    ("Creativity", "Creatività", "palette", "#E056A0"),
    ("Inner Peace", "Pace Interiore", "lotus", "#00A889"),
    ("Confidence", "Fiducia", "shield", "#1CB0F6"),
    ("Perseverance", "Perseveranza", "mountain", "#FF7A00"),
    ("Inspiration", "Ispirazione", "sparkles", "#A560E8"),
    ("Positive Life", "Vita Positiva", "sun", "#58CC02"),
    ("Courage", "Coraggio", "shield", "#FF4B4B"),
    ("Kindness", "Gentilezza", "heart", "#E056A0"),
    ("Patience", "Pazienza", "hourglass", "#00A889"),
    ("Forgiveness", "Perdono", "hands", "#FF7A00"),
    ("Strength", "Forza", "dumbbell", "#FF4B4B"),
    ("Joy", "Gioia", "smile", "#F5A700"),
    ("Balance", "Equilibrio", "scale", "#00A889"),
    ("Growth", "Crescita", "sprout", "#58CC02"),
    ("Purpose", "Scopo", "target", "#A560E8"),
    ("Mindfulness", "Consapevolezza", "lotus", "#00A889"),
]
# ==== CATEGORY TABLE END ====

CATEGORIES = [c[0] for c in CATEGORY_TABLE]
CATEGORIES_NATIVE = {c[0]: c[1] for c in CATEGORY_TABLE}
CATEGORY_META = {c[0]: {"native": c[1], "icon": c[2], "accent": c[3]} for c in CATEGORY_TABLE}
MAX_RECENT_CATEGORIES = 25

# ==== HASHTAGS START ====
HASHTAGS = [
    "#learnitalian",
    "#italianlessons",
    "#italianforbeginners",
    "#languagelearning",
    "#italianvocabulary",
    "#velocityitalian",
    "#dailyitalian",
    "#italian",
    "#learnlanguages",
    "#speakitalian",
    "#bilingual",
    "#languagetips",
]
# ==== HASHTAGS END ====
