# viseme_rules.py

"""
Master viseme rule table
This file defines WHAT each viseme means.
Nothing here draws images or moves pixels.
"""

# -------------------------------------------------
# Viseme rule structure
# -------------------------------------------------
# jaw: 0.0 → 1.0
# tongue:
#   "none"
#   "deep"
#   "tip_up"
#   "forward"
#
# teeth:
#   upper: True / False
#   lower: True / False
# -------------------------------------------------

VISEME_RULES = {

    # -----------------------------------------
    # Neutral
    # -----------------------------------------
    "X": {
        "jaw": 0.0,
        "upper_teeth": False,
        "lower_teeth": False,
        "tongue": "none"
    },

    # -----------------------------------------
    # Vowels
    # -----------------------------------------
    "A": {
        "jaw": 1.0,
        "upper_teeth": True,
        "lower_teeth": True,
        "tongue": "deep"
    },

    "E": {
        "jaw": 0.4,
        "upper_teeth": True,
        "lower_teeth": True,
        "tongue": "flat"
    },

    "O": {
        "jaw": 0.6,
        "upper_teeth": False,
        "lower_teeth": False,
        "tongue": "back"
    },

    "U": {
        "jaw": 0.3,
        "upper_teeth": False,
        "lower_teeth": False,
        "tongue": "back"
    },

    # -----------------------------------------
    # Closures
    # -----------------------------------------
    "M": {
        "jaw": 0.0,
        "upper_teeth": False,
        "lower_teeth": False,
        "tongue": "none"
    },

    "F": {
        "jaw": 0.2,
        "upper_teeth": True,
        "lower_teeth": False,
        "tongue": "none"
    },

    # -----------------------------------------
    # Tongue articulation
    # -----------------------------------------
    "L": {
        "jaw": 0.3,
        "upper_teeth": True,
        "lower_teeth": False,
        "tongue": "tip_up"
    },

    "TH": {
        "jaw": 0.4,
        "upper_teeth": False,
        "lower_teeth": False,
        "tongue": "forward"
    }
}


# -------------------------------------------------
# Helper function
# -------------------------------------------------

def get_viseme_rule(viseme):
    """
    Returns rule dictionary for a viseme.
    Falls back to neutral if unknown.
    """
    return VISEME_RULES.get(viseme, VISEME_RULES["X"])
