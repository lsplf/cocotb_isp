# This file is public domain, it can be freely copied without restrictions.
# SPDX-License-Identifier: CC0-1.0

RTL_PATH ?= $(shell pwd)/../rtl/hdl
TOPLEVEL_LANG ?= verilog

ifeq ($(TOPLEVEL_LANG),verilog)
  VERILOG_SOURCES = $(RTL_PATH)/mul_wrapper.sv $(RTL_PATH)/mul.sv
else ifeq ($(TOPLEVEL_LANG),vhdl)
  $(error "A valid value (verilog or vhdl) was not provided for TOPLEVEL_LANG=$(TOPLEVEL_LANG)")
endif

MODULE = test_mult
TOPLEVEL = mul_wrapper

include $(shell cocotb-config --makefiles)/Makefile.sim
