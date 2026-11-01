# -*- coding: utf-8 -*-
"""
Typographer engine for Russian text in HTML and plain text documents.
Binds hanging prepositions, conjunctions, particles, numbers, units, and initials
with non-breaking spaces (&nbsp;) so they never hang at the end of lines,
without ever corrupting spaces between subsequent words.
"""

import re

BASE_PREPS = [
    # 1-letter
    'в', 'и', 'с', 'к', 'о', 'у', 'а', 'я',
    # 2-letter
    'на', 'за', 'по', 'из', 'от', 'до', 'не', 'но', 'со', 'во', 'ко', 'об', 'да', 'ни', 'же', 'ли', 'бы',
    # 3-letter
    'под', 'над', 'при', 'про', 'без', 'для'
]

PREPOSITIONS = []
for p in BASE_PREPS:
    PREPOSITIONS.extend([p.lower(), p.capitalize(), p.upper()])

PREPOSITIONS = sorted(list(set(PREPOSITIONS)), key=len, reverse=True)
PREP_REGEX = '|'.join(re.escape(p) for p in PREPOSITIONS)
PREP_PATTERN = re.compile(r'(^|[\s>(«"„\(\[])(' + PREP_REGEX + r')[ \t]+(?=[а-яА-Яa-zA-Z0-9«"„\(\[])')

UNITS = (
    r'млн|млрд|тыс\.|руб\.|рублей|голосов|голоса|голос|лет|года|году|г\.|'
    r'суток|человек|активистов|депутатов|делегатов|кодов|МЛН|РУБЛЕЙ|ГОЛОСОВ'
)

def typograph_text_node(text):
    if not text:
        return text

    # 1. Bind prepositions & conjunctions (3 passes for chains like "и в", "не по", "а под")
    text = PREP_PATTERN.sub(r'\1\2&nbsp;', text)
    text = PREP_PATTERN.sub(r'\1\2&nbsp;', text)
    text = PREP_PATTERN.sub(r'\1\2&nbsp;', text)

    # 2. Bind numbers with units & symbols (using word boundary \b so space after unit is NOT consumed!)
    # № 197 -> №&nbsp;197
    text = re.sub(r'№[ \t]+(\d+)', r'№&nbsp;\1', text)

    # ст. 207.3 -> ст.&nbsp;207.3, ч. 5 -> ч.&nbsp;5
    text = re.sub(r'\b(ст\.|ч\.|п\.|пп\.|корп\.|д\.|кв\.|пом\.|оф\.|г\.)[ \t]+([0-9а-яА-Я]+)', r'\1&nbsp;\2', text)

    # Number + unit word: 24,2 млн -> 24,2&nbsp;млн, 8,5 лет -> 8,5&nbsp;лет
    text = re.sub(
        r'(\d+[\d\s,.]*)[ \t]+(' + UNITS + r')\b',
        lambda m: m.group(1).replace(' ', '&nbsp;') + '&nbsp;' + m.group(2),
        text
    )

    # Number + currency symbol: 24,2 ₽ -> 24,2&nbsp;₽, 100 % -> 100&nbsp;%
    text = re.sub(r'(\d+[\d\s,.]*)[ \t]+([₽%])', lambda m: m.group(1).replace(' ', '&nbsp;') + '&nbsp;' + m.group(2), text)

    # Bind adjacent units: МЛН РУБЛЕЙ -> МЛН&nbsp;РУБЛЕЙ, млн руб. -> млн&nbsp;руб.
    text = re.sub(r'\b(млн|МЛН)[ \t]+(руб\.|рублей|РУБЛЕЙ)\b', r'\1&nbsp;\2', text)

    # 3. Bind organization prefixes with quoted names
    text = re.sub(r'\b(ООО|АНО|ПАО|ИП|фонд|фонда|фонду|партии|партия|партию|отделение|отделения|округе|округ|округа|суд|суда|судья|судьи)[ \t]+(«[^»]+»)', r'\1&nbsp;\2', text)

    # 4. Bind names and initials:
    text = re.sub(r'([А-ЯЁ][а-яё]+)[ \t]+([А-ЯЁ]\.)[ \t]*([А-ЯЁ]\.)', r'\1&nbsp;\2&nbsp;\3', text)
    text = re.sub(r'([А-ЯЁ]\.)[ \t]*([А-ЯЁ]\.)[ \t]+([А-ЯЁ][а-яё]+)', r'\1&nbsp;\2&nbsp;\3', text)

    return text

def typograph_html(html_str):
    """
    Applies typographer to HTML text nodes only, preserving all tags, script, and style blocks.
    """
    parts = re.split(r'(<script[\s\S]*?</script>|<style[\s\S]*?</style>)', html_str, flags=re.IGNORECASE)
    result_parts = []
    for part in parts:
        if not part:
            continue
        if part.lower().startswith('<script') or part.lower().startswith('<style'):
            result_parts.append(part)
        else:
            tokens = re.split(r'(<[^>]+>)', part)
            processed = []
            for tok in tokens:
                if tok.startswith('<') and tok.endswith('>'):
                    processed.append(tok)
                else:
                    processed.append(typograph_text_node(tok))
            result_parts.append(''.join(processed))
    return ''.join(result_parts)

if __name__ == '__main__':
    sample = '<p>В современной России Илья Яшин получил 8,5 лет строгого режима, а 24,2 МЛН РУБЛЕЙ ушли от мэрии.</p>'
    print("Test output:\n", typograph_html(sample))
