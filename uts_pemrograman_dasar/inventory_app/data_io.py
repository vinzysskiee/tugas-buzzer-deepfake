import csv
import json
from pathlib import Path

REQUIRED_FIELDS = {
    "kode", "nama", "kategori",
    "jumlah", "lokasi", "kondisi"
}


def load_inventory(csv_path):
    """Membaca data inventaris dari file CSV."""

    path = Path(csv_path)

    if not path.exists():
        raise FileNotFoundError(
            f"File input tidak ditemukan: {path}"
        )

    items = []

    with path.open(
        "r", newline="", encoding="utf-8-sig"
    ) as file:

        reader = csv.DictReader(file)

        if not reader.fieldnames:
            raise ValueError(
                "CSV kosong atau tidak memiliki header."
            )

        missing = REQUIRED_FIELDS - set(reader.fieldnames)

        if missing:
            raise ValueError(
                "Kolom CSV tidak lengkap: "
                + ", ".join(sorted(missing))
            )

        for line, row in enumerate(reader, start=2):

            try:
                qty = int(row["jumlah"])

                if qty < 0:
                    raise ValueError(
                        "Jumlah tidak boleh negatif."
                    )

                item = {
                    key: row[key].strip()
                    for key in (
                        "kode",
                        "nama",
                        "kategori",
                        "lokasi",
                        "kondisi"
                    )
                }

                if not all(item.values()):
                    raise ValueError(
                        "Kolom teks wajib diisi."
                    )

                item["jumlah"] = qty
                item["kondisi"] = item["kondisi"].lower()

                items.append(item)

            except (TypeError, ValueError) as error:
                raise ValueError(
                    f"Data tidak valid pada baris {line}: {error}"
                ) from error

    return items


def save_json(data, output_path):
    """Menyimpan hasil laporan ke file JSON."""

    path = Path(output_path)

    path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    with path.open("w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )

    return path