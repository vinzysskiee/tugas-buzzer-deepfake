def remove_duplicate_codes(items):
    """Menghapus barang dengan kode yang sama."""

    seen = set()
    result = []

    for item in items:

        if item["kode"] not in seen:

            seen.add(item["kode"])
            result.append(item)

    return result


def search_items(items, keyword):
    """Mencari barang berdasarkan kata kunci."""

    term = keyword.casefold().strip()

    if not term:
        return []

    return [
        item for item in items
        if any(
            term in item[key].casefold()
            for key in (
                "kode",
                "nama",
                "kategori",
                "lokasi"
            )
        )
    ]


def filter_by_condition(items, condition):
    """Memfilter barang berdasarkan kondisi."""

    target = condition.casefold().strip()

    return [
        item for item in items
        if item["kondisi"] == target
    ]


def low_stock(items, threshold):
    """Menampilkan barang dengan stok rendah."""

    if threshold < 0:
        raise ValueError(
            "Batas stok tidak boleh negatif."
        )

    return [
        item for item in items
        if item["jumlah"] <= threshold
    ]


def summarize(items):
    """Menghitung ringkasan data inventaris."""

    categories = {
        item["kategori"] for item in items
    }

    conditions = {}

    for item in items:

        kondisi = item["kondisi"]

        conditions[kondisi] = (
            conditions.get(kondisi, 0) + 1
        )

    return {
        "jumlah_jenis_barang": len(items),
        "total_unit": sum(
            item["jumlah"] for item in items
        ),
        "kategori": sorted(categories),
        "jumlah_per_kondisi": conditions
    }


def build_report(items):
    """Membuat laporan inventaris."""

    unique_items = remove_duplicate_codes(items)

    return {
        "judul": "Laporan Inventaris Laboratorium",
        "total_data": len(unique_items),
        "ringkasan": summarize(unique_items),
        "barang": unique_items
    }