#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
from six import with_metaclass

from bwtougu.const import SIDE
from bwtougu.environment import Environment


class BaseTax(with_metaclass(abc.ABCMeta)):
    @abc.abstractmethod
    def get_tax(self, trade):
        raise NotImplementedError


class StockTax(BaseTax):
    def __init__(self, rate=None):
        if rate is None:
            self.rate = 0.001
        else:
            self.rate = rate

    def get_tax(self, trade):
        cost_money = trade.last_price * trade.last_quantity
        if Environment.get_instance().get_instrument(trade.order_book_id).type == 'CS':
            return cost_money * self.rate if trade.side == SIDE.SELL else 0
        else:
            return 0


class FutureTax(BaseTax):
    def __init__(self, rate=0):
        self.rate = rate

    def get_tax(self, trade):
        return 0
