# Hash256 ASIC

## Common Registers

- Work registers

	- work cfg:

		Spdgo[24]: enable cfg values to pll registers.

		FTneed[23:15]: pass core success numbers, if greater than FTneed, FTpass is 1 and for success.

		RstFifo[12]: clean all FIFO registers.

		RollEn[10]: roll ntime enable, when rolltime timeout and ntime add 1.

		FTst[9]: FT start, 1 cycle high.

		ChkEn[8]: check enable, if check disable, spdlog will fail all.

		Mask[7:0]: mask hash values.

	- TargetL/H:

		Pool difficulty.

	- Tbase:

		ntime base, sending work times.

	- RollTime:

		if rollen = 1, when timeout overflow send next work.

	- FTLog:

		FTPass[9]: FT pass flag.

		FTcnt[8:0]: pass coretest count.

- CFG registers

	- Global:

		SpdHigh[16:14]: ss max_spd level.

		SpdLow[13:11]: ss mix_spd level.

		SpdRst[9]: reset spdlog.

		GlbSetVld[8]: enable set speed vaild.

		GlbSet[7:0]: Global set speed level select.

	- H2LTime0:

		SpdSetup[23:16]: setting spd pll asic count.

- PLL STS registers

	- PllChgT:

		After setting PLL, ASIC gate time.

- SPD registers

	- Spd/SpdCore:

		record config pll value.

- ECC registers

	- ECC0/1/2:

		receive position error datas.
