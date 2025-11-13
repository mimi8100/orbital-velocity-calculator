import math

# --- Constants for Earth Orbit Calculations ---

# Gravitational Constant (G): N*m^2/kg^2
G = 6.67430e-11

# Mass of the Earth (M): kg
M_EARTH = 5.972e24

# Average Radius of the Earth (R_earth): meters (used to convert altitude to orbital radius)
R_EARTH = 6371000

# The standard gravitational parameter (mu = G * M) is often used for cleaner calculations
MU_EARTH = G * M_EARTH


def calculate_orbital_velocity(orbital_radius_m):
    """
    Calculates the orbital velocity (v) for a stable circular orbit 
    using the formula: v = sqrt(MU / r)

    Args:
        orbital_radius_m (float): The distance from the center of the Earth 
                                  to the satellite (in meters).

    Returns:
        float: The required orbital velocity in meters per second (m/s).
    """
    if orbital_radius_m <= R_EARTH:
        # Satellites must be outside the atmosphere to maintain orbit
        return 0.0 
    
    # Calculate the velocity using the formula v = sqrt(GM/r)
    velocity_mps = math.sqrt(MU_EARTH / orbital_radius_m)
    return velocity_mps

def main():
    """
    Main function to get user input (altitude) and display orbital velocity.
    """
    print("--- Orbital Velocity Calculator (Space Project) ---")
    print("This calculator finds the speed needed for a circular orbit around Earth.")
    print(f"Earth Radius used: {R_EARTH / 1000:.0f} km\n")
    
    try:
        # Get altitude from the user in kilometers
        altitude_km = float(input("Enter satellite altitude above Earth (in kilometers, e.g., 400 for ISS): "))

        if altitude_km <= 0:
            print("\nError: Altitude must be greater than 0 km.")
            return

        # 1. Convert inputs to standard SI units (meters)
        altitude_m = altitude_km * 1000
        
        # 2. Calculate the total orbital radius (r = R_earth + altitude)
        orbital_radius_m = R_EARTH + altitude_m
        
        # 3. Calculate the velocity
        velocity_mps = calculate_orbital_velocity(orbital_radius_m)

        # 4. Display results
        velocity_kmps = velocity_mps / 1000  # Convert m/s to km/s

        print("\n" + "="*50)
        print(f"Input Altitude: {altitude_km:.1f} km")
        print(f"Orbital Radius (from Earth center): {orbital_radius_m / 1000:.0f} km")
        print("-" * 50)
        
        if velocity_mps > 0:
            print(f"Required Orbital Velocity:")
            print(f"  {velocity_kmps:.2f} kilometers per second (km/s)")
            print(f"  {velocity_mps:.0f} meters per second (m/s)")
        else:
            print("Orbit is not possible at this altitude (it would be inside the Earth).")
            
        print("="*50)

        # Example check for International Space Station (ISS) altitude (~420 km)
        # Expected velocity is around 7.67 km/s
        if 400 <= altitude_km <= 450:
             print("\nNote: The International Space Station (ISS) orbits at a similar altitude.")

    except ValueError:
        print("\nError: Please ensure your input is a valid number.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()