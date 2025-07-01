import csv
from django.core.management.base import BaseCommand
from core.models import Bank, Branch


class Command(BaseCommand):
    help = "Load banks and branches from CSV files"

    def handle(self, *args, **kwargs):
        with open("core/data/bank_branches.csv", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                Bank.objects.get_or_create(id=row["bank_id"], name=row["bank_name"])

        with open("core/data/bank_branches.csv", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                bank = Bank.objects.get(id=row["bank_id"])
                Branch.objects.get_or_create(
                    ifsc=row["ifsc"],
                    bank=bank,
                    branch=row["branch"],
                    address=row["address"],
                    city=row["city"],
                    district=row["district"],
                    state=row["state"],
                )

        self.stdout.write(self.style.SUCCESS("Data successfully loaded from CSV."))
