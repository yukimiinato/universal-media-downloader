"""
Theme configuration module for Universal Media Downloader.
Contains 40 beautiful theme palettes with light and dark mode variants (80 total themes).
Enhanced contrast for better visibility and readability.
"""

# Define 40 beautiful theme palettes with improved contrast
THEME_PALETTES = {
    # Theme 1: Nord (Modern, Cool)
    'Nord': {
        'dark': {
            'BG_ROOT': '#2E3440', 'BG_FRAME': '#3B4252', 'FG_TEXT': '#ECEFF4',
            'BG_ENTRY': '#556A88', 'ACCENT_BLUE': '#5E81AC', 'ACCENT_GREEN': '#A3BE8C',
            'ACCENT_RED': '#BF616A', 'TITLE_COLOR': '#88C0D0', 'BG_DISABLED': '#434C5E',
            'FG_DISABLED': '#88909E'
        },
        'light': {
            'BG_ROOT': '#ECEFF4', 'BG_FRAME': '#D8DEE9', 'FG_TEXT': '#1F2937',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#81A1C1', 'ACCENT_GREEN': '#A3BE8C',
            'ACCENT_RED': '#D08770', 'TITLE_COLOR': '#2E3440', 'BG_DISABLED': '#E5E9F0',
            'FG_DISABLED': '#A3A8B1'
        }
    },
    # Theme 2: Dracula (Deep Purple)
    'Dracula': {
        'dark': {
            'BG_ROOT': '#282A36', 'BG_FRAME': '#21222C', 'FG_TEXT': '#F8F8F2',
            'BG_ENTRY': '#545760', 'ACCENT_BLUE': '#6272A4', 'ACCENT_GREEN': '#50FA7B',
            'ACCENT_RED': '#FF5555', 'TITLE_COLOR': '#8BE9FD', 'BG_DISABLED': '#3E3F47',
            'FG_DISABLED': '#6272A4'
        },
        'light': {
            'BG_ROOT': '#F8F8F2', 'BG_FRAME': '#E8E8E0', 'FG_TEXT': '#1A1C25',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#6272A4', 'ACCENT_GREEN': '#50FA7B',
            'ACCENT_RED': '#FF5555', 'TITLE_COLOR': '#282A36', 'BG_DISABLED': '#D8D8D0',
            'FG_DISABLED': '#6272A4'
        }
    },
    # Theme 3: Solarized Dark (Warm, Professional)
    'Solarized Dark': {
        'dark': {
            'BG_ROOT': '#002B36', 'BG_FRAME': '#073642', 'FG_TEXT': '#93A1A1',
            'BG_ENTRY': '#586E75', 'ACCENT_BLUE': '#268BD2', 'ACCENT_GREEN': '#859900',
            'ACCENT_RED': '#DC322F', 'TITLE_COLOR': '#2AA198', 'BG_DISABLED': '#003D47',
            'FG_DISABLED': '#657B83'
        },
        'light': {
            'BG_ROOT': '#FDF6E3', 'BG_FRAME': '#EEE8D5', 'FG_TEXT': '#1A1A1A',
            'BG_ENTRY': '#FFFDF5', 'ACCENT_BLUE': '#268BD2', 'ACCENT_GREEN': '#859900',
            'ACCENT_RED': '#DC322F', 'TITLE_COLOR': '#2AA198', 'BG_DISABLED': '#E3DCCD',
            'FG_DISABLED': '#93A1A1'
        }
    },
    # Theme 4: Monokai (Vibrant Dark)
    'Monokai': {
        'dark': {
            'BG_ROOT': '#272822', 'BG_FRAME': '#3E3D32', 'FG_TEXT': '#F8F8F2',
            'BG_ENTRY': '#4B4B46', 'ACCENT_BLUE': '#66D9EF', 'ACCENT_GREEN': '#A6E22E',
            'ACCENT_RED': '#F92672', 'TITLE_COLOR': '#AE81FF', 'BG_DISABLED': '#423F34',
            'FG_DISABLED': '#75715E'
        },
        'light': {
            'BG_ROOT': '#F8F8F2', 'BG_FRAME': '#F0F0F0', 'FG_TEXT': '#272822',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#66D9EF', 'ACCENT_GREEN': '#A6E22E',
            'ACCENT_RED': '#F92672', 'TITLE_COLOR': '#AE81FF', 'BG_DISABLED': '#E8E8E8',
            'FG_DISABLED': '#957E3B'
        }
    },
    # Theme 5: One Dark (VS Code Popular)
    'One Dark': {
        'dark': {
            'BG_ROOT': '#282C34', 'BG_FRAME': '#353B45', 'FG_TEXT': '#E0E0E0',
            'BG_ENTRY': '#3E4451', 'ACCENT_BLUE': '#61AFEF', 'ACCENT_GREEN': '#98C379',
            'ACCENT_RED': '#E06C75', 'TITLE_COLOR': '#56B6C2', 'BG_DISABLED': '#3C414D',
            'FG_DISABLED': '#5C6370'
        },
        'light': {
            'BG_ROOT': '#FAFAFA', 'BG_FRAME': '#F0F0F0', 'FG_TEXT': '#1E1E1E',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#0184BC', 'ACCENT_GREEN': '#4EC9B0',
            'ACCENT_RED': '#E45649', 'TITLE_COLOR': '#0997B3', 'BG_DISABLED': '#E8E8E8',
            'FG_DISABLED': '#A0A1A7'
        }
    },
    # Theme 6: Gruvbox Dark (Retro Groove)
    'Gruvbox Dark': {
        'dark': {
            'BG_ROOT': '#282828', 'BG_FRAME': '#3C3836', 'FG_TEXT': '#EBDBB2',
            'BG_ENTRY': '#504945', 'ACCENT_BLUE': '#83A598', 'ACCENT_GREEN': '#B8BB26',
            'ACCENT_RED': '#FB4934', 'TITLE_COLOR': '#8EC07C', 'BG_DISABLED': '#44423F',
            'FG_DISABLED': '#928374'
        },
        'light': {
            'BG_ROOT': '#FBF1C7', 'BG_FRAME': '#F9F5D7', 'FG_TEXT': '#3C3836',
            'BG_ENTRY': '#FFFBF0', 'ACCENT_BLUE': '#458588', 'ACCENT_GREEN': '#B8BB26',
            'ACCENT_RED': '#CC241D', 'TITLE_COLOR': '#689D6A', 'BG_DISABLED': '#F2E5BC',
            'FG_DISABLED': '#928374'
        }
    },
    # Theme 7: Tokyonight (Anime-inspired)
    'Tokyonight': {
        'dark': {
            'BG_ROOT': '#1A1B26', 'BG_FRAME': '#16161E', 'FG_TEXT': '#C0CAF5',
            'BG_ENTRY': '#24283B', 'ACCENT_BLUE': '#7AA2F7', 'ACCENT_GREEN': '#9ECE6A',
            'ACCENT_RED': '#F7768E', 'TITLE_COLOR': '#7DCFFF', 'BG_DISABLED': '#1F2335',
            'FG_DISABLED': '#545C7E'
        },
        'light': {
            'BG_ROOT': '#F5F5F5', 'BG_FRAME': '#FAFAFA', 'FG_TEXT': '#16161E',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#2E7DE9', 'ACCENT_GREEN': '#587539',
            'ACCENT_RED': '#D20065', 'TITLE_COLOR': '#006297', 'BG_DISABLED': '#F0F0F0',
            'FG_DISABLED': '#9CA0B0'
        }
    },
    # Theme 8: Material Darker (Google Design)
    'Material Darker': {
        'dark': {
            'BG_ROOT': '#212121', 'BG_FRAME': '#263238', 'FG_TEXT': '#EEFFFF',
            'BG_ENTRY': '#2E3C43', 'ACCENT_BLUE': '#64B5F6', 'ACCENT_GREEN': '#81C784',
            'ACCENT_RED': '#E57373', 'TITLE_COLOR': '#4DD0E1', 'BG_DISABLED': '#37474F',
            'FG_DISABLED': '#546E7A'
        },
        'light': {
            'BG_ROOT': '#FAFAFA', 'BG_FRAME': '#F5F5F5', 'FG_TEXT': '#212121',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#1976D2', 'ACCENT_GREEN': '#388E3C',
            'ACCENT_RED': '#D32F2F', 'TITLE_COLOR': '#00838F', 'BG_DISABLED': '#EEEEEE',
            'FG_DISABLED': '#9E9E9E'
        }
    },
    # Theme 9: Oceanic Next (Relaxing Blue)
    'Oceanic Next': {
        'dark': {
            'BG_ROOT': '#1B2B34', 'BG_FRAME': '#16252B', 'FG_TEXT': '#D8DEE9',
            'BG_ENTRY': '#243340', 'ACCENT_BLUE': '#6699CC', 'ACCENT_GREEN': '#99C794',
            'ACCENT_RED': '#EC5F67', 'TITLE_COLOR': '#5FB3B3', 'BG_DISABLED': '#2A3D45',
            'FG_DISABLED': '#4F7A7E'
        },
        'light': {
            'BG_ROOT': '#ECF0F1', 'BG_FRAME': '#FAFBFC', 'FG_TEXT': '#1B2B34',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#6699CC', 'ACCENT_GREEN': '#99C794',
            'ACCENT_RED': '#EC5F67', 'TITLE_COLOR': '#5FB3B3', 'BG_DISABLED': '#D5DBDE',
            'FG_DISABLED': '#8FA3AA'
        }
    },
    # Theme 10: Atom One Dark (Familiar Editor Style)
    'Atom One Dark': {
        'dark': {
            'BG_ROOT': '#282C34', 'BG_FRAME': '#353B45', 'FG_TEXT': '#E0E0E0',
            'BG_ENTRY': '#3E4451', 'ACCENT_BLUE': '#61AFEF', 'ACCENT_GREEN': '#98C379',
            'ACCENT_RED': '#E06C75', 'TITLE_COLOR': '#56B6C2', 'BG_DISABLED': '#3C414D',
            'FG_DISABLED': '#5C6370'
        },
        'light': {
            'BG_ROOT': '#FAFAFA', 'BG_FRAME': '#F5F5F5', 'FG_TEXT': '#1E1E1E',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#0184BC', 'ACCENT_GREEN': '#50A14F',
            'ACCENT_RED': '#E45649', 'TITLE_COLOR': '#4078F2', 'BG_DISABLED': '#EEEEEE',
            'FG_DISABLED': '#A0A1A7'
        }
    },
    # Theme 11: Zenburn (Warm Retro)
    'Zenburn': {
        'dark': {
            'BG_ROOT': '#383838', 'BG_FRAME': '#3F3F3F', 'FG_TEXT': '#DCDCDC',
            'BG_ENTRY': '#4A4A4A', 'ACCENT_BLUE': '#80B0FF', 'ACCENT_GREEN': '#BCEE68',
            'ACCENT_RED': '#FF8787', 'TITLE_COLOR': '#87CEEB', 'BG_DISABLED': '#505050',
            'FG_DISABLED': '#808080'
        },
        'light': {
            'BG_ROOT': '#F5F5F5', 'BG_FRAME': '#FAFAFA', 'FG_TEXT': '#383838',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#5B9BD5', 'ACCENT_GREEN': '#70AD47',
            'ACCENT_RED': '#FF6B6B', 'TITLE_COLOR': '#0B8CC9', 'BG_DISABLED': '#E8E8E8',
            'FG_DISABLED': '#A0A0A0'
        }
    },
    # Theme 12: Synthwave (Neon Cyberpunk)
    'Synthwave': {
        'dark': {
            'BG_ROOT': '#1A0033', 'BG_FRAME': '#2D0A4E', 'FG_TEXT': '#FF00FF',
            'BG_ENTRY': '#3D1565', 'ACCENT_BLUE': '#00D9FF', 'ACCENT_GREEN': '#00FF41',
            'ACCENT_RED': '#FF006E', 'TITLE_COLOR': '#FFBE0B', 'BG_DISABLED': '#4A1D7F',
            'FG_DISABLED': '#AA00FF'
        },
        'light': {
            'BG_ROOT': '#FFF5E6', 'BG_FRAME': '#FFFBF0', 'FG_TEXT': '#333333',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#0099FF', 'ACCENT_GREEN': '#00CC44',
            'ACCENT_RED': '#FF1493', 'TITLE_COLOR': '#FF8C00', 'BG_DISABLED': '#F0E6FF',
            'FG_DISABLED': '#666666'
        }
    },
    # Theme 13: Forest (Nature Inspired)
    'Forest': {
        'dark': {
            'BG_ROOT': '#1B2F1B', 'BG_FRAME': '#274E27', 'FG_TEXT': '#C7E5C7',
            'BG_ENTRY': '#2A5F2A', 'ACCENT_BLUE': '#5BA373', 'ACCENT_GREEN': '#8BC34A',
            'ACCENT_RED': '#FF6B6B', 'TITLE_COLOR': '#4CAF50', 'BG_DISABLED': '#1F4620',
            'FG_DISABLED': '#558655'
        },
        'light': {
            'BG_ROOT': '#E8F5E9', 'BG_FRAME': '#F1F8F6', 'FG_TEXT': '#1B5E20',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#2E7D32', 'ACCENT_GREEN': '#43A047',
            'ACCENT_RED': '#E53935', 'TITLE_COLOR': '#00897B', 'BG_DISABLED': '#C8E6C9',
            'FG_DISABLED': '#558B2F'
        }
    },
    # Theme 14: Ocean (Serene Water)
    'Ocean': {
        'dark': {
            'BG_ROOT': '#0F1B3C', 'BG_FRAME': '#1A2F5A', 'FG_TEXT': '#B8D4E8',
            'BG_ENTRY': '#254173', 'ACCENT_BLUE': '#5B8FC7', 'ACCENT_GREEN': '#6ECDC1',
            'ACCENT_RED': '#FF8C42', 'TITLE_COLOR': '#00B4D8', 'BG_DISABLED': '#1E3A5F',
            'FG_DISABLED': '#4A6FA5'
        },
        'light': {
            'BG_ROOT': '#E0F2FE', 'BG_FRAME': '#F0F8FF', 'FG_TEXT': '#003D5C',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#0077B6', 'ACCENT_GREEN': '#00B4D8',
            'ACCENT_RED': '#FF006E', 'TITLE_COLOR': '#0096C7', 'BG_DISABLED': '#B3E5FC',
            'FG_DISABLED': '#0288D1'
        }
    },
    # Theme 15: Sunset (Warm Evening)
    'Sunset': {
        'dark': {
            'BG_ROOT': '#2C1810', 'BG_FRAME': '#3D2414', 'FG_TEXT': '#F5DCC3',
            'BG_ENTRY': '#5C3D2E', 'ACCENT_BLUE': '#D4A574', 'ACCENT_GREEN': '#C5B35E',
            'ACCENT_RED': '#FF6B5B', 'TITLE_COLOR': '#FF9F43', 'BG_DISABLED': '#4A3728',
            'FG_DISABLED': '#A0826D'
        },
        'light': {
            'BG_ROOT': '#FFE8D1', 'BG_FRAME': '#FFF4E6', 'FG_TEXT': '#5D4E37',
            'BG_ENTRY': '#FFFBF0', 'ACCENT_BLUE': '#D4A574', 'ACCENT_GREEN': '#E8BB4D',
            'ACCENT_RED': '#E0574B', 'TITLE_COLOR': '#FF9F00', 'BG_DISABLED': '#FFD7B8',
            'FG_DISABLED': '#C17A4A'
        }
    },
    # Theme 16: Lavender (Soft Purple)
    'Lavender': {
        'dark': {
            'BG_ROOT': '#2D1B3D', 'BG_FRAME': '#3D2B4D', 'FG_TEXT': '#E8D7F1',
            'BG_ENTRY': '#4D3B5D', 'ACCENT_BLUE': '#B5A7D8', 'ACCENT_GREEN': '#C4B5FD',
            'ACCENT_RED': '#F5A8D8', 'TITLE_COLOR': '#D4A5D8', 'BG_DISABLED': '#433A52',
            'FG_DISABLED': '#8B7AA8'
        },
        'light': {
            'BG_ROOT': '#F3EEFB', 'BG_FRAME': '#F7F3FB', 'FG_TEXT': '#4A3B5F',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#7C5BA5', 'ACCENT_GREEN': '#957DAD',
            'ACCENT_RED': '#D946A6', 'TITLE_COLOR': '#8E44AD', 'BG_DISABLED': '#E6D9F0',
            'FG_DISABLED': '#AA8FBD'
        }
    },
    # Theme 17: Coral (Vibrant Pink-Orange)
    'Coral': {
        'dark': {
            'BG_ROOT': '#3D1F1F', 'BG_FRAME': '#5C2E2E', 'FG_TEXT': '#FFD4CC',
            'BG_ENTRY': '#6E4343', 'ACCENT_BLUE': '#FF8A80', 'ACCENT_GREEN': '#FF6D7A',
            'ACCENT_RED': '#FF4757', 'TITLE_COLOR': '#FF6348', 'BG_DISABLED': '#703A3A',
            'FG_DISABLED': '#B8746B'
        },
        'light': {
            'BG_ROOT': '#FFE8E8', 'BG_FRAME': '#FFF5F5', 'FG_TEXT': '#5C2D2D',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#FF6D7A', 'ACCENT_GREEN': '#FF9E64',
            'ACCENT_RED': '#E63946', 'TITLE_COLOR': '#FF6348', 'BG_DISABLED': '#FFCCCC',
            'FG_DISABLED': '#D97060'
        }
    },
    # Theme 18: Peacock (Teal & Blue)
    'Peacock': {
        'dark': {
            'BG_ROOT': '#0D3B3B', 'BG_FRAME': '#1A4D4D', 'FG_TEXT': '#B3E5FC',
            'BG_ENTRY': '#2B5F5F', 'ACCENT_BLUE': '#4FC3F7', 'ACCENT_GREEN': '#69F0AE',
            'ACCENT_RED': '#FF6E40', 'TITLE_COLOR': '#26C6DA', 'BG_DISABLED': '#1F6B6B',
            'FG_DISABLED': '#5A9EA0'
        },
        'light': {
            'BG_ROOT': '#E0F7FA', 'BG_FRAME': '#F0FFFF', 'FG_TEXT': '#004D4D',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#0097A7', 'ACCENT_GREEN': '#00897B',
            'ACCENT_RED': '#FF5722', 'TITLE_COLOR': '#00ACC1', 'BG_DISABLED': '#B2DFDB',
            'FG_DISABLED': '#00897B'
        }
    },
    # Theme 19: Midnight (Cool Dark Blue)
    'Midnight': {
        'dark': {
            'BG_ROOT': '#0F1419', 'BG_FRAME': '#1A202C', 'FG_TEXT': '#E2E8F0',
            'BG_ENTRY': '#2D3748', 'ACCENT_BLUE': '#63B3ED', 'ACCENT_GREEN': '#9AE6B4',
            'ACCENT_RED': '#FC8181', 'TITLE_COLOR': '#81E6D9', 'BG_DISABLED': '#2A3542',
            'FG_DISABLED': '#4A5568'
        },
        'light': {
            'BG_ROOT': '#F0F4F8', 'BG_FRAME': '#F8FAFC', 'FG_TEXT': '#0F1419',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#3B82F6', 'ACCENT_GREEN': '#10B981',
            'ACCENT_RED': '#EF4444', 'TITLE_COLOR': '#06B6D4', 'BG_DISABLED': '#E2E8F0',
            'FG_DISABLED': '#64748B'
        }
    },
    # Theme 20: Ruby (Deep Red)
    'Ruby': {
        'dark': {
            'BG_ROOT': '#2B1A20', 'BG_FRAME': '#3D252D', 'FG_TEXT': '#F5C6D0',
            'BG_ENTRY': '#5C3C48', 'ACCENT_BLUE': '#D47F9E', 'ACCENT_GREEN': '#E0A080',
            'ACCENT_RED': '#E74C3C', 'TITLE_COLOR': '#E74C3C', 'BG_DISABLED': '#4A3540',
            'FG_DISABLED': '#A0747D'
        },
        'light': {
            'BG_ROOT': '#FDEEF2', 'BG_FRAME': '#FFF5F8', 'FG_TEXT': '#5C2E37',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#C92A2A', 'ACCENT_GREEN': '#E8612C',
            'ACCENT_RED': '#A61E4D', 'TITLE_COLOR': '#C92A2A', 'BG_DISABLED': '#F8BCC8',
            'FG_DISABLED': '#DA3860'
        }
    },
    # Theme 21: Arctic (Icy Light)
    'Arctic': {
        'dark': {
            'BG_ROOT': '#1C2540', 'BG_FRAME': '#252F4A', 'FG_TEXT': '#D4E4F7',
            'BG_ENTRY': '#3A4B63', 'ACCENT_BLUE': '#80CAFF', 'ACCENT_GREEN': '#A8E6CF',
            'ACCENT_RED': '#FFB3BA', 'TITLE_COLOR': '#A8D8EA', 'BG_DISABLED': '#3A4858',
            'FG_DISABLED': '#6B7FA3'
        },
        'light': {
            'BG_ROOT': '#E6F1FF', 'BG_FRAME': '#F0F5FF', 'FG_TEXT': '#1C2540',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#0066CC', 'ACCENT_GREEN': '#00B4A6',
            'ACCENT_RED': '#FF6B9D', 'TITLE_COLOR': '#0099CC', 'BG_DISABLED': '#C8E0FF',
            'FG_DISABLED': '#0066CC'
        }
    },
    # Theme 22: Aubergine (Deep Purple Berry)
    'Aubergine': {
        'dark': {
            'BG_ROOT': '#291A33', 'BG_FRAME': '#3D2E47', 'FG_TEXT': '#E8D4F0',
            'BG_ENTRY': '#4D3F59', 'ACCENT_BLUE': '#B8A0D4', 'ACCENT_GREEN': '#C9A8E8',
            'ACCENT_RED': '#E6A3C8', 'TITLE_COLOR': '#D4B0E8', 'BG_DISABLED': '#443D52',
            'FG_DISABLED': '#9B7FAE'
        },
        'light': {
            'BG_ROOT': '#F3EAFB', 'BG_FRAME': '#F8F3FC', 'FG_TEXT': '#4A3A5E',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#6B46C1', 'ACCENT_GREEN': '#7C5AA6',
            'ACCENT_RED': '#C53030', 'TITLE_COLOR': '#6B46C1', 'BG_DISABLED': '#E1CFF0',
            'FG_DISABLED': '#9333EA'
        }
    },
    # Theme 23: Minion (Happy Yellow)
    'Minion': {
        'dark': {
            'BG_ROOT': '#332F1E', 'BG_FRAME': '#4A4428', 'FG_TEXT': '#F5E8CC',
            'BG_ENTRY': '#5D5533', 'ACCENT_BLUE': '#FFD700', 'ACCENT_GREEN': '#F0E68C',
            'ACCENT_RED': '#FFAB91', 'TITLE_COLOR': '#FFC107', 'BG_DISABLED': '#605839',
            'FG_DISABLED': '#999970'
        },
        'light': {
            'BG_ROOT': '#FFFAF0', 'BG_FRAME': '#FFFFF0', 'FG_TEXT': '#4A4428',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#FFAB00', 'ACCENT_GREEN': '#FFB300',
            'ACCENT_RED': '#FF6B6B', 'TITLE_COLOR': '#FFA500', 'BG_DISABLED': '#FFE082',
            'FG_DISABLED': '#FFB300'
        }
    },
    # Theme 24: Rose (Pink Romance)
    'Rose': {
        'dark': {
            'BG_ROOT': '#39202B', 'BG_FRAME': '#4A2A38', 'FG_TEXT': '#F0C4D4',
            'BG_ENTRY': '#5E3D4D', 'ACCENT_BLUE': '#D98AA5', 'ACCENT_GREEN': '#E8A8D0',
            'ACCENT_RED': '#E75480', 'TITLE_COLOR': '#E88AA8', 'BG_DISABLED': '#54354A',
            'FG_DISABLED': '#B08CA0'
        },
        'light': {
            'BG_ROOT': '#FBE9EF', 'BG_FRAME': '#FFF0F5', 'FG_TEXT': '#5A2E3B',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#C2185B', 'ACCENT_GREEN': '#D81B60',
            'ACCENT_RED': '#AD1457', 'TITLE_COLOR': '#C2185B', 'BG_DISABLED': '#F8D7E8',
            'FG_DISABLED': '#EC407A'
        }
    },
    # Theme 25: Sage (Calm Green)
    'Sage': {
        'dark': {
            'BG_ROOT': '#253236', 'BG_FRAME': '#344B50', 'FG_TEXT': '#C5D8D4',
            'BG_ENTRY': '#435962', 'ACCENT_BLUE': '#7BA6A6', 'ACCENT_GREEN': '#A0BFB3',
            'ACCENT_RED': '#C1826B', 'TITLE_COLOR': '#8FADA6', 'BG_DISABLED': '#3D4F58',
            'FG_DISABLED': '#7A8B89'
        },
        'light': {
            'BG_ROOT': '#E8F0EE', 'BG_FRAME': '#F5FAFE', 'FG_TEXT': '#2B3E42',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#2D5F66', 'ACCENT_GREEN': '#2A7F62',
            'ACCENT_RED': '#A67355', 'TITLE_COLOR': '#2F8F80', 'BG_DISABLED': '#C8E0DC',
            'FG_DISABLED': '#4A9B89'
        }
    },
    # Theme 26: Honey (Warm Gold)
    'Honey': {
        'dark': {
            'BG_ROOT': '#2F2419', 'BG_FRAME': '#4A381F', 'FG_TEXT': '#F5E8D4',
            'BG_ENTRY': '#5C4B2F', 'ACCENT_BLUE': '#D9A85C', 'ACCENT_GREEN': '#E8C547',
            'ACCENT_RED': '#E8724C', 'TITLE_COLOR': '#F0B84A', 'BG_DISABLED': '#5C4829',
            'FG_DISABLED': '#B8956D'
        },
        'light': {
            'BG_ROOT': '#FFFBF0', 'BG_FRAME': '#FFFDF5', 'FG_TEXT': '#5C4B2F',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#D4A000', 'ACCENT_GREEN': '#F0B84A',
            'ACCENT_RED': '#E67E22', 'TITLE_COLOR': '#E8B84A', 'BG_DISABLED': '#FFE8B6',
            'FG_DISABLED': '#D4A000'
        }
    },
    # Theme 27: Storm (Dramatic Gray)
    'Storm': {
        'dark': {
            'BG_ROOT': '#1B1D23', 'BG_FRAME': '#27292F', 'FG_TEXT': '#D4D9E8',
            'BG_ENTRY': '#3A3E47', 'ACCENT_BLUE': '#7C8BA8', 'ACCENT_GREEN': '#A8B8D8',
            'ACCENT_RED': '#B8959D', 'TITLE_COLOR': '#8F9FBD', 'BG_DISABLED': '#3D414A',
            'FG_DISABLED': '#6B7080'
        },
        'light': {
            'BG_ROOT': '#E8EAED', 'BG_FRAME': '#F0F2F5', 'FG_TEXT': '#202124',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#1F2937', 'ACCENT_GREEN': '#4B5563',
            'ACCENT_RED': '#6B7280', 'TITLE_COLOR': '#374151', 'BG_DISABLED': '#D1D5DB',
            'FG_DISABLED': '#6B7280'
        }
    },
    # Theme 28: Mint (Fresh Green)
    'Mint': {
        'dark': {
            'BG_ROOT': '#192C2F', 'BG_FRAME': '#2A4047', 'FG_TEXT': '#C0DED7',
            'BG_ENTRY': '#3D5860', 'ACCENT_BLUE': '#6FC5D4', 'ACCENT_GREEN': '#52D28E',
            'ACCENT_RED': '#FF8A80', 'TITLE_COLOR': '#4ED8C1', 'BG_DISABLED': '#3A505A',
            'FG_DISABLED': '#7A9DA0'
        },
        'light': {
            'BG_ROOT': '#E0F7F4', 'BG_FRAME': '#F0FFFE', 'FG_TEXT': '#0D4E4E',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#00897B', 'ACCENT_GREEN': '#26A69A',
            'ACCENT_RED': '#FF6E6E', 'TITLE_COLOR': '#009688', 'BG_DISABLED': '#B2DFDB',
            'FG_DISABLED': '#4DB8A8'
        }
    },
    # Theme 29: Marigold (Bright Warm)
    'Marigold': {
        'dark': {
            'BG_ROOT': '#3D2A15', 'BG_FRAME': '#5C3F1F', 'FG_TEXT': '#F5D9A8',
            'BG_ENTRY': '#7A5A33', 'ACCENT_BLUE': '#E8A84A', 'ACCENT_GREEN': '#F0C84A',
            'ACCENT_RED': '#FF9F5A', 'TITLE_COLOR': '#F0B84A', 'BG_DISABLED': '#6B5C47',
            'FG_DISABLED': '#C8A878'
        },
        'light': {
            'BG_ROOT': '#FFFBF0', 'BG_FRAME': '#FFFEEE', 'FG_TEXT': '#664D1F',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#E67E22', 'ACCENT_GREEN': '#F39C12',
            'ACCENT_RED': '#E74C3C', 'TITLE_COLOR': '#D68910', 'BG_DISABLED': '#FFE8B6',
            'FG_DISABLED': '#E67E22'
        }
    },
    # Theme 30: Amethyst (Royal Purple)
    'Amethyst': {
        'dark': {
            'BG_ROOT': '#2B1F3D', 'BG_FRAME': '#3D2D52', 'FG_TEXT': '#E8D9F5',
            'BG_ENTRY': '#4F3F62', 'ACCENT_BLUE': '#B395D4', 'ACCENT_GREEN': '#D4A8E8',
            'ACCENT_RED': '#E8A5D8', 'TITLE_COLOR': '#D4A8D4', 'BG_DISABLED': '#4A3E5A',
            'FG_DISABLED': '#9B7DB8'
        },
        'light': {
            'BG_ROOT': '#F3EEFB', 'BG_FRAME': '#F8F5FC', 'FG_TEXT': '#3D2D52',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#7C3AED', 'ACCENT_GREEN': '#A78BFA',
            'ACCENT_RED': '#D946EF', 'TITLE_COLOR': '#9333EA', 'BG_DISABLED': '#E9D5FF',
            'FG_DISABLED': '#C084FC'
        }
    },
    # NEW Theme 31: Vibrant (Modern Neon)
    'Vibrant': {
        'dark': {
            'BG_ROOT': '#0A0E27', 'BG_FRAME': '#111C3E', 'FG_TEXT': '#E8F0FF',
            'BG_ENTRY': '#1A2855', 'ACCENT_BLUE': '#00E5FF', 'ACCENT_GREEN': '#39FF14',
            'ACCENT_RED': '#FF10F0', 'TITLE_COLOR': '#FFD60A', 'BG_DISABLED': '#1F2844',
            'FG_DISABLED': '#4A66FF'
        },
        'light': {
            'BG_ROOT': '#F0F4FF', 'BG_FRAME': '#E8ECFF', 'FG_TEXT': '#0A0E27',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#0066FF', 'ACCENT_GREEN': '#00AA00',
            'ACCENT_RED': '#FF0080', 'TITLE_COLOR': '#FF6600', 'BG_DISABLED': '#DDE5FF',
            'FG_DISABLED': '#0066FF'
        }
    },
    # NEW Theme 32: Emerald (Rich Green)
    'Emerald': {
        'dark': {
            'BG_ROOT': '#0D2B1F', 'BG_FRAME': '#1A3A2D', 'FG_TEXT': '#D0E8DC',
            'BG_ENTRY': '#2A5244', 'ACCENT_BLUE': '#5EEAD4', 'ACCENT_GREEN': '#10B981',
            'ACCENT_RED': '#EF4444', 'TITLE_COLOR': '#14B8A6', 'BG_DISABLED': '#1F4434',
            'FG_DISABLED': '#6CA97C'
        },
        'light': {
            'BG_ROOT': '#E0F8F4', 'BG_FRAME': '#ECF9F6', 'FG_TEXT': '#0D2B1F',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#059669', 'ACCENT_GREEN': '#047857',
            'ACCENT_RED': '#DC2626', 'TITLE_COLOR': '#0891B2', 'BG_DISABLED': '#CCEDE8',
            'FG_DISABLED': '#047857'
        }
    },
    # NEW Theme 33: Sunset Blaze (Warm Orange-Red)
    'Sunset Blaze': {
        'dark': {
            'BG_ROOT': '#3D1A0F', 'BG_FRAME': '#4F2516', 'FG_TEXT': '#FDD9B5',
            'BG_ENTRY': '#6B3A23', 'ACCENT_BLUE': '#FF8A65', 'ACCENT_GREEN': '#FFB74D',
            'ACCENT_RED': '#FF5252', 'TITLE_COLOR': '#FF7043', 'BG_DISABLED': '#56301A',
            'FG_DISABLED': '#B8704B'
        },
        'light': {
            'BG_ROOT': '#FFF3E0', 'BG_FRAME': '#FFF8F0', 'FG_TEXT': '#4D2313',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#FF6F00', 'ACCENT_GREEN': '#FF9800',
            'ACCENT_RED': '#D84315', 'TITLE_COLOR': '#FF5722', 'BG_DISABLED': '#FFD7A8',
            'FG_DISABLED': '#FF6F00'
        }
    },
    # NEW Theme 34: Cyber (High Contrast)
    'Cyber': {
        'dark': {
            'BG_ROOT': '#000000', 'BG_FRAME': '#0A0A0A', 'FG_TEXT': '#00FF00',
            'BG_ENTRY': '#1A1A1A', 'ACCENT_BLUE': '#00FFFF', 'ACCENT_GREEN': '#00FF00',
            'ACCENT_RED': '#FF0000', 'TITLE_COLOR': '#FFFF00', 'BG_DISABLED': '#333333',
            'FG_DISABLED': '#666666'
        },
        'light': {
            'BG_ROOT': '#F5F5F5', 'BG_FRAME': '#E0E0E0', 'FG_TEXT': '#000000',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#0000FF', 'ACCENT_GREEN': '#008000',
            'ACCENT_RED': '#FF0000', 'TITLE_COLOR': '#FF8800', 'BG_DISABLED': '#CCCCCC',
            'FG_DISABLED': '#666666'
        }
    },
    # NEW Theme 35: Grape (Deep Purple)
    'Grape': {
        'dark': {
            'BG_ROOT': '#251C3D', 'BG_FRAME': '#3B2D55', 'FG_TEXT': '#E8D9F5',
            'BG_ENTRY': '#503C6D', 'ACCENT_BLUE': '#A78BFA', 'ACCENT_GREEN': '#C4B5FD',
            'ACCENT_RED': '#F472B6', 'TITLE_COLOR': '#D8B4FE', 'BG_DISABLED': '#4A3E66',
            'FG_DISABLED': '#9D8DC8'
        },
        'light': {
            'BG_ROOT': '#F8F1FF', 'BG_FRAME': '#FAF5FF', 'FG_TEXT': '#3D2554',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#7C3AED', 'ACCENT_GREEN': '#A855F7',
            'ACCENT_RED': '#EC4899', 'TITLE_COLOR': '#9333EA', 'BG_DISABLED': '#EDE9FE',
            'FG_DISABLED': '#A855F7'
        }
    },
    # NEW Theme 36: Teal Dream
    'Teal Dream': {
        'dark': {
            'BG_ROOT': '#0F2F38', 'BG_FRAME': '#1A3F4C', 'FG_TEXT': '#B3E5FC',
            'BG_ENTRY': '#2B5A6F', 'ACCENT_BLUE': '#4DD0E1', 'ACCENT_GREEN': '#80DEEA',
            'ACCENT_RED': '#FF6F61', 'TITLE_COLOR': '#26C6DA', 'BG_DISABLED': '#1E4D5F',
            'FG_DISABLED': '#5FA5B0'
        },
        'light': {
            'BG_ROOT': '#E0F2F1', 'BG_FRAME': '#EBF5F5', 'FG_TEXT': '#004D4D',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#00897B', 'ACCENT_GREEN': '#009688',
            'ACCENT_RED': '#FF5252', 'TITLE_COLOR': '#00796B', 'BG_DISABLED': '#B2DFDB',
            'FG_DISABLED': '#00897B'
        }
    },
    # NEW Theme 37: Warm Spice
    'Warm Spice': {
        'dark': {
            'BG_ROOT': '#3B2520', 'BG_FRAME': '#4A3028', 'FG_TEXT': '#E8CAB0',
            'BG_ENTRY': '#5E3F30', 'ACCENT_BLUE': '#D9A574', 'ACCENT_GREEN': '#E8B76D',
            'ACCENT_RED': '#FF7043', 'TITLE_COLOR': '#FFAB91', 'BG_DISABLED': '#56352C',
            'FG_DISABLED': '#B8704B'
        },
        'light': {
            'BG_ROOT': '#FFF1E6', 'BG_FRAME': '#FFFAF5', 'FG_TEXT': '#5D3A29',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#D4A574', 'ACCENT_GREEN': '#E8B84A',
            'ACCENT_RED': '#E0574B', 'TITLE_COLOR': '#D2691E', 'BG_DISABLED': '#FFE0C0',
            'FG_DISABLED': '#D4A574'
        }
    },
    # NEW Theme 38: Steel (Modern Gray)
    'Steel': {
        'dark': {
            'BG_ROOT': '#1C1C24', 'BG_FRAME': '#262631', 'FG_TEXT': '#D4D7E3',
            'BG_ENTRY': '#3A3D47', 'ACCENT_BLUE': '#7B8DA3', 'ACCENT_GREEN': '#A3B3C3',
            'ACCENT_RED': '#C07A7A', 'TITLE_COLOR': '#9BAFC7', 'BG_DISABLED': '#3A3E48',
            'FG_DISABLED': '#6B7C8F'
        },
        'light': {
            'BG_ROOT': '#ECECF1', 'BG_FRAME': '#F5F5FA', 'FG_TEXT': '#1C1C24',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#2C3E50', 'ACCENT_GREEN': '#546E7A',
            'ACCENT_RED': '#7F8C8D', 'TITLE_COLOR': '#34495E', 'BG_DISABLED': '#D5D8E1',
            'FG_DISABLED': '#546E7A'
        }
    },
    # NEW Theme 39: Sunset Pink (Rose-Peach)
    'Sunset Pink': {
        'dark': {
            'BG_ROOT': '#3F1A24', 'BG_FRAME': '#582A38', 'FG_TEXT': '#F0C4D0',
            'BG_ENTRY': '#6B3F52', 'ACCENT_BLUE': '#E68BAD', 'ACCENT_GREEN': '#F4A5C9',
            'ACCENT_RED': '#FF5E78', 'TITLE_COLOR': '#FF9AB9', 'BG_DISABLED': '#5C3D50',
            'FG_DISABLED': '#B88FA8'
        },
        'light': {
            'BG_ROOT': '#FDE8ED', 'BG_FRAME': '#FFF5FA', 'FG_TEXT': '#5C2E3D',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#D81B60', 'ACCENT_GREEN': '#EC407A',
            'ACCENT_RED': '#C2185B', 'TITLE_COLOR': '#AD1457', 'BG_DISABLED': '#F8D7E5',
            'FG_DISABLED': '#E91E63'
        }
    },
    # NEW Theme 40: Forest Fire (Green-Gold)
    'Forest Fire': {
        'dark': {
            'BG_ROOT': '#1B2812', 'BG_FRAME': '#2A3A1F', 'FG_TEXT': '#D4E5A0',
            'BG_ENTRY': '#3D5A28', 'ACCENT_BLUE': '#8BC34A', 'ACCENT_GREEN': '#AED581',
            'ACCENT_RED': '#FF6F6F', 'TITLE_COLOR': '#C5E1A5', 'BG_DISABLED': '#2E4620',
            'FG_DISABLED': '#7BA34D'
        },
        'light': {
            'BG_ROOT': '#E8F5E9', 'BG_FRAME': '#F1F8E9', 'FG_TEXT': '#1B5E20',
            'BG_ENTRY': '#FFFFFF', 'ACCENT_BLUE': '#558B2F', 'ACCENT_GREEN': '#689F38',
            'ACCENT_RED': '#D32F2F', 'TITLE_COLOR': '#7CB342', 'BG_DISABLED': '#C8E6C9',
            'FG_DISABLED': '#558B2F'
        }
    },
}


def build_themes_dictionary():
    """Build THEMES dictionary with both light and dark modes."""
    themes = {}
    for theme_name, modes in THEME_PALETTES.items():
        for mode_name, colors in modes.items():
            key = f"{theme_name} ({mode_name.capitalize()})"
            themes[key] = colors
    return themes


# Build and export the THEMES dictionary
THEMES = build_themes_dictionary()


def get_theme(theme_name, mode='dark'):
    """
    Get a specific theme by name and mode.
    
    Args:
        theme_name: Name of the theme (e.g., 'Nord')
        mode: 'dark' or 'light'
    
    Returns:
        Dictionary of colors for the theme, or default Nord dark if not found
    """
    key = f"{theme_name} ({mode.capitalize()})"
    return THEMES.get(key, THEMES.get('Nord (Dark)'))


def get_all_theme_names():
    """Get a sorted list of all available themes."""
    return sorted(list(THEMES.keys()))
