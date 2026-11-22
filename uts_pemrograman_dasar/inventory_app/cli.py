import argparse

from inventory_app.data_io import (
    load_inventory,
    save_json
)

from inventory_app.operations import (
    build_report,
    search_items,
    filter_by_condition,
    low_stock
)


def create_parser():
    """Membuat perintah aplikasi."""

    parser = argparse.ArgumentParser(
        description="Aplikasi Manajemen Inventaris Laboratorium"
    )

    parser.add_argument(
        "--input",
        default="data/input/inventaris.csv"
    )

    parser.add_argument(
        "--output",
        default="data/output/laporan_inventaris.json"
    )

    sub = parser.add_subparsers(
        dest="command",
        required=True
    )

    sub.add_parser("list")

    search = sub.add_parser("search")
    search.add_argument("keyword")

    condition = sub.add_parser("condition")
    condition.add_argument("value")

    stock = sub.add_parser("low-stock")
    stock.add_argument(
        "--threshold",
        type=int,
        default=5
    )

    sub.add_parser("summary")
    sub.add_parser("export")

    return parser


def print_items(items):
    """Menampilkan data barang dalam bentuk tabel."""

    if not items:
        print("Tidak ada data yang cocok.")
        return

    print(
        f"{'KODE':<8} {'NAMA':<22} "
        f"{'KATEGORI':<15} {'JUMLAH':>6} "
        f"{'LOKASI':<16} KONDISI"
    )

    print("-" * 90)

    for item in items:

        print(
            f"{item['kode']:<8} "
            f"{item['nama']:<22} "
            f"{item['kategori']:<15} "
            f"{item['jumlah']:>6} "
            f"{item['lokasi']:<16} "
            f"{item['kondisi']}"
        )


def main():
    """Menjalankan aplikasi inventaris."""

    parser = create_parser()
    args = parser.parse_args()

    try:

        items = load_inventory(args.input)

        if args.command == "list":

            print_items(items)

        elif args.command == "search":

            result = search_items(
                items,
                args.keyword
            )

            print_items(result)

        elif args.command == "condition":

            result = filter_by_condition(
                items,
                args.value
            )

            print_items(result)

        elif args.command == "low-stock":

            result = low_stock(
                items,
                args.threshold
            )

            print_items(result)

        elif args.command == "summary":

            report = build_report(items)

            for key, value in report["ringkasan"].items():
                print(f"{key}: {value}")

        elif args.command == "export":

            report = build_report(items)

            output = save_json(
                report,
                args.output
            )

            print(
                f"Laporan berhasil disimpan: {output}"
            )

    except (
        FileNotFoundError,
        ValueError,
        OSError
    ) as error:

        print(f"ERROR: {error}")

        raise SystemExit(1)


if __name__ == "__main__":
    main()