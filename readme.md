

![logo_gslv.png](figures%2Flogo_gslv.png)



GSLV (Grid SoLVer) is a C++ library for advanced power systems simulation
that has been exposed to python closely following the VeraGrid API design.

## Supported OS and platforms

GSLV is available for Linux x64 (based on the kernel of Ubuntu 20.04 or newer), 
OSX with *M* architectures (ARM) , and Microsoft's Windows 10 or newer on x64 platforms.

For the time being, only the python module is made available. 
Upon special request a static or dynamic library could be provided. 

GSLV is available for python versions 3.10 to 3.13.

## Installing GSLV (Python)

The name of the GSLV package for python is `pygslv`

Installing is as simple as typing the following on your system command line:

```bash
pip install pygslv
```

Click [here](installation.md) to know more.

## License and activation

If you have purchased a license with eRoots Analytics S.L. you have
received a license file (i.e. `license.gslv`). This license file has 
to be stored in a folder with **read and write access**, this is because 
GSLV will read that file to determine whether you have a valid license or not.


Upon loading, the license will be validated online automatically and you will
be able to use GSLV.
A characteristic of the license is that once validated online, it allows 24h of 
off-line access until requiring an on-line verification. This allows for working on 
planes or other temporary off-line situations.
Special, completely off-line licenses are possible as well.

## [VeraGrid Usage](veragrid_usage.md)

GSLV is best used as a plugin engine of [VeraGrid](https://veragrid.readthedocs.org/).
The usage with GSLV is really simple and provides alternative results 
to the veragrid python engine but much much faster.
Click [here](veragrid_usage.md) to know more.

## [Standalone usage](standalone_usage.md)

This is a brief guide to get you started using GSLV.
You may want to use gslv directly. 
Its API is amost identical to the VeraGrid one, so it should be straigh forward to get started.
Click [here](standalone_usage.md) to know more.


## [Notes on performance](notes_on_performance.md)

Of course, not all systems are created equal, and GSLV 
will run better on high performance systems running Linux or OSX.
Click [here](notes_on_performance.md) to know more.

## GSLV End User License Agreement (EULA)

**Date:** 23/09/2025

This End User License Agreement ("Agreement") is made between:

**eRoots Analytics S.L.**  
Carrer del Torrent d'en Vidalet, 55, L1, Barcelona, 08024
(hereinafter referred to as "Licensor")

and  

the respective user of the GSLV software (hereinafter referred to as the "Software"),  
(hereinafter referred to as the "Licensee").  

Together referred to as the "Parties."



### 1. Grant of Licence
1. The Licensor grants the Licensee a non-exclusive, non-transferable, non-sublicensable right to use the Software solely for the contractually intended purposes and within the scope defined in the applicable license terms.
2. The Software remains the property of the Licensor at all times. Rights of use are conditional upon full payment of the agreed license fee.
3. The Software and its documentation are protected by copyright and other intellectual property laws. No rights are transferred other than those expressly stated herein.



### 2. Restrictions on Use
1. The Licensee shall not copy, modify, decompile, reverse engineer, or otherwise attempt to derive the source code of the Software except as expressly permitted by law.  
2. The Licensee shall not rent, lease, sublicense, or transfer the Software to third parties without prior written consent of the Licensor.  
3. Demo or evaluation versions of the Software may only be used for testing purposes during the agreed period and may not be used for commercial activities.  



### 3. Warranty
1. The Software is provided as a professional engineering tool but may not be error-free. The Licensee acknowledges that it represents a model of reality and must always be verified by the Licensee before relying on results for decision-making.  
2. The Licensor warrants that the Software will substantially conform to the documentation provided. In the event of a material defect, the Licensor may, at its discretion, provide an update, fix, or workaround.  



### 4. Liability
1. The Licensor is liable only for damages caused by intent or gross negligence, or where liability cannot be excluded under applicable law (e.g., personal injury).  
2. For all other cases, the Licensor’s liability for direct damages is **limited to the total amount of license fees actually paid by the Licensee for the Software giving rise to the claim.**  
3. The Licensor shall not be liable for indirect, incidental, consequential, or punitive damages, including but not limited to loss of profits, business interruption, or data loss.  
4. The Licensee is responsible for performing regular data backups and verifying the suitability of the Software for its intended application.  



### 5. Term and Termination
1. This Agreement begins upon delivery of the Software and remains in force until terminated.  
2. The Licensor may terminate the Agreement with immediate effect if the Licensee breaches material terms, including restrictions on use.  
3. Upon termination, the Licensee must immediately cease use of the Software and delete or return all copies.  



### 6. Governing Law and Jurisdiction
1. This Agreement shall be governed by and construed under the laws of Spain, excluding its conflict-of-law principles and the United Nations Convention on Contracts for the International Sale of Goods (CISG).  
2. The courts of Barcelona, Spain, shall have exclusive jurisdiction over disputes arising under this Agreement.  



### 7. Miscellaneous
1. Any amendments or modifications to this Agreement must be made in writing.  
2. If any provision of this Agreement is held invalid or unenforceable, the remaining provisions shall remain in full force and effect.  


**By installing or using the Software, the Licensee confirms acceptance of this Agreement.**
