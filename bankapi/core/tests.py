from django.test import TestCase
from core.models import Bank, Branch


class BankBranchTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        # create() both saves and returns the object
        cls.bank = Bank.objects.create(id=1, name="HDFC BANK")

        Branch.objects.create(
            ifsc="HDFC0001234",
            bank=cls.bank, 
            branch="MUMBAI MAIN",
            address="Some address",
            city="Mumbai",
            district="Mumbai",
            state="Maharashtra",
        )

    def test_get_banks(self):
        response = self.client.get("/banks/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_get_branch_by_ifsc(self):
        response = self.client.get("/branches/HDFC0001234/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["branch"], "MUMBAI MAIN")

    def test_get_branches_by_bank_and_city(self):
        response = self.client.get("/branches/?bank_name=HDFC&city=Mumbai")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
