#!/usr/bin/env python3
import os

IMG_DIR = "/home/rashid/Documents/blog/images"
os.makedirs(IMG_DIR, exist_ok=True)

svgs = {
    # 10 DEXs
    "uniswap.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <linearGradient id="uniGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF007A"/>
      <stop offset="100%" stop-color="#80003E"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="22" fill="url(#uniGrad)"/>
  <path d="M68 25 C65 23 58 26 55 30 C53 27 48 26 44 28 C38 31 36 38 38 45 C35 46 32 49 31 53 C29 59 32 66 38 69 C37 72 38 76 41 78 C45 81 50 80 54 77 C56 79 59 80 62 79 C68 77 71 70 70 64 C73 61 75 56 74 50 C73 43 69 38 68 25 Z" fill="#FFFFFF" opacity="0.95"/>
  <path d="M52 18 L55 28 L47 25 Z" fill="#FFE0EE"/>
  <circle cx="58" cy="42" r="3" fill="#FF007A"/>
</svg>""",

    "pancakeswap.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <linearGradient id="pancakeBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1FC7D4"/>
      <stop offset="100%" stop-color="#127c85"/>
    </linearGradient>
    <linearGradient id="cakeGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFE0B2"/>
      <stop offset="100%" stop-color="#D1884F"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="22" fill="url(#pancakeBg)"/>
  <ellipse cx="50" cy="68" rx="32" ry="11" fill="#A76027"/>
  <ellipse cx="50" cy="65" rx="32" ry="10" fill="url(#cakeGrad)"/>
  <ellipse cx="50" cy="55" rx="30" ry="9" fill="#A76027"/>
  <ellipse cx="50" cy="52" rx="30" ry="9" fill="url(#cakeGrad)"/>
  <ellipse cx="50" cy="42" rx="28" ry="8" fill="#A76027"/>
  <ellipse cx="50" cy="39" rx="28" ry="8" fill="url(#cakeGrad)"/>
  <rect x="43" y="31" width="14" height="9" rx="2" fill="#FFEB3B" transform="rotate(-6 50 35)"/>
  <path d="M52 40 C52 46 47 48 47 54 C47 58 51 60 51 64" stroke="#8D4311" stroke-width="4" stroke-linecap="round" fill="none"/>
</svg>""",

    "hyperliquid.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <linearGradient id="hlBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#051923"/>
      <stop offset="100%" stop-color="#000c14"/>
    </linearGradient>
    <linearGradient id="hlNeon" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F0FF"/>
      <stop offset="100%" stop-color="#7000FF"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="22" fill="url(#hlBg)"/>
  <path d="M28 25 L38 25 L38 44 L62 44 L62 25 L72 25 L72 75 L62 75 L62 56 L38 56 L38 75 L28 75 Z" fill="url(#hlNeon)"/>
  <circle cx="50" cy="50" r="7" fill="#00F0FF"/>
  <path d="M20 50 Q 50 20 80 50 Q 50 80 20 50" stroke="#00F0FF" stroke-width="2.5" fill="none" opacity="0.4"/>
</svg>""",

    "raydium.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <linearGradient id="rayBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1F0967"/>
      <stop offset="100%" stop-color="#0D042C"/>
    </linearGradient>
    <linearGradient id="rayPoly1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#5C24FF"/>
      <stop offset="100%" stop-color="#00D2FF"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="22" fill="url(#rayBg)"/>
  <polygon points="50,18 78,35 78,65 50,82 22,65 22,35" fill="none" stroke="url(#rayPoly1)" stroke-width="4"/>
  <polygon points="50,26 70,38 70,62 50,74 30,62 30,38" fill="url(#rayPoly1)" opacity="0.75"/>
  <polygon points="50,36 62,43 62,57 50,64 38,57 38,43" fill="#00FFC2"/>
</svg>""",

    "dydx.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <linearGradient id="dydxBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1B194B"/>
      <stop offset="100%" stop-color="#0C0A27"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="22" fill="url(#dydxBg)"/>
  <path d="M26 28 L44 72 L34 72 L20 28 Z" fill="#6966FF"/>
  <path d="M74 28 L56 72 L66 72 L80 28 Z" fill="#FFFFFF"/>
  <path d="M33 50 L67 50" stroke="#6966FF" stroke-width="6" stroke-linecap="round"/>
</svg>""",

    "curve.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <linearGradient id="curveBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#002266"/>
      <stop offset="100%" stop-color="#000F33"/>
    </linearGradient>
    <linearGradient id="ringGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FF3B30"/>
      <stop offset="35%" stop-color="#FF9500"/>
      <stop offset="70%" stop-color="#FFCC00"/>
      <stop offset="100%" stop-color="#007AFF"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="22" fill="url(#curveBg)"/>
  <ellipse cx="50" cy="50" rx="34" ry="20" fill="none" stroke="url(#ringGrad)" stroke-width="12" transform="rotate(-25 50 50)"/>
  <ellipse cx="50" cy="50" rx="22" ry="12" fill="none" stroke="#FFFFFF" stroke-width="3" opacity="0.6" transform="rotate(-25 50 50)"/>
</svg>""",

    "aerodrome.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <linearGradient id="aeroBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0052FF"/>
      <stop offset="100%" stop-color="#001F66"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="22" fill="url(#aeroBg)"/>
  <path d="M50 18 L78 74 L63 74 L50 46 L37 74 L22 74 Z" fill="#FFFFFF"/>
  <path d="M42 58 L58 58 L50 40 Z" fill="#0052FF"/>
  <circle cx="50" cy="30" r="4" fill="#00D2FF"/>
</svg>""",

    "orca.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <linearGradient id="orcaBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFB800"/>
      <stop offset="100%" stop-color="#E07A00"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="22" fill="url(#orcaBg)"/>
  <path d="M22 62 C26 48 38 34 56 34 C68 34 78 40 82 48 C76 46 68 47 62 52 C54 58 46 68 30 68 C25 68 22 65 22 62 Z" fill="#1A3258"/>
  <path d="M48 34 C50 25 56 22 60 20 C58 26 56 32 54 35 Z" fill="#1A3258"/>
  <ellipse cx="44" cy="50" rx="9" ry="5" fill="#FFFFFF" transform="rotate(-15 44 50)"/>
  <circle cx="70" cy="42" r="2.5" fill="#FFFFFF"/>
  <path d="M15 76 Q 30 68 45 76 T 75 76 T 95 76" stroke="#FFFFFF" stroke-width="4" fill="none" stroke-linecap="round"/>
</svg>""",

    "jupiter.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <linearGradient id="jupBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0E1E1E"/>
      <stop offset="100%" stop-color="#030808"/>
    </linearGradient>
    <linearGradient id="planetGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00FF9D"/>
      <stop offset="50%" stop-color="#00BE74"/>
      <stop offset="100%" stop-color="#004D30"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="22" fill="url(#jupBg)"/>
  <ellipse cx="50" cy="50" rx="40" ry="14" fill="none" stroke="#00FF9D" stroke-width="3.5" transform="rotate(-20 50 50)" opacity="0.85"/>
  <circle cx="50" cy="50" r="24" fill="url(#planetGrad)"/>
  <path d="M14 59 C 24 68 62 64 86 41" fill="none" stroke="#FFFFFF" stroke-width="3" opacity="0.9"/>
  <path d="M28 46 Q 50 52 72 46" stroke="#004D30" stroke-width="2.5" fill="none"/>
  <path d="M30 54 Q 50 60 70 54" stroke="#00FF9D" stroke-width="2" fill="none" opacity="0.8"/>
</svg>""",

    "meteora.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <defs>
    <linearGradient id="metBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2D1200"/>
      <stop offset="100%" stop-color="#120500"/>
    </linearGradient>
    <linearGradient id="fireGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFE600"/>
      <stop offset="50%" stop-color="#FF5D00"/>
      <stop offset="100%" stop-color="#FF0044"/>
    </linearGradient>
  </defs>
  <rect width="100" height="100" rx="22" fill="url(#metBg)"/>
  <path d="M22 22 C 35 32 40 45 42 60 C 52 52 64 45 78 22 C 65 40 60 55 58 72 C 50 65 40 65 34 70 C 35 55 30 38 22 22 Z" fill="url(#fireGrad)"/>
  <circle cx="58" cy="66" r="14" fill="#FFE600"/>
  <circle cx="58" cy="66" r="8" fill="#FFFFFF"/>
</svg>""",

    # 25 CEXs
    "bybit.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#121214"/>
  <path d="M28 25 L48 25 C58 25 64 30 64 38 C64 44 60 48 54 50 C62 52 66 58 66 64 C66 73 58 78 48 78 L28 78 Z M40 35 L40 46 L47 46 C52 46 55 43 55 40 C55 37 52 35 47 35 Z M40 56 L40 68 L48 68 C53 68 56 65 56 62 C56 59 53 56 48 56 Z" fill="#F7A600"/>
</svg>""",

    "binance.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#181A20"/>
  <g fill="#F3BA2F">
    <polygon points="50,18 62,30 50,42 38,30"/>
    <polygon points="26,42 38,54 26,66 14,54"/>
    <polygon points="74,42 86,54 74,66 62,54"/>
    <polygon points="50,66 62,78 50,90 38,78"/>
    <polygon points="50,44 60,54 50,64 40,54"/>
  </g>
</svg>""",

    "bitget.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#00202B"/>
  <path d="M28 32 L46 50 L28 68 L38 78 L66 50 L38 22 Z" fill="#00F0FF"/>
  <path d="M52 32 L70 50 L52 68 L62 78 L90 50 L62 22 Z" fill="#00A3FF" opacity="0.6"/>
</svg>""",

    "coinbase.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#0052FF"/>
  <circle cx="50" cy="50" r="26" fill="#FFFFFF"/>
  <rect x="42" y="42" width="16" height="16" rx="4" fill="#0052FF"/>
</svg>""",

    "kraken.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#5741D9"/>
  <path d="M30 25 L44 25 L44 75 L30 75 Z" fill="#FFFFFF"/>
  <path d="M44 48 L64 25 L78 25 L56 50 L78 75 L64 75 Z" fill="#FFFFFF"/>
</svg>""",

    "okx.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#000000"/>
  <rect x="24" y="24" width="22" height="22" rx="4" fill="#FFFFFF"/>
  <rect x="54" y="24" width="22" height="22" rx="4" fill="#FFFFFF"/>
  <rect x="24" y="54" width="22" height="22" rx="4" fill="#FFFFFF"/>
  <rect x="54" y="54" width="22" height="22" rx="4" fill="#FFFFFF"/>
  <circle cx="50" cy="50" r="7" fill="#000000"/>
</svg>""",

    "gate.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#1351D8"/>
  <circle cx="50" cy="50" r="28" fill="none" stroke="#FFFFFF" stroke-width="8"/>
  <rect x="50" y="22" width="28" height="28" fill="#00E5BC" rx="4"/>
</svg>""",

    "bitstamp.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#005537"/>
  <path d="M30 25 L54 25 C64 25 70 30 70 38 C70 44 66 48 60 50 C68 52 72 58 72 64 C72 73 64 78 54 78 L30 78 Z M42 35 L42 46 L52 46 C56 46 59 43 59 40 C59 37 56 35 52 35 Z M42 56 L42 68 L53 68 C58 68 61 65 61 62 C61 59 58 56 53 56 Z" fill="#FFFFFF"/>
</svg>""",

    "mexc.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#003D32"/>
  <path d="M22 75 L22 25 L40 54 L50 38 L60 54 L78 25 L78 75 L66 75 L66 45 L50 68 L34 45 L34 75 Z" fill="#00B897"/>
</svg>""",

    "lbank.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#001F5C"/>
  <path d="M32 25 L46 25 L46 64 L74 64 L74 75 L32 75 Z" fill="#0055FF"/>
</svg>""",

    "binance-us.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#1E2026"/>
  <g fill="#E5A910">
    <polygon points="50,18 62,30 50,42 38,30"/>
    <polygon points="26,42 38,54 26,66 14,54"/>
    <polygon points="74,42 86,54 74,66 62,54"/>
    <polygon points="50,66 62,78 50,90 38,78"/>
    <polygon points="50,44 60,54 50,64 40,54"/>
  </g>
  <text x="50" y="58" font-size="14" font-weight="900" fill="#FFFFFF" text-anchor="middle" font-family="sans-serif">US</text>
</svg>""",

    "crypto-com.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#061D42"/>
  <polygon points="50,20 78,35 78,65 50,80 22,65 22,35" fill="none" stroke="#1199FA" stroke-width="6"/>
  <polygon points="50,30 68,40 68,60 50,70 32,60 32,40" fill="#1199FA"/>
</svg>""",

    "bitso.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#003B1C"/>
  <circle cx="50" cy="50" r="28" fill="#00A650"/>
  <circle cx="50" cy="50" r="14" fill="#003B1C"/>
</svg>""",

    "bitunix.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#1E1B4B"/>
  <path d="M26 25 L50 62 L74 25 L86 25 L50 80 L14 25 Z" fill="#6366F1"/>
</svg>""",

    "luno.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#091638"/>
  <circle cx="38" cy="50" r="16" fill="#1A3B8B"/>
  <circle cx="62" cy="50" r="16" fill="#2D5BE3"/>
</svg>""",

    "bitkub.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#003B1F"/>
  <path d="M30 25 L45 25 L45 75 L30 75 Z" fill="#00A859"/>
  <path d="M45 42 L68 25 L80 25 L56 50 L80 75 L68 75 Z" fill="#00CC6C"/>
</svg>""",

    "kucoin.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#0B4236"/>
  <path d="M28 25 L42 25 L42 75 L28 75 Z" fill="#24AE8F"/>
  <path d="M42 48 L64 25 L78 25 L56 50 L78 75 L64 75 Z" fill="#2FD4AE"/>
  <circle cx="64" cy="50" r="6" fill="#FFFFFF"/>
</svg>""",

    "bingx.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#001A5E"/>
  <path d="M25 25 L55 50 L25 75 Z" fill="#0052FF"/>
  <path d="M50 25 L80 50 L50 75 Z" fill="#3875FF" opacity="0.8"/>
</svg>""",

    "bitvavo.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#001B52"/>
  <path d="M25 25 L48 75 L56 75 L78 25 L65 25 L52 56 L38 25 Z" fill="#0055FF"/>
</svg>""",

    "hashkey.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#001026"/>
  <path d="M30 25 L42 25 L42 75 L30 75 Z M58 25 L70 25 L70 75 L58 75 Z M42 45 L58 45 L58 55 L42 55 Z" fill="#00509D"/>
</svg>""",

    "bullish.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#18181B"/>
  <circle cx="50" cy="50" r="28" fill="none" stroke="#D4AF37" stroke-width="7"/>
  <path d="M50 22 L50 50 L70 60" stroke="#D4AF37" stroke-width="6" stroke-linecap="round" fill="none"/>
</svg>""",

    "whitebit.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#0D1B2A"/>
  <path d="M22 25 L36 75 L48 45 L60 75 L74 25 L62 25 L54 54 L44 30 L34 54 L26 25 Z" fill="#E0E1DD"/>
</svg>""",

    "bitbank.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#1C1C1C"/>
  <circle cx="50" cy="50" r="26" fill="#C0392B"/>
</svg>""",

    "niza.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#200D56"/>
  <path d="M28 25 L40 25 L64 65 L64 25 L74 25 L74 75 L62 75 L38 35 L38 75 L28 75 Z" fill="#7B4FE8"/>
</svg>""",

    "upbit.svg": """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" width="100%" height="100%">
  <rect width="100" height="100" rx="22" fill="#001547"/>
  <path d="M30 25 L44 25 L44 55 C44 65 52 70 60 70 C68 70 76 65 76 55 L76 25 L90 25 L90 55 C90 73 78 82 60 82 C42 82 30 73 30 55 Z" fill="#0033A0"/>
</svg>"""
}

for fname, content in svgs.items():
    fpath = os.path.join(IMG_DIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content.strip())

print(f"Generated {len(svgs)} local vector SVG logos in {IMG_DIR}!")
