"""Character looks for The SpaceX IPO (original designs; see characters.md for the briefs)."""
from crayon_engine.character import Look

# [HERO] Elon caricature: identity = swept-back dark-brown hair with a front quiff + all-black outfit
ELON = Look("Elon", cls="hero", skin="#F2D3B0", skin_sh="#D9AE8A", hair="elon", hair_c="#3A2B24",
            body="#24262C", inner="#3C4250")

# [EXTRAS] white heads, coloured clothes
RETAIL = [
    Look("Retail A", body="#2E9C9A", hood=True),
    Look("Retail B", body="#E8833A", hair="bob", hair_c="#E9E9EC"),
    Look("Retail C", body="#7A5CC2", hat="cap", hat_c="#F2B630"),
    Look("Retail D", body="#F2C14E", hood=True),
    Look("Retail E", body="#3FA9E0", hair="bun", hair_c="#E9E9EC"),
]
FOUNDER_FRIEND = Look("Early investor", body="#2A3556", inner="#F3F3F3", tie="#D9363E", glasses="monocle")
EMPLOYEE = Look("Employee", body="#5B6B7D", hat="hardhat", hat_c="#F3F3F3", pin="#3FA9E0")
BIG_FUND = Look("Big fund", body="#6B2234", inner="#F3F3F3", tie="#F2B630", hat="tophat")
BOUNCER = Look("Bouncer", body="#1E1C1F", inner="#F3F3F3", tie="#1E1C1F", glasses="sun", earpiece=True, width=1.18)
