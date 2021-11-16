"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730345086"


class Simpy:
    values: list[float] = []

    def __init__(self, casserole: list[float]):
        """Constructor for Floats."""
        self.values = casserole

    def __str__(self) -> str:
        """Make a Str Representation."""
        return f"Simpy({self.values})"

    def fill(self, yams: float, stuffing: int) -> None:
        """Fill Values List with Specific Repeating Values."""
        self.values = []
        i: int = 0
        while i < stuffing:
            self.values.append(yams)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill Values List with a Range of Other Values."""
        self.values = []
        assert step != 0.0
        if step > 0.0:
            next_value: float = start
            while next_value < stop:
                self.values.append(next_value)
                next_value += step
        else:
            next_value: float = start
            while next_value > stop:
                self.values.append(next_value)
                next_value += step

    def sum(self) -> float:
        """Compute and Return the Sum of Values List."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Return a New Simpy Object of Added Values from Two Lists."""
        pumpkin_pie: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                pumpkin_pie.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0 
            while i < len(self.values):
                pumpkin_pie.values.append(self.values[i] + rhs.values[i])
                i += 1
        return pumpkin_pie

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Return a New Simpy Object of Raised Values from Two Lists."""
        sweet_potato: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                sweet_potato.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                sweet_potato.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return sweet_potato

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Return an Equality-based Mask."""
        ham: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                ham.append(value == rhs)
        else:
            i: int = 0
            while i < len(self.values):
                ham.append(self.values[i] == rhs.values[i])
                i += 1
        return ham

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Return a Greater-Than Mask."""
        sweet_rolls: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                sweet_rolls.append(value > rhs)
        else:
            i: int = 0 
            while i < len(self.values):
                sweet_rolls.append(self.values[i] > rhs.values[i])
                i += 1
        return sweet_rolls

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Read and Return a New, Filtered Simpy Object."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else: 
            mashed_potato: Simpy = Simpy([])
            i: int = 0
            while i < len(self.values):
                if rhs[i]:
                    mashed_potato.values.append(self.values[i])
                i += 1
            return mashed_potato
            