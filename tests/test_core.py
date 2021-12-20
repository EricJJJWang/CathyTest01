# coding=utf-8
import pytest

from cathay.sample.customer import Customer
from cathay.sample.core import CustomerDataProcess
from decimal import Decimal, ROUND_DOWN

INIT_MONEY = 100.0


class TestCoreSuites:
    ##########################################################################################
    #
    # 假設這位客戶, 名字是 Test User, 帳號為100-1100, 一開始帳戶會先存100元, 要測試下面項目:
    #
    # 1. 之後存款 1000 元, 確認帳戶總金額為 1100 元
    # 2. 下一步提款 500 元, 確認帳戶總金額為 600 元
    # 3. 假設銀行年利率是10%, 經過一年之後確認帳戶餘額為660元
    # 4.之後提款 700 元, pytest 預期會接到 RuntimeError
    #
    ##########################################################################################

    
    def setup_class(self):
        self.test_user = Customer("Test User", "100-1100")
        self.test_user.deposit(100)

    def test_transcation(self):
        self.test_user.deposit(1000)
        assert self.test_user.balance == 1100

        self.test_user.withdraw(500)
        assert self.test_user.balance == 600

        assert int(CustomerDataProcess.add_interest(
            self.test_user, 0.1)) == 660

        with pytest.raises(RuntimeError):
            self.test_user.withdraw(700)
            
    def Disable_test_deposit_1000(self):
        self.test_user.deposit(1000)
        assert self.test_user.balance == 1100

    def Disable_test_withdraw_500(self):
        self.test_user.withdraw(500)
        assert self.test_user.balance == 600

    def Disable_test_add_interest(self):
        assert int(CustomerDataProcess.add_interest(self.test_user, 0.1)) == 660

    def Disable_test_withdraw_700(self):
        with pytest.raises(RuntimeError):
            self.test_user.withdraw(700)
