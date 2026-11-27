"""Spoken TTS text -> display text for subtitles (numbers as digits, acronyms restored)."""
import re

REPL = [
    ("I.P.O.", "IPO"), ("S.E.C.'s", "SEC's"), ("S.E.C.", "SEC"), ("S.P.C.X.", "SPCX"), ("A.I.", "AI"), ("ex AI", "xAI"),
    ("Open AI", "OpenAI"), ("Chat G.P.T.", "ChatGPT"), ("S-one", "S-1"),
    ("one hundred and thirty-five dollars", "$135"), ("one hundred and thirty-five dollar", "$135"),
    ("seventy-five billion dollars", "$75 billion"), ("twenty-four years", "24 years"),
    ("twenty twenty-five", "2025"), ("twenty twenty-six", "2026"), ("twenty twenty-seven", "2027"), ("twenty nineteen", "2019"),
    ("eighteen point seven billion dollars", "$18.7 billion"), ("five billion", "$5 billion"),
    ("five hundred and fifty-six million", "556 million"), ("twenty-nine billion dollars", "$29 billion"),
    ("eighty-five point seven billion dollars", "$85.7 billion"), ("eighty-five point seven billion", "$85.7 billion"),
    ("one hundred and fifty dollars", "$150"), ("one hundred and seventy-six dollars", "$176"),
    ("one sixty point nine five", "$160.95"), ("two hundred and twenty-five dollars and sixty-four cents", "$225.64"),
    ("one hundred and nine dollars", "$109"), ("one hundred and four dollars and eighty-three cents", "$104.83"),
    ("sixty billion dollars", "$60 billion"), ("six hundred billion dollars", "$600 billion"),
    ("nine hundred and eleven million", "911 million"), ("seven point eight billion dollars", "$7.8 billion"),
    ("eighteen point four billion dollars", "$18.4 billion"), ("four point four billion dollar", "$4.4 billion"),
    ("eighty-three dollars", "$83"), ("eighty-one point three billion dollars", "$81.3 billion"),
    ("one trillion dollars", "$1 trillion"), ("two trillion dollars", "$2 trillion"),
    ("one hundred and sixty-one percent", "161%"), ("ninety-two percent", "92%"), ("fifty-three percent", "53%"),
    ("thirty-five percent", "35%"), ("fifteen percent", "15%"), ("thirty percent", "30%"), ("nineteen percent", "19%"),
    ("six percent", "6%"), ("ten percent", "10%"), ("five to ten percent", "5-10%"), ("seven percent", "7%"),
    ("ninety days'", "90 days'"), ("One hundred and thirty-five dollars", "$135"), ("original seventy-five", "original $75 billion"),
    ("April first", "April 1"), ("May twentieth", "May 20"), ("June fourth", "June 4"), ("June eleventh", "June 11"),
    ("June twelfth", "June 12"), ("June sixteenth", "June 16"), ("July twenty-seventh", "July 27"), ("August third", "August 3"),
    ("August sixth", "August 6"), ("November eighteenth", "November 18"), ("December eighth", "December 8"),
]


def display(s: str) -> str:
    for a, b in sorted(REPL, key=lambda r: -len(r[0])):
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip()
