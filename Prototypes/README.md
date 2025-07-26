# Prototypes  
These are some prototypes and previous iterations of the QDD design. The README.MD files in each version's subdirectory describe specific differences and design parameters.  

## V5 (Current): Complete Redesign (07/22/25 - Current)
This is a complete redesign of everything. This iteration features a reduction of 23:1, removed the ring post bearings for dowel pins, added a pair of 6710-2RS bearings for output shaft support, improved file structures, etcetcetc. TLDR this version should be actually not trash.
### Fixes:
- Cycloidal disk fracturing
- Redesigned the gearbox assembly completely, removing print quality issues with the outer wall
- Fixed rotor clearance issues
- Fixed rotor centering
- Added moment support for output
- No more heat-set insert for load-bearing parts, changed to M4 hex nut
- Added proper ODrive S1 Mounting
- Added bearings for output from inside cycloidal disks
### Issues:
- Hard to print with FDM (lots of support and post processing needed)
- Plastic can only take you so far ): cycloidal disk still fractures under load, considering changing to aluminum or acetal
- ODrive S1 sticks out way too much, wanted to use ODrive Micro but out of stock ):
- Wire still sticks out of motor and not encased


## V4: Minor Changes (02/03/2025 - 02/05/2025)
Honestly dont remember what I changed, pretty burned out atp and didn't document much 
### Fixes:
- Made minor changes to the housing
### Issues:
- All previous issues persist


## V3: Major Changes and FOC Test (01/15/2025 - 01/21/2025)
Wallahi I am cooked for finals... Pretty big redesign - 11:1 gearbox, solid ring posts
### Fixes:
- Changed the gearbox to use 11:1 reduction instead of 10:1
- Redesigned output to use bigger bearings and made it deeper for bigger inserts
- Redesigned the gearbox wall to be continuous and changed the fastener pattern
- Redesigned the output shaft assembly and cycloidal disks to interface with 12mm bushing
- Added a stand to mount ODrive S1 and mount to surface
### Issues:
- Cycloidal disk fractures under any load
- No back bearing, leading to no moment support @output
- Output threaded inserts still get pulled out
- Ouptut shaft still getting destroyed ):


## V2: Integration Test, Pt 2 (12/6/2024 - 12/7/2024)
Slimmed-down package, functionally the same as V1. Printed with PLA/Unlubricated
### Fixes:
- Ngl I fixed pretty much nothing
### Issues:
- Gearbox binded up after running it really fast :skull:
- Cycloidal disk output holes get cut off by cam bearing
- Output shaft coupling assembly is overcomplicated
- Output shaft getting destroyed
- Screw heads stick out
- Low-quality cam bearings  

  
## V1: Integration Test (12/3/2024 - 12/5/2024)  
Integration test with BLDC motor (Mechanically feature complete). Printed with PLA/Unlubricated
### Fixes:
- Added spacer between cycloidal disks
- Retained camshaft
- Added thickness to output, now with 8mm M3 heat set inserts
- Added hex nut retainers to back of gearbox
- Did not fix anything but added pretty cutouts <3
### Issues:
- **Cycloidal disk output holes get cut off by cam bearing**
- Output shaft coupling assembly is overcomplicated
- Output shaft getting destroyed
- Screw heads stick out
- Low-quality cam bearings _(another one broke; perhaps should stop getting them from aliexpress)_  

  
## V0: Gearbox Only (12/1/2024 - 12/3/2024)  
Prototype gearbox design, driven by a drill. Printed with PLA/Unlubricated
### Issues:  
- ~~Insane friction between cycloidal disks~~
- ~~Middle camshaft not retained~~
- Output shaft coupling assembly is complicated since 6706-2RS Bearings were the biggest ones I had on hand
- Output shaft getting destroyed by cycloidal disks
- Cycloidal disk output holes get cut off by cam bearing
- ~~Output heat set insert only 3mm~~
- ~~Screw heads stick out and interfere with rotation (the whole thing is literally friction fit lol)~~
- Low-quality cam bearings. One blew up  






