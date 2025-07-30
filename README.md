# 3D-Printed Integrated Joint Actuator 

<img width="3840" height="2160" alt="IJA 801 - Integrated Joint Actuator (7)" src="https://github.com/user-attachments/assets/568b3e46-83d2-45a8-a37c-cf5d1bcd158b" />

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
- Hard to print with FDM (lots of support and post-processing needed)
- Plastic can only take you so far ): cycloidal disk still fractures under load, considering changing to aluminum or acetal
- ODrive S1 sticks out way too much, wanted to use ODrive Micro but out of stock ):
- Pins grind through cycloidal disk fast
- Wire still sticks out of motor and not encased  
<br />

## Subcomponents and File Naming
Custom parts should obey the XXXX YZZ - NAME file number convention:  
- XXX: Module ID (Alphabetical)  
- Y: File type classifier (Numbers)  
- ZZ: Part number (Numbers)  
- NAME: Descriptive file name in Title Capitalization Form  

### Module IDs  
- BLDC: Brushless DC Motor  
- CYC: Internal Cycloidal Gearbox  
- COTS: Commercial Off the Shelf  
- ODS1: ODrive S1 Mounting  

### File Classifiers
- 0: Top-level assemblies (No more than 1)  
- 1: Subassemblies  
- 2: Equation.txt files  
- 3: Drawings  
- 4: Individual parts  
- 5: Wiring, piping, tubing, and weldments   
- 6: Test fit files  
- 7: Solidworks FEA Simulation Files  
- 8: Solidworks VISUALIZE files  
- 9: Manufacturing files (3MF, STL, DXF, GCODE)  
