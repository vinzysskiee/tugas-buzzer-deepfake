import unittest

from inventory_app.operations import (
    remove_duplicate_codes,
    search_items,
    filter_by_condition,
    low_stock,
    summarize
)


SAMPLE = [
    {
        "kode": "A1",
        "nama": "Laptop",
        "kategori": "Elektronik",
        "jumlah": 2,
        "lokasi": "Lab A",
        "kondisi": "baik"
    },
    {
        "kode": "A2",
        "nama": "Mouse",
        "kategori": "Aksesori",
        "jumlah": 8,
        "lokasi": "Lab B",
        "kondisi": "rusak"
    },
    {
        "kode": "A1",
        "nama": "Laptop duplikat",
        "kategori": "Elektronik",
        "jumlah": 2,
        "lokasi": "Lab A",
        "kondisi": "baik"
    }
]


class InventoryTests(unittest.TestCase):

    def test_duplicate(self):
        self.assertEqual(
            len(remove_duplicate_codes(SAMPLE)),
            2
        )

    def test_search(self):
        self.assertEqual(
            len(search_items(SAMPLE, "lap")),
            2
        )

    def test_condition(self):
        self.assertEqual(
            len(filter_by_condition(SAMPLE, "rusak")),
            1
        )

    def test_low_stock(self):
        self.assertEqual(
            len(low_stock(SAMPLE, 2)),
            2
        )

    def test_negative(self):
        with self.assertRaises(ValueError):
            low_stock(SAMPLE, -1)

    def test_summary(self):
        self.assertEqual(
            summarize(SAMPLE[:2])["total_unit"],
            10
        )


if __name__ == "__main__":
    unittest.main()