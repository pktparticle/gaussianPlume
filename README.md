# Atmospheric Dispersion Modelling

### Overview
Contaminants discharged into the air are transported over long distances by large-scale air-flows and dispersed by small-scale air-flows or turbulence, which mix contaminants with clean air. This dispersion by the wind is a very complex process due to the presence of different-sized eddies in the atmospheric flow. Due to this complexity, there is no complete theory that establishes the relationship between ambient conditions of air pollutants and the causative
meteorological factors and processes.

So, to express all these to the extent possible, we make models (simplified picture of reality).
* An atmospheric dispersion model is a mathematical simulation which governs the transport, dispersion and transformation of pollutants in the atmosphere.
* Nowadays air pollution models are computer programs that use mathematical algorithms to simulate how pollutants in the ambient atmosphere disperse and, in some cases, how they react in the atmosphere, using information on the:
    * Contaminant emission rate
    * Characteristics of the emission source
    * Local topography
    * Meteorology of the area
    * Ambient or background concentrations of pollutant

The process of air pollution modelling contains four stages (data input, dispersion calculations,deriving concentrations, and analysis). The accuracy and uncertainty of each stage must be
known and evaluated to ensure a reliable assessment of the significance of any potential
adverse effects.

### Types of Pollutants representation:
#### Plumes
The flow of pollutant in the form of vapor or smoke released into the air. These
are of considerable importance in the atmospheric dispersion modelling of air pollution.
These are mainly classified in 3 types:
* **Buoyant Plumes:** Plumes which are lighter than air because they are at a higher temperature and lower density than the ambient air which surrounds them, or because they are at about the same temperature as the ambient air but have a lower molecular weight and hence lower density than the ambient air. e.g. Methane (CH4) is buoyant because it has lower molecular weight than air.

* **Dense Gas Plumes:** A plume may have a higher density than air because it has a higher molecular weight than air (for example, a plume of carbon dioxide). A plume may also have a higher density than air if the plume is at a much lower temperature than the air, such plumes are called dense gas plumes.

* **Passive Flumes:** Plumes which are neither lighter or heavier than air.

#### Particles
Pollutant releases, especially those from point sources, are often represented
by a stream of particles (even if the pollutant is a gas), which are transported by the
model winds and diffuse randomly according to the model turbulence. Particle models
are computationally expensive, needing at least 105 particles to represent a pollutant
release, but maybe the best type to represent pollutant concentrations close to the
source.

#### Puffs
Pollutant releases can also be represented by a series of puffs of material which
are also transported by the model winds. Each puff represents a discrete amount of
pollution, whose volume increases due to turbulent mixing. Puff models are far less
computationally expensive than particle models, but are not as realistic in their
description of the pollutant distribution. However, they are often more than adequate,
and are used for regulatory purposes.

#### Grid Points
Pollutant distributions are represented by concentrations on a (regular)
three-dimensional grid of points. This is the cheapest formulation computationally, but
difficulties arise when the scale of the pollutant release is smaller than the grid point
spacing.

## Gaussian-plume models
The Gaussian-plume formula is derived assuming ‘steady-state’
conditions. That is, the Gaussian-plume dispersion formulae do not depend on time, although
they do represent an ensemble time average. The meteorological conditions are assumed to
remain constant during the dispersion from source to receptor, which is effectively
instantaneous. Emissions and meteorological conditions can vary from hour to hour but the
model calculations in each hour are independent of those in other hours. Due to this
mathematical derivation, it is common to refer to Gaussian-plume models as steady-state
dispersion models. In practice, however, the plume characteristics do change over time,
because they depend on changing emissions and meteorological conditions. One consequence
of the plume formulation is that each hour the plume extends instantaneously out to infinity.
Concentrations may then be found at points too distant for emitted pollutants to have reached
them in an hour.

**Gaussian-plume models are generally applicable when:**
- The pollutants are chemically inert, a simple first-order mechanism is appropriate, or the chemistry may be carried out as a post-processing step.
- The terrain is not steep or complex
- The meteorology may be considered uniform spatially
- There are few periods of calm or light winds
