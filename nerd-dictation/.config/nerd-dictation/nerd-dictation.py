# User configuration file typically located at `~/.config/nerd-dictation/nerd-dictation.py`
import re

# -----------------------------------------------------------------------------
# Replace Multiple Words

TEXT_REPLACE_REGEX = (
    # ("\\b" "data type" "\\b", "data-type"),
    # ("\\b" "copy on write" "\\b", "copy-on-write"),
    # ("\\b" "key word" "\\b", "keyword"),
    ('get pull', 'git pull'),
    ('get paul', 'git pull'),
    ('get push', 'git push'),
    ('get check out', 'git checkout'),
    ('get branch', 'git branch --vv'),
    ('git branch', 'git branch --vv'),
    ('get status', 'git status'),
    ('get log', 'git log'),
    ('git cherry pick', 'git cherry-pick'),
    ('get cherry-pick', 'git cherry-pick'),
    ('get cherry pick', 'git cherry-pick'),
    ('get fetch', 'git fetch'),
    ('get rebase', 'git rebase'),
    ('get push upstream', 'git push upstream'),
    ('get push revamp', 'git push revamp'),
    ('get stash', 'git stash'),
    ('get stash pop', 'git stash pop'),
    ('kids checkout', 'git checkout'),
    ('kids status', 'git status'),
    ('get this', 'git diff'),
    ('get diff', 'git diff'),
    ('get ad', 'git add'),
    ('get remote', 'git remote'),
    ('h .top', 'htop'),
    ('h stop', 'htop'),
    ('b .top', 'btop'),
    ('b top', 'btop'),
    ('c d', 'cd'),
    ('c p', 'cp'),
    ('p s a x', 'ps -ax'),
    ('get rebates', 'git rebase'),
    ('pseudo nano', 'sudo nano'),
    ('system city l', 'systemctl'),
    ('as as age', 'ssh'),
    ('as this age', 'ssh'),
    ('khan fig', 'config'),
    ('get hub', 'github'),
    ('get up', 'github'),
    ('get pool', 'git pull'),
    ('did paul', 'git pull'),
    ('get comment', 'git commit'),
    ('khan fake', 'config'),
    ('pac man', 'pacman'),
    ('sie herr', 'Siehe'),
    ('shop where', 'shopware'),
    ('neil when', 'neovim'),
    ('new then', 'neovim'),
    ('get web', 'gitweb'),
    ('logan', 'login'),
    ('very able', 'variable'),
    ('and tree', 'entry'),
)
TEXT_REPLACE_REGEX = tuple(
    (re.compile(match), replacement)
    for (match, replacement) in TEXT_REPLACE_REGEX
)


# -----------------------------------------------------------------------------
# Replace Single Words

# VOSK-API doesn't use capitals anywhere so they have to be explicit added in.
WORD_REPLACE = {
    "i": "I",
    "api": "API",
    "linux": "Linux",
    "male": "mail",
    "rap": "wrap",
    "kara": "Cara",

    'dialogue': 'dialog',
    'pseudo': 'sudo',
    'grip': 'grep',
    'grab': 'grep',
    'rep': 'grep',

    # It's also possible to ignore words entirely.
    "um": "",
    "uhm": "",
    ",nd": "command",
}

# Regular expressions allow partial words to be replaced.
WORD_REPLACE_REGEX = (
    ("^i'(.*)", "I'\\1"),
)
WORD_REPLACE_REGEX = tuple(
    (re.compile(match), replacement)
    for (match, replacement) in WORD_REPLACE_REGEX
)

# -----------------------------------------------------------------------------
# Add Punctuation

CLOSING_PUNCTUATION = {
    # "period": ".",
    # "comma": ",",
    "question mark": "?",
    "close quote": '"',
    'equal': '=',
    'dash': '-',
    'backtick': '`',
    'dollar sign': '$',
}

OPENING_PUNCTUATION = {
    "open quote": '"',
}

# -----------------------------------------------------------------------------
# Main Processing Function

def nerd_dictation_process(text):

    for match, replacement in TEXT_REPLACE_REGEX:
        text = match.sub(replacement, text)

    for match, replacement in CLOSING_PUNCTUATION.items():
        text = text.replace(" " + match, replacement)

    for match, replacement in OPENING_PUNCTUATION.items():
        text = text.replace(match + " ", replacement)

    words = text.split(" ")

    for i, w in enumerate(words):
        w_init = w
        w_test = WORD_REPLACE.get(w)
        if w_test is not None:
            w = w_test
        if w_init == w:
            for match, replacement in WORD_REPLACE_REGEX:
                w_test = match.sub(replacement, w)
                if w_test != w:
                    w = w_test
                    break

        words[i] = w

    # Strip any words that were replaced with empty strings.
    words[:] = [w for w in words if w]

    return " ".join(words)

