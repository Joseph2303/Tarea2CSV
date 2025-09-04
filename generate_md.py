import pandas as pd, os, re
from pathlib import Path

df = pd.read_csv("Laptops.csv")

out_dir = Path("content/laptops")
out_dir.mkdir(parents=True, exist_ok=True)

def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return re.sub(r'-+', '-', s).strip('-')

for _, row in df.iterrows():
    brand = str(row['Brand']).strip()
    model = str(row['Model_Name']).strip()
    processor = str(row['Processor']).strip()
    os_name = str(row['Operating_System']).strip()

    # Storage_MB parece ser GB en tus datos; si viniera en MB, convertimos
    storage = float(row['Storage_MB'])
    storage_gb = storage/1024 if storage > 1024 else storage

    ram_gb = int(row['RAM_GB'])
    screen_cm = float(row['Screen_Size'])
    touch = str(row['Touch_Screen']).strip()
    price = float(row['Price'])

    slug = slugify(f"{brand}-{model}")

    md = f"""---
brand: "{brand}"
model: "{model}"
processor: "{processor}"
os: "{os_name}"
storage_gb: {int(round(storage_gb))}
ram_gb: {ram_gb}
screen_cm: {screen_cm}
touch: "{touch}"
price_usd: {price}
slug: "{slug}"
---

# {brand} {model}

- **Procesador:** {processor}
- **Sistema operativo:** {os_name}
- **Almacenamiento:** {int(round(storage_gb))} GB
- **RAM:** {ram_gb} GB
- **Pantalla:** {screen_cm} cm
- **Pantalla táctil:** {touch}
- **Precio:** ${price}
"""
    (out_dir / f"{slug}.md").write_text(md, encoding="utf-8")
