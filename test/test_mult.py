"""
    this is a test for 8 bit wallace tree multiplier

"""
import random
import sys,os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')
from model import mult_model
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge
from cocotb.triggers import FallingEdge
from cocotb.triggers import Timer

@cocotb.test()
async def test_mul(dut):
    """ Test Multiplier Module """
    clock = Clock(dut.clk, 10, units="ns")  # Create a 10us period clock on port clk
    cocotb.fork(clock.start())  # Start the clock

    for i in range(10):
        dut.rst <= 1
        await RisingEdge(dut.clk)
        dut.rst <= 0
    dut._log.info("Reset complete")

    await FallingEdge(dut.clk)

    for i in range(10):
        a = random.randint(0, 2**8 - 1)
        b = random.randint(0, 2**8 - 1)
        dut.a <= a
        dut.b <= b
        await FallingEdge(dut.clk)
        c = mult_model.mul(a, b)

        dut._log.info("the {}th cycle".format(i))
        dut._log.info("dut output: a: %d, b: %d, p: %d" %(a, b, dut.p.value))
        assert dut.p.value == c, "output q was incorrect on the {}th cycle".format(i)
