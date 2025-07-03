import random
from pathlib import Path
from datetime import datetime, timedelta
from faker import Faker

fake = Faker()

NUM_POSTS = 5

# Ensure content directory exists
Path("content").mkdir(exist_ok=True)

for _ in range(NUM_POSTS):
    title = fake.sentence(nb_words=25)
    slug = fake.slug()
    body = "\n\n".join(fake.paragraphs(nb=random.randint(3, 7)))
    date = (datetime.now() - timedelta(days=random.randint(0, 365))).strftime('%Y-%m-%d')

    with open(f"content/{slug}.md", "w", encoding="utf-8") as f:
        f.write(f"""Title: {title}
Date: {date}
Slug: {slug}
Tags:
Category:

{body}
""")
