# 3D-Printed Integrated Joint Actuator 

<img width="1549" height="1023" alt="image" src="https://github.com/user-attachments/assets/268dfcef-c98b-4cf3-8867-3965d3c084af" />


## V6 (Current): Complete Redesign (12/14/25 - Current)
Version 6 offers significantly improved performance over V5, with a 11:1 reduction, ironless halbach array rotor optimized with Ansys Motor-CAD and Ansys Maxwell, a 10020 stator instead of 10010, and significantly more compact motor controller mounting.

The cycloidal disks and the ring pins are designed to be printed with iglide® i190-PF, whereas the structural parts are designed to be printed with PA6-CF.

### Changes:
- Changed reduction ratio to 11:1
- Changed stator to 10020, and changed rotor to N52 Halbach array
- Post processing issues fixed, removed hexnut cutouts from V5  
- Fixed stability issues with tighter tolerances and thicker bearings
- Removed set screws from offset cams and rotor
- Fixed cycloidal disk fracture by printing with iglide
- Significantly reduced weight by removing aluminum ring pins
- Removed rotor back bearing and optimized ODrive S1 Mounting
- Removed purely aesthetic surface pocketing
  
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
- 7: Misc. files (Textures, Scenarios, Simulations)   
- 8: Solidworks VISUALIZE files  
- 9: Manufacturing files (3MF, STL, DXF, GCODE)  
