# Academic staff management system

A back-end for managing academic staff in a university


## Diagram and Models
### Diagram
[Digram in GoogleDrive](https://drive.google.com/file/d/1d3I85F1LHfmMR3n_x4SvY4TFgrGqdP1a/view?usp=sharing)
you can see the diagram in ERD
### Models
- Address: store address for sevral entity
    - state: name of state
    - city: name of city
    - street: name of street
    - street_number: number of street
    - building_name: name of building
    - district: in which district the address is on
    - floor: in which floor of building the address is on (0 for building without floors) 
    - unit_number: which unit the address is on (1 for floors with one unit)
    - plate_number: plate number for address (null for addresses without plate)
    - postal_code: postal code for the address
    - coordinate: coordinate for the  address in "latit"


## Features
1. An API over all entities for CRUD
2. Add authentication for create, update and delete accesses

## Deployment


## Front End Design
[Figma Design Link](https://www.figma.com/file/mSOeJXGZW9ZBRveeLNKIM1/Search-Page?type=design&node-id=0%3A1&mode=design&t=s3j0DHQkXXjsSY4n-1)

