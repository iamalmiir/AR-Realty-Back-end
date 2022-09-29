COOLING_CHOICES = (
    ("Central", "Central"),
    ("Electric", "Electric"),
    ("No data", "No data"),
)

HEATING_CHOICES = (
    ("Central", "Central"),
    ("Electric", "Electric"),
    ("Forced Air", "Forced Air"),
    ("Natural Gas", "Natural Gas"),
    ("Fireplace", "Fireplace"),
    ("No data", "No data"),
)

LISTING_TYPES = (
    ("Single Family", "Single Family"),
    ("Condo", "Condo"),
    ("Townhouse", "Townhouse"),
    ("Multi-Family", "Multi-Family"),
    ("Duplex", "Duplex"),
)

US_STATES = (
    ("AL", "Alabama"),
    ("AK", "Alaska"),
    ("AZ", "Arizona"),
    ("AR", "Arkansas"),
    ("CA", "California"),
    ("CO", "Colorado"),
    ("CT", "Connecticut"),
    ("DE", "Delaware"),
    ("DC", "District of Columbia"),
    ("FL", "Florida"),
    ("GA", "Georgia"),
    ("HI", "Hawaii"),
    ("ID", "Idaho"),
    ("IL", "Illinois"),
    ("IN", "Indiana"),
    ("IA", "Iowa"),
    ("KS", "Kansas"),
    ("KY", "Kentucky"),
    ("LA", "Louisiana"),
    ("ME", "Maine"),
    ("MD", "Maryland"),
    ("MA", "Massachusetts"),
    ("MI", "Michigan"),
    ("MN", "Minnesota"),
    ("MS", "Mississippi"),
    ("MO", "Missouri"),
    ("MT", "Montana"),
    ("NE", "Nebraska"),
    ("NV", "Nevada"),
    ("NH", "New Hampshire"),
    ("NJ", "New Jersey"),
    ("NM", "New Mexico"),
    ("NY", "New York"),
    ("NC", "North Carolina"),
    ("ND", "North Dakota"),
    ("OH", "Ohio"),
    ("OK", "Oklahoma"),
    ("OR", "Oregon"),
    ("PA", "Pennsylvania"),
    ("RI", "Rhode Island"),
    ("SC", "South Carolina"),
    ("SD", "South Dakota"),
    ("TN", "Tennessee"),
    ("TX", "Texas"),
    ("UT", "Utah"),
    ("VT", "Vermont"),
    ("VA", "Virginia"),
    ("WA", "Washington"),
    ("WV", "West Virginia"),
    ("WI", "Wisconsin"),
    ("WY", "Wyoming"),
)


# Find the state by full name and return the abbreviation
def get_state_abbreviation(state_name):
    for state in US_STATES:
        if state_name.lower() == state[1].lower():
            return state[0]
    return state_name
