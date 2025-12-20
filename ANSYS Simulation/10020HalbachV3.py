import ansys.motorcad.core as pymotorcad
import ansys.motorcad.core.geometry as geometry
import math

mc = pymotorcad.MotorCAD(open_new_instance=False)

# Reset geometry, BPMOR
mc.reset_adaptive_geometry()        
mc.set_variable("motor_type", 3)


# Basic stator setup
mc.set_variable("slot_number", 36)
mc.set_variable("armature_diameter", 100.0)
mc.set_variable("tooth_width", 2.6)
mc.set_variable("slot_depth", 10.0)
mc.set_variable("slot_corner_radius", 0.2)
mc.set_variable("slot_opening", 2.511)
mc.set_variable("tooth_tip_depth", 0.5)
mc.set_variable("tooth_tip_angle", 15.0)
mc.set_variable("airgap", 0.5)
mc.set_variable("sleeve_thickness", 0.0)
mc.set_variable("axle_dia", 78.0)
mc.set_variable("axle_hole_diameter", 78.0)


# Winding setup
mc.set_variable("wedge_model", 2) #air wedges
mc.set_variable("liner_thickness", 0.3)


# Rotor Setup
mc.set_variable("pole_number", 42)
mc.set_variable("back_iron_thickness", 5.0)
mc.set_variable("magnet_thickness", 3.0)  
mc.set_variable("Magnet_Arc_[ED]", 180)
mc.set_variable("banding_thickness", 0.0)
mc.set_variable("CircumferentialSegments", 2)


# Get Rotor Dimensions
airgap = mc.get_variable("airgap")
armature_diameter = mc.get_variable("armature_diameter")
stator_outer_radius = armature_diameter / 2
rotor_inner_radius = stator_outer_radius + airgap
num_poles = mc.get_variable("pole_number")
pole_pitch_angle = 360.0 / num_poles


# Magnet dimensions
magnet_thickness = mc.get_variable("magnet_thickness")
mag1_width = 5.0
mag2_width = 1.5
r1 = rotor_inner_radius
r2 = rotor_inner_radius + magnet_thickness


def magnetConstructor(d, r1, r2, theta, chi, offset, magnetRegion):
    """Construct magnet region based on input parameters.

    Parameters
    ----------
    theta : float
        Angle for first corner point

    d : float
        Tangential width of magnet

    r1 : float
        Inner radius of magnet

    r2 : float
        Outer radius of magnet

    offset : float
        Angle offset for magnet placement
        
    magnetRegion : RegionMagnet
        Magnet region to be constructed

    Returns
    -------
        None
    """

    print(f"Constructing magnet region with d={d}, r1={r1}, r2={r2}, offset={offset}")

    # Calculate angle1 using the equation
    theta = math.degrees(math.acos(1 - (d ** 2) / (2 * r1 ** 2))) + offset
    chi  = math.degrees(math.acos(1 - (d ** 2) / (2 * r2 ** 2))) + offset
    phi = (theta - chi) / 2

    print(f"theta: {theta}, chi: {chi}, phi: {phi}, offset: {offset}")

    # Define 4 corners
    p1 = geometry.Coordinate(*geometry.rt_to_xy(r1, theta))
    p2 = geometry.Coordinate(*geometry.rt_to_xy(r2, chi + phi))
    p3 = geometry.Coordinate(*geometry.rt_to_xy(r2, phi + offset))
    p4 = geometry.Coordinate(*geometry.rt_to_xy(r1, offset))

    entities = magnetRegion.entities
    entities[0] = geometry.Line(p1, p4)
    entities[1] = geometry.Line(p1, p2)
    entities[2] = geometry.Line(p2, p3)
    entities[3] = geometry.Line(p3, p4)

    magnetRegion.entities = entities

    if magnetRegion.is_closed():
        mc.set_region(magnetRegion)

    return


# Magnet Radial Segment
magnet_radial = mc.get_region("1Magnet1")
# magnet_radial.name = "Magnet_Radial"

d_radial = 5.0
offset_radial = 0.0

theta_radial = math.degrees(math.acos(1 - (d_radial ** 2) / (2 * r1 ** 2)))
chi_radial = math.degrees(math.acos(1 - (d_radial ** 2) / (2 * r2 ** 2)))
magnet_radial.magnet_angle = offset_radial + (theta_radial / 2)

magnetConstructor(d_radial, r1, r2, theta_radial, chi_radial, offset_radial, magnet_radial)


# Magnet Tangential Segment
magnet_tangential = mc.get_region("2Magnet1")
# magnet_tangential.name = "Magnet_Tangential"
d_tangential = 1.5

theta_tangential = math.degrees(math.acos(1 - (d_tangential ** 2) / (2 * r1 ** 2)))
chi_tangential = math.degrees(math.acos(1 - (d_tangential ** 2) / (2 * r2 ** 2)))

offset = (pole_pitch_angle - (theta_radial + theta_tangential)) / 2
offset_tangential = theta_radial + offset
magnet_tangential.magnet_angle = offset_tangential + (chi_tangential / 2) - 90

magnetConstructor(d_tangential, r1, r2, theta_tangential, chi_tangential, offset_tangential, magnet_tangential)
