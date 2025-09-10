#!/usr/bin/env python3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = [
    (ROOT / 'index.html', 'Big Why Movers'),
    (ROOT / 'about.html', 'About'),
    (ROOT / 'services.html', 'Services'),
    (ROOT / 'contact.html', 'Contact'),
    (ROOT / 'gallery.html', 'Gallery'),
    (ROOT / 'tips.html', 'Tips'),
]

def read(path: Path) -> str:
    try:
        return path.read_text(encoding='utf-8')
    except Exception as e:
        print(f"FAIL: could not read {path}: {e}")
        sys.exit(1)

def assert_contains(haystack: str, needle: str, context: str):
    if needle not in haystack:
        print(f"FAIL: {context} missing expected content: {needle!r}")
        return False
    return True

def main() -> int:
    ok = True

    for page, expect in PAGES:
        if not page.exists():
            print(f"FAIL: missing page {page}")
            ok = False
            continue
        html = read(page)
        # basic checks
        ok &= assert_contains(html, '<title', f'{page.name}')
        # nav links
        for link in ('index.html', 'about.html', 'services.html', 'gallery.html', 'tips.html', 'contact.html'):
            ok &= assert_contains(html, link, f'{page.name}')

    # landing page content
    landing = read(ROOT / 'index.html')
    for city in ('Bozeman', 'Livingston', 'Big Sky'):
        ok &= assert_contains(landing, city, 'index.html')

    # contact page form and phone
    contact = read(ROOT / 'contact.html')
    ok &= assert_contains(contact, 'id="contact-form"', 'contact.html')
    ok &= assert_contains(contact, 'Sam Harlan', 'contact.html')
    ok &= assert_contains(contact, '+1 (406) 589-4641', 'contact.html')
    ok &= assert_contains(contact, 'name="links[]"', 'contact.html')

    # U-Haul partner link on site
    uhaul_url = 'https://www.uhaul.com/MovingHelp/Bozeman-MT-59715/1/Xip-Moving-Pros/?id=8E0B44F119FE42'
    ok &= assert_contains(read(ROOT / 'index.html'), uhaul_url, 'index.html')
    ok &= assert_contains(read(ROOT / 'services.html'), 'U‑Haul', 'services.html')
    ok &= assert_contains(read(ROOT / 'tips.html'), 'U‑Haul', 'tips.html')

    # Gallery contains the Imgur album link
    ok &= assert_contains(read(ROOT / 'gallery.html'), 'imgur.com/a/L8eFhdV', 'gallery.html')

    if ok:
        print('PASS: basic site smoke tests')
        return 0
    else:
        return 2

if __name__ == '__main__':
    raise SystemExit(main())
